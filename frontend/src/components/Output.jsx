import React, { Component, useEffect } from "react";
import Plot from "react-plotly.js";

const Output = ({x_data, y_data}) => {
  {
    return (
      <div className="output_show">
          <Plot
            data={[
              {
                x: x_data,
                y: y_data,
                type: "bar",
                marker: { color: "cyan" },
              },
            ]}
            layout={{
              width: '50%',
              height: '50%',
              title: "Users vs Message Count",
              paper_bgcolor: "",
              plot_bgcolor: "#172042",
            }}
          />
      </div>
    );
  }
};

export default Output;