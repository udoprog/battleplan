<%inherit file="/layout/main.mako" />

<h2>List of hashes</h2>
<ul class="hashes">
%if c.page.item_count == 0:
    <li class="notice">No hashes</li>
%endif
%for hash in c.page:
    <li>#${h.link_to(hash.name, url("hash", id=hash.id.hex))}</li>
%endfor
</ul>

${c.page.pager()}
