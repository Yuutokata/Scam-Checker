document.getElementById("submit-url").addEventListener("click", async function(event) {
    let url = document.getElementById("url-input").value
    const valid = isValidUrl(url)

    if(!valid) {
        showErrorMessage()
        return
    }

    hideErrorMessage()

    url = url.replace("https://", "").replace("http://", "")

    hideSubmitButton()
    showCurrentCheck()

    await checkSafeSearch(url)
})

document.getElementById("new-request").addEventListener("click", function (event) {
    resetCurrentCheck()
    showSubmitButton()
})

function hideErrorMessage() {
    const errorMessage = document.getElementById("error-message")
    errorMessage.classList.add("hidden")
}

function showErrorMessage() {
    const errorMessage = document.getElementById("error-message")
    errorMessage.classList.remove("hidden")
}

function hideSubmitButton() {
    const submitButton = document.getElementById("submit-url")
    submitButton.classList.add("hidden")
}

function showSubmitButton() {
    const submitButton = document.getElementById("submit-url")
    submitButton.classList.remove("hidden")
}

function showCurrentCheck() {
    const currentCheck = document.getElementById("current-check")
    currentCheck.classList.remove("hidden")
}

function resetCurrentCheck() {
    const currentCheck = document.getElementById("current-check")
    currentCheck.classList.add("hidden")

    const safeSearch = document.getElementById("safe-search")
    safeSearch.classList.remove("check-icon")
    safeSearch.classList.add("load-icon")

    const phishing = document.getElementById("phishing")
    phishing.classList.remove("check-icon")
    phishing.classList.add("wait-icon")

    const dns = document.getElementById("dns")
    dns.classList.remove("check-icon")
    dns.classList.add("wait-icon")

    document.getElementById("progress-bar").style.width = "0"
    document.getElementById("score").innerText = ""
    document.getElementById("rating").innerText = ""
    document.getElementById("new-request").classList.add("hidden")
}

function isValidUrl(string) {
    let url;

    try {
        url = new URL(string);
    } catch (_) {
        return false;
    }

    return url.protocol === "http:" || url.protocol === "https:";
}
