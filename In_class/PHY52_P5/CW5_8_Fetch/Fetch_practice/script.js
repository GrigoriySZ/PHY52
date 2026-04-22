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
const modal = document.getElementById('madal');
const modalBody = document.getElementById('modal-body');
const closeModal = document.querySelector('.close-modal');

let currentSearch = '';
let currentPage = 1;
let currentType = '';

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

    // console.log(movies);
    // Выводим фильмы при помощи .map()
    moviesGrid.innerHTML = movies.map(movie => {
        const isFav = favorites.some(f => f.imdbID === movie.imdbID);
        return `
            <div class="movie-card">
                <button class="btn-fav-add ${isFav ? 'active' : ''}"
                        onclick="toggleFavorite(
                            '${movie.imdbID}', 
                            '${movie.Title.replace(/'/g, "")}', 
                            '${movie.Year}', 
                            '${movie.Poster}'
                        )">
                    ${isFav ? '❤' : '🤍'}
                </button>
                <img src="${movie.Poster}">
                <div>${movie.Type}</div>
                <h3>${movie.Title}</h3>
                <div class="movie-info-text">${movie.Year}</div>
                <button onclick="getDetails('${movie.imdbID}')">Details</button>
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
        btns.forEach(btn => {
            const isActive = favorites.some(f => f.imdbID === id);
            btn.classList.toggle('active', isActive);
            btn.innerHTML = isActive ? '❤' : '🤍';
        });
    }
}

// Функция обновления счетчика избранных фильмов
function updateFavCount () {
    document.getElementById('fav-count').innerHTML = favorites.length; 
    const list = document.getElementById('fav-list');
    list.innerHTML = favorites.map(m => `
            <div class="fav-item" onclick="handleFavItem(event, "${m.imdbID}")">
                <img src="${m.Poster}">
                <div>
                    <h4>${m.Title}</h4>
                    <p>${m.Year}</p>
                </div>
                <button class="remove-fav" onclick="removeFav(event, "${m.imdbID}")">&times;</button>
            </div>
        `).join('');
}

// Функция 
function handleFavItem (e, id) {
    getDetails(id);
}

// Функция удаления фильма из избранного
function removeFav (e, id) {
    e.stopPropagation();
    toggleFavorite(id);
}

// 
function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('open');

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
        <div>
            <img src="${movie.Poster}">
            <div>
                <h2>${movie.Title}</h2>
                <p>Рейтинг IMDB: ${movie.imdbRating}</p>
                <p>Дата выхода: ${movie.Released}</p>
                <p>Жанр: ${movie.Genre}</p>
                <p>Актеры: ${movie.Actors}</p>
                <p>Режисcер: ${movie.Director}</p>
                <p>${movie.Plot}</p>
            </div>
        </div>`;
        modal.classList.add('show');
    } else {
        modalBody.innerHTML = '<h2>Детали не найдены</h2>';
    }
}

closeModal.onclick = () => modal.classList.remove('show');
window.onclick = (e) => {if (e.target === modal) modal.classList.remove('show');}