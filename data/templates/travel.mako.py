# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294008806.809526
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/travel.mako'
_template_uri='/travel.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        if not c.ts:
            # SOURCE LINE 2
            __M_writer(u'    Could not find a system to travel to\n    ')
            # SOURCE LINE 3
            return 
            
            __M_writer(u'\n')
            pass
        # SOURCE LINE 5
        __M_writer(u'\nHello ')
        # SOURCE LINE 6
        __M_writer(escape(c.ts.solarSystemName))
        __M_writer(u'<br />\n\nJumps: ')
        # SOURCE LINE 8
        __M_writer(escape(len(c.route) - 1))
        __M_writer(u'\n\n<table>\n')
        # SOURCE LINE 11
        for i in range(0, len(c.route) - 1):
            # SOURCE LINE 12
            __M_writer(u'    <tr>\n        <td>')
            # SOURCE LINE 13
            __M_writer(escape(c.route[i].solarSystemName))
            __M_writer(u'</td>\n        <td>-></td>\n        <td>')
            # SOURCE LINE 15
            __M_writer(escape(c.route[i+1].solarSystemName))
            __M_writer(u'</td>\n    </tr>\n')
            pass
        # SOURCE LINE 18
        __M_writer(u'</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


