// 1) Исходное состояние (State)
export const initialState = {
    rubBalance: 50000,
    usdBalance: 0,
    exchangeRate: 92.5,
    amountToExchange: 0,
    status: 'Ожидание'
};

// Reducer (F)
export function bankReducer(state, action) {
    switch (action.type) {
        case 'SET_AMOUNT': 
            return {
                ...state,  // Копируем старые данные
                amountToExchange: action.payload,
                status: action.payload > state.rubBalance
                    ? 'Недостаточно средств'
                    : 'Готов к обмену'
            };
        case 'CONFIRM_EXCHANGE':
            if (state.amountToExchange > state.rubBalance || state.amountToExchange < 0) {
                return state;
            }
            return {
                ...state,
                rubBalance: state.rubBalance - state.amountToExchange,
                usdBalance: state.usdBalance + (state.amountToExchange / state.exchangeRate),
                amountToExchange: 0,
                status: 'Операция успешно завершина'
            };
            default:
                return state;
    };
}

// ...state - spread-оператор (отвечает за неизменяемость)

// Последовательность react при spread:
// 1) React сравнивает ссылки;
// 2) Иммутабильность (неизменяемость);
// 3) Создание нового объекта в памяти (...state);