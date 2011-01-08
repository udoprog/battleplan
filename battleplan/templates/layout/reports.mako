<%inherit file="/layout/main.mako" />
<%def name="top()">
<ul class="nav sub" style="text-align: center;">
    <li class="center">
        ${h.link_to("New Intel", url('new_report'))}
    </li>
</ul>
<%include file="/errors.mako"/>
</%def>
${next.body()}
