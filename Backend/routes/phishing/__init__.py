import json
from flask import request


def checkPishing(url: str):
    with open("routes/phishing/data.json", "r") as f:  # Öffnet die Liste mit phishing domains
        data = json.load(f)

    for domain in data:
        if domain.lower() == url.lower():
            return True

    return False


def phishing():
    url = request.args.get('url')
    phish = checkPishing(url=url)
    score = 0
    if not phish:
        score += 20
    if phish:
        score += 0

    return {"check": "phishing", "max_score": 20, "score": score}