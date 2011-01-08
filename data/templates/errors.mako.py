# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294503115.1190741
_template_filename=u'/home/udoprog/repo/git/battleplan/battleplan/templates/errors.mako'
_template_uri=u'/errors.mako'
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
        for error in c.errors.messages:
            # SOURCE LINE 2
            __M_writer(u'<div class="error">')
            __M_writer(escape(error))
            __M_writer(u'</div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


