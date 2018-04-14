# Example: Column operations
This example demonstrates some simple functionality of the SSE protocol.

We have tried to provide well documented code that you can easily follow along with. If something is unclear, please let us know so that we can update and improve our documentation. In this file, we guide you through a few key points in the implementation that are worth clarifying for this particular example.

## Content
* [Script evaluation](#script-evaluation)
* [Defined functions](#defined-functions)
* [Qlik documents](#qlik-documents)
* [Run the example!](#run-the-example)

## Script evaluation
Script evaluation is enabled in this example but only numeric data is handled by the plugin. That meaning, the only script functions supported by the plugin are `ScriptEval`, `ScriptAggr`, `ScriptEvalEx` and `ScriptAggrEx`. The plugin will throw an error if any other data type than numeric is sent as parameter of the last two mentioned functions.  

The given script is evaluated with the python method `eval`. `eval` evaluates a python expression and does not work very well with more complex scripts. See documentation of the method `eval` [here](https://docs.python.org/3/library/functions.html#eval). For tensor and scalar functions the script is evaluated row wise and for aggregations the script is evaluated once after all data is retrieved.  

The parameters sent from Qlik are stored in a _list_ called `args` where the first element corresponds to the first parameter. Note how the function types affect the list storing the given parameters, and hence the script itself, when the script is evaluated:
* If the function type is an aggregation the type of `args[0]` is a list containing all rows of the first parameter.
* If the function type is scalar or tensor, the type of `args[0]` will be a single numeric value representing the first row of the first parameter.

## Defined functions
In this plugin we have a couple of pre-defined functions, which cannot be modified from the UI. The function definitions are located in the  JSON file and include the following information:

| __Id__ | __Function Name__ | __Type__ | __ReturnType__ | __Parameters__ | Calculation | Remarks |
| ----- | ----- | ----- | ------ | ----- | ----- | ----- |
| 0 | SumOfRows | 2 (tensor) | 1 (numeric) | __name:__ 'col1', __type:__ 1 (numeric); __name:__ 'col2', __type:__ 1(numeric) | Built-in Python | The `SumOfRows` function is a tensor function summing two columns row-wise. |
| 1 | SumOfColumn| 1 (aggregation) | 1 (numeric) | __name:__ 'col1', __type:__ 1 (numeric) | Built-in Python | The `SumOfColumn` function is an aggregation and sums the values in a column. |
| 2 | MaxOfColumns_2 | 2 (tensor) | 1 (numeric) | __name:__ 'col1', __type:__ 1 (numeric); __name:__ 'col2', __type:__ 1(numeric) | Built-in Python | The `MaxOfColumns_2` function computes the maximum in each of two columns and returns the maximum values in two columns, therefore making it appropriate to be used from the Qlik load script. The function also sets the TableDescription header before sending the result.  |
| 3 | CalcOfColumn | 1 (aggregation) | 1 (numeric) | __name:__ 'col1', __type:__ 1 (numeric); __name:__ 'col2', __type:__ 1(numeric) | CustomCalc Library | The `CalcOfColumn` function is an aggregation and multiplies the values in a column. |
| 4 | CalcOfRows | 2 (tensor) | 1 (numeric) | __name:__ 'col1', __type:__ 1 (numeric); __name:__ 'col2', __type:__ 1(numeric) | CustomCalc Library | The `CalcOfRows` function is a tensor function multiplying two columns row-wise. |
| 5 | ConvertUSDtoINR | 2 (tensor) | 1 (numeric) | __name:__ 'col1', __type:__ 1 (numeric) | CustomCalc Library |  The `ConvertUSDtoINR` function is a tensor function that converts column with values in USD to INR currency. This function uses forex_python API.|
| 6 | ConvertUSDtoGBP | 2 (tensor) | 1 (numeric) | __name:__ 'col1', __type:__ 2 (string); __name:__ 'col2', __type:__ 1(numeric) | CustomCalc Library | The `ConvertUSDtoGBP` function is a tensor function that converts column with values in USD to GBP currency. This function uses forex_python API and the users.csv file. In addition, this function takes in the Qlik built-in function OSUser() for authentication and authorization.  |
| 7 | GetUserRole | 2 (tensor) | 2 (string) | __name:__ 'col1', __type:__ 2 (string) | CustomCalc Library | The `GetUserRole` function is a tensor function that retrieves the role for a given user. This function uses the users.csv file. In addition, this function takes in the Qlik built-in function OSUser() for authentication and authorization. |

In addition, the 'MaxOfColumns_2' function uses TableDescription

```python
# Set and send Table header
table = SSE.TableDescription(name='MaxOfColumns', numberOfRows=1)
table.fields.add(name='Max1', dataType=SSE.NUMERIC)
table.fields.add(name='Max2', dataType=SSE.NUMERIC)
md = (('qlik-tabledescription-bin', table.SerializeToString()),)
context.send_initial_metadata(md)
```

## Qlik Documents
We provide example documents for Qlik Sense (SSE_Column_Operations.qvf) and QlikView (SSE_Column_Operations.qvw).

There are a number of examples in the sheets demonstrating the same simple functionality using script functions as well as defined functions.

In the Qlik load script there is an example of the `Load ...  Extension ...` syntax for a table load using SSE. The field names given in the sent `TableDescription` are mapped to generic ones: _A_max_ and _B_max_. There are also examples of using SSE expressions within a regular load. In that case the SSE call is treated as a scalar or aggregation and only one column can be returned.

Qlik Sense Desktop Loader calling SSE function:

![Function called from Loader](qlik-sense-ldr.png?raw=true "Function called from Loader")

Qlik Sense Desktop Sheet calling SSE functions:

![Functions called from Sheet](qlik-sense-fns.png?raw=true "Functions called from Sheet")

## Run the example!
To run this example, follow the instructions in [Getting started with the Python examples](../GetStarted.md).
