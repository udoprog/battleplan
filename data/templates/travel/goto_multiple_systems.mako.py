# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294034510.0750511
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/travel/goto_multiple_systems.mako'
_template_uri='/travel/goto_multiple_systems.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<p>\n    There are multiple destination alternatives available:\n</p>\n\n<ul>\n')
        # SOURCE LINE 7
        for s in c.systems:
            # SOURCE LINE 8
            __M_writer(u'    <li>')
            __M_writer(escape(h.link_to(s.solarSystemName, url.current(dest=s.solarSystemName) + "?" + request.query_string)))
            __M_writer(u'</li>\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


