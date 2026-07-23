import { useState } from "react";
import { useNavigate } from "react-router-dom";

import styles from "./ContactForm.module.css"

export default function ContactForm({ dispatch, contactsCount, storageLimit }) {
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [error, setError] = useState('');

    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();

        if (contactsCount >= storageLimit) {
            setError("Достигнуто максимальное количество контактов");
            return;
        }

        if (!name.trim() || !phone.trim()) {
            setError("Пожалуйста, заполните все поля");
            return;
        }

        dispatch({
            type: "ADD_CONTACT",
            payload: {
                id: Date.now(),
                name: name.trim(),
                phone: phone.trim()
            }
        });

        setName('');
        setPhone('');
        setError('');

        navigate('/contacts');
    };

    return (
        <form
            className={styles.form}
            onSubmit={handleSubmit}
        >
            <div className={styles.formField}>
                <label htmlFor="nameInput">Имя</label>
                <input
                    id="nameInput"
                    className={styles.formInput}
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Введите имя"
                />
            </div>

            <div className={styles.formField}>
                <label htmlFor="phoneInput">Телефон</label>
                <input
                    id="phoneInput"
                    className={styles.formInput}
                    type="text"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    placeholder="Введите телефон"
                />
            </div>

            {error && 
                <p className={styles.errorMessage}>
                    {error}
                </p>
            }

            <button type="submit" className={styles.formBtn}>
                Добавить контакт
            </button>
        </form>
    )
};