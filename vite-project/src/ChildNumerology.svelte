<script>

let fileContent = '';

async function fetchCharacterTraits() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('https://Astrologi.onrender.com/characterTraits', {
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
            console.log(data.fileContent); // Обработка полученного ответа
            // Здесь можно добавить логику для отображения информации пользователю
            fileContent = data.fileContent;
        } else {
            console.error('Failed to fetch character traits info');
        }
    }


async function fetchEducationRecommendations() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('https://Astrologi.onrender.com/educationRecommendations', {
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
            console.log(data.message); // Обработка полученного ответа
            // Здесь можно добавить логику для отображения информации пользователю
            fileContent = data.fileContent;
        } else {
            console.error('Failed to fetch education recommendations');
        }
    }


    async function fetchProfessionInfo() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('https://Astrologi.onrender.com/professionInfoKids', {
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
            console.log(data.message); // Обработка полученного ответа
            // Здесь можно добавить логику для отображения информации пользователю
            fileContent = data.fileContent;
        } else {
            console.error('Failed to fetch profession info');
        }
    }
</script>

<main>
    <h1>Hello</h1>
    <button on:click={fetchCharacterTraits}>Характе, сильные и слабые стороны</button>
    <button on:click={fetchEducationRecommendations}>рекомендации по воспитанию</button>
    <button on:click={fetchProfessionInfo}>професия</button>

    <div>
        {#if fileContent}
            <div class="file-content">{fileContent}</div>
        {/if}
    </div>
</main>