// КУКИ
// Функция установка куки 
function setCookie(name, value, minutes) {
    let expires = '';
    if (minutes) {
        const date = new Date();
        date.setTime(date.getTime() + minutes * 60 * 1000);
        expires = '; expires=' + date.toUTCString();
    }
    document.cookie = `${name}=${encodeURIComponent(value)}${expires}; path=/`;
};

// Функция получения куки
function getCookie(nameCookie) {
    const name = nameCookie + '=';
    const cookies = document.cookie.split(';');
    for (let i=0; i<cookies.length; i++) {
        let c = cookies[i].trimStart();
        if (c.indexOf(name) === 0) {
            return decodeURIComponent(c.substring(name.length, c.length));
        };
    }
    return null;
}; 

// Функция удаления куки
function deleteCookie(name) {
    document.cookie = name + '=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
}

// ЛОГИРОВАНИЕ
// Функция логирования
function login() {
    // Получаем элементы страницы
    const username = document.getElementById('user-name').value.trim();
    const accessCode = document.getElementById('access-code').value;
    const accessLevel = document.getElementById('access-lvl').value;
    const error = document.getElementById('login-error');

    if (!username) {
        error.textContent = 'Введите имя';
        error.style.display = 'block';
        return;
    }

    if ((accessLevel === "employee" && accessCode === "1234") || 
        (accessLevel === "admin" && accessCode === "5678")) 
    {
        error.textContent = '';
        error.style.display = 'none';
        setCookie('user', username, 5);
        window.location.href = 'control.html';
    }
    
    error.textContent = 'Неверный код доступа';
        error.style.display = 'block';
        return;
};

// Функция проверки аутентификации пользователя
function checkAuth() {
    // Проверям активного пользователя
    const currentUser = getCookie('user');

    // Перенаправляем на панель управления
    if (currentUser) {
        window.location.href = 'control.html';
    };
};

// Функция проверки необходимости аутентификации
function requireAuth() {
    const user = getCookie('user');

    if (!user) {
        window.location.href = 'index.html';
    }

    return user;
};

// Функция разлогирования
function logout() {
    deleteCookie('user');
    window.location.href = 'index.html';
}

// ПАНЕЛЬ УПРАВЛЕНИЯ
// Функция применения тревоги
function applyAlarm() {
    const alarmIsActive = localStorage.getItem('isAlarm') === 'true';
    const alarmSignal = document.getElementById('alarm-signal');

    if (alarmIsActive) {
        alarmSignal.classList.add('alarm');
    } else {
        alarmSignal.classList.remove('alarm');
    }
};

// Функция загрузки панели управления
function loadControlPanel() {
    // Проверяем наличие авторизованного пользователя
    const user = requireAuth();

    const currentUser = document.getElementById('user-placeholder');
    currentUser.textContent = user;

    const alarmBtn = document.getElementById('alarm-handle');
    const isAlarm = localStorage.getItem('isAlarm') === 'true'; 

    if (isAlarm) {
        alarmBtn.classList.add('alarm');
    }

    applyAlarm();

    alarmBtn.addEventListener('click', (e) => {
        e.target.classList.toggle('alarm');
        localStorage.setItem('isAlarm', alarmBtn.classList.contains('alarm'));
        applyAlarm();
    });
}

window.addEventListener('storage', (e) => {
    if (e.key === 'isAlarm') {
        
        const alarmIsActive = localStorage.getItem('isAlarm') === 'true';
        const alarmBtn = document.getElementById('alarm-handle');
        
        if (alarmIsActive) {
            alarmBtn.classList.add('alarm');
        } else {
            alarmBtn.classList.remove('alarm');
        }

        applyAlarm();
    };
});

// ЖУРНАЛ
// Функция загрузки данных из хранилища
function loadJournal() {
    
    // Проверяем состояния авторизации и тревоги
    requireAuth();
    applyAlarm();

    // Получаем элементы со страницы
    const noteInput = document.getElementById('note-input');
    const noteContainer = document.getElementById('notes-container')
    const journal = document.querySelector('#journal-table tbody');

    // Загружаем данные из хранилища
    const journalNotes = JSON.parse(localStorage.getItem('journalNotes') || '[]') ;
    if (journalNotes.length > 0) {
        journalNotes.map(note => {
            const {id, data, date} = note;
            journal.innerHTML += `
                <tr>
                    <td class="num-col journal-col">${id}</td>
                    <td class="data-col journal-col">${data}</td>
                    <td class="date-col journal-col">${date}</td>
                </tr>
            `
        });
    };

    noteInput.value = sessionStorage.getItem('inputDraw') || '';

    noteInput.addEventListener('input', () => {
        sessionStorage.setItem('inputDraw', noteInput.value);
    });
};

// Функция очистки записей в поле ввода
function handleClearNote() {
    const noteInput = document.getElementById('note-input');
    const journal = document.querySelector('#journal-table tbody');

    if (noteInput.value === '' && journal.innerHTML === '') return;
    
    localStorage.setItem('journalNotes', []);
    sessionStorage.setItem('inputDraw', '');
    noteInput.value = '';
    journal.innerHTML = ''
};

// Функция добавления записи в журнал
function handleAddNote() {
    const journal = document.querySelector('#journal-table tbody');
    const noteInput = document.getElementById('note-input');
    const journalNotes = JSON.parse(localStorage.getItem('journalNotes') || '[]');

    const inputValue = noteInput.value.trim();
    const nextNum = journal.querySelectorAll('tr').length + 1;

    if (inputValue === '') return;

    const date = new Date().toLocaleString('ru-RU', {dateStyle: 'short', timeStyle: 'medium'});
    const newNote = {id: nextNum, data: inputValue, date: date};

    // Добавляем запись в журнал
    journal.innerHTML += `
        <tr>
            <td class="num-col journal-col">${nextNum}</td>
            <td class="data-col journal-col">${inputValue}</td>
            <td class="date-col journal-col">${date}</td>
        </tr>
    `;

    // Добавляем запись в хранилище
    journalNotes.push(newNote);
    localStorage.setItem('journalNotes', JSON.stringify(journalNotes));

    // Очищаем поле ввода
    noteInput.value = '';
    sessionStorage.setItem('inputDraw', '')
};