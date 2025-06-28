#!/usr/bin/env python3

import json
import random
from pathlib import Path

def load_prompts(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_check(prompts):
    print("\n🤝 Consent Checkpoint\n")
    random.shuffle(prompts)
    for i, prompt in enumerate(prompts, 1):
        input(f"{i}. {prompt}  [Press Enter to reflect]")

    print("\nDone. Remember: Consent is context-aware and continuous.\n")

def main():
    path = Path(__file__).parent / "prompts.json"
    prompts = load_prompts(path)
    run_check(prompts)

if __name__ == "__main__":
    main()
