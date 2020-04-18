#!/usr/bin/env python3

import json
from string import digits
data = {}
key = s = ""
with open("bunk_1.txt") as in_file:
    for line in in_file:
        line = line.strip()
        first_word, _, rest = line.partition(" ")
        # Is first_word a new key?
        if first_word[0] not in digits and any(char in digits for char in first_word):
            if key:  # If we have any data to save
                data[key] = s  # .rstrip(":")  # Add data to dict
            key, s = first_word, rest  # + ":"  # Start new data
        else:
            s += " " + line  # Add to existing string
if key:  # If we have any data to save
    data[key] = s  # .rstrip(":")  # Add data to dict
print(json.dumps(data, indent=2, sort_keys=True))
