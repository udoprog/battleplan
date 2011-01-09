<%inherit file="/layout/solarsystems.mako" />

${h.form(url('filter_solarsystems'))}
${h.text("q", value=c.q)} ${h.submit("filter", "Filter")}
${h.end_form()}

<h2>List of Solar Systems</h2>
<ul class="solarsystems">
%if c.page.item_count == 0:
    <li class="notice">No Solar Systems</li>
%endif
%for solarsystem in c.page:
    <li>@${h.link_to(solarsystem.solarSystemName, url("solarsystem", id=solarsystem.solarSystemID))}</li>
%endfor
</ul>

${c.page.pager()}
