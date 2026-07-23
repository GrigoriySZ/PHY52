import React from "react";
import ContactForm from "../components/ContactForm/ContactForm";
// import styles from "./AddContact.module.css";

export default function AddContact({ dispatch, contactsCount, storageLimit }) {

    return (
        <div style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center'
        }}>
            <h1>Добавление контакта</h1>

            <ContactForm dispatch={dispatch} 
                contactsCount={contactsCount}
                storageLimit={storageLimit}
            />
        </div>
    );
}