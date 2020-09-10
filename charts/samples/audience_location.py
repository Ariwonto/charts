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
          "label": "Todos los Jueves 2x1"
        },
        {
          "label": "Peperoni Lovers"
        },
        {
          "label": "La siguiente Pizza 1Euro"
        },
        {
          "label": "Pizza Familiar + Postre"
        },
        {
          "label": "Lunes + Pizza = Felicidad"
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
          "value": "97294205"
        },
        {
          "value": "95482197"
        },
        {
          "value": "60224172"
        },
        {
          "value": "33018247"
        },
        {
          "value": "31615028"
        },
        {
          "value": "28984878"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})