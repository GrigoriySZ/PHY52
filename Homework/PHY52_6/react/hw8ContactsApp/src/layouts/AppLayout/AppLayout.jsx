import { NavLink, Link, Outlet, useNavigate } from 'react-router-dom';
import { IoIosContacts } from "react-icons/io";
import styles from './AppLayout.module.css';

export default function AppLayout () {
    // Класс стилей для активной ссылки
    const setNavClass = ({ isActive }) => isActive ? 
        `${styles.navLink} ${styles.active}` : 
        `${styles.navLink}`; 

    const navigate = useNavigate();

    return (
        <>
            {/* HEADER */}
            <header>
                <div className={styles.wrapper}>
                    <Link
                        to={{ pathname: '/home' }}
                        className={styles.logo}
                    >
                        <IoIosContacts className={styles.logoIcon}/>
                        <span className={styles.accentLetter}>
                            К
                        </span>
                        онтакты
                    </Link>
                    <nav className={styles.navLinks}>
                        <NavLink to='/home' className={setNavClass}>
                            Главная
                        </NavLink>
                        <NavLink to='/contacts' className={setNavClass}>
                            Список контактов
                        </NavLink>
                        <NavLink to='/add-contact' className={setNavClass}>
                            Добавить контакт
                        </NavLink>
                    </nav>
                </div>
            </header>
            {/* MAIN PLACEHOLDER */}
            <main>
                <div className={styles.wrapper}>
                    <Outlet />
                </div>
            </main>
        </>
    )
}