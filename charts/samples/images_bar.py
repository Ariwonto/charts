from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts

from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'column2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
        "caption": "Top Soft Drinks Brand",
    "subcaption": "Last Year",
    "yaxisname": "Amount (In USD)",
    "numberprefix": "$",
    "yaxismaxvalue": "10000000000",
    "theme": "fusion",
    "plotfillalpha": "0",
    "plothovereffect": "0",
    "plottooltext": "Annual Revenue earned{br} by $label : <b>$dataValue</b>"
  },
  "annotations": {
    "groups": [
      {
        "id": "user-images",
        "autoscale": "1",
        "scaleimage": "1",
        "items": [
          {
            "id": "coke",
            "type": "image",
            "url": "http://cdn7.bigcommerce.com/s-9dfc48dsn9/images/stencil/500x659/products/112/376/Coke_Can_12oz_99c__43854.1469287831.png?c=2",
            "x": "$dataset.0.set.0.X-45",
            "y": "$canvasEndY-195",
            "xscale": "29",
            "yscale": "29"
          },
          {
            "id": "redbull",
            "type": "image",
            "url": "http://pluspng.com/img-png/red-bull-png-more-views-600.png",
            "x": "$dataset.0.set.1.X-83",
            "y": "$canvasEndY-162",
            "xscale": "29",
            "yscale": "29"
          },
          {
            "id": "pepsi",
            "type": "image",
            "url": "https://www.freeiconspng.com/uploads/pepsi-icon-0.png",
            "x": "$dataset.0.set.2.X-55",
            "y": "$canvasEndY-128",
            "xscale": "22",
            "yscale": "27"
          },
          {
            "id": "sprite",
            "type": "image",
            "url": "https://telugu.samayam.com/photo/msid-49820508,width-473,resizemode-4/business/business-news/cocacola-to-launch-sprite-zero-in-india.jpg",
            "x": "$dataset.0.set.3.STARTX",
            "y": "$canvasEndY-96",
            "xscale": "17",
            "yscale": "19"
          }
        ]
      }
    ]
  },
  "data": [
    {
      "label": "Coke",
      "value": "2900000000"
    },
    {
      "label": "Red Bull",
      "value": "5100000000"
    },
    {
      "label": "Pepsi",
      "value": "4100000000"
    },
    {
      "label": "Sprite",
      "value": "3300000000"
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})