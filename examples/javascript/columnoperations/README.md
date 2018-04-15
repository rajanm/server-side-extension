# Example: SSE Column Operations in a Visualization
This example demonstrates some simple functionality of the SSE protocol integrated with a custom visualization.

The custom visualization provides a "search" capability to retrieve data, both from Qlik as well as the Qlik server side extension plugin (which is a gGRPC server).

Thanks to [Nick Webster](https://github.com/websy85), this example is based on the implementation from [sense-search-components](https://github.com/websy85/sense-search-components)

## Content
* [Defined functions](#defined-functions)
* [Qlik documents](#qlik-documents)
* [Run the example!](#run-the-example)

## Defined functions
In the Qlik SSE plugin, many functions are defined. This plugin uses the specific function shown below:

| __Id__ | __Function Name__ | __Type__ | __ReturnType__ | __Parameters__ | Calculation | Remarks |
| ----- | ----- | ----- | ------ | ----- | ----- | ----- |
| 4 | CalcOfRows | 2 (tensor) | 1 (numeric) | __name:__ 'col1', __type:__ 1 (numeric); __name:__ 'col2', __type:__ 1(numeric) | CustomCalc Library | The `CalcOfRows` function is a tensor function multiplying two columns row-wise. |

In the HTML web page, the below snippet shows how the functions in the Qlik SSE plugin can be invoked like any other Qlik function. Quantity and Price columns are multiplied using custom function 'CalcOfRows'.

```javascript
{
  "measure": "round(CustomCalcs.CalcOfRows([Quantity],[Price]))",
  "label": "Stock Value",
  "sortType" : "qSortByNumeric",
  "order" : -1
}
```

## Qlik Documents
We provide an example document for Qlik Sense (SSESample.qvf.qvf).

## Qlik Sense Desktop Loader calling SSE function:

![Qlik Sense Loader](qlik-ldr.PNG?raw=true "There are no columns or data sources for stock value calculation.")

## Qlik Sense Desktop Sheet calling SSE functions:

![Qlik Sense Visualization](qlik-sse-cse.PNG?raw=true "Function called from visualization.")

## Run the example!
Python & Qlik
To run Python gRPC server and Qlik, follow the instructions in [Getting started with the Python examples](../../python/GetStarted.md).

HTML
To run this example, open the standard_qsd_sse.html in browser once the Qlik SSE plugin and Qlik Sense Desktop are running.
