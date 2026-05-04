import React from "react";
import styles from "./Dashboard.module.css";
import EmployeeCard from "../EmployeeCard/EmployeeCard";

function Dashboard({ employees, theme }) {

    return (
        <>
            <main className={styles.dashboard}>
                <h2>Team Performance</h2>
                <div className={styles.grid}>
                    {employees.map(emp => (
                        <EmployeeCard key={emp.id} employee={emp} theme={theme} />
                    ))}
                </div>
            </main>
        </>
    );
}

export default Dashboard;