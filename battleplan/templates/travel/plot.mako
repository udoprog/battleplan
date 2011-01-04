
<table>
    <tr>
        <td colspan="5">${len(c.route)} Jumps</td>
    </tr>
    %if c.no_route:
    <tr>
        <td colspan="5"><b>No route</b></td>
    </tr>
    %else:
        <tr>
            <td colspan="2"><b>System</b></td>
            <td></td>
            <td colspan="2"><b>To</b></td>
        </tr>
        %for system, dest in c.route:
            <tr>
                <td>${system.solarSystemName}</td>
                <td>(${round(system.security, 1)})</td>
                <td>&mdash;</td>
                <td><b>${dest.solarSystemName}</b></td>
                <td>(${round(dest.security, 1)})</td>
            </tr>
        %endfor
    %endif
</table>
