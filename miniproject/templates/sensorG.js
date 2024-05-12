var opts_temp = {
    angle: 0, // The span of the gauge arc
    lineWidth: 0.20, // The line thickness
    radiusScale: 1, // Relative radius
    pointer: {
      length: 0.35, // // Relative to gauge radius
      strokeWidth: 0.035, // The thickness
      color: '#000000' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#6F6EA0',   // Colors
    colorStop: '#C0C0DB',    // just experiment with them
    strokeColor: '#EEEEEE',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support
    staticLabels: {
      font: "10px sans-serif",  // Specifies font
      labels: [10, 18, 22, 30],  // Print labels at these values
      color: "#000000",  // Optional: Label text color
      fractionDigits: 0  // Optional: Numerical precision. 0=round off.
    },
    staticZones: [
      {strokeStyle: "#f03e3e", min: 10, max: 18},
      {strokeStyle: "#30B32D", min: 18, max: 22}, 
      {strokeStyle: "#f03e3e", min: 22, max: 30}, 
    ]
  };

var opts_humidity = {
    angle: 0, // The span of the gauge arc
    lineWidth: 0.20, // The line thickness
    radiusScale: 1, // Relative radius
    pointer: {
      length: 0.35, // // Relative to gauge radius
      strokeWidth: 0.035, // The thickness
      color: '#000000' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#6F6EA0',   // Colors
    colorStop: '#C0C0DB',    // just experiment with them
    strokeColor: '#EEEEEE',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support
    staticLabels: {
      font: "10px sans-serif",  // Specifies font
      labels: [30, 40, 60, 70],  // Print labels at these values
      color: "#000000",  // Optional: Label text color
      fractionDigits: 0  // Optional: Numerical precision. 0=round off.
    },
    staticZones: [
      {strokeStyle: "#f03e3e", min: 30, max: 40},
      {strokeStyle: "#30B32D", min: 40, max: 60}, 
      {strokeStyle: "#f03e3e", min: 60, max: 70}, 
    ]
  };

var opts_lumi = {
    angle: 0, // The span of the gauge arc
    lineWidth: 0.20, // The line thickness
    radiusScale: 1, // Relative radius
    pointer: {
      length: 0.35, // // Relative to gauge radius
      strokeWidth: 0.035, // The thickness
      color: '#000000' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#6F6EA0',   // Colors
    colorStop: '#C0C0DB',    // just experiment with them
    strokeColor: '#EEEEEE',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support
    staticLabels: {
      font: "10px sans-serif",  // Specifies font
      labels: [0, 200, 400],  // Print labels at these values
      color: "#000000",  // Optional: Label text color
      fractionDigits: 0  // Optional: Numerical precision. 0=round off.
    },
    staticZones: [
      {strokeStyle: "#f03e3e", min: 0, max: 200},
      {strokeStyle: "#30B32D", min: 200, max: 400}, 
    ]
  };

function setTemp(value){
    gauge_temp.set(value);
    gauge_temp.setTextField(document.getElementById("textfield-temp"));
}

function setHumidity(value){
    gauge_humidity.set(value);
    gauge_humidity.setTextField(document.getElementById("textfield-humidity"));
}

function setLumi(value){
    gauge_lumi.set(value);
    gauge_lumi.setTextField(document.getElementById('textfield-lumi'));
}

var target_temp = document.getElementById('canvas-temp'); // your canvas element
var target_humidity = document.getElementById('canvas-humidity');
var target_lumi = document.getElementById('canvas-lumi');

var gauge_temp = new Gauge(target_temp).setOptions(opts_temp); // create sexy gauge!
var gauge_humidity = new Gauge(target_humidity).setOptions(opts_humidity);
var gauge_lumi = new Gauge(target_lumi).setOptions(opts_lumi);

gauge_temp.maxValue = 30; // set max gauge value
gauge_temp.setMinValue(10);  // Prefer setter over gauge.minValue = 0
gauge_temp.animationSpeed = 32; // set animation speed (32 is default value)


gauge_humidity.maxValue = 70; // set max gauge value
gauge_humidity.setMinValue(30);  // Prefer setter over gauge.minValue = 0
gauge_humidity.animationSpeed = 32; // set animation speed (32 is default value)


gauge_lumi.maxValue = 400;
gauge_lumi.setMinValue(0);
gauge_lumi.animationSpeed = 32;
