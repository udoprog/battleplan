# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294602350.261929
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
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<h1>Locked <em>')
        # SOURCE LINE 3
        __M_writer(escape(c.path_before_login))
        __M_writer(u'</em></h1>\n\n')
        # SOURCE LINE 5
        runtime._include_file(context, u'/errors.mako', _template_uri)
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        if "name" in c.errors:
            # SOURCE LINE 8
            __M_writer(u'    <div class="error">Name: ')
            __M_writer(escape(c.errors.name))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        if "api_userid" in c.errors:
            # SOURCE LINE 12
            __M_writer(u'    <div class="error">Api User-ID: ')
            __M_writer(escape(c.errors.api_userid))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\n')
        # SOURCE LINE 15
        if "api_key" in c.errors:
            # SOURCE LINE 16
            __M_writer(u'    <div class="error">Api Key: ')
            __M_writer(escape(c.errors.api_key))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(escape(h.form(url("auth_signin"), method="post")))
        __M_writer(u'\n<table>\n    <tr>\n        <td>Name:</td>\n        <td>')
        # SOURCE LINE 23
        __M_writer(escape(h.text("name", value=c.name)))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td>Api User-ID:</td>\n        <td>')
        # SOURCE LINE 27
        __M_writer(escape(h.text("api_userid", value=c.api_userid)))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td>Api Key:</td>\n        <td>')
        # SOURCE LINE 31
        __M_writer(escape(h.text("api_key", value=c.api_key)))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td colspan="2">')
        # SOURCE LINE 34
        __M_writer(escape(h.submit("authenticate", "Authenticate")))
        __M_writer(u'</td>\n    </tr>\n</table>\n\n')
        # SOURCE LINE 38
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\n<h4>Allowed Alliances</h4>\n<ul>\n')
        # SOURCE LINE 42
        if len(c.alliances) == 0:
            # SOURCE LINE 43
            __M_writer(u'    <li>No registered alliances</li>\n')
            pass
        # SOURCE LINE 45
        for a in c.alliances:
            # SOURCE LINE 46
            __M_writer(u'    <li><b>')
            __M_writer(escape(a))
            __M_writer(u'</b></li>\n')
            pass
        # SOURCE LINE 48
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


