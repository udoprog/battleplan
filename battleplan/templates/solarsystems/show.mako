<%inherit file="/layout/main.mako" />

<%
today = -1
%>

<h1>${c.solarsystem.solarSystemName}</h1>

<ul class="reports">
%if len(c.reports) == 0:
    <li>no reports</li>
%endif
%for r in c.reports:
%if today != r.created.day:
    <li class="date"><span class="date">${r.created.strftime("%Y-%m-%d")}</span></li>
%endif
<li>
    <span class="time">${r.created.strftime("%H:%M:%S")}:</span>
    <span class="text">${r.text}</span>
</li>
<% today = r.created.day %>
%endfor
</ul>

<h2>${c.solarsystem.constellation.constellationName}</h2>
<canvas id="map_constellation" width="300" height="300"></canvas>

<h2>${c.solarsystem.region.regionName}</h2>
<canvas id="map_region" width="300" height="300"></canvas>

<script type="text/javascript">
$(document).ready(function() {
    var url = "${url('/map/systems')}";
    var solarSystem = ${c.solarsystem.solarSystemID}
    var constellation = ${c.solarsystem.constellationID};
    var region = ${c.solarsystem.regionID};

    var map_constellation = document.getElementById("map_constellation");
    var map_region = document.getElementById("map_region");
    
    draw_systems(url, map_constellation, {'solarSystem': solarSystem, 'constellation': constellation, 'text': true, 'size': 10, 'line-width': 3, 'font': '12px sans-serif', 'padding': 20})
    draw_systems(url, map_region, {'solarSystem': solarSystem, 'region': region, 'constellation': constellation , 'size': 4, 'line-width': 1, 'font': '8px sans-serif', 'padding': 20})
});
</script>
