from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt

def chart(request):
   chartObj = FusionCharts( 'heatmap', 'ex1', '600', '400', 'chart-1', 'json', """{
  "colorrange": {
    "gradient": "1",
    "minvalue": "0",
    "startlabel": "Poor",
    "endlabel": "Outstanding"
  },
  "dataset": [
    {
      "data": [
        {
          "rowid": "JA",
          "columnid": "EN",
          "value": "3.7"
        },
        {
          "rowid": "JA",
          "columnid": "PY",
          "value": "4.3"
        },
        {
          "rowid": "JA",
          "columnid": "MT",
          "value": "4.0"
        },
        {
          "rowid": "JA",
          "columnid": "HS",
          "value": "3.3"
        },
        {
          "rowid": "JA",
          "columnid": "EC",
          "value": "3.1"
        },
        {
          "rowid": "EM",
          "columnid": "EN",
          "value": "3.6"
        },
        {
          "rowid": "EM",
          "columnid": "PY",
          "value": "4.0"
        },
        {
          "rowid": "EM",
          "columnid": "MT",
          "value": "3.2"
        },
        {
          "rowid": "EM",
          "columnid": "HS",
          "value": "2.6"
        },
        {
          "rowid": "EM",
          "columnid": "EC",
          "value": "3.2"
        },
        {
          "rowid": "JY",
          "columnid": "EN",
          "value": "3.8"
        },
        {
          "rowid": "JY",
          "columnid": "PY",
          "value": "4.1"
        },
        {
          "rowid": "JY",
          "columnid": "MT",
          "value": "3.9"
        },
        {
          "rowid": "JY",
          "columnid": "HS",
          "value": "2.6"
        },
        {
          "rowid": "JY",
          "columnid": "EC",
          "value": "2"
        },
        {
          "rowid": "WL",
          "columnid": "EN",
          "value": "3.4"
        },
        {
          "rowid": "WL",
          "columnid": "PY",
          "value": "3.2"
        },
        {
          "rowid": "WL",
          "columnid": "MT",
          "value": "4"
        },
        {
          "rowid": "WL",
          "columnid": "HS",
          "value": "2.5"
        },
        {
          "rowid": "WL",
          "columnid": "EC",
          "value": "3.1"
        }
      ]
    }
  ],
  "columns": {
    "column": [
      {
        "id": "EN",
        "label": "English"
      },
      {
        "id": "MT",
        "label": "Maths"
      },
      {
        "id": "PY",
        "label": "Physics"
      },
      {
        "id": "HS",
        "label": "History"
      },
      {
        "id": "EC",
        "label": "Economics"
      }
    ]
  },
  "rows": {
    "row": [
      {
        "id": "JA",
        "label": "Jacob"
      },
      {
        "id": "EM",
        "label": "Emma"
      },
      {
        "id": "JY",
        "label": "Jayden"
      },
      {
        "id": "WL",
        "label": "William"
      }
    ]
  },
  "chart": {
    "theme": "fusion",
    "caption": "Distribution of Marks for Students",
    "subcaption": "Bell Curve Grading",
    "xaxisname": "Subjects",
    "yaxisname": "Student Name",
    "showvalues": "1",
    "valuefontcolor": "#ffffff",
    "plottooltext": "$rowlabel's $columnlabel grading score: <b>$value</b>"
  }
}""")
   return render(request, 'index.html', {'output': chartObj.render()})