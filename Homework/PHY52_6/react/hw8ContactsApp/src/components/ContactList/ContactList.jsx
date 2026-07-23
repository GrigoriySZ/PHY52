import ContactCard from "../ContactCard/ContactCard";
import styles from "./ContactList.module.css";

export default function ContactList({ contacts, dispatch }) {

    if (contacts.length === 0) {
        return (
            <p className={styles.empty}>
                Контакты не найдены.
            </p>
        );
    }

    return(
        <div className={styles.list}>
            {contacts.map((contact) => (
                <ContactCard 
                    key={contact.id}
                    contact={contact}
                    dispatch={dispatch}
                />
            ))}
        </div>
    )
};