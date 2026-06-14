import React from "react";
import styles from "./Home.module.css";

export default function Home({ counter }) {

    return (
        <>
            <h1>Книга контактов</h1>
            <p className={styles.description}>
                В этом сервисе вы сможете хранить все необходимые контакты и 
                    иметь к ним легкий и удобный доступ.
            </p>
            <p className={styles.contactsCounter}>В записной книжке контактов: {counter}</p>
        </>
    )
}