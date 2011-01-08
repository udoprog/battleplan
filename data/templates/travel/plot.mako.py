# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294053748.7470629
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/travel/plot.mako'
_template_uri='/travel/plot.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        round = context.get('round', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<table>\n    <tr>\n        <td colspan="5">')
        # SOURCE LINE 4
        __M_writer(escape(len(c.route)))
        __M_writer(u' Jumps</td>\n    </tr>\n')
        # SOURCE LINE 6
        if c.no_route:
            # SOURCE LINE 7
            __M_writer(u'    <tr>\n        <td colspan="5"><b>No route</b></td>\n    </tr>\n')
            # SOURCE LINE 10
        else:
            # SOURCE LINE 11
            __M_writer(u'        <tr>\n            <td colspan="2"><b>System</b></td>\n            <td></td>\n            <td colspan="2"><b>To</b></td>\n        </tr>\n')
            # SOURCE LINE 16
            for system, dest in c.route:
                # SOURCE LINE 17
                __M_writer(u'            <tr>\n                <td>')
                # SOURCE LINE 18
                __M_writer(escape(system.solarSystemName))
                __M_writer(u'</td>\n                <td>(')
                # SOURCE LINE 19
                __M_writer(escape(round(system.security, 1)))
                __M_writer(u')</td>\n                <td>&mdash;</td>\n                <td><b>')
                # SOURCE LINE 21
                __M_writer(escape(dest.solarSystemName))
                __M_writer(u'</b></td>\n                <td>(')
                # SOURCE LINE 22
                __M_writer(escape(round(dest.security, 1)))
                __M_writer(u')</td>\n            </tr>\n')
                pass
            pass
        # SOURCE LINE 26
        __M_writer(u'</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


