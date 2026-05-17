
// API для поиска локации
const LOCATION_API = 'https://geocoding-api.open-meteo.com/v1/search';
// API для получения погоды
const WEATHER_API = ' https://api.open-meteo.com/v1/forecast';
// WMO коды погоды
const weatherCodes = {
    0: {textRu: 'Ясно', textEn: 'Clear sky', icon: 'wi-day-sunny'},
    1: {textRu: 'Преимущественно ясно', textEn: 'Mainly clear', icon: 'wi-day-cloudy'},
    2: {textRu: 'Переменная облачность', textEn: 'Partly cloudy', icon: 'wi-cloud'},
    3: {textRu: 'Пасмурно', textEn: 'Overcast', icon: 'wi-cloudy'},
    45: {textRu: 'Туман', textEn: 'Fog', icon: 'wi-fog'},
    48: {textRu: 'Изморозь', textEn: 'Depositiong rime fog', icon: 'wi-fog'},
    51: {textRu: 'Слабая морось', textEn: 'Light drizzle', icon: 'wi-sprinkle'},
    53: {textRu: 'Моросящий дождь', textEn: 'Moderate drizzle', icon: 'wi-sprinkle'},
    55: {textRu: 'Плотная морось', textEn: 'Dense intensity drizzle', icon: 'wi-sprinkle'},
    56: {textRu: 'Легкая ледяная морось', textEn: 'Light freezing drizzle', icon: 'wi-rain-mix'},
    57: {textRu: 'Ледяная морось', textEn: 'Dense freezing drizzle', icon: 'wi-rain-mix'},
    61: {textRu: 'Небольшой дождь', textEn: 'Slight rain', icon: 'wi-rain'},
    63: {textRu: 'Дождь', textEn: 'Moderate rain', icon: 'wi-rain'},
    65: {textRu: 'Сильный дождь', textEn: 'Heavy rain', icon: 'wi-rain'},
    66: {textRu: 'Легкий ледяной дождь', textEn: 'Light freezing rain', icon: 'wi-rain-mix'},
    67: {textRu: 'Сильный ледяной дождь', textEn: 'Heavy freezing rain', icon: 'wi-rain-mix'},
    71: {textRu: 'Небольшой снег', textEn: 'Slight show', icon: 'wi-snow'},
    73: {textRu: 'Снег', textEn: 'Moderate snow', icon: 'wi-snow'},
    75: {textRu: 'Сильный снег', textEn: 'Heavy snow', icon: 'wi-snow'},
    77: {textRu: 'Крупицы снега', textEn: 'Snow grains', icon: 'wi-snowflake-cold'},
    80: {textRu: 'Небольшой ливень', textEn: 'Slight rain shower', icon: 'wi-showers'},
    81: {textRu: 'Ливень', textEn: 'Moderate rain shower', icon: 'wi-showers'},
    82: {textRu: 'Сильный ливень', textEn: 'Heavy eain shower', icon: 'wi-showers'},
    85: {textRu: 'Легкий снегопад', textEn: 'Slight snow shower', icon: 'wi-snow'},
    86: {textRu: 'Сильный снегопад', textEn: 'Heavy snow shower', icon: 'wi-snow'},
    95: {textRu: 'Гроза', textEn: 'Thunderstorm', icon: 'wi-thunderstorm'},
    96: {textRu: 'Небольшая гроза с градом', textEn: 'Thunderstorm with slight hail', icon: 'wi-thunderstorm'},
    99: {textRu: 'Сильная гроза с градом', textEn: 'Thunderstorm with heavy hail', icon: 'wi-thunderstorm'}
}

// Элементы страницы
const locationInput = document.getElementById('location-input');
const forecatDaysInput = document.getElementById('forecast-days-input');
const requestBtn = document.getElementById('request-btn');
const resultContainer = document.getElementById('result-container');
const currentWeatherContainer = document.getElementById('current-weather');
const dailyWeatherContainer = document.getElementById('daily-weather');
const errorContainer = document.getElementById('error-msg-container');
const pageLanguage = document.documentElement.lang;

// Конвертеры даты
const options = {month: 'short', day: 'numeric'};
const ruDate = (rowDate) => new Intl.DateTimeFormat('ru', options).format(rowDate);
const enDate = (rowDate) => new Intl.DateTimeFormat('en', options).format(rowDate);

const inputLang = (inputDate) => /^[а-яА-ЯёЁ]{1,}$/.test(inputDate) ? 'ru' : 'en';

// Функция для получения коодинат локации по названию [location] в зависимости от языка страницы [language]
async function getLocation(location, language) {
    // Кодируем название места для запроса координат
    const encodeLocation = encodeURIComponent(location); 
    
    // Ссылка на получение координат локации 
    const url = `${LOCATION_API}?name=${encodeLocation}&language=${language}&format=json`;
    // console.log(url);

    // Отправляем запрос с данными
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Ошибка сервера ${response}`);
    }

    // Десериализуем JSON в объект
    const data = await response.json();
    if (!data.results || data.results.length === 0) {
        throw new Error('Локацика не найдена');
    }

    // Передаем первый город из запроса
    return data.results[0];
};

// Функция для получения прогноза погоды на [forecastDays] дней в месте с координатми [latitude, longitude]
async function getWeather(latitude, longitude, forecastDays) {
    // Ссылка запроса к API для получения погоды
    const url = `${WEATHER_API}?latitude=${latitude}&longitude=${longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min&current=weather_code,temperature_2m&timezone=auto&forecast_days=${forecastDays}`;
    // console.log(url);
    // Отправляем запрос к API
    const response = await fetch(url);

    // Проверяем ошибки
    if (!response.ok) {
        throw new Error('Ошибка получения данных погоды')
    }

    // Десериализуем JSON с погодой в объект
    const data = await response.json(); 

    return data;
};

// Функция вывода текущей погоды [currentData] в локации [locationName]
function showCurrentWeather(locationName, currentData, currentUnit) {
    // Постоянная с погодой в данный момент 
    const currentWeather = currentData.weather_code ? weatherCodes[currentData.weather_code] : {
        textRu: 'Неизвестно', 
        textEn: 'Unknown', 
        icon: 'wi-na'
    };
    const textLang = pageLanguage === 'ru' ? 'textRu' : 'textEn';

    // Выводим текущую погоду на страницу
    currentWeatherContainer.innerHTML = `
        <div class="weather-box">
            <h3 class="location-name">${locationName}</h3>
            <div class="weather-row">
                <i class="wi ${currentWeather.icon}"></i>
                <div class="temperature-col">
                    <p class="tempetature">${currentData.temperature_2m}${currentUnit}</p>     
                </div>
            </div>
            <p class="weather-text">${currentWeather[textLang]}</p>
        </div>
    `;
}; 

// Функция вывода прогноза погоды [dailyData] на следующие [forecastDays] дней
function showDailyForecast(dailyData, dailyUnit, forecastDays) {
    // Определяем язык страницы
    const textLang = pageLanguage === 'ru' ? 'textRu' : 'textEn';

    // Очищаем контейнер перед выводом
    dailyWeatherContainer.innerHTML = '';

    // Распаковываем данные из API
    for (let i = 0; i < forecastDays; i++) {

        // Код и описание погоды
        const code = dailyData.weather_code[i];
        const weather = code ? weatherCodes[code] : {
            textRu: 'Неизвестно', 
            textEn: 'Unknown', 
            icon: 'wi-na'
        };
        const date = new Date(dailyData.time[i]);

        // Создаем карточку для погоды
        const card = document.createElement('div');
        card.classList.add('weather-card');
        const formatedDate = pageLanguage === 'ru' ? ruDate(date) : enDate(date);

        // Заполняем карточку данными
        card.innerHTML = `
            <div class="weather-box">
                <h3 class="weather-time">
                    ${pageLanguage === 'ru' ? ruDate(date) : enDate(date)}
                </h3>
                <div class="weather-row">
                    <i class="wi ${weather.icon}"></i>
                    <div class="temperature-col">
                        <p>
                            ${dailyData.temperature_2m_max[i]}${dailyUnit}
                        </p>
                        <p>
                            ${dailyData.temperature_2m_min[i]}${dailyUnit}
                        </p>
                    </div>
                </div>
                <p class="weather-text">${weather[textLang]}</p>
            </div>
        `;

        dailyWeatherContainer.appendChild(card);
    }
}; 

// Функция загрузки погоды
async function loadWeather() {
    // Получение данных из запросов
    const trimedLocation = locationInput.value.trim();
    const forecastDays = Number(forecatDaysInput.value);
    
    // Очищаем контейнеры
    errorContainer.textContent = '';
    errorContainer.classList.remove('active');
    currentWeatherContainer.innerHTML = '';
    dailyWeatherContainer.innerHTML = '';

    // Проверяем поля ввода
    if (!trimedLocation) {
        errorContainer.textContent = "Введите название города";
        errorContainer.classList.add('active');
        return;
    }

    // Запускаем функции с запросами и выводами
    try {
        // Запрашиваем координаты по имени локации
        const location = await getLocation(trimedLocation, pageLanguage);

        // Запрашиваем погоду по координатам
        const weather = await getWeather(
            location.latitude, 
            location.longitude,
            forecastDays
        );

        // Выводим погоду
        showCurrentWeather(
            location.name,
            weather.current,
            weather.current_units.temperature_2m
        );
        showDailyForecast(
            weather.daily, 
            weather.daily_units.temperature_2m_max,
            forecastDays
        );
    } catch(error) {
        errorContainer.textContent = error.message;
        errorContainer.classList.remove('active');
    }
};
