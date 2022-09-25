#!/usr/bin/env python3

import json

import requests


headers = {
    "Authorization": "Bearer 8b161d77b4b84b3ebc4f77f9a8b011273085bfb470a24061b99be7880b2df9c4"
}


def get_sentry(latest_release_only: bool = True) -> dict:
    url = "https://sentry.archive.org/api/0/projects/ia-ux/ol-web/issues/"
    params = {"query": "first-release:latest", "environment": "production"}
    if not latest_release_only:
        params.pop("query")
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(url, params=params)
        response.raise_for_status()
        print(response.status_code)
        data = response.json()
        print(len(data))
        return data


if __name__ == "__main__":
    # print(get_sentry())
    with open("sentry_latest.json", "w") as out_file:
        json.dump(get_sentry(), out_file)  # 22 events
    with open("sentry_all.json", "w") as out_file:
        json.dump(get_sentry(False), out_file)  # 100 events

