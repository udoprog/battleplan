# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294046775.8869629
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/travel/display_route.mako'
_template_uri='/travel/display_route.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<table>\n    <tr>\n        <td><b>System</b></td>\n        <td></td>\n        <td><b>To</b></td>\n    </tr>\n')
        # SOURCE LINE 7
        for step in c.route:
            # SOURCE LINE 8
            __M_writer(u'        <tr>\n            <td>')
            # SOURCE LINE 9
            __M_writer(escape(step[0].solarSystemName))
            __M_writer(u'</td>\n            <td>&mdash;&gt;</td>\n            <td>')
            # SOURCE LINE 11
            __M_writer(escape(step[1].solarSystemName))
            __M_writer(u'</td>\n        </tr>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


