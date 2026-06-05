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
    const [isBrewing, setIsBrewing] = useState(false); // Статус процесса варки
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
    
    useEffect(() => {
        if (isBrewing) return;

        if (water < 20) {
            setStatus("error")
            setMessage('Недостаточно воды');
            return;
        };

        if (!hasEnoughResources) {
            setStatus("error")
            setMessage('Недостаточно ресурсов');
            return;
        };

        setStatus('idle');
        setMessage('');
    }, [coffeeType, water, beans, milk, isBrewing])
    
    // Отсматрваем начало варки кофе
    useEffect(() => {
        if (status !== 'brewing') return;

        // Создаем таймер
        const timer = setTimeout(() => {
            setWater((prev) => prev - currentRecipe.water);
            setBeans((prev) => prev - currentRecipe.beans);
            setMilk((prev) => prev - currentRecipe.milk)
        
            // Передаем новый статус
            console.log('Кофе готов!')
            setStatus('ready');
        }, 3000);

        return () => clearTimeout(timer);
    }, [status, coffeeType]);

    // Отсматриваем завершение варкеи кофе
    useEffect(() => {
        if (status !== 'ready') return;

        // Устанавливаем таймер готовности 
        const timer = setTimeout(() => {
            setStatus('idle');
            setIsBrewing(false);
        }, 5000);

        return () => clearTimeout(timer)
    }, [status]);

    // Процентный расчет уровня воды, зерен и молока
    const waterPercent = Math.min((water / 100) * 100, 100);
    const beansPercent = Math.min((beans / 200) * 100, 100);
    const milkPercent = Math.min((milk / 1000) * 100, 100);

    // Функция для начала варки кофе
    const handleBrewing = () => {
        if (status === 'idle') {
            setStatus('brewing');
            setIsBrewing(true);
        };
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
                        disabled={isBrewing}
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
                        disabled={isBrewing}
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
                    disabled={isBrewing}
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
                    disabled={isBrewing}
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
                    disabled={isBrewing}
                >
                    <LuMilk /> Add Milk
                </button>
                <button
                    className={styles.controlBtn}
                    onClick={handleBrewing}
                    disabled={status !== 'idle'}
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