import requests
from flask import request
from utils.config import Config


def makeRequest(url: str):
    data = {
        "client": {
            "clientId": "safesearch",
            "clientVersion": "1.0.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "POTENTIALLY_HARMFUL_APPLICATION", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    r = requests.post(f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={Config().safeSearch}",
                      json=data,
                      headers={"Content-Type": "application/json"}
                      )  # Requesting Googles Safebrowsing api

    return r.json()


def safeSearch():
    url = request.args.get('url')
    r = makeRequest(url)
    score = 0
    if "matches" in r:
        for match in r["matches"]:
            if not match["threatType"] == "MALWARE":
                score += 15
            if not match["threatType"] == "SOCIAL_ENGINEERING":
                score += 15
            if not match["threatType"] == "POTENTIALLY_HARMFUL_APPLICATION":
                score += 15
            if not match["threatType"] == "UNWANTED_SOFTWARE":
                score += 15
    else:
        score += 60

    return {"check": "safe-search", "max_score": 60, "score": score}
