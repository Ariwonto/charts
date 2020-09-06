from django.shortcuts import render

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from charts.fusioncharts import FusionCharts
from charts.fusioncharts import FusionTable
from charts.fusioncharts import TimeSeries
import requests
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
# Loading Data and schema from a Static JSON String url
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

    data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/candlestick-chart-data.json').text
    schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/candlestick-chart-schema.json').text

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("caption", """{ 
											text: 'Apple Inc. Stock Price'
										}""")

    timeSeries.AddAttribute("yAxis", """[{
										  plot: {
											value: {
											  open: 'Open',
											  high: 'High',
											  low: 'Low',
											  close: 'Close'
											},
											type: 'candlestick'
										  },
										  format: {
											prefix: '$'
										  },
										  title: 'Stock Value'
                                        }]""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'output' : fcChart.render(), 'chartTitle': "Interactive candlestick chart"})