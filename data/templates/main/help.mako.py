# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294543362.2409339
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
        __M_writer(u'\n\n<h2>Help</h2>\n\n<div id="help">\n    <p>\n        topics: <a href="#posting">Posting</a>\n        <a href="#hashes">Hashes</a>\n    </p>\n\n    <h3 id="posting">How to post Intel</h3>\n\n    <p>Locate the \'New Intel\' link - should be on top of the front page</p>\n\n    <img src="')
        # SOURCE LINE 15
        __M_writer(escape(url('/help/posting.png')))
        __M_writer(u'" width="314" height="400" />\n\n    <p>Fill out the form and post new intel</p>\n\n    <img src="')
        # SOURCE LINE 19
        __M_writer(escape(url('/help/posting-form.png')))
        __M_writer(u'" width="314" height="400" />\n\n    <h3 id="hashes">Hashes</h3>\n\n    <p>\n        Hashes are special markers which will add an anchor to your report, allowing people who filters their view to receive only the type of reports they are interested in.\n    </p>\n    <p>\n        Anchors are marked with a <em>number sign</em> (e.g. <code>#hash</code>) and are read without case, meaning <em>foo</em> will be treated as the same anchor as <em>FOO</em>.\n    </p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


