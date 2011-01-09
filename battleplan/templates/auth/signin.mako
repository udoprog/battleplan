<%inherit file="/layout/main.mako" />

<h1>Locked <em>${c.path_before_login}</em></h1>

${h.form(url("auth_signin"), method="post")}
<table>
    <tr>
        <td>Name:</td>
        <td>${h.text("name", value=c.name)}</td>
    </tr>
    <tr>
        <td>Api User-ID:</td>
        <td>${h.text("api_userid", value=c.api_userid)}</td>
    </tr>
    <tr>
        <td>Api Key:</td>
        <td>${h.text("api_key", value=c.api_key)}</td>
    </tr>
    <tr>
        <td colspan="2">${h.submit("authenticate", "Authenticate")}</td>
    </tr>
</table>

${h.end_form()}

<h4>Allowed Alliances</h4>
<ul>
%if len(c.alliances) == 0:
    <li>No registered alliances</li>
%endif
%for a in c.alliances:
    <li><b>${a}</b></li>
%endfor
</ul>
