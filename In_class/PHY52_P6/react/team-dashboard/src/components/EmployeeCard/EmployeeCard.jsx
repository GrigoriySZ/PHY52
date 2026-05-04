import React from "react";
import styles from "./EmployeeCard.module.css";
import { FaUserAlt } from 'react-icons/fa';

function EmployeeCard({ employee, theme}) {
    const cardClass = theme === 'dark' ? styles.cardDark : styles.cardLight;

    const getKPIColor = (val) => {
        if (val < 50) return '#ef4444';
        if (val <= 80) return '#facc15';
        return '#22c55e';
    };

    return (
        <div className={cardClass}>
            <div className={styles.statusDot}></div>
            <div className={styles.avatarContainer}>
                <img src={employee.avatar} />
            </div>
            <h3>{employee.name}</h3>
            <p className={styles.role}>{employee.role}</p>
            <div className={styles.kpiSection}>
                <div className={styles.kpiText}>KPI: [{employee.performance}%]</div>
                <div className={styles.progressBar}>
                    <div
                        className={styles.progressFill}
                        style={{
                            width: `${employee.performance}%`,
                            backgroundColor: getKPIColor(employee.performance)
                        }}
                    ></div>
                </div>
            </div>
            <p className={styles.lastActive}>{employee.lastActive}</p>
        </div>
    );
}

export default EmployeeCard;