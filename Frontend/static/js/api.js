async function checkSafeSearch(url) {
    await delay(1000)

    const data = await request("/check/safe-search", url, "safe-search", 0)

    checkPhishing(url, data.score)
}

async function checkPhishing(url, score) {
    await delay(1000)

    const data = await request("/check/phishing", url, "phishing", score)

    await checkDNS(url, score + data.score)
}

async function checkDNS(url, score) {
    await delay(1000)

    const response = await request("/check/dns", url, "dns", score)

    document.getElementById("new-request").classList.remove("hidden")

    const finalScore = score + response.score
    const rating = document.getElementById("rating")

    if(finalScore >= 89) {
        rating.innerText = "Eher vertrauenswürdig"
    } else if (finalScore >= 39) {
        rating.innerText = "Vorsicht geboten!"
    } else {
        rating.innerText = "Eher nicht vertrauenswürdig"
    }
}

async function request(endpoint, toCheck, elementId, percent) {
    const element = document.getElementById(elementId)
    element.classList.remove("wait-icon")
    element.classList.add("load-icon")

    const url = `https://api.dominic-habel.me${endpoint}?url=${toCheck}`
    const response = await (await fetch(url)).json()

    await delay(500)

    const score = percent + response.score

    const progressBar = document.getElementById("progress-bar")
    progressBar.style.width = `${score}%`

    countUp(percent, score)

    element.classList.remove("load-icon")

    if(response.score < response["max_score"]) {
        element.classList.add("cross-icon")
    } else {
        element.classList.add("check-icon")
    }

    return response
}

function countUp(start, end) {
    let number = start
    const element = document.getElementById("score")

    setInterval(function () {
        if(number >= end) return

        number++
        element.innerText = `${number}/100`
    }, 20)
}

function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}