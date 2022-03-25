const updateURL = () => {
    const selectElement = document.getElementById('filter');
    return selectElement.addEventListener('change', (event) => {
        window.location.href = `/artworks?category=${event.target.value}`
    })
}

updateURL()