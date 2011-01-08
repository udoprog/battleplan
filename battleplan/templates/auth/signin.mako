<%inherit file="/layout/main.mako" />

<b>${c.path_before_login}</b>

%if hasattr(c, "error"):
    ${c.error}
%endif

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
