from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'scrollbar2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Top 25 NPM Packages for Node.js Developers",
    "subcaption": "March 2019 ",
    "plottooltext": "$dataValue Downloads",
    "yaxisname": "Number of Downloads",
    "xaxisname": "Packages",
    "theme": "fusion"
  },
  "categories": [
    {
      "category": [
        {
          "label": "Commander.js"
        },
        {
          "label": "Async.js"
        },
        {
          "label": "Request"
        },
        {
          "label": "Express"
        },
        {
          "label": "WebPack"
        },
        {
          "label": "Underscore"
        },
        {
          "label": "React"
        },
        {
          "label": "JSDom"
        },
        {
          "label": "Cheerio"
        },
        {
          "label": "Mocha"
        },
        {
          "label": "Marked"
        },
        {
          "label": "LESS"
        },
        {
          "label": "Morgan"
        },
        {
          "label": "Karma"
        },
        {
          "label": "MongoDB Driver"
        },
        {
          "label": "Nodemailer"
        },
        {
          "label": "Passport"
        },
        {
          "label": "Browserify"
        },
        {
          "label": "Grunt"
        },
        {
          "label": "JSHint"
        },
        {
          "label": "Angular"
        },
        {
          "label": "Bower"
        },
        {
          "label": "Pug"
        },
        {
          "label": "PM2"
        },
        {
          "label": "Hapi"
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
        },
        {
          "value": "25391784"
        },
        {
          "value": "23581733"
        },
        {
          "value": "12321215"
        },
        {
          "value": "10838161"
        },
        {
          "value": "7808888"
        },
        {
          "value": "7127519"
        },
        {
          "value": "6659395"
        },
        {
          "value": "5731933"
        },
        {
          "value": "4843888"
        },
        {
          "value": "3264090"
        },
        {
          "value": "2755188"
        },
        {
          "value": "2661761"
        },
        {
          "value": "2371272"
        },
        {
          "value": "2201511"
        },
        {
          "value": "1821149"
        },
        {
          "value": "1683996"
        },
        {
          "value": "1602832"
        },
        {
          "value": "1267422"
        },
        {
          "value": "1042206"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})