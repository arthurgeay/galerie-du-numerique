const updateURL = () => {
    const selectElement = document.getElementById('filter');
    return selectElement.addEventListener('change', (event) => {
        console.log(event.target.value)
        window.location.href = `/artworks?category=${event.target.value}`
    })
}

updateURL()