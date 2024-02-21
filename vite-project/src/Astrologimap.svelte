<script>
    import { onMount } from 'svelte';
    import Header from "./header.svelte";
    import Footer from "./footer.svelte";

    let birthDate = '';
    let answer = '';

    let Datebirt = false;

    function opendataberd () {
        var modal = document.getElementById('heppybey')
        modal.style.display = 'block';
    }

    function closeCreateSectionModal() {
        var modal = document.getElementById('heppybey')
        modal.style.display = 'none';
    }

    function submitForm() {
        // Получаем данные из локального хранилища
        const email = localStorage.getItem('email');
        const idToken = localStorage.getItem('idToken');
        const accessToken = localStorage.getItem('accessToken');

        // Формируем данные для отправки на бэкенд
        const formData = {
            email,
            idToken,
            accessToken,
            birthDate,
            answer
        };
        
        // Отправляем данные на бэкенд
        fetch('http://127.0.0.1:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        }).then(response => {
            // Обработка ответа от бэкенда (если необходимо)
            console.log('Данные отправлены успешно');
            Datebirt = true;
            closeCreateSectionModal(); // Закрываем модальное окно после отправки
        }).catch(error => {
            console.error('Ошибка отправки данных:', error);
        });
    }

    onMount(async () => {
        const idToken = localStorage.getItem('idToken');
        const accessToken = localStorage.getItem('accessToken');
        const email = localStorage.getItem('email');
        try {
            const response = await fetch('http://127.0.0.1:5000//api/checldatebird', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    // Здесь можно отправить дополнительные данные для проверки
                    // Например, можете отправить идентификатор пользователя или его токен
                    idToken,
                    accessToken,
                    email
                })
            });

            if (response.ok) {
                const data = await response.json();
                // В этом месте вы можете обработать ответ от сервера
                // Например, если пользователь найден, можете выполнить определенные действия
            } else {
                console.error('Ошибка при проверке пользователя:', response.statusText);
            }
        } catch (error) {
            console.error('Ошибка при отправке запроса:', error);
        }
    });

</script>

<style>
    .smotr {
        display: flex;
        justify-content: flex-end;
    }

    .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.7);
    }

    .modal-content {
        background-color: #fff;
        margin: 10% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 50%;
    }

    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
    }
</style>

<main>
    <Header/>
    {#if !Datebirt}
    <div class="smotr">
        <button on:click={opendataberd}>Смотреть астральную карту</button>
    </div>
    <div id="heppybey" class="modal">
        <div class="modal-content">
            <span class="close" on:click={closeCreateSectionModal}>&times;</span>
            <h1>Заполните форму</h1>
            <form on:submit|preventDefault={submitForm}>
                <label>Дата рождения:</label>
                <input type="date" bind:value={birthDate} required>
                
                <label>Родился с 00:00-03:00:</label>
                <input type="radio" id="yes" name="answer" value="yes" bind:group={answer}>
                <label for="yes">Да</label>
                <input type="radio" id="no" name="answer" value="no" bind:group={answer}>
                <label for="no">Нет</label>
                
                <button type="submit">Отправить</button>
            </form>
        </div>
    </div>
    {:else}
        <h1>Hello</h1>
    {/if}

    <div>
        <p>Астральная карта представляет собой индивидуальное астрологическое изображение небесного свода в определенный момент времени и места на Земле. Эта карта является инструментом астрологии, который используется для анализа и интерпретации натального гороскопа — карты небесного свода, созданной на основе точной даты, времени и места рождения человека.</p>

        <h1>Элементы астральной карты:</h1>
            
        <h1>Знаки Зодиака:</h1> 
        <p>Карта отображает положение знаков Зодиака в момент рождения, что определяет индивидуальные характеристики личности.</p>

        <h1>Планеты:</h1> 
        <p>Позиции планет в различных знаках и домах карты влияют на различные аспекты жизни человека, такие как личность, карьера, отношения и здоровье.</p>

        <h1>Аспекты:</h1>
        <p>Взаимодействие между планетами образует аспекты, которые указывают на потенциальные силы и слабости в натальной карте.</p>

        <h1>Дома:</h1> <p>Дома представляют различные области жизни (например, семья, карьера, друзья) и показывают, как планеты взаимодействуют в каждой из них.</p>
            
        <h1>Индивидуальная консультация:</h1> 
        <p>Астролог использует карту для предоставления клиенту глубокого понимания его характеристик, тенденций и потенциала в различных областях жизни.</p>

        <h1>Самопознание:</h1> 
        <p>Люди могут изучать свою астральную карту, чтобы лучше понять свои сильные и слабые стороны, а также найти направления для личного развития.</p>

        <h1>Прогнозирование:</h1>
        <p>Астрологическая карта может использоваться для предсказания тенденций и событий, которые могут произойти в жизни человека в будущем.</p>

        <h1>Заключение:</h1>
        <p>Астральная карта является мощным инструментом астрологии, который помогает нам глубже понять себя и мир вокруг нас, а также обрести понимание о наших возможностях и потенциале.</p>
    </div>

    <Footer/>
</main>