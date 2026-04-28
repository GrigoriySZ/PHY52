import React from "react";
import styles from './Header.module.css';
import { HiSun } from "react-icons/hi";
import { HiMoon } from "react-icons/hi";

function Header({theme, onToggleTheme}) {
    const headerClass = theme === 'dark' ? styles.dark-header : styles.light-header;

    return (
        <>
            <header className={headerClass}>
                <div>[TD]Dashboard</div>
                <div>
                    <span>Mode: {theme === 'dark' ? 'Dark' : 'Light'}</span>
                    <button onClick={onToggleTheme}>
                        {theme === 'dark' ? <HiSun size={24} /> : <HiMoon size={24} />}
                    </button>
                </div>
            </header>
        </>
    );
}

export default Header;