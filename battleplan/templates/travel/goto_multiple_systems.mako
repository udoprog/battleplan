
<p>
    There are multiple destination alternatives available:
</p>

<ul>
%for s in c.systems:
    <li>${h.link_to(s.solarSystemName, url.current(dest=s.solarSystemName) + "?" + request.query_string)}</li>
%endfor
</ul>
