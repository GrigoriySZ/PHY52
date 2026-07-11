import React, { useState } from "react";
import styles from './TodoList.module.css';
import ListElement from "../ListElement/ListElement";

function TodoList () {

    // Инициализируем хуки состояния
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState('');
    
    // Функция добавления задачи в список
    const addTask = () => {
        // Проверяме строку ввода на наличие символов
        if (newTask.trim() === '') return;

        // Создаем объект задачи
        const task = {
            id: Date.now(),
            text: newTask, 
            completed: false
        };

        // Передаем состояние списка задач
        setTasks([...tasks, task]);
        // Обнуяем состояние новой задачи
        setNewTask('');
    };

    // Функция изменения статуса выполнения
    const toggleTaks = (id) => {
        setTasks(
            tasks.map((task) => task.id === id 
                ? { ...task, completed: !task.completed } 
                : task
            )
        );
    };

    // Функция удления задачи
    const deletaTask = (id) => {
        setTasks(tasks.filter((task) => task.id !== id));
    };

    // Счетчик выполненных задач
    const completedTask = tasks.filter(
        (task) => task.completed
    ).length;

    return (
        <div className={styles.listContainer}>
            <h1 id={styles.listTitle}>
                To Do List
            </h1>
            {/* NEW TASK SECTION */}
            <div className={styles.newTaskContainer}>
                <input 
                    type="text"
                    className={styles.newTaskInput}
                    placeholder="Введите текст задачи"
                    value={newTask}
                    onChange={(e) => setNewTask(e.target.value)}
                />
                <button 
                    className={styles.newTaskBtn}
                    onClick={addTask}
                >
                    Добавить
                </button>
            </div>
            {/* TASKS COUNET */}
            <p className={styles.tasksCounter}>
                Выполнено {completedTask} из {tasks.length > 0 ? tasks.length : 'N'}
            </p>

            {/* LIST SECTION */}
            {tasks.length === 0 ? (
                <p>Нет задач</p>
            ) : (
                <ul className={styles.currentTasksContainer}>
                    {tasks.map((task) => (
                        <ListElement 
                            key={task.id}
                            task={task}
                            onToggle={toggleTaks}
                            onDelete={deletaTask}
                        />
                    ))}
                </ul>
            )}
        </div>
    )
};

export default TodoList;