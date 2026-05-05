import React, { useState, useEffect } from 'react'
import ExchangeTerminal from './ExchangeTerminal';


function App() {
  const [count, setCount] = useState(0);
  const [font, setFontSize] = useState(16);

  useEffect(() => {
    const newSize = 16 + Math.abs(count); 
    setFontSize(newSize);
  }, [count])
  // [] - зависимости, при изменении которых отрабатывает useEffect

  return (
    <>
      <ExchangeTerminal />
      <br></br>
      <button onClick={() => {setCount(count+1)}}>+</button>
      <p style={{fontSize: `${font}px`}}>{count}</p>
      <button onClick={() => {setCount(count-1)}}>-</button>
    </>
  );
}

export default App;
