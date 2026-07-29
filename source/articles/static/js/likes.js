


async function makeRequest(url, method = "GET") {
    let response = await fetch(url, { method: method })
    if (response.ok) {
        return await response.json();
    } else {
        let error = await response.json();
        // throw new Error("Возникла ошибка",error.message);
        let p = document.createElement('p');
        p.innerText = "Возникла ошибка";
        p.style.color = 'red';
        container.appendChild(p);
    }
}

async function onClick(event) {
    event.preventDefault();
    like = 1
    let link = event.target;
    let counterId = link.dataset.counterId;
    let counter = document.getElementById(counterId)
    let url = link.href;
    counter.innerText = 'response.test';
    link.innerHTML = '<i class="bi bi-hand-thumbs-up-fill"></i>'

}

function onLoad() {
    let links = document.querySelectorAll('[data-key="likes"]');
    for (let link of links) {
        link.addEventListener('click', onClick);
    }
}

window.addEventListener("load", onLoad);