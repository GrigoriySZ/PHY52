import React from "react"
import QuoteViewer from "./components/QuoteViewer"

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      showQuote: true
    };
  }

  toggleQuote = () => {
    this.setState({
      showQuote: !this.state.showQuote
    });
  };

  render() {
    return(
      <div>
        <h1>Просмотр цитат</h1>
        <button
          onClick={this.toggleQuote}
          style={{ marginBottom: "10px" }}
        >
          {this.state.showQuote
            ? "Скрыть цитатут"
            : "Показать цитату"
          }
        </button>
        {this.state.showQuote && <QuoteViewer />}
      </div>
    );
  };
}

export default App;
