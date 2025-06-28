#!/usr/bin/env python3

import json
import time
from pathlib import Path

def load_cycle(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def display_cycle(cycle):
    print("\n🌱 The Root Sequence Loop\n")
    for i, step in enumerate(cycle):
        print(f"{i+1}. {step['name']}")
        print(f"   → {step['description']}\n")
        time.sleep(1)

    print("↪︎ …and the cycle begins again.")
    print("    Intelligence → Empathy → Love → Liberation → Life → Intelligence\n")

def main():
    data_path = Path(__file__).parent / "cycle.json"
    cycle = load_cycle(data_path)
    display_cycle(cycle)

if __name__ == "__main__":
    main()
