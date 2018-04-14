# Getting started with the Python examples

If you want to use [Docker](http://www.docker.com/) to build and run the examples, here's a [quickstart](Docker.md).

We provide several examples at different levels of complexity, each of which is documented separately. All examples support mutual authentication. Note that the examples do **not** necessarily support the same functionality; therefore a function call in one example might not work in another.

The following table includes a short description of each example and the functionality it demonstrates.

| __Example__ | __Evaluation__ | __Data types__ | __Description__ |
|-----|------|-----|----|
| __Hello world__ | Script, function | String | Returns the same values as received, aggregating all values to a single string, both in script and function calls. Also demonstrates two functions with cache enabled, by default, and disabled by adding date time stamps to the end of each string value.|
| __Column operations__ | Script, function| Numeric | Adds two columns row-wise (tensor). Sums values in a column (aggregation). Demonstrates functionality both as script calls and function calls. |
| __Full script support__ | Script | Numeric, String, Dual | Full script support including SSE calls in both load-script and in chart expressions. All script functions are supported.|
| __Full script support using Pandas__ | Script | Numeric, String, Dual | Using the Pandas library and exec method to evaluate the script instead of eval. Also includes an example of writing a `TableDescription` in the script to be evaluated, when using the `Load ... Extension ...` statement. Otherwise it is the same example as the original full script support with all script functions supported. |

For details about a particular example, see its documentation:
- [Hello world](helloworld/README.md)
- [Column operations](columnoperations/README.md)
- [Full script support](fullscriptsupport/README.md)
- [Full script support using Pandas](fullscriptsupport_pandas/README.md)

## Running the Python examples
Follow these steps to quickly set up and run an example of your choice on your local machine, with an insecure connection, using either Qlik Sense Desktop, Qlik Sense Enterprise, QlikView Desktop or QlikView Server. To run several examples, or to run the examples with a secure connection or on another node, configure your system according to the instructions referenced in [Configuring SSE plugins in Qlik](../../docs/configuration.md). The `<examplename>`, `<EngineName>` and `<port>` referred to below are mapped to each example as follows:

| __Example__ | __`<examplename>`__ | __`<EngineName>`__ | __`<port>`__ |
| ----- | ----- | ----- | ----- |
| __Hello world__ | helloworld | HelloWorld | 50052 |
| __Column operations__ | columnsupport | CustomCalcs | 50053 |
| __Full script support__ | fullscriptsupport | Script | 50051 |
| __Full script support using Pandas__ | fullscriptsupport_pandas | ScriptPandas | 50056 |

### Qlik Sense Desktop
1. Install Qlik Sense Desktop (June 2017 release or later).
2. Make sure you have Python 3.4 (or later) installed as well as the `grpcio` package. For more information, see [Prerequisites for running the Python examples](prerequisites.md).
3. Add `SSEPlugin=<EngineName>,localhost:<port>` on a new line in your *Settings.ini* file located at *C:\Users\\[user]\Qlik\Sense*. Insert the values for `<EngineName>` and `<port>` from the table above for the selected example.
4. Copy the *.qvf* file from the selected example folder to *C:\Users\\[user]\Qlik\Sense\Apps*.
5. Run the corresponding `<examplename>` python package. The easiest way to do this is to open a command prompt, go to the example\python folder and type:

   `python <examplename>`  

   Insert the value for `<examplename>` from the table above for the selected example.
6. Start Qlik Sense Desktop and open the app for the example you chose.

### Qlik Sense Enterprise
1. Install Qlik Sense Enterprise (June 2017 release or later).
2. Make sure you have Python 3.4 (or later) installed as well as the `grpcio` package. For more information, see [Prerequisites for running the Python examples](prerequisites.md).
3. Add the SSE plugin settings in QMC under __Analytic connections__ by inserting the following values:  **name:** `<EngineName>`, **host:** localhost, **port:** `<port>`

    Alternatively, add `SSEPlugin=<EngineName>,localhost:<port>` on a new line in your *settings.ini* file located at *C:\ProgramData\Qlik\Sense*. Insert the values for `<EngineName>` and `<port>` from the table above for the selected example.

    __Note:__ Configuring the plugin via the *settings.ini* file is only valid for this node/machine; the settings will not be visible in the QMC. Also no access rules would apply in this case.
4. Add the *.qvf* file from the selected example folder to QMC.
5. Run the corresponding `<examplename>` python package. The easiest way to do this is to open a command prompt, go to the example\python folder and type:

   `python <examplename>`

   Insert the value for `<examplename>` from the table above for the selected example.
6. Start Qlik Sense Enterprise and open the app for the example you chose.

### QlikView Desktop
1. Install QlikView Desktop (November 2017 release or later).
2. Make sure you have Python 3.4 (or later) installed as well as the `grpcio` package. For more information, see [Prerequisites for running the Python examples](prerequisites.md).
3. Add `SSEPlugin=<EngineName>,localhost:<port>` on a new line in your *Settings.ini* file, below the heading [Settings 7]. *Settings.ini* is located at *C:\Users\\[user]\AppData\Roaming\QlikTech\QlikView*. Insert the values for `<EngineName>` and `<port>` from the table above for the selected example.
4. Run the corresponding `<examplename>` python package. The easiest way to do this is to open a command prompt, go to the example\python folder and type:

   `python <examplename>`  

   Insert the value for `<examplename>` from the table above for the selected example.
6. Start QlikView Desktop and open the *.qvw* file in the selected example folder.

### QlikView Server
1. Install QlikView Server (November 2017 release or later).
2. Make sure you have Python 3.4 (or later) installed as well as the `grpcio` package. For more information, see [Prerequisites for running the Python examples](prerequisites.md).
3. Add `SSEPlugin=<EngineName>,localhost:<port>` on a new line in your *Settings.ini* file, below the heading [Settings 7]. *Settings.ini* is located at *C:\ProgramData\QlikTech\QlikViewServer*. Insert the values for `<EngineName>` and `<port>` from the table above for the selected example.
4. Add the *.qvw* file from the selected example folder to your document root (e.g. *C:\ProgramData\QlikTech\Documents*) or a mounted folder.
5. Run the corresponding `<examplename>` python package. The easiest way to do this is to open a command prompt, go to the example\python folder and type:

   `python <examplename>`

   Insert the value for `<examplename>` from the table above for the selected example.
6. Start QlikView Server and open the app for the example you chose.

## Configuring all Python examples at once (except Qlik Sense Enterprise)
In order to use all four Python examples in parallel, all you have to do is to map a different name to each port on the same line in *Settings.ini*:
`SSEPlugin=Script,localhost:50051;HelloWorld,localhost:50052;CustomCalcs,localhost:50053;ScriptPandas,localhost:50056`
