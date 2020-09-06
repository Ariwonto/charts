from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'column3d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Countries with Highest Deforestation Rate",
    "subcaption": "For the year 2017",
    "yaxisname": "Deforested Area{br}(in Hectares)",
    "decimals": "1",
    "theme": "fusion"
  },
  "data": [
    {
      "label": "Brazil",
      "value": "1466000"
    },
    {
      "label": "Indonesia",
      "value": "1147800"
    },
    {
      "label": "Russian Federation",
      "value": "532200"
    },
    {
      "label": "Mexico",
      "value": "395000"
    },
    {
      "label": "Papua New Guinea",
      "value": "250200"
    },
    {
      "label": "Peru",
      "value": "224600"
    },
    {
      "label": "U.S.A",
      "value": "215200"
    },
    {
      "label": "Bolivia",
      "value": "135200"
    },
    {
      "label": "Sudan",
      "value": "117807"
    },
    {
      "label": "Nigeria",
      "value": "82000"
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})