from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt

def chart(request):
   chartObj = FusionCharts( 'pareto2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": " Top Hardware Defects Frequency",
    "subcaption": "Last year - ACME Computers",
    "theme": "fusion",
    "yaxisname": "# reported instances",
    "syaxisname": "% of total instances",
    "decimals": "1",
    "drawcrossline": "1"
  },
  "data": [
    {
      "label": "Hard-Disk",
      "value": "40"
    },
    {
      "label": "PCB",
      "value": "22"
    },
    {
      "label": "Printer",
      "value": "12"
    },
    {
      "label": "CDROM",
      "value": "10"
    },
    {
      "label": "Keyboard",
      "value": "6"
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})