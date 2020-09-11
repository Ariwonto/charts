from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'column3d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Promos displayed",
    "subcaption": "For Pepitos Pizza",
    "yaxisname": "Number of views{br}(in thousands)",
    "decimals": "1",
    "theme": "fusion"
  },
  "data": [
    {
      "label": "TOPii Mobile",
      "value": "14660"
    },
    {
      "label": "TOPii Web",
      "value": "11478"
    },
    {
      "label": "Facebook",
      "value": "5322"
    },
    {
      "label": "Instagram",
      "value": "3950"
    },
    {
      "label": "Organic Web",
      "value": "2502"
    }

  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})