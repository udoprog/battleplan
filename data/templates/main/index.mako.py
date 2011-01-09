# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294547462.5460241
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/main/index.mako'
_template_uri='/main/index.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<h1>BattlePlanner</h1>\n\n<p>\n    <b>BattlePlanner</b> is an <b>intelligence hub</b>, allowing you to quickly link and share intelligence with your fellow pilots.\n</p>\n<p>\n    It works as a <b>lightweight</b> and <b>limited messaging</b> system (like twitter) but <b>notifications</b> will pop up and disturb you, meaning it will be easy to take notice on important events.\n</p>\n<p>\n    If you are interested in only a certain type of event, there are <b>hash-marks</b> in the messages, that will allow you to look or filter at notifications related to a specific type of event.\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


