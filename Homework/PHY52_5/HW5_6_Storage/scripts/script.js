document.addEventListener('DOMContentLoaded', () => {
    const alarmHandle = document.getElementById('alarm-handle'); 

    // Функция усиановка куки 
    function setCookie(name, value, minutes) {
        let expires = '';
        if (minutes) {
            const date = new Date();
            date.setTime(date.getTime() + minutes * 1000);
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

    // Функция применения тревоги
    function applyAlarm() {
        // Получаем информацию о синглае из локального хранилища
        const isAlarm = localStorage.getItem('isAlarm') || false;
        // Элементы вигнала
        const alarmSignal = document.getElementById('alarm-signal');
        const alarmHadle = document.getElementById('alarm-handle');
        // Добавляем класс объектам
        if (isAlarm === true) {
            alarmSignal.classList.add('alarm');
            alarmHadle.classList.add('alarm');
        } else {
            alarmSignal.classList.remove('alarm');
            alarmHadle.classList.remove('alarm');
        }
    };

    applyAlarm();

    window.addEventListener('storage', (e) => {
        if (e.key === 'isAlarm' && e.newValue) {
            applyAlarm();
        };
    });
    

    alarmHandle.addEventListener('click', () => {
        const isAlarm = localStorage.getItem('isAlarm');
        isAlarm === true 
            ? localStorage.setItem('isAlarm', false) 
            : localStorage.setItem('isAlarm', true);
        applyAlarm();
    });

    const alarmSignal = document.getElementById('alarm-signal');    
    console.log(alarmSignal);
    console.log(alarmSignal.classList);
    console.log(!alarmSignal.classList.contains('alarm'));

});