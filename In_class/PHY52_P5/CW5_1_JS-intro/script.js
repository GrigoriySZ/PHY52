// - комментарии в JS 

// В современном виде JS есть 8 видов данных:

// - Примитивы
// 1. Number() - числовой тип данных
// 2. String() - строчный тип данных
// 3. Boolean() - true/false
// 4. null - пустота
// 5. undefined - значение по умолчанию для необъявленных переменный

// - Объекты
// 6. Object: array(массивы данных), function(функции), object(объекты)

// let age = 32;
// let name = 'Grisha';
// let isStudent = true;
// console.log(`Name: ${name}, age: ${age}`);  // Вывод в консоль

// let testVar;
// console.log(`Значение testVar: ${testVar}`);
// console.log(typeof testVar);

// let car = null;
// console.log(`Значение car: ${car}`);
// console.log(typeof car);  // Консоль покажет object - это является старой ошибкой JS

// console.log(null == undefined);  // сравнение по значениям
// console.log(null === undefined);  // строгое сравнение и по типу данных

// console.log(5 == '5');  // true
// console.log(5 === '5');  // false

// 3 способа объявлять переменные:
// var - функциональная область видимости (глобальная)
// let - блочная область видимости (локальная)
// const - постоянное значение (константа)

// ! Ошибка при попытки изменить константу
// const PI = 3.14;
// console.log(PI);
// PI = 3;

// ! Ошибка при обращении до инициализации переменной let
// console.log(x);
// let x = 10;
// console.log(x);

// Ошбики не возникнет, просто переменная будет undefined, а потом со значением
// console.log(y);
// var y = 10;
// console.log(y);

// Операторы в JS:
// + - сложение
// - - вычетание
// / - деление (всегда дает дробное число, даже при разеделении без остатка)
// * - умножение
// % - целочисленное деление
// ** - возведение в степень

// Инкремент (++) - увеличение на один [a +=1 -> a++]
// Декремент (--) - уменьшение на один [a -=1 -> a--]

// let a = 10;
// let b = 3; 
// console.log(a / b); 
// console.log(a ** b);
// let counter = 5;
// counter++;
// console.log(counter);

// Операторы сравнения:
// > - больше
// < - меньше
// >= - больше или равно
// <= - меньше или равно
// == - нестрогое равенство (значение)
// === - строгое равенство (значение и тип)

// != - нестрогое неравенство (значение) - часто приводит к ошибкам
// !== - строгое неравенство (значение и тип) - предпочтительный вариант

// Логические операторы:
// && - and - возвращает true, если обе операнда истины
// || - or - возвращает true, если один из операндов инстинен
// ! - not - возвращает true, если операнд не инстинен

// let hasMoney = true;
// let isHungry = true;
// let restaurantOpen = false;

// // Пример синтаксиса условных выражений
// if (hasMoney && (isHungry || restaurantOpen)) {
//     console.log('идем обедать');
// } else {
//     console.log('остаемся дома');
// }

// console.log('5' + 2);  // = 52
// console.log('5' - 2);  // = 3
// console.log('five' * 2);  // NaN (not a number)

// console.log('ананас' > 'яблоко');  // Сравнение строк по коичесиву и Unicod
// console.log(true + 1); // true (1) + 1 = 2

// -- ВЫВОД В КОНСОЛЬ --

// alert('Hello'); // - модальное окно
// document.write(); // - прямая запись в HTML
// prompt(); // - позволяет ввести текст (возвщарает строку или null при отмене)
// confirm(); // - запрос подверждения [OK-true || Cancel(false)]

// alert('Добро пожаловать!');
// let userName = prompt('Как вас зовут?');
// if (userName !== null){
//     console.log(`Привет, ${userName}`);
// }
// let ageInput = prompt('Сколько тебе лет?');
// let userAge = Number(ageInput)
// if (userAge > 18) {
//     alert('Доступ разрешен!');
// } else if (userAge === 18) {
//     alert('Тебе 18 лет');
// } else {
//     alert('Доступ запрещен!');
// }

// let isAdmin = confirm('Ты администратор?');
// console.log(`Статус админа: ${isAdmin}`); 

// Тернарный оператор для записи в одну строку
// условие ? значение_если_true : значение_если_false

// let userAge = 20;
// let access = (userAge >= 18) ? 'Разрешено' : 'Запрещено';
// console.log(access)

// // Конструкция switch case - сравнение с несколькими значениями
// let color = 'red';
// switch (color) {
//     case 'red':
//         console.log('stop');
//         break;
//     case 'green': 
//         console.log('go');
//         break;
//     default:
//         console.log('светофор сломался');
// }

// -- ЦИКЛЫ --
// for 
// while - проверяет условие переда каждой итеррацией
// do...while

// let i = 0; 
// while (i < 3) {
//     console.log(i);
//     i++;
// }

// for i in range(3):  - Python
// for (let i = 0; i < 3; i++) {
//     console.log(i);
// }

// let count = 0; 
// do {
//     console.log('Выполнюсь хотя бы один раз');
//     count++;
// } while (count < 0);

// for (let i = 1; i <= 20; i++) {
//     if (i % 3 === 0 && i % 5 === 0) {
//         console.log('FizzBuzz');
//     } else if (i % 3 === 0) {
//         console.log('Fizz');
//     } else if (i % 5 === 0) {
//         console.log('Buzz');
//     } else {
//         console.log(i);
//     }
// }

// -- СТРУКТУРЫ ДАННЫХ --
// String & Array
// в JS нет срезов и отрицательного обращения к индексу
// let str = 'abracadabra';
// console.log(str[3]);
// console.log(str.length);  // это свойство
// console.log(str.toUpperCase());  // toLowerCase() - для смены регистра
// console.log(str.includes('dab'));  // true/false - проверяет наличие подстроки в строке
// console.log(str.slice(3, 6));  // Делает сред в диапазоне от 3 до 6
// let str2 = '       apple, orange, kiwi           ';
// console.log(str2.trim());  // Уберает пробелы по краям строки
// console.log(str2.split(','));  // Делит строку по разделителю 

// for (let i = 0; i < str.length; i++) {
//     console.log(str[i]);
// }

// let nums = [6, 8, 3, 4, 2, 0];
// nums.push(10);  // значение добавляет в конец массива
// console.log(nums);
// let end = nums.pop();  // удаляет с конца и возвращает значение
// console.log(end, nums);
// nums.unshift(22);  // добавляет значение в начало массива (медленная операция)
// console.log(nums);
// let start = nums.shift();
// console.log(start, nums);

// for num in nums: 
// nums.forEach(num => console.log(`Число ${num}`));

// let fruits = ['Apple', 'Banana', 'Orange'];
// // map() создает новый массив, трансформируя каждый элемент
// let fruits2 = fruits.map(fruit => fruit.toUpperCase());
// let numbers = [1, 2, 3, 4, 5, 6]; 
// doubled = [number ** number for number in numbers]
// let doubled = numbers.map(number => number ** number);
// let doubled2 = numbers.map(number => number * 2); 
// console.log(fruits, fruits2);
// console.log(numbers, doubled, doubled2); 

// списковое включение:
// -- ФИЛЬТР --
// Создает список из элементов, подходящих под условие 
// evens = [num for num in nums if num % 2 == 0]
// let evens = numbers.filter(num => num % 2 === 0);
// console.log(evens);  // [2, 4, 6]

// -- ФУНКЦИИ -- 
// function sayHello(name) {
//     return `Hello, ${name}`;
// }

// let message = sayHello('Student'); 
// alert(message);

// -- ФУНКЦИОНАЛЬНОЕ ВЫРАЖЕНИЕ --
const multiply = function(a, b) {
    return a * b;
}

console.log(multiply(2, 5)); 

// -- СТРЕЛОЧНАЯ ФУНКЦИЯ --
const square = (n) => {
    return n * n;
}
// Сокращенный вариант стрелочной функции
const double = n => n * 2;

console.log(square(3));