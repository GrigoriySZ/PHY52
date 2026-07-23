import { useState } from "react";

// COMPONENTS
import SearchBar from "../components/SearchBar/SearchBar";
import ContactList from "../components/ContactList/ContactList";

export default function Contacnts({ contacts, dispatch }) {

    const [search, setSearch] = useState("");

    const filteredContacts = contacts.filter((contact) => 
        contact.name.toLowerCase().includes(search.toLowerCase())
            || contact.phone.toLowerCase().includes(search.toLowerCase())
    );

    return (
        <div>
            <h1>Список контактов</h1>
            <SearchBar 
                search={search}
                setSearch={setSearch}
            />

            <ContactList 
                contacts={filteredContacts}
                dispatch={dispatch}
            />
        </div>
    )
}