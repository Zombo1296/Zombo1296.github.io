
    var myConfig = {
      "layout": "2x1",
      "graphset": [{
        "type": "line",
        "zoom": {
          "shared": true,
          "background-color": "#3399ff"
        },
        "scale-x": {
          "values": "1:4",
          "zooming": true,
         
          "item": {
            "font-size": 10
          }
        },
        "scale-y": {
          "values": "0:300:150",
          "item": {
            "font-size": 10
          }
        },
        "plot": {
          "line-color": "#3399ff",
          "marker": {
            "background-color": "#3399ff"
          }
        },
        "plotarea": {
          "margin": "dynamic"
        },
        "series": [{
          "values": [
            138.2, 196.3, 153.6, 127.4
          ]
        }]
      }, {
        "type": "scatter",
        "zoom": {
          "shared": true,
          "background-color": "#ff0080"
        },
        "scale-x": {
          "values": "1:4",
          "zooming": true,
          "item": {
            "font-size": 10
          }
        },
        "scale-y": {
          "values": "0:300:150",
          "item": {
            "font-size": 10
          }
        },
       
        "series": [
        {
          "values": [
            [1,138.2],
            [1,28.2],
            [1,58.2],
            [2,118.2],
            [3,150.2],
            [4,197]
          ],
          "marker":{
              "type": "star5",
              "size": 4
            }
        },
        {"values": [
            [1,238.2],
            [1,228.2],
            [1,258.2],
            [2,218.2],
            [3,250.2],
            [4,257]
          ],
          "marker":{
              "type": "circle",
              "size": 5
            }
        }
        ]
      }, ]
    };

    zingchart.render({
      id: 'myChart',
      data: myConfig,
      height: 400,
      width: "100%"
    });