from typing import Iterable
import ollama

def classify_commit_message(message: str) -> str:
    prompt = f"""
given the following git commit: {message}
    
classify it in one of the following categories: bug fix, refactoring or new feature.
Reply typing only the name of the category
"""
    return ollama.generate(model="llama3.1", prompt=prompt, stream=False, options={'temperature':0.0})['response'].lower()

def classify_commits_message(messages: Iterable[str]) -> Iterable[str]:
    for m in messages:
        yield classify_commit_message(m)
