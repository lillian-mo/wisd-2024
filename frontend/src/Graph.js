// src/Graph.js
import React, { useState } from 'react';
import './graph.css';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ScatterChart, Scatter } from 'recharts';

const data = [
  { name: 'Jan', high: 40, low: 33 },
  { name: 'Feb', high: 30, low: 12 },
  { name: 'Mar', high: 20, low: 6 },
  { name: 'Apr', high: 27, low: -1 },
  { name: 'May', high: 18, low: 11 },
  { name: 'Jun', high: 23, low: 7 },
  { name: 'Jul', high: 30, low: 15 },
];

const Graph = () => {
  const [chartType, setChartType] = useState('line');

  const toggleChartType = () => {
    setChartType(chartType === 'line' ? 'scatter' : 'line');
  };

  const renderChart = () => {
    if (chartType === 'line') {
      return (
        <LineChart
          data={data}
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="high" stroke="#8884d8" />
          <Line type="monotone" dataKey="low" stroke="#82ca9d" />
        </LineChart>
      );
    } else if (chartType === 'scatter') {
      return (
        <ScatterChart
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" allowDuplicatedCategory={false}/>
          <YAxis />
          <Tooltip />
          <Legend />
          <Scatter name="High" data={data} dataKey="high" fill="#8884d8" />
          <Scatter name="Low" data={data} dataKey="low" fill="#82ca9d" />
        </ScatterChart>
      );
    }
  };

  return (
    <div>
      <button className="toggle-button" onClick={toggleChartType}>
        Switch to {chartType === 'line' ? 'Scatter Plot' : 'Line Chart'}
      </button>
      <div className="mygraph">
        <ResponsiveContainer width="100%" height={400}>
          {renderChart()}
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default Graph;
