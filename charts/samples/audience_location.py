from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'scrollbar2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Number of redemptions per promos",
    "subcaption": "Pepitos Pizza ",
    "plottooltext": "$dataValue Redemptions",
    "yaxisname": "Number of Redemptions",
    "xaxisname": "Promos",
    "theme": "fusion"
  },
  "categories": [
    {
      "category": [
        {
          "label": "Every Thursday 2x1"
        },
        {
          "label": "Pepperoni Lovers"
        },
        {
          "label": "The next Pizza 1Euro"
        },
        {
          "label": "Family Pizza + Dessert"
        },
        {
          "label": "Monday + Pizza = Happiness"
        },
        {
          "label": "Carnivoras 3x1"
         }
      ]
    }
  ],
  "dataset": [
    {
      "data": [
        {
          "value": "972"
        },
        {
          "value": "9548"
        },
        {
          "value": "602"
        },
        {
          "value": "3301"
        },
        {
          "value": "3161"
        },
        {
          "value": "2884"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})