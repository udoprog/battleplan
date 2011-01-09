<%inherit file="/layout/reports.mako" />

${h.form(url('reports'), method="post")}

%if "solarSystem" in c.errors:
    <div class="error">System: ${c.errors.solarSystem}</div>
%endif

%if "title" in c.errors:
    <div class="error">Title: ${c.errors.title}</div>
%endif

%if "text" in c.errors:
    <div class="error">Report: ${c.errors.text}</div>
%endif

<table>
    <tr>
        <td>System:</td>
        <td>${h.text('solarSystem', value=c.solarSystem, style='width: 200px;')}</td>
    </tr>
    <tr>
        <td valign="top">Title:</td>
        <td>${h.text('title', style='width: 200px;', maxlength=36, value=c.title)}</td>
    <tr>
    </tr>
        <td colspan="2"><em>To add ${h.link_to("hashes", url('help', anchor="hashes"))}, prefix a word with '#'</em></td>
    </tr>
    </tr>
        <td valign="top">Report:</td>
        <td>${h.textarea('text', style='width: 200px; height: 100px;', maxlength=140, content=c.text)}</td>
    </tr>
    <tr>
        <td valign="top">Priority:</td>
        <td>
            <span class="level-0" style='padding: 0.2em;'>${h.radio('priority', value="0", checked=(c.priority==0))}1</span>
            <span class="level-1" style='padding: 0.2em;'>${h.radio('priority', value="1", checked=(c.priority==1))}2</span>
            <span class="level-2" style='padding: 0.2em;'>${h.radio('priority', value="2", checked=(c.priority==2))}3</span>
            <span class="level-3" style='padding: 0.2em;'>${h.radio('priority', value="3", checked=(c.priority==3))}4</span>
            <span class="level-4" style='padding: 0.2em;'>${h.radio('priority', value="4", checked=(c.priority==4))}5</span>
        </td>
    </tr>
    <tr>
        <td colspan="2">${h.submit('report','Report')}</td>
    </tr>
</table>
${h.end_form()}

<script type="text/javascript">
$(document).ready(function() {
    $("#solarsystem").autocomplete("${url('/map/complete')}")
});
</script>
