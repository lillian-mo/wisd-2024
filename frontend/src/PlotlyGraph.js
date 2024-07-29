import React from "react";
import Plot from "react-plotly.js";

const PVDiagram = () => {
  // Define the data for the p-V diagram (simplified, for demonstration)
  const volumeBaseline = [0.6, 1.6, 2.6, 4.1, 5.6, 6.0, 5.1, 4.6, 3.6, 3.1, 2.1, 1.1, 0.6]; // Volume values for baseline (in cc)
  const pressureBaseline = [
    0.25,
    0.5,
    1.0,
    1.5,
    2.0,
    2.4,
    2.4,
    2.0,
    1.5,
    1.0,
    0.5,
    0.25,
    0.25
  ]; // Pressure values for baseline (in bar)

  const volumeIVO = [0.6, -1.0, -1.5, -2.0, -2.5, 3.1, 3.6, 4.1, 4.6, 5.1, 5.6, 6.0]; // Volume values for IVO (in cc)
  const pressureIVO = [1.5, 1.8, 2.1, 2.3, 2.4, 2.4, 2.3, 2.1, 1.8, 1.5, 1.0, 0.5, 0.25]; // Pressure values for IVO (in bar)

  // Create a trace for the baseline curve
  const baselineTrace = {
    x: volumeBaseline,
    y: pressureBaseline,
    mode: "lines",
    name: "bat head",
    type: "scatter",
    line: { shape: "spline" } // Customize the shape of the line
  };

  // Create a trace for the IVO curve
  const IVOTrace = {
    x: volumeIVO,
    y: pressureIVO,
    mode: "lines",
    name: "bat handle",
    type: "scatter",
    line: { shape: "spline" } // Customize the shape of the line
  };

  // Create layout for the diagram
  const layout = {
    // title: "Complex p-V Diagram",
    // autosize: false,
    xaxis: {
      // title: "Volume cyl/cc",
      type: "linear",
      range: [-4, 0], // Set the x-axis range
      ticks: 'outside',
      // tickvals: [-4, -3, -2, -1, 0], // Set the y-axis tick values
      tickmode: "array",
      showdividers: true,
      zeroline: false,
      linecolor: 'grey',
      linewidth: 1.5,
      mirror: true
    },
    yaxis: {
      // title: "Pressure cyl.bar",
      type: "linear",
      range: [-2, 1.5], // Set the y-axis range
      ticks: 'outside',
      // tickvals: [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5], // Set the x-axis tick values
      tickmode: "array",
      showdividers: true,
      zeroline: false,
      linecolor: 'grey',
      linewidth: 1.5,
      mirror: true

    }
  };

  return (
    <div>
      <Plot data={[baselineTrace, IVOTrace]} layout={layout} />
    </div>
  );
};

export default PVDiagram;
