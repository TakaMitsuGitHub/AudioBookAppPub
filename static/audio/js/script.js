

fetch('/audio/api/book_titles/')
    .then(response => response.json())
    .then(data => {
        let select = document.getElementById('book-select');
        data.forEach(item => {
            let option = document.createElement('option');
            option.value = option.textContent = item.title;
            select.appendChild(option);
        });
    })
    .catch(error => console.error('Error:', error));
