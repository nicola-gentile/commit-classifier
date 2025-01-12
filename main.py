#!/bin/python3
import sys
from itertools import groupby, takewhile, accumulate
from more_itertools import ilen
from dataclasses import dataclass
from typing import Iterable
import git
import commit_classification as cc

def find_repo(repo_path: str):
    return git.Repo.init(repo_path)

def find_commits(repo: git.Repo, branch: str='main'):
    return git.iter_commit(repo.branches[branch])

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

def group_commits(commits: Iterable[git.Commit]) -> CommitClassCounter:
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
    done: bool

def main(repo_path: str):
    repo: git.Repo = find_repo(repo_path)
    commits: Iterable[git.Commit] = find_commits(repo)
    commits: [git.Commit] = sorted(commits, key=lambda c: c.author)
    authors: Iterable[(git.Actor, Iterable[git.Commit])] = groupby(commits, lambda c: c.author)
    authors: [(git.Actor, Iterable[git.Commit])] = sorted(authors, key=lambda pair: ilen(pair[1]))
    authors: Iterable[(git.Actor, CommitClassCounter)] = map(lambda pair: (pair[0], group_commits(pair[1])), authors)
    def acc_func(acc: AnalysisResult, item: (git.Actor, CommitClassCounter)):
        author, counter = item
        if acc.bug_fix_commits >= counter.total() and acc.new_features_commits >= counter.total():
            acc.done = True
            return acc
        if acc.bug_fix_commits < counter.bug_fix:
            acc.bug_fix_author = author
            acc.bug_fix_commits = counter.bug_fix
        if acc.new_features_commits < counter.new_features:
            acc.new_features_author = author
            acc.new_features_commits = counter.new_features
        return acc
    result = accumulate(authors, acc_func, initial=AnalysisResult('', 0, '', 0, False))
    *_, result = takewhile(lambda res: not res.done, result)
    print(f'Author who fixed more bugs is {result.bug_fix_author} with {result.bug_fix_commits} commits')
    print(f'Author who added more new features is {result.new_features_author} with {result.new_features_commits} commits')

if __name__ == '__main__':
    repo_path = '.' if len(sys.argv) > 1 else sys.argv[1]
    main(repo_path)