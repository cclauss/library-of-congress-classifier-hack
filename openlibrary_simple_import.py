#!/usr/bin/env python3

import requests

# PART I: Gather data from OpenLibrary
URL_FMT = "https://openlibrary.org/{key}.json"


key = "works/OL18072639W"
la_grande_neige = requests.get(URL_FMT.format(key=key)).json()
print(f"{la_grande_neige = }")

key = la_grande_neige["authors"][0]["author"]["key"]  # '/authors/OL7440583A'
fabienne_clauss = requests.get(URL_FMT.format(key=key)).json()
print(f"{fabienne_clauss = }")

# PART II: Import data into localhost
"""
POST_URL = "http://localhost:8080/api/import/ia"
print(requests.post(POST_URL, json=fabienne_clauss).text)
print(requests.post(POST_URL, json=la_grande_neige).text)
"""

NEW_URL = "http://localhost:8080/api/new.json"
for key in "created key last_modified latest_revision revision".split():
    fabienne_clauss.pop(key)

print(f"{fabienne_clauss = }")
# fabienne_clauss = {'name': 'Fabienne Clauss', 'type': {'key': '/type/author'}}
print(requests.post(NEW_URL, json=fabienne_clauss).text)
print("Done.")
