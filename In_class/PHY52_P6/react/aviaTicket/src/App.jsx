import React, { useState, useEffect } from 'react';
import TicketCard from './components/TickedCard/TicketCard';
import Search from './components/Search/Search';
import DatePicker from './components/DataPicker/DataPicker';
import Loader from './components/Loader/Loader'
import styles from './App.module.css';

function App() { 
  // Состояния данных с билетами
  const [tickets, setTickets] = useState([]);
  const [loader, setLoader] = useState(false);
  const [origin, setOrigin] = useState('MOW');
  const [destination, setDestination] = useState('LED');
  const [departeDate, setDeparteDate] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      setLoader(true);
      const proxy = 'https://cors-anywhere.herokuapp.com/';
      const apiUrl = `https://api.travelpayouts.com/v2/prices/latest?origin=${origin}&destination=${destination}&token=c4c4803704e456e75677a1714b230275`;
      
      try {
        const response = await fetch(proxy+apiUrl);
        if (response.ok) {
          const data = await response.json();  // десериализация данных от API
          if (data.success) {
            console.log(data.success);
            let allTickets = data.data;  // Получаем данные всех билетов
            if (departeDate) {
              allTickets = allTickets.filter(ticket => ticket.depart_date === departeDate);
            }
            setTickets(allTickets);  // Обновляем состояние 
          }
        }
      } catch(error) {
        console.error('Ошибка загрузки данных:', error);
      } finally {
        setLoader(false);
      }
    };
    fetchData();
  }, [origin, destination, departeDate]);


return (
    <div className={styles.container}> 
      <h1>Поиск билетов</h1>
      <div className={styles.searchBar}>
        <Search  
          placeholder="Введите город отправления"
          onSelect={setOrigin}
        />
        <Search 
          placeholder="Введите город назначения"
          onSelect={setDestination}
        />
        <DatePicker 
          value={departeDate}
          onChange={setDeparteDate}
        />
      </div>
      {loader ? (
        <Loader />
      ) : (
        <div className={styles.grid}>
          {
            tickets.map((ticket, index) => (
              <TicketCard key={index} data={ticket} />
            ))
          }
        </div>
      )}
    </div>
  );
}

export default App;
