import React from "react";
import styles from './Product.module.css';
import imagePic from './assets/img-1.jpg'

function Product({name, price}) {
    // inline-стили (если нужно вычислить динамически)
    // {{}} - внешние - для входа в JS; внутренние - для создания объекта;
    const blueText = {
        color: 'blue',
        fontSize: '20px'
    };

    return (
        <div className={styles.card}>
            <img src={imagePic} />
            <h3>{name}</h3>
            <p>Цена: {price} руб.</p>
            <p style={blueText}>
                Синий цвет
            </p>
        </div>
    );
}

export default Product