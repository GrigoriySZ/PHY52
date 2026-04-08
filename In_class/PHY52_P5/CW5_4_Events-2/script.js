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
const mtmBtn = document.getElementById('mtmBtn');
const bpmCounter = document.getElementById('bpmCounter');
const mtmVolumeSlider = document.getElementById('mtmVolumeSlider')
const mtmPlay = document.getElementById('mtmPlay');
const mtmStop = document.getElementById('mtmStop');

// Инициализируем переменные 
let recordedSequence = [];
let isRecording = false;
let startTime = 0;
let currentVolume = 0.5;
let mtmIsPlaying = false;
let currentBpm = 120;
let mtmCurrnetVolume = 0.5;
let intervalId

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

bpmCounter.addEventListener('input', (e) => {
    currentBpm = e.target.value;
    console.log(currentBpm);
});

mtmVolumeSlider.addEventListener('input', (e) => {
    mtmCurrnetVolume = e.target.value;
});

mtmBtn.addEventListener('click', () => {
    
    // Инициализируем звук метронома
    const mtmAudio = new Audio('sounds/click.mp3');
    // const mtmPlay = document.getElementById('mtmPlay');
    // const mtmStop = document.getElementById('mtmStop');
    
    if (!mtmIsPlaying) {
        
        // Менямем цвет кнопки
        mtmStop.classList.remove('active');
        mtmPlay.classList.add('active');

        // Запускаем звук
        mtmAudio.play();

        // Считаем частоту ударов 
        let intervalMs = (60 / currentBpm) * 1000;

        // Задаем воспроизведение с интервалом 
        intervalId = setInterval(() => {
            mtmAudio.volume = mtmCurrnetVolume;
            mtmAudio.currentTime = 0;
            mtmAudio.play();
        }, intervalMs);

        mtmIsPlaying = true;
    } else {

        // Изменяем цвет кнопки
        mtmPlay.classList.remove('active');
        mtmStop.classList.add('active');

        // Останавливаем цикл
        clearInterval(intervalId);
        mtmAudio.pause();
        mtmAudio.currentTime = 0;
        mtmIsPlaying = false;
    }
});