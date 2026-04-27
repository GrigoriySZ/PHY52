// Сохраняем элементы панели редактирования
const titleSetting = document.getElementById('title-setting');
const descriptionSetting = document.getElementById('description-setting');
const priceSetting = document.getElementById('price-setting');
const colorSetting = document.getElementById('color-editor');

// Созраняем элементы карточки товара
const productTitle = document.getElementById('product-title');
const productDescription = document.getElementById('description-container');
const productCost = document.getElementById('product-cost');
const siteBody = document.querySelector('body');
const layout = document.getElementById('layout');
const productImg = document.getElementById('product-img');
const wishlistBtn = document.getElementById('wishlist');
const wishlistCounter = document.getElementById('wishlist-counter');

// Добавляем исходный текст в инпуты панели
titleSetting.value = productTitle.textContent;
descriptionSetting.value = productDescription.innerText;
priceSetting.value = productCost.innerText;

let likeCount = parseInt(wishlistCounter.innerText);
let isLiked = false;

// Обработчик событий изменения заголовка
titleSetting.addEventListener('input', () => {
    productTitle.textContent = titleSetting.value; 
});

// Обработчик событий изменения описания
descriptionSetting.addEventListener('input', () => {
    productDescription.innerHTML = '';
    const newText = descriptionSetting.value.replace(/\n/g, '</p><p>');
    productDescription.innerHTML = `<p>${newText}</p>`;
});

// Обработчик событий изменения цены
priceSetting.addEventListener('input', () => {
    const units = parseInt(priceSetting.value);
    const subunits = parseInt(priceSetting.value*100 % 100);
    productCost.innerHTML = `<span id="product-cost">${units}.<span class="subunit">${subunits}</span>`;
});

// Добавляем селекторам цветовой темы слушатель событий
colorSetting.addEventListener('change', (e) => {
    const theme = e.target.value;
    siteBody.className = theme;
});

// Добавляем эфект изменения цвета кнопке like
wishlistBtn.addEventListener('click', () => {
    wishlistBtn.classList.toggle('active');
    if (!isLiked) {
        ++likeCount;
        isLiked = true;
    } else {
        --likeCount
        isLiked = false;
    }
    wishlistCounter.innerText = likeCount;
});

// Добавляем увеличение картинки при наведении
productImg.addEventListener('mouseenter', () => {
    productImg.classList.add('active');
    layout.style.display = 'block';
});

// Убераем увеличение картинки
productImg.addEventListener('mouseleave', () => {
    productImg.classList.remove('active');
    layout.style.display = 'none';
});

