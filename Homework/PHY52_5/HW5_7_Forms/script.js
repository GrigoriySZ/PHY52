document.addEventListener('DOMContentLoaded', () => {
    
    // Сохраняем элемениты формы
    const form = document.getElementById('registration-form');
    const inputUserName = document.getElementById('user-name');
    const inputUserAge = document.getElementById('user-age');
    const fieldsetUserDiet = document.getElementById('user-diet');
    const fieldsetUserRestrict = document.getElementById('user-restrict');
    const inputDietCheckboxes = document.querySelectorAll('#user-diet input');
    const inputRestrictCheckboxes = document.querySelectorAll('#user-restrict input');
    const inputInviteCode = document.getElementById('invite-code');
    const inputAboutUser = document.getElementById('about-user');
    const inputAboutCounter = document.getElementById('about-counter');
    const submitBtn = document.querySelector('#registration-form button[type="submit"]');

    const isValidFields = {
        userName: null,
        userAge: null, 
        userDiet: null, 
        userRestricts: null, 
        inviteCode: null,
        aboutUser: null
    }

    function validateName(userName) {
        const trimedName = userName.trim();
        const regex = /^(([A-Za-zА-Яа-яЁё]{1,})\s+){1,}([A-Za-zА-Яа-яЁё]{1,})$/;

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

    function validateCheckboxesSet(cbSetName, needChecked) {
        // Сохраняем нобор чекбоксов по категории
        const cbSet = document.querySelectorAll(`input[name=${cbSetName}]`);
        // Считаем отмеченные чекбоксы в ккатегории
        const checkedCbSet = document.querySelectorAll(`input[name=${cbSetName}]:checked`);
        let minLimit = needChecked;

        // Определяем количество чекбоксов
        if (cbSet.length <= needChecked) {
            minLimit = Math.floor(cbSet.length / 2); 
        }

        if (checkedCbSet.length < minLimit) {
            checkedCbSet.forEach(cb => {
                cb.classList.add('invalid');
                cb.classList.remove('valid');
            })
            return {isValid: false, error: `Необходмо выбрать минимум ${minLimit}`};
        }

        checkedCbSet.forEach(cb => {
                cb.classList.add('valid');
                cb.classList.remove('invalid');
            })
        return {isValid: true, error: null};
    }

    function validInviteCode(inviteCode) {
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

        if (trimedText.length < 50) {
            return {isValid: false, error: 'Эссе о себе должно содержать минимум 50 символов'};
        }

        return {isValid: true, error: null};
    };

    function showError(inputElement, errorMess) {
        const errorContainer = document.querySelector(`.error-mess[data-for="${inputElement.id}"]`);

        if (errorContainer) {
            errorContainer.textContent = errorMess;
            errorContainer.style.display = 'block';
        }

        inputElement.classList.add('invalid');
        inputElement.classList.remove('valid');
    };

    function hideError(inputElement) {
        const errorContainer = document.querySelector(`.error-mess[data-for="${inputElement.id}"]`);

        if (errorContainer) {
            errorContainer.textContent = '';
            errorContainer.style.display = 'none';
        }

        inputElement.classList.add('valid');
        inputElement.classList.remove('invalid');
    };

    form.addEventListener('input', () => {
        const isFormValid = Object.values(isValidFields).every(value => value === true);

        submitBtn.disabled = !isFormValid;
    })

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const btnText = document.getElementById('btnText');
        const btnSpinner = document.getElementById('btnSpinner');

        btnText.style.display = 'none';
        btnSpinner.style.display = 'inline';
        submitBtn.disabled = true;

        const timedSubmit = setTimeout(() => {
            btnText.style.display = 'inline';
            btnSpinner.style.display = 'none';
            submitBtn.disabled = false;
            alert('Заявка отправлена');
        }, 2000)

    });

    inputUserName.addEventListener('input', (e) => {
        const validateRes = validateName(e.target.value);

        if (validateRes.isValid === true) {
            hideError(e.target);
        } else {
            showError(e.target, validateRes.error);
        }

        isValidFields.userName = validateRes.isValid; 
    });

    inputUserAge.addEventListener('input', (e) => {
        const validateRes = validateAge(e.target.value);

        if (validateRes.isValid === true) {
            hideError(e.target);
        } else {
            showError(e.target, validateRes.error);
        }

        isValidFields.userAge = validateRes.isValid; 
    });

    inputInviteCode.addEventListener('input', function(e) {
        const currentText = e.target.value.toUpperCase().replace(/[^A-Z0-9]/g, '');
        let formattedText = ''; 

        for (let i = 0; i < currentText.length; i++) {
            if (i === 4) {
                formattedText += '-';
            }
            formattedText += currentText[i];
        }

        e.target.value = formattedText.substring(0, 9);
        
        const validateRes = validInviteCode(formattedText);

        if (validateRes.isValid === true) {
            hideError(e.target);
        } else {
            showError(e.target, validateRes.error);
        }

        isValidFields.inviteCode = validateRes.isValid; 
    });

    inputAboutUser.addEventListener('input', (e) => {
        const validateRes = validateAboutText(e.target.value);
        const currentCount = e.target.value.length;
        const needToInput = 50 - currentCount; 
        const result = (needToInput > 0) ? needToInput : 0;

        if (validateRes.isValid === true) {
            hideError(e.target);
        } else {
            showError(e.target, validateRes.error);
        }

        inputAboutCounter.innerText = result;

        isValidFields.aboutUser = validateRes.isValid; 
    });

    inputDietCheckboxes.forEach(cb => {
        cb.addEventListener('change', (e) => {
            const validateRes = validateCheckboxesSet(e.target.name, 2);  

            if (validateRes.isValid === true) {
                hideError(e.target.parentElement.parentElement);
            } else {
                showError(e.target.parentElement.parentElement, validateRes.error);
            }

            isValidFields.userDiet = validateRes.isValid; 
            console.log(isValidFields);
        });
    });

    inputRestrictCheckboxes.forEach(cb => {
        cb.addEventListener('change', (e) => {
            const validateRes = validateCheckboxesSet(e.target.name, 1);  

            if (validateRes.isValid === true) {
                hideError(e.target.parentElement.parentElement);
            } else {
                showError(e.target.parentElement.parentElement, validateRes.error);
            }

            isValidFields.userRestricts = validateRes.isValid; 
            console.log(isValidFields);
        });
    });
});