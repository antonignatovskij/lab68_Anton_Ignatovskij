function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

async function makeRequest(url, method = "GET", body) {
    let headers = {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken
    }
    let requestData = {'method': method, 'headers': headers}
    if (body) {
        requestData['body'] = JSON.stringify(body);
    }
    let response = await fetch(url, requestData);
    return await response.json()
}

async function onClick(event) {
    event.preventDefault();
    let link = event.currentTarget;
    let counter = document.getElementById('calculate-result')
    let url = link.href;
    let body = {
        'a': Number(document.getElementsByName("a")[0].value),
        'b': Number(document.getElementsByName("b")[0].value)
    }
    console.log(body)
    let response = await makeRequest(url, "POST", body)
    console.log(response)
    if ("answer" in response) {
        if (counter.classList.contains('text-danger')) {counter.classList.remove('text-danger')}
        counter.classList.add('text-success')
        counter.innerText = response.answer;
    } else if ("error" in response) {
        if (counter.classList.contains('text-success')) {counter.classList.remove('text-text-success')}
        counter.classList.add('text-danger')
        counter.innerText = response.error;
    }
}

function onLoad() {
    let links = document.querySelectorAll('[data-key="calclink"]');
    for (let link of links) {
        link.addEventListener('click', onClick);
    }
}

window.addEventListener("load", onLoad);