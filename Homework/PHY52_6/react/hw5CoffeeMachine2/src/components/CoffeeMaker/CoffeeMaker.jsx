import React, { useState, useEffect } from "react";
import styles from './CoffeeMaker.module.css';
import { GiCoffeeCup, GiWaterDrop } from "react-icons/gi";
import { PiCoffeeBeanFill } from "react-icons/pi";
import { GrStatusInfo } from "react-icons/gr";
import { LuMilk } from "react-icons/lu";
import { BiCoffee, BiCoffeeTogo } from "react-icons/bi";

function CoffeeMaker() {
    // Инициализуем состояния
    const [water, setWater] = useState(40);  // Количество воды в %
    const [beans, setBeans] = useState(80);  // Количество зерен в г
    const [milk, setMilk] = useState(500);  // Количество молока в мл
    const [coffeeType, setCoffeeType] = useState(''); // Тип отвариваемого кофе
    const [status, setStatus] = useState('idle'); // Статус приготовления
    const [isBerwing, setIsBerwing] = useState(false); // Триггер для начала варки
    const [message, setMessage] = useState('') // Контейнер для ошибки
    
    // Иницилизуем эффект запуска кофеварки
    useEffect(() => {
        console.log('эффект воды начало')
        if (water < 20) {
            setStatus('error');
            setMessage('Недостаточно воды');
            return
        }
        console.log('эффект воды конец')
    }, [water]);

    useEffect(() => {
        if (isBerwing === true) {
            console.log('эффект варки начало')
            // Проверям наличие ингридиентов для эспрессо
            if (coffeeType === 'espresso') {
                setWater(water - 20);
                setBeans(beans - 20);
            }

            // Проверям наличие ингридиентов для латте
            if (coffeeType === "latte") {
                setWater(water - 10); 
                setBeans(beans - 20);
                setMilk(milk - 150);
            }
            
            // Ставим статус варки кофе
            setStatus('brewing');

            // Имитируем приготовление кофе
            setTimeout(() => {
                setStatus('ready');
                console.log('Кофе готов!');
            }, 3000);

            // Имитируем готовность для повторной варки
            setTimeout(() => {
                setStatus('idle');
            }, 5000)
            
            // Сбрасываем статус начала варки
            setIsBerwing(false);
            console.log('эффект варки конец')
        }
        
    }, [isBerwing]);

    // Эффект на изменениен выбора типа кофе
    useEffect (() => {
        console.log('эффект типа кофе начало')
        // Проверям выбор типа кофе
        if (!coffeeType) {
            setStatus('error');
            setMessage('Выберите тип кофе');
            return
        }

        if (coffeeType === 'espresso') {
            if (water < 20 || beans < 20) {
                setStatus('error');
                setMessage('Недостаточно ресурсов для эспрессо')
                return
            }
        }

        // Проверям наличие ингридиентов для латте
        if (coffeeType === "latte") {
            if (water < 10 || beans < 20 || milk < 150) {
                setStatus('error');
                setMessage('Недостаточно ресурсов для латте')
                return
            }
        }
        console.log('эффект типа кофе конец')
        setStatus('idle');
        setMessage('');
    }, [coffeeType])

    // Профентный расчет уровня воды и зерен
    const waterPercent = Math.min((water / 100) * 100, 100);
    const beansPercent = Math.min((beans / 200) * 100, 100);
    const milkPercent = Math.min((milk / 1000) * 100, 100);

    const handleBrewing = () => {
        setIsBerwing(true);
        setMessage('');
    };
    
    return (
        <div className={styles.coffeeMaker}>
            <h1>
                <GiCoffeeCup size={50} className="styles.icon" color="red"/> 
                The Bestest Coffee
            </h1>
            <div className={styles.machine}>

                {/* WATER LEVEL */}
                <div className={styles.container}>
                    <div
                        className={styles.waterLevel}
                        style={{
                            height: `${waterPercent}%`
                        }}
                    >
                    </div>
                </div>
                

                {/* BEANS LEVEL */}
                <div className={styles.container}>
                    <div
                        className={styles.beansLevel}
                        style={{
                            height: `${beansPercent}%`
                        }}
                    >
                    </div>
                </div>

                {/* MILK LEVEL */}
                <div className={styles.container}>
                    <div
                        className={styles.milkLevel}
                        style={{
                            height: `${milkPercent}%`
                        }}
                    >
                    </div>
                </div>
            </div>
            {/* INFO BLOCK */}
            <div className={styles.info}>
                <span>
                    <GiWaterDrop 
                        className={styles.icon} 
                        color={water < 20 
                            ? "red"
                            : "skyblue"
                        }
                    /> 
                    {water} / 100%
                </span>
                <span>
                    <PiCoffeeBeanFill className={styles.icon} color="brown"/> 
                    {beans} / 200g
                </span>
                <span>
                    <LuMilk className={styles.icon} color="grey"/>
                    {milk} / 1000ml
                </span>
                <span id={styles.statusBar}>
                    <GrStatusInfo 
                        className={styles.icon} 
                        color={status === "error" 
                            ? "red"
                            : "green"}
                    />
                    Status: {" "}
                    {status}
                    {message !== '' && <> ({message})</>}
                </span>
            </div>
            

            {/* COFFEE TYPE SELECT */}
            <div className={styles.coffeeTypeContainer}>
                <h3>Тип кофе</h3>
                <label htmlFor="espresso" className={styles.coffeeTypeSelect}>
                    <BiCoffee className={styles.coffeeTypeIcon}/>
                    <input 
                        type="radio" 
                        name="coffeeType"
                        id="espresso"
                        value="espresso"
                        onChange={() => setCoffeeType('espresso')}
                    />
                    Espresso
                </label>
                <label htmlFor="latte" className={styles.coffeeTypeSelect}>
                    <BiCoffeeTogo className={styles.coffeeTypeIcon}/>
                    <input 
                        type="radio"
                        name="coffeeType" 
                        id="latte"
                        value="latte"
                        onChange={() => setCoffeeType('latte')}
                    />
                    Latte
                </label>
            </div>

            {/* CONTROL BUTTONS */}
            <div className={styles.controlPanel}>
                <button
                    className={styles.controlBtn}
                    onClick={() => {
                        if (water < 80) {
                            setWater(water + 20)
                        } else {
                            setWater(100);
                        }
                    }}
                >
                    <GiWaterDrop />  Add Water
                </button>
                <button
                    className={styles.controlBtn}
                    onClick={() => {
                        if (beans < 150) {
                            setBeans(beans + 50)
                        } else {
                            setBeans(200);
                        }
                    }}
                >
                    <PiCoffeeBeanFill /> Add Beans
                </button>
                <button
                    className={styles.controlBtn}
                    onClick={() => {
                        if (milk < 750) {
                            setMilk(milk + 250)
                        } else {
                            setMilk(1000);
                        }
                    }}
                >
                    <LuMilk /> Add Milk
                </button>
                <button
                    className={styles.controlBtn}
                    onClick={() => handleBrewing()}
                    disabled={status !== 'idle'}
                >
                    Start
                </button>
            </div>
        </div>
    );
};

export default CoffeeMaker;