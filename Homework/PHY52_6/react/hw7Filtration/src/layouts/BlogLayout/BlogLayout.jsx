import { NavLink, Link, Outlet, useNavigate } from "react-router-dom";
import { DiAtom } from "react-icons/di";
import styles from './BlogLayout.module.css';

function BlogLayout() {
    const setNavClass = ({ isActive }) => isActive ? 
        `${styles.navLink} ${styles.active}` : 
        `${styles.navLink}`; 
    const navigate = useNavigate();

    return (
        <>
            {/* ШАПКА САЙТА */}
            <header>
                <div className={styles.wrapper}>
                    <Link 
                        to={{ pathname: '/home' }} 
                        className={styles.logo}
                    >
                        <DiAtom className={styles.logoIcon} />
                        <span className={styles.accentFont}>ATOM</span>digital
                    </Link>
                    <nav className={styles.navLinks}>
                        <NavLink to="/home" className={setNavClass}>Главная</NavLink>
                        <NavLink to="/services" className={setNavClass}>Услуги</NavLink>
                        <NavLink to="/about" className={setNavClass}>О компании</NavLink>
                    </nav>
                </div>
            </header>
            {/* МЕСТО ВСТАВКИ КОМПОНЕНТОВ СТРАНИЦ */}
            <main>
                <div className={styles.wrapper}>
                    <Outlet />
                </div>
            </main>
            {/* ПОДВАЛ САЙТА */}
            <footer>
                <div className={styles.wrapper}>
                    <p>&copy; 2020-2026 Компания Digital Agency</p>
                </div>
            </footer>
        </>
    );
}

export default BlogLayout;