<%inherit file="/layout/solarsystems.mako" />

<h2>Latest intel at <em>@${c.solarsystem.solarSystemName}</em></h2>

<ul id="latest-reports" class="reports">
    <li>loading reports...</li>
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
    
    /* request and draw out the constellation map */
    draw_systems(url, map_constellation, {'solarSystem': solarSystem, 'constellation': constellation, 'text': true, 'size': 10, 'line-width': 3, 'font': '12px sans-serif', 'padding': 20})
    
    /* request and draw out the region map */
    draw_systems(url, map_region, {'solarSystem': solarSystem, 'region': region, 'constellation': constellation , 'size': 4, 'line-width': 1, 'font': '8px sans-serif', 'padding': 20})

    var options = {
        'url.reports': "${url('latest.json')}",
        'url.check': "${url('check.json')}",
        'url.system_base': "${url('solarsystems')}",
        'url.report_base': "${url('reports')}",
        'flashing': 20,
        'solarsystem': ${c.solarsystem.solarSystemID}
    }

    dynamic_reports("#latest-reports", options);
});
</script>
