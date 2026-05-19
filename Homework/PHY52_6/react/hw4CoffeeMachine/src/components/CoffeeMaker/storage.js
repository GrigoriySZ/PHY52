// Изначальное состояние кофеварки
export const initialState = {
    water: 800,
    beans: 150, 
    isBreaving: false
};

// Функция редбюсер с экшенами
export function coffeeReducer(state, action) {
    switch (action.type) {
        case 'ADD_WATER':
            return {
                ...state,
                water: state.water + action.payload
            };
        case 'ADD_BEANS': 
            return {   
                ...state,
                beans: state.beans + action.payload
            };
        case 'START_BREWING':
            if (state.water < 200 || state.beans < 20) {
                alert("Недостаточно ресурсов!");
                return state;
            };
            return {
                ...state,
                isBreaving: true
            };
        case 'FINISH_BREWING': 
            return {
                ...state, 
                isBreaving: false,
                water: state.water - 200,
                beans: state.beans - 20
            };
        default: 
            return state;
    }
};