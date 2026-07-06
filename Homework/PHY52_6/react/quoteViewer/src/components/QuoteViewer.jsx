import React from "react";

class QuoteViewer extends React.Component {
    constructor(props) {
        super(props);
        
        this.quotesArr = [
            "Если до вашей планки не дотягиваются, это не повод ее занижать.",
            "Разум бессилен перед криком сердца.",
            "Только смерть непоправима.",
            "Что разум человека может постигнуть и во что он может поверить, того он способен достичь.",
            "Возможности не приходят сами — вы создаете их.",
            "Упал – начни сначала.",
            "Я знаю, что я ничего не знаю.",
            "Мужество — это делать то, что нужно, даже когда страшно.",
            "В основном свободу человек проявляет только в выборе зависимости."
        ];

        this.state = {
            currentQuote: this.getRandomQuote()
        };
    };

    getRandomQuote = () => {
        const randomIndex = Math.floor(Math.random() * this.quotesArr.length);
        return this.quotesArr[randomIndex];
    };

    nextQuote = () => {
        let newQuote = this.getRandomQuote(); 

        while (newQuote === this.state.currentQuote && this.quotesArr.length > 1) {
            newQuote = this.getRandomQuote();
        }

        this.setState({ currentQuote: newQuote });
    };

    componentDidMount() {
        // Выводим сообщение в консоль при монтировании компонента
        console.log("Компонент QuoteViewer смонтирован")
    };

    componentDidUpdate(prevProps, prevState) {
        // Выводим сообщение в консоли, если изменилась цитата
        if (prevState.currentQuote !== this.state.currentQuote) {
            console.log('Цитата обновлена');
        }
    };

    componentWillUnmount() {
        // Выводим сообщениие в консоль при размонтировании элемента
        console.log("Компонент QuoteViewer размонтирован")
    };

    render() {
        return (
            <div>
                <p>{this.state.currentQuote}</p>
                <button onClick={this.nextQuote}>
                    Следующая цитата
                </button>
            </div>
        );
    }
}

export default QuoteViewer;