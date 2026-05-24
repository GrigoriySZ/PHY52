import React from "react";
import styles from './ListElement.module.css';

function ListElement({ task, onToggle, onDelete }) {

    return (
        <li className={styles.listElement}>
            <input 
                type="checkbox"
                className={styles.elementCheckbox}
                checked={task.completed}
                onChange={() => onToggle(task.id)}
            />
            <span className={styles.elementText}>
                {task.text}
            </span>
            <button
                className={styles.elementDelBtn}
                onClick={() => onDelete(task.id)}
            >
                Удалить
            </button>
        </li>
    );
};

export default ListElement;