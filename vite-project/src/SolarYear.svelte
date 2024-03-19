<script>
    let interestedYear; // Переменная для хранения интересующего года
    let fileContent = '';

    async function fetchSolarYearInfo() {
        const idToken = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');

        const response = await fetch('https://Astrologi.onrender.com/solarYearInfo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                idToken,
                interestedYear,
                accessToken
            })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message); // Обработка полученного ответа
            // Здесь можно добавить логику для отображения информации пользователю
            fileContent = data.fileContent;
        } else {
            console.error('Failed to fetch solar year info');
        }
    }
</script>


<input type="number" bind:value={interestedYear} placeholder="Введите интересующий год" />
<button on:click={fetchSolarYearInfo}>Получить информацию о солярном годе</button>
{#if fileContent}
    <div class="file-content">{fileContent}</div>
{/if}