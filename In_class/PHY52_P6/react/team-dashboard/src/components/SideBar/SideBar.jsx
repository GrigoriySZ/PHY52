import React from "react";
import styles from './Sidebar.module.css';
import { HiChartBar, HiUsers, HiViewGrid } from 'react-icons/hi';

function SideBar({theme}) {
    const sidebarClass = theme === 'dark' ? styles.sidebarDark : styles.sidebarLight;

    return (
        <>
            <aside className={sidebarClass}>
                <nav>
                    <div className={styles.navItem}>
                        <HiViewGrid /> Dashboard
                    </div>
                    <div className={styles.navItem}>
                        <HiUsers /> Team
                    </div>
                    <div className={styles.navItem}>
                        <HiChartBar /> Reports
                    </div>
                </nav>
            </aside>
        </>
    );
}

export default SideBar;