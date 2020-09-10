from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'heatmap', 'ex1', '600', '400', 'chart-1', 'json', """{
  "colorrange": {
    "gradient": "0",
    "color": [
      {
        "code": "#6da81e",
        "minvalue": "0",
        "maxvalue": "50",
        "label": "Freezing"
      },
      {
        "code": "#f6bc33",
        "minvalue": "50",
        "maxvalue": "70",
        "label": "Warm"
      },
      {
        "code": "#e24b1a",
        "minvalue": "70",
        "maxvalue": "85",
        "label": "Hot"
      }
    ]
  },
  "dataset": [
    {
      "data": [
        {
          "rowid": "LA",
          "columnid": "WI",
          "displayvalue": "60.1",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "LA",
          "columnid": "SP",
          "displayvalue": "64.5",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "LA",
          "columnid": "SU",
          "displayvalue": "68.2",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "LA",
          "columnid": "AU",
          "displayvalue": "65.7",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "NY",
          "columnid": "WI",
          "displayvalue": "33.7",
          "colorrangelabel": "Freezing"
        },
        {
          "rowid": "NY",
          "columnid": "SP",
          "displayvalue": "57.8",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "NY",
          "columnid": "SU",
          "displayvalue": "74.49",
          "colorrangelabel": "Hot"
        },
        {
          "rowid": "NY",
          "columnid": "AU",
          "displayvalue": "57.6",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "CH",
          "columnid": "WI",
          "displayvalue": "22.89",
          "colorrangelabel": "Freezing"
        },
        {
          "rowid": "CH",
          "columnid": "SP",
          "displayvalue": "55.7",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "CH",
          "columnid": "SU",
          "displayvalue": "72.2",
          "colorrangelabel": "Hot"
        },
        {
          "rowid": "CH",
          "columnid": "AU",
          "displayvalue": "51.6",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "HO",
          "columnid": "WI",
          "displayvalue": "53.0",
          "colorrangelabel": "Warm"
        },
        {
          "rowid": "HO",
          "columnid": "SP",
          "displayvalue": "72.7",
          "colorrangelabel": "Hot"
        },
        {
          "rowid": "HO",
          "columnid": "SU",
          "displayvalue": "83.3",
          "colorrangelabel": "Hot"
        },
        {
          "rowid": "HO",
          "columnid": "AU",
          "displayvalue": "53.0",
          "colorrangelabel": "Warm"
        }
      ]
    }
  ],
  "columns": {
    "column": [
      {
        "id": "WI",
        "label": "Tuesday"
      },
      {
        "id": "SU",
        "label": "Wednesday"
      },
      {
        "id": "SP",
        "label": "Thursday"
      },
      {
        "id": "AU",
        "label": "Friday"
      }
    ]
  },
  "rows": {
    "row": [
      {
        "id": "NY",
        "label": "16:00"
      },
      {
        "id": "LA",
        "label": "17:00"
      },
      {
        "id": "CH",
        "label": "18:00"
      },
      {
        "id": "HO",
        "label": "19:00"
      }
    ]
  },
  "chart": {
    "theme": "fusion",
    "caption": "Time of the day of most activities",
    "subcaption": "Pepitos Pizza",
    "showvalues": "1",
    "mapbycategory": "1",
    "plottooltext": "$rowlabel's average visitor on the day $columnlabel is $displayvalue"
  }
}""")
   return render(request, 'index.html', {'output': chartObj.render()})