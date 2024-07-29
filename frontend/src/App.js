// src/App.js
import React from 'react';
import Graph from './Graph';
import PlotlyGraph from "./PlotlyGraph"
import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import {Routes} from './Route.js'
import NavBar from "./components/index.js";

import './App.css';

function App() {
  return (
    <Router>
      <NavBar/ >
      <Routes/ >
    </Router>

  );
}

export default App;
