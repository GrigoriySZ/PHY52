import { useState, useReducer, act } from 'react'

const loadContactsStorage = () => {
  try {
    const savedData = localStorage.getItem('contacts');
    if (savedData) return JSON.parse(savedData);
  } catch (e) {
    console.error('Ошибка чтения localStorage', e)
  }

  return {
    contacts: [
      {id: Date.now(), 
      name: '',
      phone: ''},
    ]
  }
};

export function contactReducer(state, action) {
  switch (action.type) {
    case 'ADD_CONTACT': 
      return {
        ...state,
        contacts: [
          ...state.contacts, 
          {
            id: Date.now(),
            name: '',
            phone: ''
          }
        ]
      }
    
    case 'UPDATE_CONTACT': 
      return {
        ...state,
        contacts: state.contacts.map((con) => con.id === action.payload.id
        ? {...con, [action.payload.field]: action.payload.value}
        : con
      )
      }
    
    case 'REMOVE_CONTACT':
      return {
        ...state, 
        contacts: state.contacts.filter((cont) => cont.id !== action.payload)
      }
    
    default: 
      return state;
  }
};

export function App() {



  return (
    <>

    </>
  )
};