export const updateAmount = (val) => ({
    type: 'SET_AMOUNT',
    payload: val // payload - это то, что ввел пользователь
});

export const executeTransaction = () => ({
    type: 'CONFIRM_EXCHANGE'
});