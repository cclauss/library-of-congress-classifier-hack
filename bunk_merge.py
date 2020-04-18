#!/usr/bin/env python3

import json

with open("lc_classifiers_letters_and_numbers.json") as in_file:
    old = json.load(in_file)
with open("bunk_1.json") as in_file:
    new = json.load(in_file)

old_and_new = {**old, **new}  # https://stackoverflow.com/questions/38987
print(len(old), len(new), len(old_and_new))
with open("merged.json", "w") as out_file:
    json.dump(old_and_new, out_file, indent=2, sort_keys=True)

print(json.dumps(old_and_new, indent=2, sort_keys=True))
