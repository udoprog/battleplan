# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294127394.5129299
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/travel/index.mako'
_template_uri='/travel/index.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<canvas id="map" width="300" height="300"></canvas>\n\n<script>\nfunction draw_jump(context, from, to, active, request) {\n    var with_text = request["text"] || false\n    var size = request["size"] || 4\n    var padding = (request["padding"] || 50) + 0.5;\n    var line_width = request["line-width"] || 2;\n\n    context.lineWidth = line_width\n    \n    if (active) {\n        context.strokeStyle = \'#999\'\n    } else {\n        context.strokeStyle = \'#333\'\n    }\n    \n    context.beginPath();\n    context.moveTo(from.x + padding, from.z + padding);\n    context.lineTo(to.x + padding, to.z + padding);\n    context.closePath();\n    context.stroke();\n}\n\nfunction draw_system(context, s, request) {\n    var with_text = request["text"] || false\n    var size = request["size"] || 4\n    var padding = (request["padding"] || 50) - size / 2 + 0.5;\n    var font = request["font"] || \'10px sans-serif\'\n    \n    if (s.security > 8) {\n        context.fillStyle = \'#0f0\'\n    }\n    else if (s.security > 6) {\n        context.fillStyle = \'#2d0\'\n    }\n    else if (s.security > 4) {\n        context.fillStyle = \'#4b0\'\n    }\n    else if (s.security > 2) {\n        context.fillStyle = \'#990\'\n    }\n    else if (s.security > 0) {\n        context.fillStyle = \'#a70\'\n    }\n    else if (s.security > -2) {\n        context.fillStyle = \'#c50\'\n    }\n    else if (s.security > -4) {\n        context.fillStyle = \'#d20\'\n    }\n    else {\n        context.fillStyle = \'#f00\'\n    }\n    \n    context.fillRect(s.x + padding, s.z + padding, size, size)\n    \n    if (with_text) {\n        context.font = font\n        context.fillText(s.name, s.x + padding + size / 2 + 8, s.z + padding)\n    }\n}\n\nfunction draw_systems(canvas, request) {\n    var request = request || {};\n\n    var context = canvas.getContext("2d")\n\n    var padding = request["padding"] || 50;\n    \n    request[\'resolution\'] = (canvas.width > canvas.height ? canvas.height: canvas.width) - padding * 2;\n    \n    context.fillStyle = \'#000000\'\n    context.fillRect(0,0,canvas.width,canvas.height)\n    \n    $.getJSON("')
        # SOURCE LINE 78
        __M_writer(escape(url('/map/systems')))
        __M_writer(u'", request, function(data){\n        for (i in data.jumps) {\n            var j = data.jumps[i];\n            var from = data.systems[j[0]];\n            var to = data.systems[j[1]];\n            var active = j[2];\n            draw_jump(context, from, to, active, request)\n        }\n        \n        for (i in data.systems) {\n            draw_system(context, data.systems[i], request);\n        }\n    });\n}\n\n$(document).ready(function() {\n    //var map_1 = document.getElementById("map_1");\n    //var map_2 = document.getElementById("map_2");\n    var map = document.getElementById("map");\n    \n    //draw_systems(map_1, {\'text\': false, \'padding\': 50, size: 2, \'line-width\': 1})\n    //draw_systems(map_2, {\'region\': 10000035, \'text\': false, \'padding\': 20, \'line-width\': 1})\n    draw_systems(map, {\'constellation\': 20000425, \'text\': true, \'size\': 10, \'line-width\': 3, \'font\': \'12px sans-serif\', \'padding\': 20})\n})\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


