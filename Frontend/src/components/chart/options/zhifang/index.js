import * as echarts from "echarts";

const xAxisData = Array.from({ length: 256 }, (v, k) => k);

const testBar = (_data) => {
  const defaultConfig = {
    title: {
      text: "图像直方图",
    },
    color: ["#DE6E6A", "#ADDE8B", "#5A6FC0", "#F3F6FA"],
    tooltip: {
      trigger: "item",
      axisPointer: {
        type: "cross",
        snap: true,
      },
    },
    legend: {
      data: ["RED", "GREEN", "BLUE", "GRAY"],
    },
    toolbox: {
      show: true,
      feature: {
        saveAsImage: {},
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        data: xAxisData,
      },
    ],
    yAxis: [
      {
        type: "value",
      },
    ],
    series: [
      {
        name: "RED",
        data: _data.r,
        type: "line",
        smooth: true,
        areaStyle: {
          opacity: 0.8,
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "#DE6E6A",
            },
            {
              offset: 1,
              color: "#DE6E6A",
            },
          ]),
        },
      },
      {
        name: "GREEN",
        data: _data.g,
        type: "line",
        smooth: true,
        areaStyle: {
          opacity: 0.8,
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "#ADDE8B",
            },
            {
              offset: 1,
              color: "#ADDE8B",
            },
          ]),
        },
      },
      {
        name: "BLUE",
        data: _data.b,
        type: "line",
        smooth: true,
        areaStyle: {
          opacity: 0.8,
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "#5A6FC0",
            },
            {
              offset: 1,
              color: "#5A6FC0",
            },
          ]),
        },
      },
      {
        name: "GRAY",
        data: _data.gray,
        type: "line",
        smooth: true,
        areaStyle: {
          opacity: 0.8,
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "#F3F6FA",
            },
            {
              offset: 1,
              color: "#F3F6FA",
            },
          ]),
        },
      },
      // {
      //   name: "RED",
      //   type: "line",
      //   stack: "Total",
      //   smooth: true,
      //   lineStyle: {
      //     width: 0,
      //   },
      //   showSymbol: true,
      //   areaStyle: {
      //     opacity: 0.8,
      //     color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
      //       {
      //         offset: 0,
      //         color: "#DE6E6A",
      //       },
      //       {
      //         offset: 1,
      //         color: "#DE6E6A",
      //       },
      //     ]),
      //   },
      //   emphasis: {
      //     focus: "series",
      //   },
      //   data: xAxisData,
      // },
      // {
      //   name: "GREEN",
      //   type: "line",
      //   stack: "Total",
      //   smooth: true,
      //   lineStyle: {
      //     width: 0,
      //   },
      //   showSymbol: true,
      //   areaStyle: {
      //     opacity: 0.8,
      //     color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
      //       {
      //         offset: 0,
      //         color: "#ADDE8B",
      //       },
      //       {
      //         offset: 1,
      //         color: "#ADDE8B",
      //       },
      //     ]),
      //   },
      //   emphasis: {
      //     focus: "series",
      //   },
      //   data: xAxisData,
      // },
      // {
      //   name: "BLUE",
      //   type: "line",
      //   stack: "Total",
      //   smooth: true,
      //   lineStyle: {
      //     width: 0,
      //   },
      //   showSymbol: true,
      //   areaStyle: {
      //     opacity: 0.8,
      //     color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
      //       {
      //         offset: 0,
      //         color: "#5A6FC0",
      //       },
      //       {
      //         offset: 1,
      //         color: "#5A6FC0",
      //       },
      //     ]),
      //   },
      //   emphasis: {
      //     focus: "series",
      //   },
      //   data: xAxisData,
      // },
    ],
  };

  const opt = Object.assign({}, defaultConfig);
  return opt;
};

export default {
  testBar,
};
