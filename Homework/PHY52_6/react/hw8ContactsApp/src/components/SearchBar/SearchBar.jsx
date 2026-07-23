import styles from "./SearchBar.module.css";

export default function SearchBar({ search, setSearch }) {
    
    return(
        <div className={styles.searchContainer}>
            <input 
                type="text"
                placeholder="Введите имя"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className={styles.searchInput}
            />
        </div>
    );
};