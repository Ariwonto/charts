from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'mscolumn2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Promo Share",
    "subcaption": "Pepitos Pizza",
    "xaxisname": "Months",
    "yaxisname": "Total Promos Share",
    "formatnumberscale": "1",
    "plottooltext": "<b>$dataValue</b> shared promos on <b>$seriesName</b> in $label",
    "theme": "fusion",
    "drawcrossline": "1"
  },
  "categories": [
    {
      "category": [
        {
          "label": "Jan"
        },
        {
          "label": "Feb"
        },
        {
          "label": "Mar"
        },
        {
          "label": "Apr"
        },
        {
          "label": "May"
        }
      ]
    }
  ],
  "dataset": [
    {
      "seriesname": "Instagram",
      "data": [
        {
          "value": "125000"
        },
        {
          "value": "300000"
        },
        {
          "value": "480000"
        },
        {
          "value": "800000"
        },
        {
          "value": "1100000"
        }
      ]
    },
    {
      "seriesname": "Facebook",
      "data": [
        {
          "value": "70000"
        },
        {
          "value": "150000"
        },
        {
          "value": "350000"
        },
        {
          "value": "600000"
        },
        {
          "value": "1400000"
        }
      ]
    },
    {
      "seriesname": "Twitter",
      "data": [
        {
          "value": "10000"
        },
        {
          "value": "100000"
        },
        {
          "value": "300000"
        },
        {
          "value": "600000"
        },
        {
          "value": "900000"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})