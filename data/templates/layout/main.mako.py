# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294522981.4326789
_template_filename=u'/home/udoprog/repo/git/battleplan/battleplan/templates/layout/main.mako'
_template_uri=u'/layout/main.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['headtags', 'top']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        c = context.get('c', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" \n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n    <head>\n        <script src="')
        # SOURCE LINE 5
        __M_writer(escape(url('/jquery-1.4.4.min.js')))
        __M_writer(u'" type="text/javascript"></script>\n        <script src="')
        # SOURCE LINE 6
        __M_writer(escape(url('/jquery.dateFormat-1.0.js')))
        __M_writer(u'" type="text/javascript"></script>\n        <script src="')
        # SOURCE LINE 7
        __M_writer(escape(url('/jquery.autocomplete.js')))
        __M_writer(u'" type="text/javascript"></script>\n        <script src="')
        # SOURCE LINE 8
        __M_writer(escape(url('/jquery.color.js')))
        __M_writer(u'" type="text/javascript"></script>\n        <script src="')
        # SOURCE LINE 9
        __M_writer(escape(url('/master.js')))
        __M_writer(u'" type="text/javascript"></script>\n        <script src="')
        # SOURCE LINE 10
        __M_writer(escape(url('/map.js')))
        __M_writer(u'" type="text/javascript"></script>\n        <link href="')
        # SOURCE LINE 11
        __M_writer(escape(url('/main.css')))
        __M_writer(u'" type="text/css" rel="stylesheet" />\n        <link href="')
        # SOURCE LINE 12
        __M_writer(escape(url('/jquery.autocomplete.css')))
        __M_writer(u'" type="text/css" rel="stylesheet" />\n        ')
        # SOURCE LINE 13
        __M_writer(escape(self.headtags()))
        __M_writer(u'\n        <script>\n            $(document).ready(function(){\n')
        # SOURCE LINE 16
        if not c.eve.trusted:
            # SOURCE LINE 17
            __M_writer(u'                    if (window.CCPEVE) CCPEVE.requestTrust("')
            __M_writer(escape(url('', qualified=True)))
            __M_writer(u'")\n')
            pass
        # SOURCE LINE 19
        __M_writer(u'            });\n        </script>\n    </head>\n    <body>\n        <ul class="nav">\n            <li>\n                ')
        # SOURCE LINE 25
        __M_writer(escape(h.link_to("Intel", url('reports'))))
        __M_writer(u'\n            </li>\n            \n            <li>\n                ')
        # SOURCE LINE 29
        __M_writer(escape(h.link_to("Hash", url('hashes'))))
        __M_writer(u'\n            </li>\n            \n')
        # SOURCE LINE 32
        if not c.eve.trusted:
            # SOURCE LINE 33
            __M_writer(u'                <li class="notice">Trust Site<li>\n')
            # SOURCE LINE 34
        else:
            # SOURCE LINE 35
            __M_writer(u'                <li>')
            __M_writer(escape(h.link_to("Current", url('solarsystem', id="current"))))
            __M_writer(u'</li>\n')
            pass
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        if c.user:
            # SOURCE LINE 39
            __M_writer(u'                <li class="right">')
            __M_writer(escape(h.link_to("Sign Out", url('auth_signout'))))
            __M_writer(u'</li>\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'            \n            <li class="right">')
        # SOURCE LINE 42
        __M_writer(escape(h.link_to("Help", url('help'))))
        __M_writer(u'</li>\n        </ul>\n        ')
        # SOURCE LINE 44
        __M_writer(escape(self.top()))
        __M_writer(u'\n        <div id="main">\n            ')
        # SOURCE LINE 46
        __M_writer(escape(next.body()))
        __M_writer(u'\n        </div>\n    </body>\n</html>\n')
        # SOURCE LINE 52
        __M_writer(u'\n')
        # SOURCE LINE 53
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headtags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 51
        runtime._include_file(context, u'/errors.mako', _template_uri)
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


