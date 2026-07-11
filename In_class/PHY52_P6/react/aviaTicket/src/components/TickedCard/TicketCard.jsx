import React from "react";
import styles from "./TicketCard.module.css";

function TicketCard({ data }){
    // "2026-05-13"
    const formatDate = (dateString) => {
        if (!dateString) return 'Дата не указана';
        const date = new Date(dateString);  // Создаем объект даты
        return date.toLocaleDateString('ru-RU', {
            day: 'numeric',
            month: 'long',
            year: 'numeric'
        });
    }

    return (
        <div className={styles.container}>
            <div className={styles.destination}>
                {data.origin} -- {data.destination}
            </div>
            <div className={styles.price}>{data.value}</div>
            <div className={styles.info}>
                {formatDate(data.depart_date)}
            </div>
            <div className={styles.gate}>
                {data.gate}
            </div>
            <button className={styles.btn}>Купить</button>
        </div>
    );
}

export default TicketCard;