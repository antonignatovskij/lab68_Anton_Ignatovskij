


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
    let link = event.currentTarget;
    let counterId = link.dataset.counterId;
    let counter = document.getElementById(counterId)
    let url = link.href;

    let response = await makeRequest(url)
    counter.innerText = response.likes_count;
    if (response.liked){
        link.innerHTML = '<i class="bi bi-hand-thumbs-up-fill"></i>'
    }
    else {
        link.innerHTML = '<i class="bi bi-hand-thumbs-up"></i>'
    }

}

function onLoad() {
    let links = document.querySelectorAll('[data-key="likes"]');
    for (let link of links) {
        link.addEventListener('click', onClick);
    }
}

window.addEventListener("load", onLoad);