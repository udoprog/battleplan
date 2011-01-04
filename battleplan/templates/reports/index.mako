<%inherit file="/layout/main.mako" />

<%
import datetime
today = -1
%>

<h4>Ten Last Reports</h4>
<ul class="reports">
%if len(c.reports) == 0:
    <li><em>No Reports</em></li>
%endif
%for r in c.reports:
%if today != r.created.day:
    <li class="date"><span class="date">${r.created.strftime("%Y-%m-%d")}</span></li>
%endif
%if (datetime.datetime.now() - r.created).seconds < 120:
<li class="flash">
%else:
<li>
%endif
    <span class="time">
        ${r.created.strftime("%H:%M:%S")}
        @
        ${h.link_to(r.solarSystem.solarSystemName, url('solarsystem', id=r.solarSystem.solarSystemID))}
    </span>
    <span class="text">${r.text}</span>
</li>
<% today = r.created.day %>
%endfor
</ul>

${h.link_to("create new", url('new_report'))}

<script type="text/javascript">

$(document).ready(function() {
    var $flash = $(".flash");
    
    function doFlash() {
        $flash.toggleClass("bright");
    }
    
    setInterval(doFlash, 750);
    setTimeout(function() {
        document.location = document.location;
    }, 10000);
});

</script>
