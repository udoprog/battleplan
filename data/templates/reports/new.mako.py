# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294547140.7813449
_template_filename='/home/udoprog/repo/git/battleplan/battleplan/templates/reports/new.mako'
_template_uri='/reports/new.mako'
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
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(escape(h.form(url('reports'), method="post")))
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        if "solarSystem" in c.errors:
            # SOURCE LINE 6
            __M_writer(u'    <div class="error">System: ')
            __M_writer(escape(c.errors.solarSystem))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        if "title" in c.errors:
            # SOURCE LINE 10
            __M_writer(u'    <div class="error">Title: ')
            __M_writer(escape(c.errors.title))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        if "text" in c.errors:
            # SOURCE LINE 14
            __M_writer(u'    <div class="error">Report: ')
            __M_writer(escape(c.errors.text))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 16
        __M_writer(u'\n<table>\n    <tr>\n        <td>System:</td>\n        <td>')
        # SOURCE LINE 20
        __M_writer(escape(h.text('solarSystem', value=c.solarSystem, style='width: 200px;')))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td valign="top">Title:</td>\n        <td>')
        # SOURCE LINE 24
        __M_writer(escape(h.text('title', style='width: 200px;', maxlength=36, value=c.title)))
        __M_writer(u'</td>\n    <tr>\n    </tr>\n        <td colspan="2"><em>To add ')
        # SOURCE LINE 27
        __M_writer(escape(h.link_to("hashes", url('help', anchor="hashes"))))
        __M_writer(u', prefix a word with \'#\'</em></td>\n    </tr>\n    </tr>\n        <td valign="top">Report:</td>\n        <td>')
        # SOURCE LINE 31
        __M_writer(escape(h.textarea('text', style='width: 200px; height: 100px;', maxlength=140, content=c.text)))
        __M_writer(u'</td>\n    </tr>\n    <tr>\n        <td valign="top">Priority:</td>\n        <td>\n            <span class="level-0" style=\'padding: 0.2em;\'>')
        # SOURCE LINE 36
        __M_writer(escape(h.radio('priority', value="0", checked=(c.priority==0))))
        __M_writer(u'1</span>\n            <span class="level-1" style=\'padding: 0.2em;\'>')
        # SOURCE LINE 37
        __M_writer(escape(h.radio('priority', value="1", checked=(c.priority==1))))
        __M_writer(u'2</span>\n            <span class="level-2" style=\'padding: 0.2em;\'>')
        # SOURCE LINE 38
        __M_writer(escape(h.radio('priority', value="2", checked=(c.priority==2))))
        __M_writer(u'3</span>\n            <span class="level-3" style=\'padding: 0.2em;\'>')
        # SOURCE LINE 39
        __M_writer(escape(h.radio('priority', value="3", checked=(c.priority==3))))
        __M_writer(u'4</span>\n            <span class="level-4" style=\'padding: 0.2em;\'>')
        # SOURCE LINE 40
        __M_writer(escape(h.radio('priority', value="4", checked=(c.priority==4))))
        __M_writer(u'5</span>\n        </td>\n    </tr>\n    <tr>\n        <td colspan="2">')
        # SOURCE LINE 44
        __M_writer(escape(h.submit('report','Report')))
        __M_writer(u'</td>\n    </tr>\n</table>\n')
        # SOURCE LINE 47
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\n<script type="text/javascript">\n$(document).ready(function() {\n    $("#solarsystem").autocomplete("')
        # SOURCE LINE 51
        __M_writer(escape(url('/map/complete')))
        __M_writer(u'")\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


