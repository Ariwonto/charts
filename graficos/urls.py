"""graficos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from charts.views import catalogue

from charts import datahandler
from charts.samples import rendering_angular_gauge_using_dictionary_example, rendering_column2d_chart_using_dictionary_example
from charts.samples import rendering_map_using_dictionary_example, rendering_multiseries_column2d_chart_using_json_example
from charts.samples import rendering_multiseries_StackedColumn2dline_using_json_example, rendering_pie3d_using_json_example
from charts.samples import rendering_column_line_area_combi_using_json_example, rendering_map_using_json_example
from charts.samples import rendering_angular_gauge_using_json_example, client_side_chart_export
from charts.samples import fetching_json_data_from_url, fetching_xml_data_from_url, fetching_data_from_database
from charts.samples import drilldown_from_database_example, rendering_charts_by_common_theme
from charts.samples import export_chart_using_export_handler
from charts.samples import dynamic_chart_resize, dynamic_chart_type, chart_annotation, chart_update_onclick
from charts.samples import chart_tooltip, rendering_chart_with_different_language, chart_special_chart
from charts.samples import product_life_cycle_event, special_event, chart_message, interactive_event, number_format_module
from charts.samples import special_chart_type_api, chart_instance_level_api, chart_product_level_api
from charts.samples import updating_chart_properties, highlight_specific_data_points, update_data_runtime
from charts.samples import get_data_from_scatter_chart
from charts.samples import Line_Chart_With_Time_Axis, Plotting_Multiple_Series_On_Time_Axis
from charts.samples import Column_and_line_combination_on_time_axis, Plotting_Two_Variables
from charts.samples import Different_Plot_Type_Chart, ColumnChart_With_Time_Axis
from charts.samples import AreaChart_With_Time_Axis, Interactive_candlestick_chart
from charts.samples import Annotating_single_data_point, Single_Event_Overlay
from charts.samples import Date_range_event_overlay, Adding_Reference_Line
from charts.samples import bubble_xy
from charts.samples import displays_bar
from charts.samples import spline_data
from charts.samples import social_network
from charts.samples import audience_location
from charts.samples import heat_map_most_redeem
from charts.samples import bar_chart_custom_labels
from charts.samples import spline_area
from charts.samples import stacked_egative_values, chord_diagram
from charts.samples import simple_sankey, sunburst_with_multiple_roots

urlpatterns = [
    url(r'^$', catalogue),
    url(r'^admin/', admin.site.urls),
    url(r'^datahandler', datahandler.getdata),
    url(r'^rendering-angular-gauge-using-dictionary-example', rendering_angular_gauge_using_dictionary_example.chart, name='chart'),
    url(r'^rendering-angular-gauge-using-json-example', rendering_angular_gauge_using_json_example.chart, name='chart'),
    url(r'^rendering-column2d-chart-using-dictionary-example', rendering_column2d_chart_using_dictionary_example.chart, name='chart'),
    url(r'^rendering-map-using-dictionary-example', rendering_map_using_dictionary_example.chart, name='chart'),
    url(r'^rendering-map-using-json-example', rendering_map_using_json_example.chart, name='chart'),
    url(r'^rendering-multiseries-column2d-chart-using-json-example', rendering_multiseries_column2d_chart_using_json_example.chart, name='chart'),
    url(r'^rendering-multiseries-StackedColumn2dline-using-json-example', rendering_multiseries_StackedColumn2dline_using_json_example.chart, name='chart'),
    url(r'^rendering-pie3d-using-json-example', rendering_pie3d_using_json_example.chart, name='chart'),
    url(r'^rendering-column-line-area-combi-using-json-example', rendering_column_line_area_combi_using_json_example.chart, name='chart'),
    url(r'^client-side-chart-export', client_side_chart_export.chart, name='chart'),
    url(r'^fetching-json-data-from-url', fetching_json_data_from_url.chart, name='chart'),
    url(r'^fetching-xml-data-from-url', fetching_xml_data_from_url.chart, name='chart'),
    url(r'^fetching-data-from-database', fetching_data_from_database.chart, name='chart'),
    url(r'^drilldown-from-database-example', drilldown_from_database_example.chart, name='chart'),
    url(r'^rendering-charts-by-common-theme', rendering_charts_by_common_theme.chart, name='chart'),
    url(r'^export-chart-using-export-handler', export_chart_using_export_handler.chart, name='chart'),
    url(r'^dynamic-chart-resize', dynamic_chart_resize.chart, name='chart'),
    url(r'^dynamic-chart-type', dynamic_chart_type.chart, name='chart'),
    url(r'^chart-annotation', chart_annotation.chart, name='chart'),
    url(r'^chart-update-onclick', chart_update_onclick.chart, name='chart'),
    url(r'^rendering-chart-with-different-language', rendering_chart_with_different_language.chart, name='chart'),
    url(r'^chart-special-chart', chart_special_chart.chart, name='chart'),
    url(r'^chart-tooltip', chart_tooltip.chart, name='chart'),
    url(r'^product-life-cycle-event', product_life_cycle_event.chart, name='chart'),
    url(r'^special-event', special_event.chart, name='chart'),
    url(r'^chart-message', chart_message.chart, name='chart'),
    url(r'^interactive-event', interactive_event.chart, name='chart'),
    url(r'^number-format-module', number_format_module.chart, name='chart'),
    url(r'^special-chart-type-api', special_chart_type_api.chart, name='chart'),
    url(r'^chart-instance-level-api', chart_instance_level_api.chart, name='chart'),
    url(r'^chart-product-level-api', chart_product_level_api.chart, name='chart'),
    url(r'^updating-chart-properties', updating_chart_properties.chart, name='chart'),
    url(r'^highlight-specific-data-points', highlight_specific_data_points.chart, name='chart'),
    url(r'^update-data-runtime', update_data_runtime.chart, name='chart'),
    url(r'^get-data-from-scatter-chart', get_data_from_scatter_chart.chart, name='chart'),
    url(r'^Line-Chart-With-Time-Axis', Line_Chart_With_Time_Axis.chart, name='chart'),
    url(r'^Plotting-Multiple-Series-On-Time-Axis', Plotting_Multiple_Series_On_Time_Axis.chart, name='chart'),
    url(r'^Column-and-line-combination-on-time-axis', Column_and_line_combination_on_time_axis.chart, name='chart'),
    url(r'^Plotting-Two-Variables', Plotting_Two_Variables.chart, name='chart'),
    url(r'^Different-Plot-Type-Chart', Different_Plot_Type_Chart.chart, name='chart'),
    url(r'^ColumnChart-With-Time-Axis', ColumnChart_With_Time_Axis.chart, name='chart'),
    url(r'^AreaChart-With-Time-Axis', AreaChart_With_Time_Axis.chart, name='chart'),
    url(r'^Interactive-candlestick-chart', Interactive_candlestick_chart.chart, name='chart'),
    url(r'^Annotating-single-data-point', Annotating_single_data_point.chart, name='chart'),
    url(r'^Single-Event-Overlay', Single_Event_Overlay.chart, name='chart'),
    url(r'^Date-range-event-overlay', Date_range_event_overlay.chart, name='chart'),
    url(r'^Adding-Reference-Line', Adding_Reference_Line.chart, name='chart'),
    url(r'^bubble-xy', bubble_xy.chart, name='chart'),
    url(r'^displays-bar', displays_bar.chart, name='chart'),
    url(r'^spline-data', spline_data.chart, name='chart'),
    url(r'^social-network', social_network.chart, name='chart'),
    url(r'^audience-location', audience_location.chart, name='chart'),
    url(r'^heat-map-most-redeem', heat_map_most_redeem.chart, name='chart'),
    url(r'^bar-chart-custom-labels', bar_chart_custom_labels.chart, name='chart'),
    url(r'^spline-area', spline_area.chart, name='chart'),
    url(r'^stacked-egative-values', stacked_egative_values.chart, name='chart'),
    url(r'^simple-sankey', simple_sankey.chart, name='chart'),
    url(r'^sunburst-with-multiple-roots', sunburst_with_multiple_roots.chart, name='chart'),
    url(r'^chord-diagram', chord_diagram.chart, name='chart')

]

