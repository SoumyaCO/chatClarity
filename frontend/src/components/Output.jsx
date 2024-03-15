import React, { Component, useEffect } from "react";
import Plot from "react-plotly.js";
// import { handleQuery } from "./FileUploder";
const Output = () => {
  {


    // useEffect(() => {
    //   // handleQuery()
    //   .then(data => setApiData(data))
    //   .catch(error => console.error('Error', error))
    // }, []);

    return (
      <div className="output_show">
          <Plot
            data={[
              {
                x: ['Abbas', 'Akbar', 'Anil', 'Amal'],
                y: [230, 160, 340, 432],
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
