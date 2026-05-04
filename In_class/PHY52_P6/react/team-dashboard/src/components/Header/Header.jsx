import React from "react";
import styles from './Header.module.css';
import { HiSun, HiMoon } from "react-icons/hi";

function Header({theme, onToggleTheme}) {
    const headerClass = theme === 'dark' ? styles.darkHeader : styles.lightHeader;

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