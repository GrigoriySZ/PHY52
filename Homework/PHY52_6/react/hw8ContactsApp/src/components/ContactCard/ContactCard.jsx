import { useState } from "react";
import styles from "./ContactCard.module.css";

export default function ContactCard({ contact, dispatch }) {
    const [isHovered, setIsHovered] = useState(false);

    const handleDelete = () => {
        dispatch({
            type: "REMOVE_CONTACT",
            payload: contact.id 
        })
    };

    return (
        <div className={styles.card}>
            <div>
                <h3>{contact.name}</h3>
                <p>{contact.phone}</p>
            </div>
            <button
                className={styles.delBtn}
                style={{
                    backgroundColor: isHovered ? "var(--button-red)" : "var(--button-white)",
                    color: isHovered ? "var(--button-white)" : "var(--button-red)",
                    border: "2px solid var(--button-red)"
                }}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                onClick={handleDelete}
            >
                Удалить
            </button>
        </div>
    );
};