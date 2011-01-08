# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294174854.041281
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
    return runtime._inherit_from(context, u'/layout/main.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3

        today = -1
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['today'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 5
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 7
        __M_writer(escape(c.solarsystem.solarSystemName))
        __M_writer(u'</h1>\n\n<ul class="reports">\n')
        # SOURCE LINE 10
        if len(c.reports) == 0:
            # SOURCE LINE 11
            __M_writer(u'    <li>no reports</li>\n')
            pass
        # SOURCE LINE 13
        for r in c.reports:
            # SOURCE LINE 14
            if today != r.created.day:
                # SOURCE LINE 15
                __M_writer(u'    <li class="date"><span class="date">')
                __M_writer(escape(r.created.strftime("%Y-%m-%d")))
                __M_writer(u'</span></li>\n')
                pass
            # SOURCE LINE 17
            __M_writer(u'<li>\n    <span class="time">')
            # SOURCE LINE 18
            __M_writer(escape(r.created.strftime("%H:%M:%S")))
            __M_writer(u':</span>\n    <span class="text">')
            # SOURCE LINE 19
            __M_writer(escape(r.text))
            __M_writer(u'</span>\n</li>\n')
            # SOURCE LINE 21
            today = r.created.day 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['today'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 23
        __M_writer(u'</ul>\n\n<h2>')
        # SOURCE LINE 25
        __M_writer(escape(c.solarsystem.constellation.constellationName))
        __M_writer(u'</h2>\n<canvas id="map_constellation" width="300" height="300"></canvas>\n\n<h2>')
        # SOURCE LINE 28
        __M_writer(escape(c.solarsystem.region.regionName))
        __M_writer(u'</h2>\n<canvas id="map_region" width="300" height="300"></canvas>\n\n<script type="text/javascript">\n$(document).ready(function() {\n    var url = "')
        # SOURCE LINE 33
        __M_writer(escape(url('/map/systems')))
        __M_writer(u'";\n    var solarSystem = ')
        # SOURCE LINE 34
        __M_writer(escape(c.solarsystem.solarSystemID))
        __M_writer(u'\n    var constellation = ')
        # SOURCE LINE 35
        __M_writer(escape(c.solarsystem.constellationID))
        __M_writer(u';\n    var region = ')
        # SOURCE LINE 36
        __M_writer(escape(c.solarsystem.regionID))
        __M_writer(u';\n\n    var map_constellation = document.getElementById("map_constellation");\n    var map_region = document.getElementById("map_region");\n    \n    draw_systems(url, map_constellation, {\'solarSystem\': solarSystem, \'constellation\': constellation, \'text\': true, \'size\': 10, \'line-width\': 3, \'font\': \'12px sans-serif\', \'padding\': 20})\n    draw_systems(url, map_region, {\'solarSystem\': solarSystem, \'region\': region, \'constellation\': constellation , \'size\': 4, \'line-width\': 1, \'font\': \'8px sans-serif\', \'padding\': 20})\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


