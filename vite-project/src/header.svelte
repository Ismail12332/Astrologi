<script>
    import { Link } from "svelte-navigator";
    import { onMount } from 'svelte';
    import Auth0 from 'auth0-js';


    let webAuth;
    let isAuthenticated = false;

    onMount(() => {
        webAuth = new Auth0.WebAuth({
            domain: 'dev-whbba5qnfveb88fc.us.auth0.com',
            clientID: 'ab7q8GJ0KvwbL0zAC6UwwLaQcXjgbUGT',
            redirectUri: 'http://localhost:5173/',
            responseType: 'token id_token',
            scope: 'openid profile email',
        });

        // Проверяем, есть ли токен в URL
        webAuth.parseHash((err, authResult) => {
            if (authResult && authResult.accessToken && authResult.idToken) {
                // Сохраняем токен в локальном хранилище
                localStorage.setItem('accessToken', authResult.accessToken);
                localStorage.setItem('idToken', authResult.idToken);
                localStorage.setItem('email', authResult.idTokenPayload.email);

                // Отправляем запрос на сервер для добавления пользователя в базу данных
                const formData = {
                    email: authResult.idTokenPayload.email,
                    id_token_hash: authResult.idToken,
                    accessToken: authResult.accessToken
                };
                fetch('http://127.0.0.1:5000/test', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Ошибка при добавлении пользователя');
                    }
                })
                .then(data => {
                    // Пользователь успешно добавлен в базу данных
                    // Генерируем ключ доступа и сохраняем его в локальном хранилище (если нужно)
                    // Например, localStorage.setItem('accessToken', data.accessToken);
                })
                .catch(error => {
                    console.error('Ошибка:', error);
                });

                // Перенаправляем пользователя на домашнюю страницу или другую страницу после успешной аутентификации
                window.location.href = '/';
            }
        });

        // Проверяем, есть ли токен доступа в локальном хранилище
        const accessToken = localStorage.getItem('accessToken');
        if (accessToken) {
            isAuthenticated = true;
        }
    });

    async function loginWithGoogle() {
        webAuth.authorize();
    }

    function showProfileModal() {
        const modal = document.getElementById('profile-modal');
        modal.style.display = 'block';
    }

    function closeProfileModal() {
        const modal = document.getElementById('profile-modal');
        modal.style.display = 'none';
    }

    // Close the modal if the user clicks outside of it
    window.onclick = function(event) {
        var modal = document.getElementById('RegistForm');
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }


    function makeActive(button) {
        // Убираем класс 'active' у всех кнопок
        var buttons = document.querySelectorAll('.knopki button');
        buttons.forEach(function(btn) {
            btn.classList.remove('active');
        });

        // Добавляем класс 'active' только к нажатой кнопке
        button.target.classList.add('active');
    }

    async function logout() {
        // Очищаем локальное хранилище
        localStorage.removeItem('email');
        localStorage.removeItem('accessToken');
        localStorage.removeItem('idToken');
        isAuthenticated = false;
        
        // Дополнительно выход с Auth0
        webAuth.logout({
            returnTo: 'http://localhost:5173/',
            client_id: 'ab7q8GJ0KvwbL0zAC6UwwLaQcXjgbUGT',
        });
    }
</script>

<style>
    /*TOP */
.verx {
    margin: 20px;
}

.knopki {
    display: flex;
    justify-content: center;
    padding: 10px;
    margin-right: 10px;
    
}

.knopki button {
    margin-right: 100px; /* Измените значение на необходимое расстояние */
    border: none;
    outline: none;
    background-color: white;
}

.knopki button.active {
    font-weight: bold; /* Шрифт жирный для активной кнопки */
}


.vxod {
    display: flex;
    justify-content: flex-end;
    margin-right: 75px;
}

.vxod button {
    border: none;
    outline: none;
    background-color: rgb(255, 255, 255);
}

/* модальные окна */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
    position: absolute;
    top: 50%;
    width: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
}

.close {
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
}
</style>

<main>
    <div class="verx">
        <div>
            <h1>Астролигия</h1>
        </div>
        <div class="knopki">
            <Link to={"/"}>
                <button on:click={makeActive}>Главная</button>
            </Link>

            <Link to={`/Onas`}>
                <button on:click={makeActive}>О нас</button>
            </Link>

            <Link to={`/Sviz`}>
                <button on:click={makeActive}>Связь</button>
            </Link>
            {#if isAuthenticated}
            <Link to={`/Astrologimap`}>
                <button on:click={makeActive}>Астральная карта</button>
            </Link>
            {/if}
        </div>
        <div class="vxod">
            {#if isAuthenticated}
            <div class="profile-container">
                <!-- Изображение профиля -->
                <img src="path/to/profile/image" alt="Profile Image">
                
                <!-- Кнопка для открытия модального окна -->
                <button on:click={showProfileModal}>Профиль</button>
            </div>
        
            <!-- Модальное окно -->
            <div id="profile-modal" class="modal">
                <div class="modal-content">
                    <span class="close" on:click={closeProfileModal}>&times;</span>
                    <h2>Профиль пользователя</h2>
                    <!-- Вкладки с общей информацией, настройками и кнопкой выхода -->
                    <!-- Здесь должен быть код для вкладок -->
                    <!-- Пример: -->
                    <div class="tabs">
                        <!-- Вкладка с общей информацией -->
                        <button>Общая информация</button>
                        <!-- Вкладка с настройками -->
                        <button>Настройки</button>
                        <!-- Кнопка выхода из аккаунта -->
                        <button on:click={logout}>Выход</button>
                    </div>
                </div>
            </div>
            {:else}
                <button on:click={loginWithGoogle}>Вход с помощью Google</button>
            {/if}
        </div>
    </div>
</main>