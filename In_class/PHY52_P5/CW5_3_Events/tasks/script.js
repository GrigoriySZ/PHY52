// ЗАДАЧА 1
const links = document.querySelectorAll('#link-list li a');
// console.log(links);

links.forEach(link => {
    if (link.getAttribute('href').startsWith('http')) {
        link.classList.add('external-link');
    }
});

// ЗАДАЧА 2
const display = document.getElementById('text-display');
const edit = document.getElementById('text-edit');

document.addEventListener('keydown', (e) => {
    if (e.code === 'KeyE' && e.ctrlKey) {
        e.preventDefault();
        edit.value = display.innerText;
        display.style.display = 'none';
        edit.style.display = 'block';
        edit.focus();
    }
    
    if (e.code === 'KeyS' && e.ctrlKey) {
        e.preventDefault();
        display.innerText = edit.value;
        edit.style.display = 'none';
        display.style.display = 'block';
    }
});

// ЗАДАЧА 3
document.getElementById('nameInput').addEventListener('keypress', (e) => {
    if (/\d/.test(e.key)) {
        e.preventDefault();
    };
})

// ЗАДАЧА 4
const field = document.getElementById('field');
const ball = document.getElementById('ball');

field.addEventListener('click', (e) => {
    const rect = field.getBoundingClientRect();

    let x = e.clientX - rect.left - 50;
    let y = e.clientY - rect.top - 50;

    if (x < 0) x = 0; 
    if (y < 0) y = 0; 
    if (x > rect.width - 100) x = rect.width - 100;
    if (y > rect.height - 100) y = rect.height - 100;
    ball.style.left = x + 'px';
    ball.style.top = y + 'px';

    // console.log(rect.width, rect.height);
    // console.log(rect.right, rect.left);
    // console.log(rect.top, rect.bottom);
});

// ЗАДАЧА 5
let currentLight = -1;



function changeLight() {
    const lamps = ['red', 'yellow', 'green'];
    lamps.forEach(id => document.getElementById(id).classList.remove(id));
    // Циклический сдвиг 
    currentLight = (currentLight + 1) % lamps.length;
    const activeId = lamps[currentLight];
    document.getElementById(activeId).classList.add(activeId);
}

// ЗАДАЧА 6
console.log(new Date(2026, 3, 1).getDay());
function calendar() {
    const m = document.getElementById('calMonth').value-1;  // Считает с нуля
    const y = document.getElementById('calYear').value;
    const container = document.getElementById('calendar-container');
    
    const firstDay = new Date(y, m, 1).getDay();  // День недели первого числа
    // console.log(firstDay);
    const startDay = firstDay === 0 ? 6 : firstDay - 1; 
    const daysInMonth = new Date(y, m+1, 0).getDate();
    console.log(daysInMonth);

    // Создаем шапку
    let html = '<table> <tr> <th>ПН</th> <th>ВТ</th> <th>СР</th> <th>ЧТ</th> <th>ПТ</th> <th>СБ</th> <th>ВС</th> </tr> <tr>';

    // Добавляем пустые ячейки
    for(let i = 0; i < startDay; i++) html += '<td></td>';

    // Заполняем числами
    for (let day = 1; day <= daysInMonth; day++) {
        if ((startDay + day -1) % 7 === 0 && day > 1) html += '</tr><tr>'; 
        html += `<td>${day}</td>`;
    }

    let fill = (startDay + daysInMonth) % 7;
    for(day = startDay; day < fill-1; day++) html += '<td></td>';

    html += '</tr></table>';
    container.innerHTML = html;
}

// ЗАДАЧА 7
const task7 = document.getElementById('task7');
task7.addEventListener('contextmenu', (e) => {
    e.preventDefault();
})

// ЗАДАЧА 8
window.addEventListener('scroll', () => {
    const btnScroll = document.getElementById('task8');
    if (window.scrollY > 100) {
        btnScroll.style.display = 'block';
    } else {
        btnScroll.style.display = 'none';
    }
})

function up() {
    window.scrollTo({ top:0, behavior: 'smooth' });
}

// ЗАДАЧА 9
function addBlock() {
    const container = document.getElementById('block-container');

    let block = document.createElement('div');
    block.classList.add('block');
    let randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    block.style.backgroundColor = randomColor;
    block.onclick = function () {
        // container.removeChild(block);
        block.style.opacity = '0';
        block.style.cursor = 'auto';
    }
    container.appendChild(block);
}