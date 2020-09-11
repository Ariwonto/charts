from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'radar', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Business Analysis of Pepitos Pizza",
    "subcaption": "Scale: 1 (low) to 5 (high)",
    "theme": "fusion",
    "showlegend": "0",
    "showdivlinevalues": "0",
    "showlimits": "0",
    "showvalues": "1",
    "plotfillalpha": "40",
    "plottooltext": "Pepitos Pizza's <b>$label</b> skill is rated as <b>$value</b>"
  },
  "categories": [
    {
      "category": [
        {
          "label": "Shoppers preferences"
        },
        {
          "label": "Shoppers trends"
        },
        {
          "label": "Product demand"
        },
        {
          "label": "Redemption volume"
        },
        {
          "label": "View volume"
        }
      ]
    }
  ],
  "dataset": [
    {
      "seriesname": "User Ratings",
      "data": [
        {
          "value": "3"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        },
        {
          "value": "3"
        },
        {
          "value": "2"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})