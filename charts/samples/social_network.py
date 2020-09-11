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
          "value": "12500"
        },
        {
          "value": "3000"
        },
        {
          "value": "4800"
        },
        {
          "value": "8000"
        },
        {
          "value": "11000"
        }
      ]
    },
    {
      "seriesname": "Facebook",
      "data": [
        {
          "value": "7000"
        },
        {
          "value": "1500"
        },
        {
          "value": "3500"
        },
        {
          "value": "6000"
        },
        {
          "value": "14000"
        }
      ]
    },
    {
      "seriesname": "Twitter",
      "data": [
        {
          "value": "1000"
        },
        {
          "value": "4502"
        },
        {
          "value": "2390"
        },
        {
          "value": "23500"
        },
        {
          "value": "29000"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})