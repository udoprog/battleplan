# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294547345.554508
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/reports/show.mako'
_template_uri='/reports/show.mako'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<h2>')
        # SOURCE LINE 3
        __M_writer(escape(c.report.title))
        __M_writer(u'</h2>\n<code style="display: block; background-color: white; border: 1px solid #777777; padding: 4px;">')
        # SOURCE LINE 4
        __M_writer(escape(c.text))
        __M_writer(u'</code>\n<p>\nReported for ')
        # SOURCE LINE 6
        __M_writer(escape(h.link_to(c.report.solarSystem.solarSystemName, url('solarsystem', id=c.report.solarSystem.solarSystemID))))
        __M_writer(u'<br />\nCreated at ')
        # SOURCE LINE 7
        __M_writer(escape(c.report.created))
        __M_writer(u'\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


