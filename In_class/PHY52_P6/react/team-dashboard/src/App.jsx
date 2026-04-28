import { useState } from 'react'
import './App.css';
import avatar1 from './assets/avatar-1.jpg';
import avatar2 from './assets/avatar-2.jpg';
import avatar3 from './assets/avatar-3.jpg';
import Header from './components/Header/Header';

const employeesData = [
  {
    id: 1, 
    name: 'Иван Иванов',
    role: 'Senior DevOps Engineer',
    avatar: avatar1,
    lastActive: '2 часа назад',
    performance: 85
  }, {
    id: 2, 
    name: 'Светлана Светлова',
    role: 'Middle QA Engineer',
    avatar: avatar2,
    lastActive: '5 минут назад',
    performance: 73
  }, {
    id: 3, 
    name: 'Антонов Антон',
    role: 'Junior Backend Engineer',
    avatar: avatar3,
    lastActive: '1 день назад',
    performance: 48
  }
];

function App() {

  const toggleTheme = () => {

  };

  return (
    <>
      <Header theme='dark' onToggleTheme={toggleTheme} />
    </>
  )
}

export default App
