<%inherit file="/layout/main.mako" />

${h.form(url('filter_hashes'))}
${h.text("q", value=c.q)} ${h.submit("filter", "Filter")}
${h.end_form()}

<h2>List of Hashes</h2>
<ul class="hashes">
%if c.page.item_count == 0:
    <li class="notice">No hashes</li>
%endif
%for hash in c.page:
    <li>#${h.link_to(hash.name, url("hash", id=hash.id.hex))}</li>
%endfor
</ul>

${c.page.pager()}
