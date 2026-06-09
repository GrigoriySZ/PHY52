import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { TbArrowBackUp } from "react-icons/tb";
import { RiHomeLine } from "react-icons/ri";
import styles from './ServicePage.module.css';

function ServicePage() {
    const { serviceId } = useParams();
    const navigate = useNavigate();
    const [service, setService] = useState(null);

    useEffect(() => {
        const savedServices = JSON.parse(localStorage.getItem('services') || '[]');
        const foundService = savedServices.find(s => s.id === serviceId);
        setService(foundService);
    }, [serviceId]);
    
    const handleGoBack = () => {
        navigate(-1);
    };

    const handleGoHome = () => {
        navigate('/home');
    }

    if (!service) {
        return (
            <>
                <h2>Страница услуги не найдена</h2>
                <button onClick={handleGoHome}>
                    На главную ленту
                </button>
            </>
        );
    } 

    return (
        <div className={styles.subservicePage}>  
            <button 
                onClick={handleGoBack}
                className={`${styles.activeBtn} ${styles.backBtn}`}
            >
                <TbArrowBackUp/>
            </button>
            <div className={styles.serviseContainer}>
                <h1>{service.title}</h1>
                <p>{service.description}</p>
                <hr />
                <div className={styles.subserviseContainer}>
                    {service.subservises.map((subserv) => (
                        <div 
                            key={subserv.id}
                            className={styles.subserviceItem}
                        >
                            <h2>{subserv.title}</h2>
                            <p>{subserv.description}</p>
                        </div>
                    ))}
                </div>
            </div>
            <button 
                className={`${styles.activeBtn} ${styles.homeBtn}`}
                onClick={handleGoHome}
            >
                <RiHomeLine />
            </button>
        </div>
    );
}; 

export default ServicePage;