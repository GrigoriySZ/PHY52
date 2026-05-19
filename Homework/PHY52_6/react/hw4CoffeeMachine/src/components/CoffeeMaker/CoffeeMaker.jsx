import React, { useReducer, useEffect } from "react";
import styles from './CoffeeMaker.module.css';
import { coffeeReducer, initialState } from './storage';
import { GiCoffeeBeans, GiCoffeeCup, GiWaterDrop } from "react-icons/gi";
import { PiCoffeeBeanFill } from "react-icons/pi";
import { GrStatusInfo } from "react-icons/gr";

function CoffeeMaker() {
    // Инициализуем редьюсер
    const [state, dispatch] = useReducer(coffeeReducer, initialState);
    // Иницилизуем эффект запуска кофеварки
    useEffect(() => {
        // Переменная таймера
        let brewingTimer; 
        // Отрабатывает экшен начала варки
        if (state.isBrewing) {
            brewingTimer = setTimeout(() => {
                dispatch({ type: "FINISH_BREWING" });
                console.log('Кофе готов!');
            }, 3000);
        };

        return () => clearTimeout(brewingTimer);
    }, [state.isBrewing]);

    // Профентный расчет уровня воды и зерен
    const waterPercent = Math.min((state.water / 1000) * 100, 100);
    const beansPercent = Math.min((state.beans / 200) * 100, 100);

    return (
        <div className={state.coffeeMaker}>
            <h1>
                <GiCoffeeCup size={50} /> 
                Taste of the Bestest Coffee
            </h1>
            <div className={styles.machine}>
                <div className={styles.waterTank}>
                    <div
                        className={styles.waterLevel}
                        style={{
                            height: `${waterPercent}%`
                        }}
                    >
                    </div>
                </div>
                <div className={styles.beansStorage}>
                    <div
                        className={styles.beansLevel}
                        style={{
                            height: `${beansPercent}%`
                        }}
                    >
                    </div>
                </div>
                <div className={styles.info}>
                    <span>
                        <GiWaterDrop size={24}/> Water: {state.water} ml
                    </span>
                    <span>
                        <PiCoffeeBeanFill size={24}/> 
                        Beans: {state.beans} g
                    </span>
                    <span>
                        <GrStatusInfo size={24}/>
                        Status: {" "}
                        {state.isBrewing ? 'Brewing...' : 'Ready'}
                    </span>
                </div>
            </div>
            <div className={styles.controlPanel}>
                <button
                    className={styles.contolBtn}
                    onClick={() => dispatch({
                        type: 'ADD_WATER',
                        payload: 200
                    })}
                >
                    Add Water
                </button>
                <button
                    className={styles.contolBtn}
                    onClick={() => dispatch({
                        type: 'ADD_BEANS',
                        payload: 20
                    })}
                >
                    Add Beans
                </button>
                <button
                    className={styles.contolBtn}
                    onClick={() => dispatch({
                        type: 'START_BREWING'
                    })}
                    disabled={state.isBrewing}
                >
                    Brew Coffee
                </button>
            </div>
        </div>
    );
};

export default CoffeeMaker;