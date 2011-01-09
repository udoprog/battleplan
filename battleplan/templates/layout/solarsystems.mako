<%inherit file="/layout/main.mako" />
<%def name="top()">
%if c.eve.trusted:
<ul class="nav sub" style="text-align: center;">
    <li class="center">
        ${h.link_to("Current", url('solarsystem', id="current"))}
    </li>
</ul>
%endif
<%include file="/errors.mako"/>
</%def>
${next.body()}
