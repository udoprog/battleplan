# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294004655.138046
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/where.mako'
_template_uri='/where.mako'
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
        __M_writer(u'Hello World\n\n')
        # SOURCE LINE 3
        if c.eve.trusted:
            # SOURCE LINE 4
            __M_writer(u'    ')
            __M_writer(escape(c.eve.solarsystem_name))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(escape(c.ss.solarSystemName))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


