from flask import request
import PyFunceble


def dns_records():
    url = request.args.get("url")
    check = PyFunceble.URLReputationChecker(url).get_status()  # Status ob PyFunceble die URl/Domain als malicious sieht
    score = 0
    if check.is_malicious():
        score += 0
    if not check.is_malicious():
        score += 20

    return {"check": "dns_records", "max_score": 20, "score": score}
