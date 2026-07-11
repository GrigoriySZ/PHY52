import React, { useState, useEffect } from "react";
import styles from './Search.module.css';

function Search ({ placeholder, onSelect}) {
    const [inputValue, setInputValue] = useState('');
    const [cities, setCities] = useState([]);
    // Управляет показом выпадающего списка
    const [isVisible, setIsVisible] = useState(false);  
    // shouldEffect нужен, чтобы не делать запрос к API, 
    // когда мы уже выбрали город из списка
    const [shouldEffect, setShouldEffect] = useState(true);

    useEffect(() => {
        const fetchCities = async () => {
            if (shouldEffect && inputValue.length > 1) {
                const proxy = 'https://cors-anywhere.herokuapp.com/';
                let apiUrl = `http://autocomplete.travelpayouts.com/places2?term=${inputValue}&locale=ru&types[]=city`;
                const response = await fetch(apiUrl); 
                if (response.ok) {
                    const data = await response.json();  // десериализация данных от API
                    setCities(data);
                    setIsVisible(data.length > 0);
                }
            }
            else if (inputValue.length <= 1) {
                setCities([]);
                setIsVisible(false);
            }
        };
        fetchCities();
    }, [inputValue, shouldEffect]);

    const handleSelect = (cityCode, cityName) => {
        setShouldEffect(false);
        setIsVisible(false);
        setCities([]); 
        setInputValue(cityName);  // Подставляем значение выбора
        onSelect(cityCode);  // Передаем код города родителю 
    }

    return (
        <div className={styles.container}>
            <input 
                type="text"
                className={styles.input}
                placeholder={placeholder}
                value={inputValue}
                onBlur={() => setTimeout(() => setIsVisible(false), 200)}
                onInput={(e) => {
                    setInputValue(e.target.value);
                    setShouldEffect(true)
                    setIsVisible(true)
                }}
            />
            <ul className={styles.list}>
                {isVisible && inputValue.length > 1 && (
                    cities.map((city) => (
                        <li
                            key={city.code}
                            onClick={() => handleSelect(city.code, city.name)}
                            className={styles.item}
                        >
                            <span className={styles.city}>{city.name}</span>
                            <span className={styles.code}>{city.code}</span>   
                        </li>
                    ))
                ) }
            </ul>
        </div>
    );
};

export default Search;