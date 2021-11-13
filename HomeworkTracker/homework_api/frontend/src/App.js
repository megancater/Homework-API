import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

import React, { Component } from "react"

class App exends Component {
	constructor(props) {
		super(props);
		this.state = {
			viewCompleted: false,
			activeAssignment: {
				name: "",
				due_date: "",
				class_name: "",
				description: "",
				completed: false
			},
		}
	}
}

