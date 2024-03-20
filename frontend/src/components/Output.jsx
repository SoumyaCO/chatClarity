import React from "react";
import Plot from "react-plotly.js";

const Output = ({ x_data, y_data }) => {
  return (
    <div className="output_show">
      <Plot
        data={[
          {
            x: x_data,
            y: y_data,
            type: "bar",
            marker: {
              color: "cyan",
              line: {
                color: "rgb(8,48,107)",
              },
            },
          },
        ]}
        layout={{
          showlegend: false,
          width: "100%",
          height: "100%",
          title: "Users vs Message Count",
          paper_bgcolor: "transparent",
          plot_bgcolor: "transparent",
          xaxis: {
            tickformat: "+91 %",
            showgrid: false,
            zeroline: false,
            tickfont: {
              size: 14,
              color: "#E8751A",
            },
          },
          font: {
            color: "#FF204E",
          },
          yaxis: {
            showgrid: false,
            zeroline: false,
            tickfont: {
              size: 14,
              color: "#E8751A",
            },
          },
          autosize: true,
          margin: {
            l: 50,
            r: 50,
            b: 100,
            t: 100,
            pad: 4,
          },
        }}
        config={{ displayModeBar: false }}
      />
    </div>
  );
};

export default Output;
