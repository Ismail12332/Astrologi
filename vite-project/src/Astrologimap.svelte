<script>
    import { onMount } from 'svelte';
    import Header from "./header.svelte";
    import Footer from "./footer.svelte";

    let birthDate;
    let answer;

    function opendataberd () {
        var modal = document.getElementById('heppybey')
        modal.style.display = 'block';
    }

    function closeCreateSectionModal() {
        var modal = document.getElementById('heppybey')
        modal.style.display = 'none';
    }

    async function submitForm() {
        const token = localStorage.getItem('idToken'); // Получение токена из localStorage
        const accessToken = localStorage.getItem('accessToken');
        const response = await fetch('https://Astrologi.onrender.com/update_user_info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',// Отправка токена в заголовке
            },
            body: JSON.stringify({
                birthDate,
                bornAtNight: answer, // 'yes' или 'no'
                idTokenHash: token,
                accessToken
            })
        });

        const responseData = await response.json();
        if (responseData.success) {
            showModal();
            // Обработка успешного обновления данных пользователя
            console.log(responseData.message);
        } else {
            // Обработка ошибок
            console.error(responseData.error);
        }
    }


    function showModal() {
        const modal = document.getElementById('optionsModal');
        modal.style.display = 'block';
    }

    function closeModal() {
        const modal = document.getElementById('optionsModal');
        modal.style.display = 'none';
    }

    function showAllAboutYou() {
        window.location.href = '/AllAboutYou';
        // Логика отображения информации о личном солярном годе
        console.log("Личный солярный год");
        closeModal();
    }

    function showCompatibility() {
        document.getElementById('compatibilityModal').style.display = 'block';
        // Логика отображения информации о совместимости
        console.log("Совместимость");
        closeModal();
    }

    function showChildNumerology() {
        window.location.href = '/ChildNumerology';
        // Логика отображения информации о детской нумерологии
        console.log("Детская нумерология");
        closeModal();
    }

    function showSolirnuy() {
        window.location.href = '/SolarYear';
        // Логика отображения информации об Astrologi
        console.log("солярном год");
        closeModal();
    }


    function closeModals() {
        document.getElementById('optionsModal').style.display = 'none';
        document.getElementById('compatibilityModal').style.display = 'none';
    }

    function savePartnerData() {
        const partnerBirthDate = document.getElementById('partnerBirthDate').value;
        const partnerBornAtNight = document.getElementById('partnerBornAtNight').checked;
        localStorage.setItem('partnerBirthDate', partnerBirthDate);
        localStorage.setItem('partnerBornAtNight', partnerBornAtNight);
        window.location.href = '/Sovmestimost';
    }
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
        height: 300px;
    }

    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
    }

    .form {
        display: flex;
    }
</style>

<main>
    <Header/>
    <div class="smotr">
        <button on:click={opendataberd}>Смотреть астральную карту</button>
    </div>
    <div id="heppybey" class="modal">
        <div class="modal-content">
            <span class="close" on:click={closeCreateSectionModal}>&times;</span>
            <h1>Заполните форму</h1>
            <form on:submit|preventDefault={submitForm} class="form">
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

    <div id="optionsModal" class="modal" style="display:none;">
        <div class="modal-content">
            <span class="close" on:click={closeModal()}>&times;</span>
            <h1>Выберите опцию</h1>
            <ul>
                <li><button on:click={showAllAboutYou}>Все о личном</button></li>
                <li><button on:click={showSolirnuy}>солярном год</button></li>
                <li><button on:click={showCompatibility}>Совместимость</button></li>
                <li><button on:click={showChildNumerology}>Детская нумерология</button></li>
            </ul>
        </div>
    </div>

    <div id="compatibilityModal" class="modal" style="display:none;">
        <div class="modal-content">
            <span class="close" on:click={closeModals()}>&times;</span>
            <h1>Введите данные партнера</h1>
            <div>
                <label for="partnerBirthDate">Дата рождения партнера:</label>
                <input type="date" id="partnerBirthDate">
            </div>
            <div>
                <label for="partnerBornAtNight">Рожден с 0 до 3:</label>
                <input type="checkbox" id="partnerBornAtNight">
            </div>
            <button on:click={savePartnerData}>Сохранить</button>
        </div>
    </div>

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