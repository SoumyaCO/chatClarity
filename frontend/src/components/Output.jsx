import React from "react";
import Chart from "react-apexcharts";

class Output extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      options: {
        chart: {
          id: "basic-bar",
        },
        xaxis: {
          categories: props.x_data,
          labels: {
            style: {
              colors: '#90D26D',
            },
          },
        },
        yaxis: {
          labels: {
            style: {
              colors: '#F6995C',
            
            },
          },
        },
        grid: {
          show: false, 
        },
        plot_bgcolor: "transparent",
        paper_bgcolor: "transparent",
        autosize: true,
      },
      series: [
        {
          name: "series-1",
          data: props.y_data,
        },
      ],
    };
    
  }

  render() {
    return (
      <div className="app">
        <div className="row">
          <div className="mixed-chart">
            <Chart
              options={this.state.options}
              series={this.state.series}
              type="bar"
              width="700"
            />
          </div>
        </div>
      </div>
    );
  }
}

export default Output;
