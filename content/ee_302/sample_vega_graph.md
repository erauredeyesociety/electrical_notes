The following is a sample vega script that wil render a basic graph with two black lines. This gives the illusion of a graph with the normal 4 quadrants with (0,0) being at the center becuase I cannot change where the axis starts in vega.

[Vega Graph Axis Documentation](https://vega.github.io/vega-lite/docs/axis.html#example-using-axis-minextent-to-align-multi-view-plots)

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

<div id="vis"></div>

<script type="text/javascript">
var spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "width": 400,
  "height": 400,
  "layer": [
    {
      "data": {
        "values": [
          {"x": -10, "x2": 10, "y": 0}
        ]
      },
      "mark": {
        "type": "rule",
        "color": "black",
        "strokeWidth": 2
      },
      "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "x2": {"field": "x2"},
        "y": {"field": "y", "type": "quantitative"}
      }
    },
    {
      "data": {
        "values": [
          {"y": -10, "y2": 10, "x": 0}
        ]
      },
      "mark": {
        "type": "rule",
        "color": "black",
        "strokeWidth": 2
      },
      "encoding": {
        "y": {"field": "y", "type": "quantitative"},
        "y2": {"field": "y2"},
        "x": {"field": "x", "type": "quantitative"}
      }
    }
  ],
  "encoding": {
    "x": {
      "type": "quantitative",
      "scale": {"domain": [-10, 10]},
      "axis": {
        "grid": true,
        "domain": false,
        "ticks": false,
        "labelFontSize": 12
      }
    },
    "y": {
      "type": "quantitative",
      "scale": {"domain": [-10, 10]},
      "axis": {
        "grid": true,
        "domain": false,
        "ticks": false,
        "labelFontSize": 12
      }
    }
  }
}
;
vegaEmbed('#vis', spec);
</script>