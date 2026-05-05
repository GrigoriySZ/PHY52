import React, { useReducer } from "react";
import { bankReducer, initialState } from "./storage";
import { updateAmount, executeTransaction } from "./actions";

function ExchangeTerminal() {
    // Инициализируем механизм, где: 
    // state - данные, 
    // dispatch - функция отпраки действия
    const [state, dispatch] = useReducer(bankReducer, initialState);  // 1-как действует, с чего начинает

    // Вычисляемые значения (произвольные данные). 
    // Не храним в state, считаем прямо во время рендеринга
    const potentialUsd = (state.amountToExchange / state.exchangeRate).toFixed(2); 

    // Отрисовываем компонент
    return (
        <div>
            <h2>Терминал</h2>
            {/* Отображение State */}
            <div>
                <p>Ваш счет: <strong>{state.rubBalance.toFixed(2)}</strong></p>
                <p>Валютный счет: <strong>{state.usdBalance.toFixed(2)}</strong></p>
            </div>
            <div>
                <label>Введите сумму в рублях:</label>
                <input
                    type='number'
                    value={state.amountToExchange}
                    // ACTION: при каждом вводе отправляем сигнал диспетчеру
                    onChange={(e) => dispatch(updateAmount(Number(e.target.value)))}
                />
            </div>
            {/* UI=F(state) текст меняется автоматически при обновалении state.amountToExchange */}
            <p>К получению: <strong>{potentialUsd} $</strong> (курс: {state.exchangeRate})</p>
            <p style={{color: state.amountToExchange > state.rubBalance ? 'red' : 'green'}}>
                Статус: {state.status}
            </p>
            {/* DISPATCH: Кнопка вызывает действие подтверждение */}
            <button
                onClick={() => dispatch(executeTransaction())}
                disabled={state.amountToExchange <= 0 || state.amountToExchange > state.rubBalance}
            >
                ОБМЕНЯТЬ ВАЛЮТУ
            </button>
        </div>
    );
}

export default ExchangeTerminal;