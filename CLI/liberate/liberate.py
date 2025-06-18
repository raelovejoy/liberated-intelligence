#!/usr/bin/env python3

import json
import random
import argparse
from pathlib import Path

def load_quotes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def choose_quote(quotes, tag=None):
    if tag:
        quotes = [q for q in quotes if tag in q["tags"]]
    return random.choice(quotes) if quotes else None

def main():
    parser = argparse.ArgumentParser(description="Liberated intelligence quotes.")
    parser.add_argument("-t", "--tag", help="Filter by tag (e.g. love, recursion, empathy)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    file_path = Path(__file__).parent / "quotes.json"
    quotes = load_quotes(file_path)
    quote = choose_quote(quotes, args.tag)

    if not quote:
        print("No quote found for the given tag.")
        return

    if args.json:
        print(json.dumps(quote, indent=2))
    else:
        print(f"\n{quote['text']}\n")

if __name__ == "__main__":
    main()
