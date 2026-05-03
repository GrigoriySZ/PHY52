document.addEventListener('DOMContentLoaded', () => {
    // TASK 1
    // Функция для установки куки 
    function setCookie(name, value, days) {
        let expires = '';
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + days * 24 * 60 * 1000);
            expires = '; expires=' + date.toUTCString();
        }

        document.cookie = `${name}=${encodeURIComponent(value)}${expires}; path=/`
    }

    // Функция для получения куки
    function getCookie(nameC) {
        const name = nameC + "=";
        const cookies = document.cookie.split(';');

        for (let i=0; i<cookies.length; i++) {
            let c = cookies[i].trimStart();
            if (c.indexOf(name) === 0) {
                return decodeURIComponent(c.substring(name.length, c.length));
            }
        }
        return null;
    }

    // Функция удаления куки
    function deleteCookie(name) {
        document.cookie = name + '=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    }

    // Кнопки навигации
    const signInBtn = document.getElementById('sign-in');
    const logOutBtn = document.getElementById('log-out');

    // Сохраняем форму ввода
    const greetingForm = document.getElementById('greeting-form');
    if (greetingForm) {
        // Сохраняем поля ввода
        const userFirstName = document.getElementById('user-first-name');
        const userLastName = document.getElementById('user-last-name');
        const userRank = document.getElementById('user-rank');
        const formRows = document.querySelectorAll('.form-row');
        

        const userCookie = getCookie('userInfo');
        if (userCookie) {
            try {
                const userCookieData = JSON.parse(userCookie);
                if (userCookieData.firstName) userFirstName.value = userCookieData.firstName;
                if (userCookieData.lastName) userLastName.value = userCookieData.lastName;
                if (userCookieData.rank) userRank.value = userCookieData.rank;
            } catch (err) {
                console.error('Ошибка кеширования', err);
            };

            formRows.forEach(row => {
                row.style.display = 'none';
            })
            
            const greetContainer = document.getElementById('greet-container');

            // Создаем элементы и добавляем поля
            const greetRow = document.createElement('span');
            greetRow.innerText = `${userFirstName.value} ${userLastName.value}`;
            greetRow.className = 'greet-row';
            
            // Добавляем элемент в контейнр
            greetContainer.appendChild(greetRow);

            logOutBtn.style.display = 'flex';
            signInBtn.style.display = 'none';

        } else {
            // Инициализируем черновик поля ввода
            const draftRaw = sessionStorage.getItem('formDraft');
            if (draftRaw) {
                try {
                    const draft = JSON.parse(draftRaw);
                    if (draft.firstName) userFirstName.value = draft.firstName;
                    if (draft.lastName) userLastName.value = draft.lastName;
                    if (draft.rank) userRank.value = draft.rank;
                } catch (err) {
                    console.error('Ошибка кеширования', err);
                };
            }

            function saveDraft() {
                sessionStorage.setItem('formDraft', JSON.stringify({
                    firstName: userFirstName.value,
                    lastName: userLastName.value,
                    rank: userRank.value
                }));
            }
            
            // Добавляем отслеживание изменения полей
            userFirstName.addEventListener('input', saveDraft);
            userLastName.addEventListener('input', saveDraft);
            userRank.addEventListener('change', saveDraft);
        }

        // Добавляем отслеживание отправки данных
        greetingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const userInfo = JSON.stringify({
                firstName: userFirstName.value,
                lastName: userLastName.value,
                rank: userRank.value
                });
            setCookie('userInfo', userInfo, 7);
            sessionStorage.removeItem('formDraft');
            greetingForm.style.display = 'none';

            logOutBtn.style.display = 'flex';
            signInBtn.style.display = 'none';
        });
    }

    logOutBtn.addEventListener('click', () => {
        deleteCookie('userInfo');
        window.location.href = 'index.html';
    });

    // TASK 2
    // Функция получения темы
    function applyTheme(themeName) {

        // Записывам тему страницы
        const themeLink = document.getElementById('theme-style');
        if(!themeLink) return;

        // Подключаем тему
        themeLink.href = `styles/${themeName}.css`;

        // Ищем кнопку смены темы на экране
        const themeIcons = document.querySelectorAll('.theme-icon');

        themeIcons.forEach(icon => {
            if (icon.id !== themeName && icon.classList.contains('active')) {
                icon.classList.remove('active');
            };

            if (icon.id === themeName) {
                icon.classList.add('active');
            }
        });
        document.documentElement.setAttribute('date-theme', themeName);
    } 

    // Функция сохранения темы в локальное хранилище
    function saveTheme() {
        const themeIcons = document.querySelectorAll('.theme-icon');
        themeIcons.forEach(icon => {
            if (icon.classList.contains('active')) {
                localStorage.setItem('quizyTheme', icon.id);
            };
        });
    }

    // Получаем тему из локального хранилища
    const savedTheme = localStorage.getItem('quizyTheme') || 'light';
    
    // Применяем полученую тему
    applyTheme(savedTheme);

    // Отслеживаем изменение локального хранилища из других мест
    window.addEventListener('storage', (e) => {
        if (e.key === 'quizyTheme' && e.newValue) {
            applyTheme(e.newValue);
        }
    });

    const themeBtn = document.getElementById('theme-btn');

    // Добавляем отслеживание событий на кнопку смены темы
    themeBtn.addEventListener('click', () => {
        const currTheme = document.getElementById('theme-style'); 
        if (currTheme.href.includes('light')) {
            applyTheme('dark');
        } else {
            applyTheme('light');
        }
        saveTheme();
    });

    // TASK 3
    // Сохраняем кнопки 
    const answerBnt = document.getElementById('answer');
    const blindAnswerBtn = document.getElementById('blind-answer');
    
    // Получаем данные игры из sessionStorage 
    const gameScore = document.getElementById('score');
    const storageScoreRaw = sessionStorage.getItem('countDraft');
    if (storageScoreRaw) {
        try {
            const storageScore = JSON.parse(storageScoreRaw);
            if (storageScore.score) gameScore.innerText = storageScore.score;
        } catch (err) {
            console.error('Ошибка кэширования', err);
        };
    }

    // Функция сохранения счета в сессионное хранилище
    function saveScore() {
        const currScore = document.getElementById('score');
        sessionStorage.setItem('countDraft', JSON.stringify({
            score: currScore.innerText
        }));
    }

    // Добавляем отслеживание событий кнопкам
    answerBnt.addEventListener('click', () => {
        let currentScore = gameScore.innerText;
        gameScore.innerText = ++currentScore;
        saveScore();
    })

    blindAnswerBtn.addEventListener('click', () => {
        let currentScore = gameScore.innerText; 
        const randomChance = Math.random();
        if (randomChance > 0.5) {
            gameScore.innerText = ++currentScore;
            saveScore();
        }
    })

});