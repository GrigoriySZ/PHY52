// let a = document.getElement('a');

let a = document.createElement('div');
document.body.appendChild(a);
// Рефлоу репайнт - перерасчет интерфейста(меняется позиция, отступы, окно браузера)
// (репайнт - перерисока пикселей интерфейста виртуального представления, 
// не трогает позиции, размеры на экране )

// DOM - document object model

// Virtual DOM - хранится в виде дерева в виртуальной печати.

// Компоненты - отдельные элементы интерфейса со своими свойствами

import React from "react";

// Button - компонент
// label, onClick, disable=false - props (properties)
// props'ы всегда принемают значения извне - от родителя, не могут меняться внутри компонента
// jsx - расщирение языка JavaScript
// jsx - расширение, в котором мы можем использовать JS код. 
function Button({label, onClick, disable=false}) {
    
    // Компонен возвращает развертку в круглых скобочках
    // Компонено должен быть обернут либо в div (<div></div>) , либо в синтаксис JSX  (<></>)
    // Если не обернуть компонент, то при запуске кода будет вызываться ошибка
    return (
        <>
            <button
                onClick={onClick}  // обработчик из props
                disable={disable}  // из props
            >{label} 
            </button>
        </>
    )   
}

// Команда позволяет увидеть компонент снаружи для импорта
export default Button

// CamelCase для атрибутов: 
// class -> className, 
// onclick -> onClick,
// и т.д.

// Негласное правило - желательно, чтобы название файла называлось так же, как и компонент