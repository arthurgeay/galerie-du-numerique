const updateURLPath = () => {
        const selectElement = document.getElementById('filter');
        const sortElement = document.getElementById('sort');
        let url = '';
        let sortChoices = ["DESC", "ASC"]
        let choice = sortChoices[0]

        let updateChoice = () => {
                return choice = choice == sortChoices[0] ? sortChoices[1] : sortChoices[0]
            }
            // TODO : check the case if category is added after sort 
        let updateFunction = () => {
            if (!url.includes(`sort=`) && !url.includes(`category=`)) {
                console.log('url does not include sort or category')
                url = url + `?sort=${choice}`
                console.log(url)
                updateChoice()

            } else if (!url.includes(`sort=`) && url.includes(`category=`)) {
                console.log('url contains category params but not sort')
                url = url + `&sort=${choice}`
                console.log(url)
                updateChoice()

            } else if (url.includes(`sort=`) && url.includes(`category=`)) {
                console.log('url contains sort params & category')
                console.log(url)
                url = url.replace(url.substring(url.search('sort='), url.length), `&sort=${choice}`)
                updateChoice()
            } else {
                console.log('url contains sort params but not category')
                url = `&sort=${choice}`
                updateChoice()
            }

            console.log("final url", url)

        }
        return sortElement.addEventListener('click', (event => {
            updateFunction()
        }))
    }
    // selectElement.addEventListener('change', (event) => {
    //     console.log('selectElement')
    //     url = `/artworks?sort=${event.target.value}`
    //     window.location.href = url
    // })




updateURLPath()