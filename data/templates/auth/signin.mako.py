# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294503314.695811
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/auth/signin.mako'
_template_uri='/auth/signin.mako'
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
        c = context.get('c', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<b>')
        # SOURCE LINE 3
        __M_writer(escape(c.path_before_login))
        __M_writer(u'</b>\n\n')
        # SOURCE LINE 5
        if hasattr(c, "error"):
            # SOURCE LINE 6
            __M_writer(u'    ')
            __M_writer(escape(c.error))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(escape(h.form(url("auth_signin"), method="post")))
        __M_writer(u'\n<table>\n    <tr>\n        <td>Name:</td>\n        <td>')
        # SOURCE LINE 13
        __M_writer(escape(h.text("name", value=c.name)))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td>Api User-ID:</td>\n        <td>')
        # SOURCE LINE 17
        __M_writer(escape(h.text("api_userid", value=c.api_userid)))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td>Api Key:</td>\n        <td>')
        # SOURCE LINE 21
        __M_writer(escape(h.text("api_key", value=c.api_key)))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td colspan="2">')
        # SOURCE LINE 24
        __M_writer(escape(h.submit("authenticate", "Authenticate")))
        __M_writer(u'</td>\n    </tr>\n</table>\n\n')
        # SOURCE LINE 28
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


