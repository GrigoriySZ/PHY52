import styles from './ServicesPage.module.css';
import { SERVICES_DATA } from '../../storage';
import { useState, useEffect } from 'react';
import { Link, useSearchParams } from 'react-router-dom';

function ServicesPage() {
    const [services, setServices] = useState([]);
    
    useEffect(() => {
        const savedServices = localStorage.getItem('services');
        if (savedServices) {
            setServices(JSON.parse(savedServices));
        } else {
            localStorage.setItem('services', JSON.stringify(SERVICES_DATA));
        };
    }, []);

    // Хук для обработки параметров из URL
    const [searchParams, setSearchParams] = useSearchParams();
    // Запросы из URL
    const searchQuery = searchParams.get('search') || '';
    const categoryQuery = searchParams.get('category') || '';

    // Изменение поиска по словам
    const handleSearchChange = (event) => {
        const text = event.target.value;
        const newParams = new URLSearchParams(searchParams);

        if (text) {
            newParams.set('search', text);
        } else {
            newParams.delete('search');
        };

        setSearchParams(newParams);
    };

    // Изменение категории фильтрации
    const handleCategoryChange = (event) => {
        const category = event.target.value;
        const newParams = new URLSearchParams(searchParams);

        if (category) {
            newParams.set('category', category);
        } else {
            newParams.delete('category');
        };

        setSearchParams(newParams);
    };

    // Сброс фильтров поиска
    const handleResetFilters = () => {
        setSearchParams({})
    };

    // Фильтрация услуг на основе фильтров
    const filtredServices = services.filter((service) => {
        // Совпадению по текстовому полю
        const matchesSearch = service.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
            service.description.toLowerCase().includes(searchQuery.toLowerCase());
        
        const matchesCategory = categoryQuery === '' || service.category === categoryQuery;
        return matchesSearch && matchesCategory;
    });

    return (
        <>
            <h1>Список услуг</h1>
            {/* БЛОК ФИЛЬТРОВ И ПОИСКА */}
            <div className={styles.searchContainer}
                style={(searchQuery || categoryQuery) ?
                    {borderColor: 'var(--accent)', boxShadow: '0 1px 0 1px var(--accent)'} :
                    {borderColor: 'var(--border)', boxShadow: 'none'}}
            >
                
                {/* ТЕКСТОВЫЙ ПОИСК */}
                <div className={styles.searchGroup}>
                    <label htmlFor='search-input'>Поиск по тексту</label>
                    <input 
                        type="text"
                        id="search-input"
                        value={searchQuery}
                        onInput={handleSearchChange}
                    />
                </div>

                {/* СПИСОК КАТЕГОРИЙ */}
                <div className={styles.searchGroup}>
                    <label htmlFor='category-select'>Поиск по тексту</label>
                    <select 
                        type="text"
                        id="search-input"
                        value={categoryQuery}
                        onInput={handleCategoryChange}
                    >
                        <option value="">Все категории</option>
                        <option value="marketing">Маркетинг</option>
                        <option value="development">Разработка</option>
                        <option value="design">Дизайн</option>
                        <option value="smm">SMM</option>
                    </select>
                </div>
                <button 
                    className={styles.activeBtn}
                    onClick={handleResetFilters}
                    style={(searchQuery || categoryQuery) ?
                        {color: 'var(--accent)', borderColor: 'var(--accent)'} :
                        {color: 'var(--text)', borderColor: 'var(--border)'}
                    }
                    >
                    Сброс
                </button>
            </div>

            {/* СЕРВИСЫ */}
            <div>
                { filtredServices.length > 0 ? (
                    filtredServices.map((service) => (
                        <article 
                            key={service.id}
                            className={styles.serviceContainer}

                        >
                            <h2>{service.title}</h2>
                            <p>{service.description}</p>
                            <Link 
                                to={`/services/${service.id}`}
                                className={styles.serviceLink}
                            >
                                Перейти к услуге
                            </Link>
                        </article>
                    ))
                ) : (
                    <p>Искомая услуга отсутствует</p>
                )}
            </div>
        </>
    );
};

export default ServicesPage;