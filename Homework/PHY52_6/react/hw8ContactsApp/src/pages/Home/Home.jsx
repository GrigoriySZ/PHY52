import React from "react";
import { Link } from "react-router-dom";
import styles from "./Home.module.css";

export default function Home({ contacts, contactsLimit }) {

    const contactPercent = (contacts / contactsLimit) * 100;

    return (
        <div>
            <h1>
                Добро пожаловать в вашу <span>Книгу контактов</span>
            </h1>
            <p className={styles.description}>
                Это простое SPA-приложение для хранение списка ваших контактов
            </p>
            <h2>Всего контактов: {contacts.length}</h2>
            <div className={styles.storageBarContainer} 
                style={{
                
            }}>
                <div 
                    className={styles.storageBar} 
                    style={{width: `${contactPercent}%`}}
                ></div>
            </div>
            <div className={styles.btnContainer}>
                <Link to="/contacts">
                    <button className={styles.routeBtn}>
                        Список контактов
                    </button>
                    
                </Link>
                <Link to="/add-contact">
                    <button className={styles.routeBtn}>
                        Добавить контакт
                    </button>
                </Link>
            </div>
            
        </div>
    );
}