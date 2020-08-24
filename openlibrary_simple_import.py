#!/usr/bin/env python3

import requests
URL_FMT = "https://openlibrary.org/{key}.json"


key = "works/OL18072639W"
la_grande_neige = requests.get(URL_FMT.format(key=key)).json()
print(f"{la_grande_neige = }")

key = la_grande_neige["authors"][0]["author"]["key"]  # '/authors/OL7440583A'
fabienne_clauss = requests.get(URL_FMT.format(key=key)).json()
print(f"{fabienne_clauss = }")

"""
POST_URL = "http://localhost:8080/api/import/ia"
print(requests.post(POST_URL, json=fabienne_clauss).text)
print(requests.post(POST_URL, json=la_grande_neige).text)
"""

NEW_URL = "https://openlibrary.org/api/new.json"
fabienne_clauss.pop("created")
fabienne_clauss.pop("last_modified")
fabienne_clauss.pop("latest_revision")
print(requests.post(NEW_URL, json=fabienne_clauss).text)
# --> Permission Denied.
