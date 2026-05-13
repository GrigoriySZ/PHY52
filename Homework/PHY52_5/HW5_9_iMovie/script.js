// API для поиска фильмов
const BASE_URL = 'http://www.omdbapi.com/';
const APIKEY = '54326f80';

// Переменная для загрузки списка избранных фильмов из локального хранилеща
let favorites = JSON.parse(localStorage.getItem('myMovies')) || [];

// Обновляем счетчик избранного при загрузке страницы
window.onload = () => {
    updateFavCount();
}

// Сохраняем элементы верстки
const searchForm = document.getElementById('search-form');
const moviesGrid = document.getElementById('movie-grid');
const pagination = document.getElementById('pagination');
const modal = document.getElementById('modal');
const modalBody = document.getElementById('modal-body');
const closeModal = document.querySelector('.close-modal');
const favSidebar = document.getElementById('sidebar');
const closeFav = document.getElementById('close-fav');

let currentSearch = '';
let currentPage = 1;
let currentType = '';

// SVG ICONS
const heartIcon = `
    <svg stroke="currentColor" fill="none" stroke-width="2" 
            viewBox="0 0 24 24" stroke-linecap="round" 
            stroke-linejoin="round" height="200px" width="200px" 
            xmlns="http://www.w3.org/2000/svg">
        <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 
                .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 
                4.05 3 5.5l7 7Z"></path>
    </svg>
`;
const heartOffIcon = `
    <svg stroke="currentColor" fill="none" stroke-width="2" 
            viewBox="0 0 24 24" stroke-linecap="round" 
            stroke-linejoin="round" height="200px" width="200px" 
            xmlns="http://www.w3.org/2000/svg">
        <line x1="2" y1="2" x2="22" y2="22"></line>
        <path d="M16.5 16.5 12 21l-7-7c-1.5-1.45-3-3.2-3-5.5a5.5 5.5 0 0 1 2.14-4.35"></path>
        <path d="M8.76 3.1c1.15.22 2.13.78 3.24 1.9 1.5-1.5 2.74-2 4.5-2A5.5 5.5 
                0 0 1 22 8.5c0 2.12-1.3 3.78-2.67 5.17"></path>
    </svg>
`;
const closeIcon = `
    <svg stroke="currentColor" fill="currentColor" stroke-width="20" 
            viewBox="0 0 512 512" height="200px" width="200px" 
            xmlns="http://www.w3.org/2000/svg">
        <path d="m289.94 256 95-95A24 24 0 0 0 351 127l-95 95-95-95a24 24 0 0 
                0-34 34l95 95-95 95a24 24 0 1 0 34 34l95-95 95 95a24 24 0 0 0 34-34z">
        </path>
    </svg>
`;
closeModal.innerHTML = closeIcon;
closeFav.innerHTML = closeIcon;


searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    currentSearch = document.getElementById('title-input').value;
    currentType = document.getElementById('type-input').value; 
    loadMovies(currentSearch, currentType, 1);
})

// http://www.omdbapi.com/?apikey=54326f80&s=Harry&type=movie&page=1

// Функция загрузки фильмов с сервера по запросу
async function loadMovies (title, type, page) {
    const response = await fetch(`${BASE_URL}?apikey=${APIKEY}&s=${title}&type=${type}&page=${page}`);
    // Проверка наличия данных запроса
    if (!response.ok) {
        throw new Error(`Ошибка сервера ${response.status}`);
    }

    // Декодирум результат
    const data = await response.json();

    // Проверяем наличие данных и передаем данные
    if (data.Response === 'True') {
        showMovies(data.Search);
        setupPagination(data.totalResults, title, type, page);
    } else {
        moviesGrid.innerHTML = '<h2>Movie not found</h2>';
        pagination.innerHTML = '';
    }
}

// Функция вывода фильмов на страницу HTML
function showMovies (movies) {

    // Выводим фильмы при помощи .map()
    moviesGrid.innerHTML = movies.map(movie => {
        const isFav = favorites.some(f => f.imdbID === movie.imdbID);
        return `
            <div class="movie-card">
                <button class="btn-fav-add action-btn ${isFav ? 'active' : ''}"
                        onclick="toggleFavorite(
                            '${movie.imdbID}', 
                            '${movie.Title.replace(/'/g, "")}', 
                            '${movie.Year}', 
                            '${movie.Poster}'
                        )">
                    ${heartIcon}
                </button>
                <img 
                    src="${movie.Poster}"
                    onerror="this.onerror=null; this.src='./images/poster-placeholder.png';"
                    alt="Постер"
                >
                <div>${movie.Type}</div>
                <h3>${movie.Title}</h3>
                <div class="movie-info-text">${movie.Year}</div>
                <button class="get-details-btn" onclick="getDetails('${movie.imdbID}')">Details</button>
            </div>
        `;}).join('');  // объединяем фильмы при помощи .join();
}

// Функция добавления в избранное через переключатель
function toggleFavorite(id, title, year, poster) {
    const index = favorites.findIndex(f => f.imdbID === id);
    if (index === -1) {
        favorites.push({imdbID: id, Title: title, Year: year, Poster: poster});
    } else {
        // Мутирует массив на месте и вырезается элемент с id = index
        favorites.splice(index, 1);
    }
    localStorage.setItem('myMovies', JSON.stringify(favorites));
    updateFavCount();
    const currentTitle = document.getElementById('title-input').value;
    if (currentTitle) {
        const btns = document.querySelectorAll(`button[onclick*="${id}"]`);
        console.log(btns);
        btns.forEach(btn => {
            const isActive = favorites.some(f => f.imdbID === id);
            btn.classList.toggle('active', isActive);
        });
    }
}

// Функция обновления счетчика избранных фильмов
function updateFavCount () {
    document.getElementById('fav-count').innerHTML = favorites.length; 
    const list = document.getElementById('fav-list');
    list.innerHTML = favorites.map(m => `
            <div class="fav-item">
                <img 
                    src="${m.Poster}"
                    onerror="this.onerror=null; this.src='./images/poster-placeholder.png';"
                    alt="Постер"
                >
                <div class="fav-item-details" onclick="handleFavItem(event, '${m.imdbID}')">
                    <h4 class="fav-item-title">${m.Title}</h4>
                    <p class="fav-item-year">(${m.Year})</p>
                </div>
                <button class="remove-fav action-btn" onclick="removeFav(event, '${m.imdbID}')">${heartOffIcon}</button>
            </div>
        `).join('');
}

// Функция 
function handleFavItem (e, id) {
    e.stopPropagation();
    getDetails(id);
}

// Функция удаления фильма из избранного
function removeFav (e, id) {
    toggleFavorite(id);
}

// Функция кнопки для открытия боковой панели
function toggleSidebar() {
    favSidebar.classList.toggle('open');
}

// Функция устройства пагинации результата
function setupPagination (total, title, type, page) {
    // Очищаем переменную
    pagination.innerHTML = '';
    currentPage = page;
    const pagesCount = Math.ceil(total / 10);  // Определяем количество страниц
    
    // Добавляем кнопку первой страницы
    const firstBtn = document.createElement('button');
    firstBtn.innerHTML = '<<';
    firstBtn.className = 'nav-btn';
    firstBtn.disabled = currentPage === 1;
    firstBtn.onclick = () => {
        window.scrollTo(0, 0);
        loadMovies(title, type, 1);
    }
    pagination.appendChild(firstBtn);

    // Добавляем кнопку назад
    const prevBtn = document.createElement('button');
    prevBtn.innerHTML = '<';
    prevBtn.className = 'nav-btn';
    prevBtn.disabled = currentPage === 1;
    prevBtn.onclick = () => {
        window.scrollTo(0, 0);
        loadMovies(title, type, currentPage-1);
    };

    pagination.appendChild(prevBtn);

    let start = Math.max(1, currentPage - 2);
    let end = Math.min(pagesCount, start + 4);
    for (let i = start; i <= end; i++) {
        const btn = document.createElement('button');
        btn.innerText = i;
        btn.className = i === currentPage ? 'page-btn active' : 'page-btn';
        btn.onclick = () => {
            window.scrollTo(0, 0)
            loadMovies(title, type, i); 
        };
        pagination.appendChild(btn);
    }

    // Добавляем кнопку вперед
    const nextBtn = document.createElement('button');
    nextBtn.innerHTML = '>';
    nextBtn.className = 'nav-btn';
    nextBtn.disabled = currentPage === pagesCount;
    nextBtn.onclick = () => {
        window.scrollTo(0, 0);
        loadMovies(title, type, currentPage+1);
    }
    pagination.appendChild(nextBtn);

    // Добавляем кнопку первой страницы
    const lastBtn = document.createElement('button');
    lastBtn.innerHTML = '>>';
    lastBtn.className = 'nav-btn';
    lastBtn.disabled = currentPage === pagesCount;
    lastBtn.onclick = () => {
        window.scrollTo(0, 0);
        loadMovies(title, type, pagesCount);
    }
    pagination.appendChild(lastBtn);

}

// Функция получения результатов запроса
async function getDetails (id) {

    // Пример формируемой ссылки
    // https://www.omdbapi.com/?apikey=54326f80&i=tt1201607&plot=full

    // Формеруем запрос по id для получения данных
    const response = await fetch(`${BASE_URL}?apikey=${APIKEY}&i=${id}&plot=full`);
    if (!response.ok) {
        throw new Error(`Ошибка сервера ${response.status}`);
    }

    // Декодируем данные в формат JS
    const movie = await response.json();
    if (movie.Response === 'True') {
        modalBody.innerHTML = `
        <div class="modal-container">
            <img 
                src="${movie.Poster}" 
                class="modal-poster"
                onerror="this.onerror=null; this.src='./images/poster-placeholder.png';"
                alt="Постер"
            >
            <div class="modal-details">
                <h2 class="modal-title">${movie.Title}</h2>
                <p>Рейтинг IMDB: ${movie.imdbRating}</p>
                <p>Дата выхода: ${movie.Released}</p>
                <p>Жанр: ${movie.Genre}</p>
                <p>Актеры: ${movie.Actors}</p>
                <p>Режисcер: ${movie.Director}</p>
            </div>
            <div class="modal-plot-container">
                <h4>Описание</h4>
                <p class="modal-plot">${movie.Plot}</p>
            </div>
        </div>`;
        modal.classList.add('show');
    } else {
        modalBody.innerHTML = '<h2>Детали не найдены</h2>';
    }
};

closeModal.onclick = () => modal.classList.remove('show');
closeFav.onclick = () => favSidebar.classList.remove('open');
window.onclick = (e) => {if (e.target === modal) modal.classList.remove('show');}