from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'msspline', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Promos : Viewed vs Saved",
    "yaxisname": "# of Promos",
    "subcaption": "Last week",
    "numdivlines": "3",
    "showvalues": "0",
    "legenditemfontsize": "15",
    "legenditemfontbold": "1",
    "plottooltext": "<b>$dataValue</b> Promos $seriesName on $label",
    "theme": "fusion"
  },
  "categories": [
    {
      "category": [
        {
          "label": "Jan 1"
        },
        {
          "label": "Jan 2"
        },
        {
          "label": "Jan 3"
        },
        {
          "label": "Jan 4"
        },
        {
          "label": "Jan 5"
        },
        {
          "label": "Jan 6"
        },
        {
          "label": "Jan 7"
        }
      ]
    }
  ],
  "dataset": [
    {
      "seriesname": "Viewed",
      "data": [
        {
          "value": "55"
        },
        {
          "value": "45"
        },
        {
          "value": "52"
        },
        {
          "value": "29"
        },
        {
          "value": "48"
        },
        {
          "value": "28"
        },
        {
          "value": "32"
        }
      ]
    },
    {
      "seriesname": "Saved",
      "data": [
        {
          "value": "50"
        },
        {
          "value": "30"
        },
        {
          "value": "49"
        },
        {
          "value": "22"
        },
        {
          "value": "43"
        },
        {
          "value": "14"
        },
        {
          "value": "31"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})