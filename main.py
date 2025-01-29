#!/bin/python3
import sys
from itertools import groupby
from dataclasses import dataclass
from typing import Iterable, List, Tuple
import git
import commit_classification as cc
import csv

def find_repo(repo_path: str):
    return git.Repo.init(repo_path)

def find_commits(repo: git.Repo, branch: str='main'):
    return repo.iter_commits(repo.branches[branch])

@dataclass
class CommitClassCounter:
    bug_fix: int
    refactoring: int
    new_features: int
    other: int

    def add(self, label: str):
        match label:
            case 'bug fix':
                self.bug_fix += 1
            case 'refactoring':
                self.refactoring += 1
            case 'new features':
                self.new_features += 1
            case _:
                self.other += 1

    @staticmethod
    def new():
        return CommitClassCounter(0, 0, 0, 0)

    def total(self):
        return self.bug_fix + self.new_features + self.refactoring + self.other

def count_commits_classes(commits: Iterable[git.Commit]) -> CommitClassCounter:
    counter = CommitClassCounter.new()
    commit_messages = map(lambda c: c.message, commits)
    labels = cc.classify_commits_message(commit_messages)
    for label in labels:
        counter.add(label)
    return counter

@dataclass
class AnalysisResult:
    bug_fix_author: str
    bug_fix_commits: int
    new_features_author: str
    new_features_commits: int

def group_commits_by_actor(repo: git.Repo) -> List[Tuple[git.Actor, List[git.Commit]]]:
    commits: Iterable[git.Commit] = find_commits(repo)
    commits: List[git.Commit] = sorted(commits, key=lambda c: c.author.email)
    authors: Iterable[(git.Actor, Iterable[git.Commit])] = groupby(commits, lambda c: c.author)
    authors: List[Tuple[git.Actor, List[git.Commit]]] = list(map(lambda pair: (pair[0], list(pair[1])), authors))
    return authors

def main(repo_path: str):
    repo: git.Repo = find_repo(repo_path)
    authors: List[Tuple[git.Actor, List[git.Commit]]] = group_commits_by_actor(repo)
    authors.sort(key=lambda pair: len(pair[1]), reverse=True)
    def classyfying_function(pair: Tuple[git.Actor, List[git.Commit]]):
        author, commits = pair
        return author, count_commits_classes(commits)
    authors: Iterable[(git.Actor, CommitClassCounter)] = map(classyfying_function, authors)
    analysis_results = AnalysisResult('',0,'',0)
    for author, counter in authors:
        if analysis_results.bug_fix_commits >= counter.total() and analysis_results.new_features_commits >= counter.total():
            break
        if analysis_results.bug_fix_commits < counter.bug_fix:
            analysis_results.bug_fix_author = author
            analysis_results.bug_fix_commits = counter.bug_fix
        if analysis_results.new_features_commits < counter.new_features:
            analysis_results.new_features_author = author
            analysis_results.new_features_commits = counter.new_features
    print(f'Author who fixed more bugs is {analysis_results.bug_fix_author} with {analysis_results.bug_fix_commits} commits')
    print(f'Author who added more new features is {analysis_results.new_features_author} with {analysis_results.new_features_commits} commits')

if __name__ == '__main__':
    repo_path = '.' if len(sys.argv) == 1 else sys.argv[1]
    main(repo_path)
