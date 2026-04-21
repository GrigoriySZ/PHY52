// API для поиска фильмов
const BASE_URL = 'http://www.omdbapi.com/';
const APIKEY = '54326f80';

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

// http://www.omdbapi.com/?apikey=54326f80&s=Harry&type=movies&page=1

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
    moviesGrid.innerHTML = movies.map(movie => `
        <div class="movie-card">
            <img src="${movie.Poster}">
            <div>${movie.Type}</div>
            <h3>${movie.Title}</h3>
            <div class="movie-info-text">${movie.Year}</div>
            <button onclick="getDetails('${movie.imdbID}')">Details</button>
        </div>
        `).join('');  // объединяем фильмы при помощи .join();
}

// Функция устройства пагинации результата
function setupPagination (total, title, type, page) {
    // Очищаем переменную
    pagination.innerHTML = '';
    currentPage = page;
    const pagesCount = Math.ceil(total / 10);  // Определяем количество страниц
    
    // Добавляем кнопку первой страницы
    const firstPageBtn = document.createElement('button');
    firstPageBtn.innerHTML = '<<';
    firstPageBtn.className = 'nav-btn';
    firstPageBtn.disabled = currentPage === 1;
    firstPageBtn.onclick = () => {
        window.scrollTo(0, 0);
        loadMovies(title, type, 1);
    }
    pagination.appendChild(firstPageBtn);

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
    const lastPageBtn = document.createElement('button');
    lastPageBtn.innerHTML = '>>';
    lastPageBtn.className = 'nav-btn';
    lastPageBtn.disabled = currentPage === pagesCount;
    lastPageBtn.onclick = () => {
        window.scrollTo(0, 0);
        loadMovies(title, type, pagesCount);
    }
    pagination.appendChild(lastPageBtn);

}

// Функция получения результатов запроса
async function getDetaild () {

}