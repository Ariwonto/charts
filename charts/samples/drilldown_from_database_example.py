from django.shortcuts import render

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt

# The `chart` function is defined to load data from a `SalesRecord` Model.
# This data will be converted to JSON and the chart will be rendered.

def chart(request):
	
	# Create an object for the column2d chart using the FusionCharts class constructor and pass the
	# json url datahandler in the `dataSource` as parameter.
	column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "jsonurl","/datahandler")

	# returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
	return  render(request, 'index.html', {'output' : column2d.render()})