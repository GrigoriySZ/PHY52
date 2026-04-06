// ЗАДАЧА 1

// Ищем список с книгами по Id списка
const booksList = document.getElementById('books-list');
const books = document.querySelectorAll('#books-list li')
const booksTitle = document.querySelectorAll('.book-title');

// Добавляем слушателя событий
booksList.addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        books.forEach(book => book.classList.remove('active'));
        e.target.classList.add('active');
    } else if (e.target.tagName == 'SPAN') {
        booksTitle.forEach(title => title.parentElement.classList.remove('active'));
        e.target.parentElement.classList.add('active');
    }
})

// ЗАДАЧА 2

// Ищем элемента папок
const folders = document.querySelectorAll('.folder');

// Добавляем всем элементам папки слушатель событий 
folders.forEach(folder => {
    folder.addEventListener('click', function() {

        // Добавляем класс соседнему списку
        this.nextElementSibling.classList.toggle('hidden');
    });
})

// ЗАДАЧА 3

// Получаем элементы кнопки со страницы
const btnLike = document.getElementById('like-btn');
const countElement = document.getElementById('like-counter');

// Инициализируем переменную счетчика
let count = countElement.innerText;

// Добавляем слоушателя событий по клику
btnLike.addEventListener('click', (e) => {
    count++;
    countElement.innerText = count;
})

// ЗАДАЧА 4

// Получаем все кнопки удаления со сотраницы
const removeBtns = document.querySelectorAll('.remove-btn');
console.log(removeBtns);

removeBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        // Ищмем родительский контейнер для кнопки
        const news = this.parentElement;
        console.log(news);
        
        // Удаляем родительский элемент кнопки
        news.remove();
    });
})