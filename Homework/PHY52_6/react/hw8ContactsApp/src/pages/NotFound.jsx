import { Link } from "react-router-dom";
// import styles from './NotFound.module.css';

export default function NotFound() {
    return (
        <>
            <h1>Ошибка 404</h1>
            <p>Страница, которую вы ищите, не существует...</p>
            <Link to='/home'>Вернуться на главную страницу</Link>
        </>
    );
};