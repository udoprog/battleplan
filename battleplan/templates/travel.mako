%if not c.ts:
    Could not find a system to travel to
    <% return %>
%endif

Hello ${c.ts.solarSystemName}<br />

Jumps: ${len(c.route) - 1}

<table>
%for i in range(0, len(c.route) - 1):
    <tr>
        <td>${c.route[i].solarSystemName}</td>
        <td>-></td>
        <td>${c.route[i+1].solarSystemName}</td>
    </tr>
%endfor
</table>
