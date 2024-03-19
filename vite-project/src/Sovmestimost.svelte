<script>
    let fileContent = '';


    async function fetchPartner1File() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

    const response = await fetch('https://Astrologi.onrender.com/partner1Info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            idToken,
            accessToken
        })
    });

    if (response.ok) {
        const data = await response.json();
        fileContent = data.fileContent;
    } else {
        console.error('Ошибка при получении файла');
    }
}


async function fetchPartner2Info() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');
        const partnerBirthDate = localStorage.getItem('partnerBirthDate'); // Дата рождения партнера 2 из локального хранилища
        const partnerBornAtNight = localStorage.getItem('partnerBornAtNight'); // Булево значение, был ли рожден партнер 2 с 0 до 3

        const response = await fetch('https://Astrologi.onrender.com/partner2Info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                idToken,
                accessToken,
                partnerBirthDate,
                partnerBornAtNight
            })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message); // Обработка полученного ответа
            // Здесь можно добавить логику для отображения информации пользователю
            fileContent = data.fileContent;
        } else {
            console.error('Failed to fetch partner 2 info');
        }
    }



    async function compatibility() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');
        const partnerBirthDate = localStorage.getItem('partnerBirthDate'); // Дата рождения партнера 2 из локального хранилища
        const partnerBornAtNight = localStorage.getItem('partnerBornAtNight'); // Булево значение, был ли рожден партнер 2 с 0 до 3

        const response = await fetch('https://Astrologi.onrender.com/compatibility', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                idToken,
                accessToken,
                partnerBirthDate,
                partnerBornAtNight
            })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message); // Обработка полученного ответа
            // Здесь можно добавить логику для отображения информации пользователю
            fileContent = data.fileContent;
        } else {
            console.error('Failed to fetch partner 2 info');
        }
    }

</script>


<button on:click={fetchPartner1File}>Партнер 1</button>
<button on:click={fetchPartner2Info}>Партнер 2</button>
<button on:click={compatibility}>Совместимость</button>
<p></p>
{#if fileContent}
    <div class="file-content">{fileContent}</div>
{/if}