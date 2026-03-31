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