import React, { useState, useEffect } from "react";
import styles from './CoffeeMaker.module.css';
import { GiCoffeeCup, GiWaterDrop } from "react-icons/gi";
import { PiCoffeeBeanFill } from "react-icons/pi";
import { GrStatusInfo } from "react-icons/gr";
import { LuMilk } from "react-icons/lu";
import { BiCoffee, BiCoffeeTogo } from "react-icons/bi";

function CoffeeMaker() {
    // Инициализуем состояния ресурсов
    const [water, setWater] = useState(60);  // Количество воды в %
    const [beans, setBeans] = useState(120);  // Количество зерен в г
    const [milk, setMilk] = useState(600);  // Количество молока в мл

    // Выбор типа отвариваемого кофе
    const [coffeeType, setCoffeeType] = useState('espresso');

    // Статус кофемашины
    const [status, setStatus] = useState('idle'); // Статус приготовления
    const [message, setMessage] = useState('') // Контейнер для ошибки
    
    // Рецепты с затратами ресурсов
    const recipes = {
        espresso: {
            water: 20,
            beans: 20, 
            milk: 0
        },
        latte: {
            water: 10,
            beans: 20,
            milk: 150
        }
    };
    const currentRecipe = recipes[coffeeType];

    // Проверка наличия ресурсов для рецепта
    const hasEnoughResources = 
            water >= currentRecipe.water &&
            beans >= currentRecipe.beans &&
            milk >= currentRecipe.milk;
    
    // Переменная для хранения таймера
    var timer; 

    useEffect(() => {
        if (status === 'brewing' || status === 'ready') return;

        // Проверяем наличие воды
        if (status !== 'ready' && water < 20) {
            if (status !== 'error' || message !== 'Недостаточно воды') {
                setStatus("error")
                setMessage('Недостаточно воды');
            }
            return;
        }

        if (status !== 'brewing' && status !== 'ready') {
            if (!hasEnoughResources) {
                if (status !== 'error' || message !== 'Недостаточно ресурсов') {
                    setStatus("error")
                    setMessage('Недостаточно ресурсов');
                }
                return;
            }

            if (status === 'error') {
                setStatus('idle');
                setMessage('');
            }
        }

        return () => clearTimeout(timer)
    }, [coffeeType, water, beans, milk, status])
    
    // Отсматрваем начало варки кофе
    useEffect(() => {
        if (status !== 'brewing') return;
        
        const recipe = recipes[coffeeType];

        // Создаем таймер
        timer = setTimeout(() => {
            setWater((prev) => prev - recipe.water);
            setBeans((prev) => prev - recipe.beans);
            setMilk((prev) => prev - recipe.milk)
        
            // Передаем новый статус
            console.log('Кофе готов!')
            setStatus('ready');
        }, 3000);

        return () => clearTimeout(timer);
    }, [status]);

    // Отсматриваем завершение варки кофе
    useEffect(() => {
        if (status !== 'ready') return;

        // Устанавливаем таймер готовности 
        timer = setTimeout(() => {
            setStatus('idle');
        }, 5000);

        return () => clearTimeout(timer)
    }, [status]);

    // Процентный расчет уровня воды, зерен и молока
    const waterPercent = Math.min((water / 100) * 100, 100);
    const beansPercent = Math.min((beans / 200) * 100, 100);
    const milkPercent = Math.min((milk / 1000) * 100, 100);

    // Функция для начала варки кофе
    const handleBrewing = () => {
        if (status === 'idle' && hasEnoughResources && water >= 20) {
            setStatus('brewing');
        } else {
            setStatus('error');
            setMessage('Недостаточно ресурсов');
        }
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
                        checked={coffeeType === "espresso"}
                        onChange={() => setCoffeeType('espresso')}
                        disabled={status === 'brewing' || status === 'ready'}
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
                        disabled={status === 'brewing' || status === 'ready'}
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
                    disabled={status === 'brewing' || status === 'ready'}
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
                    disabled={status === 'brewing' || status === 'ready'}
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
                    disabled={status === 'brewing' || status === 'ready'}
                >
                    <LuMilk /> Add Milk
                </button>
                <button
                    className={styles.controlBtn}
                    onClick={handleBrewing}
                    disabled={status !== 'idle' || status === "error"}
                    style={status === "error" ? 
                        {background: "red"} :
                        {background: ''}
                    }
                >
                    Start
                </button>
            </div>
        </div>
    );
};

export default CoffeeMaker;