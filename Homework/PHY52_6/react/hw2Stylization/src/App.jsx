import React, { useState } from 'react';
import './App.css';
import logo from './assets/logo.png';

function App() {
  const name = 'Aлекс Марков';
  const profession = 'Семейный фотограф';
  const info = [
    {icon: '🌐', text: 'www.photolab.com'},
    {icon: '👤', text: 'fb.com/photolab'},
    {icon: '📱', text: '+7(495)202041212'},
    {icon: '📍', text: 'г.Москва, ул.Правды, д.12'}
  ];

  return (
    <div className='cardContainer'>
      <h1 className='cardName'>{name}</h1>
      <h2 className='cardProfession'>{profession}</h2>
      <img src={logo} className='cardLogo' />
      <div>
        <ul className='infoContainer'>
          {info.map((item, index) => (
            <li key={index} className='infoRow'>
              <span>{item.icon}</span>
              {item.text}
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default App;
