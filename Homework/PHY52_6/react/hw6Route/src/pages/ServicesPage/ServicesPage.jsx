import styles from './ServicesPage.module.css';
import { SERVICES_DATA } from '../../storage';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function ServicesPage() {
    const [services, setServices] = useState([]);

    useEffect(() => {
        const savedServices = localStorage.getItem('services');
        if (savedServices) {
            setServices(JSON.parse(savedServices));
        } else {
            localStorage.setItem('services', JSON.stringify(SERVICES_DATA));
        }
    }, []);

    return (
        <>
            <h1>Список услуг</h1>
            <div>
                { services.map((service) => (
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
                ))}
            </div>
        </>
    );
};

export default ServicesPage;