import React, { useState, useRef, useEffect } from "react";

export default function Timer() {

    // Счетчик секунд
    const [seconds, setSeconds] = useState(0);

    // Хранение ID интервала
    const itervalRef = useRef(null);

    // Очиситка интевала при размонтировании
    useEffect(() => {
        return () => {
            if (itervalRef.current !== null) {
                clearInterval(itervalRef.current);
            };
        }
    }, []);

    // Функция начала секундомаера
    const handleStartTimer = () => {
        if (itervalRef.current !== null) return;

        itervalRef.current = setInterval(() => {
            setSeconds((prev) => prev + 1)
        }, 1000);
    }; 

    // Функция остановки секундомера
    const handleStopTimer = () => {
        if (itervalRef.current !== null) {
            clearInterval(itervalRef.current);
            itervalRef.current = null;
        };
    };

    // Функция сброса сукундомера
    const handleResetTimer = () => {
        if (itervalRef.current !== null) {
            clearInterval(itervalRef.current);
            itervalRef.current = null;
        };

        setSeconds(0);
    };

    return (
        <div>
            <h1>Секундомер (useRef + setInterval)</h1>
            <p>Прошло секунда: {seconds}</p>
            <div style={{display: 'flex', gap: '10px'}}>
                <button onClick={handleStartTimer}>Старт</button>
                <button onClick={handleStopTimer}>Стоп</button>
                <button onClick={handleResetTimer}>Сброс</button>
            </div>
        </div>
    )
};