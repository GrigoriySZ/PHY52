// Сохраняем элемениты формы
const form = document.getElementById('registration-form');
const inputUserName = document.getElementById('user-name');
const inputUserAge = document.getElementById('user-age');
const fieldsetUserDiet = document.getElementById('user-diet');
const fieldsetUserRestrict = document.getElementById('user-restricts');
const inputDietCheckboxes = document.querySelectorAll('#user-diet input');
const inputRestrictCheckboxes = document.querySelectorAll('#user-restricts input');
const inputInviteCode = document.getElementById('invite-code');
const inputAboutUser = document.getElementById('about-user');
const submitmBtn = document.querySelector('#registration-form button[type="submit"]');

function validateName(userName) {
    const trimedName = userName.trim();
    const regex = /^*([A-Za-zА-Яа-яЁё-]{2,})\s+([A-Za-zА-Яа-яЁё-]{2,})$/;

    if (trimedName === '') {
        return {isValid: false, error: 'Имя не должно быть пустым'};
    }

    if (!regex.test(trimedName)) {
        return {isValid: false, error: 'Необходимо ввести имя и фамилию'};
    }

    return {isValid: true, error: null};
}; 

function validateAge(userAge) {
    if (userAge === '') {
        return {isValid: false, error: 'Поле ввода не может быть пустым'};
    }
    
    if (userAge < 18) {
        return {isValid: false, error: 'Возраст должен быть больше 18 лет'};
    }

    if (userAge > 100) {
        return {isValid: false, error: 'Возраст должен быть меньше 100 лет'};
    }

    return {isValid: true, error: null};
};

function vadidInviteCode(inviteCode) {
    const trimedCode = inviteCode.trim();
    const regex = /^[a-zA-Z]{4}-\d{4}$/;

    if (trimedCode === '') {
        return {isValid: false, error: 'Поле пригласительного кода не может быть пустым'};
    }

    if (!regex.test(trimedCode)) {
        return {isValid: false, error: 'Код не соответствет шаблону (ABCD-1234)'};
    }

    return {isValid: true, error: null};
};

function validateAboutText(text) {
    const trimedText = text.trim();

    if (trimedText === '') {
        return {isValid: false, error: 'Поле ввода не может быть пустым'};
    }

    if (trimedText.lenght < 50) {
        return {isValid: false, error: 'Эссе о себе должно содержать минимум 50 символов'};
    }

    return {isValid: true, error: null};
};

function showError(inputElement, errorMess) {
    const errorContainer = document.querySelector(`.error-mess[date-for="${inputElement.id}"]`);
    if (errorContainer) {
        errorContainer.textContent = errorMess;
        errorContainer.computedStyleMap.display = 'block';
    }

    inputElement.classList.add('invalid');
    inputElement.classList.remove('valid');
};

function hideError(inputElement) {
    const errorContainer = document.querySelector(`.errorMess[data-for="${inputElement.id}"]`);
    if (errorContainer) {
        errorContainer.textContent = '';
        errorContainer.style.display = 'none';
    }

    inputElement.classList.add('valid');
    inputElement.classList.remove('invalid');
};

form.addEventListener('submit', (e) => {
    e.preventDefault();
});