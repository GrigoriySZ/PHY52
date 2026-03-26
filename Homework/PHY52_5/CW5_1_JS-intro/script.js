// Название корабля
const SHIP_NAME = 'Mantis';  
// Уровень топлива на корабле
let fuelLevel = 100;
// Активность двигателя
let isEngineStarted = false;
// Статус миссии
let missionStatus;
// Переменная с последней ошибкой
let lastError = null;

// Запрашиваем имя капитана от пользователя
let captainsName = prompt('Как вас зовут, капитан?');
// Приветствуем капитана через консоль
console.log(`Добро пожаловать, капитан ${captainsName.toUpperCase()}!`);

// Команда корабля
let crew = ['Спок', 'Леонар "Боунз" Маккой', 'Монтгомери "Скотти" Скотт'];

// Добавляем нового члена команды в начало списка
crew.unshift('Нийота Ухура');
// Удаляем последнего члена экипажа 
let vacationist = crew.pop(); 
// Выводим в консоль количество человек в команде
console.log(`В экипаже сейчас: ${crew.length} человек(а).`);

// Функция для проверки топлива
function checkFuel(amount) {
    if (amount >= fuelLevel) {
        return true;
    } else {
        return false;
    }
};

// Проверяем количество топлива
console.log(checkFuel(150)); 

// Создаем массив с задачами
let tasks = ['проверить шлюз', 'починить робота', 'сварить кофе'];
// Выводим список задач в консоль
console.log('Список задач:')
for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].includes('кофе') === true) {
        console.log(`- ${tasks[i]} (Приоритетно!)`);
    } else {
        console.log(`- ${tasks[i]}`);
    }
}