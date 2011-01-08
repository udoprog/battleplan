# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294131038.672668
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/intel/report.mako'
_template_uri='/intel/report.mako'
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
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(escape(h.form(url.current(), method="put")))
        __M_writer(u'\n    System:<br />\n    ')
        # SOURCE LINE 5
        __M_writer(escape(h.text('system', style='width: 200px;')))
        __M_writer(u'<br />\n    Report:<br />\n    ')
        # SOURCE LINE 7
        __M_writer(escape(h.textarea('report', style='width: 200px; height: 160px;')))
        __M_writer(u'<br />\n    ')
        # SOURCE LINE 8
        __M_writer(escape(h.submit('report','Report')))
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\n<script type="text/javascript">\n$(document).ready(function() {\n    $("#system").autocomplete("')
        # SOURCE LINE 13
        __M_writer(escape(url('/map/complete')))
        __M_writer(u'")\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


