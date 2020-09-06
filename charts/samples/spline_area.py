from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'mssplinearea', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Twitter Mentions",
    "yaxisname": "Number of mentions",
    "numbersuffix": "M",
    "subcaption": "(iPhone Vs Samsung)",
    "yaxismaxvalue": "2",
    "plottooltext": "$seriesName was mentioned <b>$dataValue</b> times on Twitter in $label",
    "theme": "fusion"
  },
  "categories": [
    {
      "category": [
        {
          "label": "2007"
        },
        {
          "label": "2008"
        },
        {
          "label": "2009"
        },
        {
          "label": "2010"
        },
        {
          "label": "2011"
        },
        {
          "label": "2012"
        },
        {
          "label": "2013"
        },
        {
          "label": "2014"
        },
        {
          "label": "2015"
        }
      ]
    }
  ],
  "dataset": [
    {
      "seriesname": "iPhone",
      "data": [
        {
          "value": "1.90"
        },
        {
          "value": "1.94"
        },
        {
          "value": "1.69"
        },
        {
          "value": "1.66"
        },
        {
          "value": "1.43"
        },
        {
          "value": "1.97"
        },
        {
          "value": "1.78"
        },
        {
          "value": "1.58"
        },
        {
          "value": "1.55"
        }
      ]
    },
    {
      "seriesname": "Samsung",
      "data": [
        {
          "value": "0.68"
        },
        {
          "value": "0.74"
        },
        {
          "value": "0.25"
        },
        {
          "value": "0.64"
        },
        {
          "value": "0.22"
        },
        {
          "value": "0.74"
        },
        {
          "value": "0.58"
        },
        {
          "value": "0.15"
        },
        {
          "value": "0.26"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})