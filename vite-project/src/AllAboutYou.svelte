<script>
    let fileContent = '';


async function fetchCharacterInfo() {
    const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
    const accessToken = localStorage.getItem('accessToken');

    const response = await fetch('http://127.0.0.1:5000/getCharacterInfo', {
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
        console.error('Failed to fetch character info');
    }
}


async function fetchSposobnoctiAndMission() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('http://127.0.0.1:5000/SposobnoctiAndMission', {
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
            console.error('Failed to fetch life approaches and methods info');
        }
    }


async function fetchSelfRealizationConditions() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('http://127.0.0.1:5000/selfRealizationConditions', {
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
            console.error('Failed to fetch self-realization conditions info');
        }
    }


async function fetchRecommendationsAndWarnings() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('http://127.0.0.1:5000/recommendationsAndWarnings', {
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
            console.error('Failed to fetch recommendations and warnings info');
        }
    }


async function fetchMainProblem() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('http://127.0.0.1:5000/mainProblem', {
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
            console.error('Failed to fetch main problem info');
        }
    }


    async function fetchHealthInfo() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('http://127.0.0.1:5000/healthInfo', {
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
            console.error('Failed to fetch health info');
        }
    }


    async function fetchProfessionInfo() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('http://127.0.0.1:5000/professionInfo', {
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


    async function fetchApproachesAndMethods() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('http://127.0.0.1:5000/approachesAndMethods', {
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
            console.error('Failed to fetch approaches and methods info');
        }
    }
</script>

<main>
    <h1>Hello</h1>

    <button on:click={fetchCharacterInfo}>Характер и сознания</button>
    <button on:click={fetchApproachesAndMethods}>Подходы и методы в жизни</button>
    <button on:click={fetchSposobnoctiAndMission}>Способность и миссии</button>
    <button on:click={fetchSelfRealizationConditions}>Условия и задачи для самореалиации</button>
    <button on:click={fetchRecommendationsAndWarnings}>рекомендации и предостеряжения</button>
    <button on:click={fetchMainProblem}>Главная проблема</button>
    <button on:click={fetchHealthInfo}>здоровье</button>
    <button on:click={fetchProfessionInfo}>професия</button>

    <div>
        {#if fileContent}
            <div class="file-content">{fileContent}</div>
        {/if}
    </div>

</main>