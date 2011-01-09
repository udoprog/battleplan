# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294532666.179352
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/main/help.mako'
_template_uri='/main/help.mako'
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
        __M_writer(u'\n\n<h2>Help</h2>\n\n<h3>How to post Intel</h3>\n\n<h4>Locate the \'New Intel\' link</h4>\n\n<img src="')
        # SOURCE LINE 9
        __M_writer(escape(url('/help/posting.png')))
        __M_writer(u'" width="314" height="400" />\n\n<h4>Fill out the form and post new intel</h4>\n\n<img src="')
        # SOURCE LINE 13
        __M_writer(escape(url('/help/posting-form.png')))
        __M_writer(u'" width="314" height="400" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


