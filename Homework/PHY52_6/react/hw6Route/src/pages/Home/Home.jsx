import { useState, useEffect } from "react";
import styles from './Home.module.css';

function Home() {
    return (
        <>
            <h1>ATOM digital <br/> помощи в цифровом мире</h1>
            <p className={styles.description}>
                Разрабатываем сайты, настраиваем рекламу и увеличиваем конверсию. 
                Помогаем брендам находить клиентов в сети с 2020 года.
            </p>
        </>
    );
};

export default Home;