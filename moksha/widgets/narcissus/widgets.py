from moksha.api.widgets.live import LiveWidget
from tw2.polymaps import PolyMap
from tw2.jqplugins.jqplot.base import dateAxisRenderer_js

from moksha.api.widgets.flot import LiveFlotWidget

import tw2.core as twc
import tw2.jquery

import logging
log = logging.getLogger(__name__)

green_css = twc.CSSLink(modname=__name__,
                        filename='static/css/custom_polymap.css')

class NarcissusMapWidget(LiveWidget, PolyMap):
    topic = 'http_geojson'
    layer_lifetime = 1000

    onmessage ="addGeoJsonToPolymap('${id}', json, %i)" % layer_lifetime

    zoom = 2.1
    center_latlon = {'lat': 35.8, 'lon' : -344.2}

    # Let the user control the map
    interact = True

    # Deep-linking
    hash = True

    # You should get your own one of these at http://cloudmade.com/register
    cloudmade_api_key = "1a1b06b230af4efdbb989ea99e9841af"

    # To style the map tiles
    cloudmade_tileset = 'midnight-commander'

    # Both specify the css_class AND include your own custom css file that
    # specifies what it looks like.
    css_class = 'midnight-commander-extras'

    resources = LiveWidget.resources + PolyMap.resources + [green_css]

class NarcissusPlotWidget(LiveFlotWidget):
    name = 'Usage of http://mirror.rit.edu'
    topic = 'http_metrics'
    width = '100%'
    height = '100%'
    onmessage = """
        if (json == null) {
            return;
        } else {
            %s
        }
        """ % LiveFlotWidget.onmessage

logswidget_js = twc.JSLink(modname=__name__, filename="static/js/logs.js")
logswidget_css = twc.CSSLink(modname=__name__, filename="static/css/logs.css")

class NarcissusLogsWidget(LiveWidget):
    resources = LiveWidget.resources + [
        tw2.jquery.jquery_js,
        logswidget_js,
        logswidget_css,
    ]

    topic = 'http_colorlogs'
    onmessage = "addLogMessage('${id}', json)"
    template = "mako:moksha.widgets.narcissus.templates.logs"

polyselect_css = twc.CSSLink(modname=__name__,
                             filename='static/css/polyselect.css')
