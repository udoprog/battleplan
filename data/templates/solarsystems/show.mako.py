# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294554278.1465549
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/solarsystems/show.mako'
_template_uri='/solarsystems/show.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layout/solarsystems.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<h2>Latest intel at <em>@')
        # SOURCE LINE 3
        __M_writer(escape(c.solarsystem.solarSystemName))
        __M_writer(u'</em></h2>\n\n<ul id="latest-reports" class="reports">\n    <li>loading reports...</li>\n</ul>\n\n<h2>')
        # SOURCE LINE 9
        __M_writer(escape(c.solarsystem.constellation.constellationName))
        __M_writer(u'</h2>\n<canvas id="map_constellation" width="300" height="300"></canvas>\n\n<h2>')
        # SOURCE LINE 12
        __M_writer(escape(c.solarsystem.region.regionName))
        __M_writer(u'</h2>\n<canvas id="map_region" width="300" height="300"></canvas>\n\n<script type="text/javascript">\n$(document).ready(function() {\n    var url = "')
        # SOURCE LINE 17
        __M_writer(escape(url('/map/systems')))
        __M_writer(u'";\n    var solarSystem = ')
        # SOURCE LINE 18
        __M_writer(escape(c.solarsystem.solarSystemID))
        __M_writer(u'\n    var constellation = ')
        # SOURCE LINE 19
        __M_writer(escape(c.solarsystem.constellationID))
        __M_writer(u';\n    var region = ')
        # SOURCE LINE 20
        __M_writer(escape(c.solarsystem.regionID))
        __M_writer(u';\n\n    var map_constellation = document.getElementById("map_constellation");\n    var map_region = document.getElementById("map_region");\n    \n    /* request and draw out the constellation map */\n    draw_systems(url, map_constellation, {\'solarSystem\': solarSystem, \'constellation\': constellation, \'text\': true, \'size\': 10, \'line-width\': 3, \'font\': \'12px sans-serif\', \'padding\': 20})\n    \n    /* request and draw out the region map */\n    draw_systems(url, map_region, {\'solarSystem\': solarSystem, \'region\': region, \'constellation\': constellation , \'size\': 4, \'line-width\': 1, \'font\': \'8px sans-serif\', \'padding\': 20})\n\n    var options = {\n        \'url.reports\': "')
        # SOURCE LINE 32
        __M_writer(escape(url('latest.json')))
        __M_writer(u'",\n        \'url.check\': "')
        # SOURCE LINE 33
        __M_writer(escape(url('check.json')))
        __M_writer(u'",\n        \'url.system_base\': "')
        # SOURCE LINE 34
        __M_writer(escape(url('solarsystems')))
        __M_writer(u'",\n        \'url.report_base\': "')
        # SOURCE LINE 35
        __M_writer(escape(url('reports')))
        __M_writer(u'",\n        \'flashing\': 20,\n        \'solarsystem\': ')
        # SOURCE LINE 37
        __M_writer(escape(c.solarsystem.solarSystemID))
        __M_writer(u'\n    }\n\n    dynamic_reports("#latest-reports", options);\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


