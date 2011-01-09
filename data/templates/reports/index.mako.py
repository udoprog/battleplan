# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294546630.1554899
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/reports/index.mako'
_template_uri='/reports/index.mako'
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
    return runtime._inherit_from(context, u'/layout/reports.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<h2>Latest Intel</h2>\n\n<ul id="latest-reports" class="reports">\n    <li>Loading Reports...</li>\n</ul>\n\n<script type="text/javascript">\n\n$(function() {\n    var options = {\n        \'url.reports\': "')
        # SOURCE LINE 12
        __M_writer(escape(url('latest.json')))
        __M_writer(u'",\n        \'url.check\': "')
        # SOURCE LINE 13
        __M_writer(escape(url('check.json')))
        __M_writer(u'",\n        \'url.system_base\': "')
        # SOURCE LINE 14
        __M_writer(escape(url('solarsystems')))
        __M_writer(u'",\n        \'url.report_base\': "')
        # SOURCE LINE 15
        __M_writer(escape(url('reports')))
        __M_writer(u'",\n        \'flashing\': 20\n    }\n\n    dynamic_reports("#latest-reports", options);\n});\n\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


