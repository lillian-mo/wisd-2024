// src/App.js
import React from 'react';
import Graph from './Graph';
import PlotlyGraph from "./PlotlyGraph"

import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>React Graphing App</h1>
      </header>
      <main>
        <Graph />
        <PlotlyGraph />
      </main>
    </div>
  );
}

export default App;
