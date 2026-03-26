// // -- ТЕОРИЯ --

// // Объект похож на словарь из py
// // Объект состоит из ключей (свойств объекта) - (как в словаре Py)
// const user = {
//     name: 'Алексей',
//     age: 35,
//     isAdmin: true
// }

// // Объект можно прочитать так же, как свойства класса
// console.log(user.age);

// // Добавляются свойства через присваивание
// user.city = 'Novosibirsk';
// // Изменение свойст объекта тоже происходит через присваивание
// user.age = 26;
// // Удаление свойства происходит через deleta
// delete user.isAdmin;

// console.log(user);

// // Добавление методов объектам
// const cat = {
//     name: 'Luna',
//     sayMeow: function () {
//         console.log('Meow');
//     }
// }

// // Вызов метода объекта
// cat.sayMeow();

// const arr = [1, 2, 3, 4, 5, 6]; 
// let f = arr.find(el => el===0);
// console.log(f);
// console.log(undefined === false);

// -- ПРАКТИКА 1 --
const employees = [
    {name: "Иван", role: "admin", pin: "1234", attempts: 0}, 
    {name: "Илья", role: "manager", pin: "6666", attempts: 0}, 
    {name: "Петр", role: "worker", pin: "0001", attempts: 0}
];

let loginHistory = [];

function authenticate() {
    let pinInput = prompt('Введите ваш PIN (exit для выхода)');
    if (pinInput === 'exit' || pinInput === '') return 'exit';
    
    let foundUser = employees.find(user => user.pin === pinInput);
    if (foundUser) {
        if (foundUser.attempts >= 3) {
            alert(`Аккаунт ${foundUser.name} заблокирован`);
            return null;
        } 
        foundUser.attempts = 0;
        return foundUser;
    } else {
        employees.forEach(emp => emp.attempts++);
        alert('Неверный PIN');
        return null;
    }
}

function grantAccess(user) {
    if (!user) return;
    let message = '';
    switch (user.role) {
        case 'admin': 
            message =  "Полный доступ к серверной и сейфу";
            break;
        case 'manager': 
            message = "Доступ к офисам и архиву";
            break;
        case 'worker': 
            message = "Доступ только в общий зал";
            break;
        default:
            message = 'Доступ запрещен';
    }
    alert(`${user.name}, приветствуем! ${message}`)
    if (!loginHistory.includes(user.name)) {
        loginHistory.push(user.name);
    }
}

while (true) {
    let result = authenticate();
    if (result === 'exit') break;

    if (result) {
        grantAccess(result);
    }
}

console.log(`Сотрудники, посетившие офис: ${loginHistory.join(', ')}`)