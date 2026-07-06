import React from "react"
import QuoteViewer from "./components/QuoteViewer"

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      showQoute: true
    };
  }

  toggleQuote = () => {
    this.setState({
      showQoute: !this.state.showQoute
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
          {this.state.showQoute
            ? "Скрыть цитатут"
            : "Показать цитату"
          }
        </button>
        {this.state.showQoute && <QuoteViewer />}
      </div>
    );
  };
}

export default App
