document.addEventListener('DOMContentLoaded', () => {

    // Установка куки в строке
    function setCookie(name, value, days) {
        let expires = '';
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + days * 24 * 60 * 1000);
            expires = '; expires=' + date.toUTCString();
        }
        // Добавляем куки на сервер
        document.cookie = `${name}=${encodeURIComponent(value)}${expires}; path=/`
    }

    // Получение куки
    function getCookie(nameC) {
        const name = nameC + '=';
        const cookis = document.cookie.split(';');
        // ['name1=value1', ' name2=value2', ' name3=value3']
        for (let i=0; i<cookis.length; i++) {
            let c = cookis[i].trimStart();
            if (c.indexOf(name) === 0) {
                return decodeURIComponent(c.substring(name.length, c.length));
            }
        }
        return null;
    }

    // Удаление куки
    function deleteCookie(name) {
        document.cookie = name + '=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    }

    // Применить тему
    function applyTheme(themeName) {
        
        // Объявляем 
        const link = document.getElementById('theme-style');
        if(!link) return; 

        // Определяем положение 
        const isRoot = !window.location.pathname.includes('/pages/');
        
        // Подключаем темы 
        link.href = isRoot ? `styles/${themeName}.css` : `../styles/${themeName}.css`;
        
        // Устанавливаем атрибуты, чтобы css переменные могли переключиться
        document.documentElement.setAttribute('data-theme', themeName);
    }

    const savedTheme = localStorage.getItem('cryptoTheme') || 'neon-green';
    applyTheme(savedTheme);

    const themeSelect = document.querySelectorAll('#themeSelect, #dashThemeSelect');
    // Устанавливаем 
    themeSelect.forEach(el => el.value = savedTheme);

    window.addEventListener('storage', (e) => {
        if (e.key === 'cryptoTheme' && e.newValue) {
            applyTheme(e.newValue);
            themeSelect.forEach(el => el.value = el.newValue);
        }
    });

    // login.html

    const logForm = document.getElementById('loginForm');
    if (logForm) {
        const themeSelect = document.getElementById('themeSelect');
        const periodSelect = document.getElementById('periodSelect');
        const checkBoxes = [
            document.getElementById('assetBTC'), 
            document.getElementById('assetETH'),
            document.getElementById('assetSOL')
        ];

        const draftRaw = sessionStorage.getItem('configDraft');
        if (draftRaw) {
            try {
                const draft = JSON.parse(draftRaw);
                if (draft.theme) themeSelect.value = draft.theme;
                if (draft.period) periodSelect.value = draft.period;
                if (Array.isArray(draft.assets)) {
                    draft.assets.forEach(asset => {
                        const cb = document.getElementById('asset' + asset);
                        if (cb) cb.checked = true;
                    });
                }
                applyTheme(themeSelect.value);
            } catch (err) { 
                console.error('Ошибка кэширования', err);
            };
        }

        function saveDraft() {
            const selectedAssets = [];
            checkBoxes.forEach(cb => {
                if (cb.checked) selectedAssets.push(cb.value);
            });
        
            sessionStorage.setItem('configDraft', JSON.stringify({
                theme: themeSelect.value,
                period: periodSelect.value,
                assets: selectedAssets
            }));
        }
        
        
        themeSelect.addEventListener('change', () => {
            saveDraft(); 
            applyTheme(themeSelect.value);
        });

        periodSelect.addEventListener('change', saveDraft);
        checkBoxes.forEach(cb => cb.addEventListener('change', saveDraft));

        logForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const apiKey = document.getElementById('apiKey').value.trim();
            if (!apiKey) return alert('Введите API-ключ');
            localStorage.setItem('cryptoTheme', themeSelect.value);
            localStorage.setItem('cryptoPeriod', periodSelect.value);

            const selectedAssets = checkBoxes.filter(cb => cb.checked).map(cb => cb.value);

            localStorage.setItem('cryptoPortfolio', JSON.stringify(selectedAssets.length ? selectedAssets: ['BTC', 'ETH', 'SOL']));
            
            sessionStorage.removeItem('configDraft');
            setCookie('sessionToken', apiKey, 1);
            window.location.href = 'dashboard.html';
        });
    }

    // dashboard.html
    const dashboardContainer = document.getElementById('assetsContainer');
    if (dashboardContainer) {
        if (!getCookie('sessionToken')) {
            window.location.href = 'login.html';
            return
        }
        const dashThemeSelect = document.getElementById('dashThemeSelect');
        const dashPeriodSelect = document.getElementById('dashPeriodSelect');
        const logoutBtn = document.getElementById('logoutBtn');

        dashThemeSelect.value = localStorage.getItem('cryptoTheme') || 'neon_green';
        dashPeriodSelect.value = localStorage.getItem('cryptoPeriod') || '5';

        dashThemeSelect.addEventListener('change', () => {
            localStorage.setItem('cryptoTheme', dashThemeSelect.value);
            applyTheme(dashThemeSelect.value);
        });

        logoutBtn.addEventListener('click', () => {
            deleteCookie('sessionToken');
            window.location.href = 'login.html';
        });

        // ГЕНЕРАЦИЯ ЖИВЫХ ДАННЫХ

        const basePrice = {BTC: 64200, ETH: 3450, SOL: 118};
        const portfolio = JSON.parse(localStorage.getItem('cryptoPortfolio'));

        function renderAssets () {
            dashboardContainer.innerHTML = '';
            portfolio.forEach(asset => {
                const base = basePrice[asset];

                // Задаём изменения
                const change = (Math.random() * 4) - 2;  // от -2% до +2%;

                // Задаем измененную цену
                const price = (base * (1 + change / 100)).toFixed(2);
                const isUp = change >= 0;  // Флаг для проверки повышения цены
                const card = document.createElement('div');
                card.className = 'card asset-card';
                card.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3>${asset}</h3>
                        <span>LIVE</span>
                    </div>
                    <p>${price}</p>
                    <p style="color: ${isUp ? '#00ff66' : '#ff4444'}";>
                        ${isUp ? '+' : '-'} ${Math.abs(change).toFixed(2)}%
                    </p>
                `;
                dashboardContainer.appendChild(card);
            });

            document.querySelectorAll('.chart-bar').forEach(bar => {
                bar.style.height = (Math.random() * 65 -15) + '%';
            });
}
            let intervalId;
            
            function startRefresh() {
                clearInterval(intervalId);
                const period = parseInt(dashPeriodSelect.value);
                renderAssets();
                intervalId = setInterval(renderAssets, period * 1000);
            }

            dashPeriodSelect.addEventListener('change', startRefresh);

            startRefresh();
        

    }

});