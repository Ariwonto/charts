from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt

def chart(request):
   chartObj = FusionCharts( 'splinearea', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Yearly sales of iPhone",
    "yaxisname": "Number of units sold",
    "subcaption": "2007-2016",
    "plottooltext": "<div><b>$dataValue</b> iPhones sold in $label</div>",
    "theme": "fusion"
  },
  "data": [
    {
      "label": "2007",
      "value": "1380000"
    },
    {
      "label": "2008",
      "value": "1450000"
    },
    {
      "label": "2009",
      "value": "1610000"
    },
    {
      "label": "2010",
      "value": "1540000"
    },
    {
      "label": "2011",
      "value": "1480000"
    },
    {
      "label": "2012",
      "value": "1573000"
    },
    {
      "label": "2013",
      "value": "2232000"
    },
    {
      "label": "2014",
      "value": "2476000"
    },
    {
      "label": "2015",
      "value": "2832000"
    },
    {
      "label": "2016",
      "value": "3808000"
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})