// Создаем словарь со звуками из дерева проекта 
const sounds = {
    'A': 'sounds/A.wav', 'S': 'sounds/S.wav',
    'D': 'sounds/D.wav', 'F': 'sounds/F.wav',
    'G': 'sounds/G.wav', 'H': 'sounds/H.wav',
    'J': 'sounds/J.wav', 'K': 'sounds/K.wav',
};

// Сохраняем в константы элементы со страницы
const pads = document.querySelectorAll('.pad');
const volumeSlider = document.getElementById('volumeSlider');
const recBtn = document.getElementById('recBtn');
const stopBtn = document.getElementById('stopBtn');
const playBtn = document.getElementById('playBtn');
const recIndicator = document.getElementById('recIndicator');
const metronomeBtn = document.getElementById('metronomeBtn');
const bpmCounter = dociment.getElementById('bpmCount');

// Инициализируем переменные 
let recordedSequence = [];
let isRecording = false;
let startTime = 0;
let currentVolume = 0.5;
let metronomIsActive = false;
let bpmCount = 120;

// setinterval JS

// Функция проигрывания звука
function playSound(key) {
    const soundPath = sounds[key]; 

    // Добавляем проверку для избежани исключений
    if (!soundPath) return;

    // Инициализируем звук
    const audio = new Audio(soundPath);
    audio.volume = currentVolume;  // Задаем громкость проигрывания
    audio.currentTime = 0;  // Скидываем время мелодии на 0
    audio.play();  // Запускаем мелодию

    // Инициализируем элемент нажатого пэда
    const pad = document.querySelector(`.pad[data-key="${key}"]`);
    if (pad) {
        pad.classList.add('active');
        setTimeout(() => pad.classList.remove('active'), 100);
    }

    if (isRecording) {
        recordedSequence.push({
            key: key,  // какая клавиша нажата
            time: Date.now() - startTime  // сколько миллисекунд прошло от начала записи
        });
    }
}

// Добавляем обработчик событий
window.addEventListener('keydown', (e) => {

    // Сохраняем нажатие клавиши
    const key = e.key.toUpperCase();

    // Проигрываем мелодию клавиши
    playSound(key);
});

pads.forEach(pad => {
    pad.addEventListener('click', () => {
        playSound(pad.dataset.key); 
    })
});

volumeSlider.addEventListener('input', (e) => {
    currentVolume = e.target.value;
});

recBtn.addEventListener('click', () => {
    isRecording = true;  // Меняем статус запими
    recordedSequence = [];  // Отчищаем переменную последовательности
    startTime = Date.now();  // Засекаем время начала трека
    recIndicator.classList.add('active');  // Включаем индикатор записи
}); 

stopBtn.addEventListener('click', () => {
    isRecording = false;
    recIndicator.classList.remove('active');
});

playBtn.addEventListener('click', () => {
    // Проверяем наличие записей 
    if (recordedSequence.length === 0) return;

    recordedSequence.forEach(item => {
        setTimeout(() => {
            playSound(item.key); 
        }, item.time);
    });
});

metronomeBtn.addEventListener('click', () => {
    
    if (!metronomIsActive) {
        metronomIsActive = true;
        const audio = new Audio('sounds/click.wav');
        audio.volume = currentVolume;
        audio.play()

    }
})