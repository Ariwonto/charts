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
      "value": "1466000"
    },
    {
      "label": "TOPii Web",
      "value": "1147800"
    },
    {
      "label": "Facebook",
      "value": "532200"
    },
    {
      "label": "Instagram",
      "value": "395000"
    },
    {
      "label": "Organic Web",
      "value": "250200"
    }

  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})