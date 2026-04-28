import { useState } from 'react'
import './App.css'
import Product from './Product'

function App() {

  return (
    <>
      <h1>Список товаров:</h1>
      {/* Вставка компонента */}
      <Product name="Мороженое" price={200}/>
      <Product name="Хлеб" price={85}/>
    </>
  );
}

export default App
