<%inherit file="/layout/main.mako"/>

<canvas id="map" width="300" height="300"></canvas>

<script>
$(document).ready(function() {
    //var map_1 = document.getElementById("map_1");
    //var map_2 = document.getElementById("map_2");
    var url = "${url('/map/systems')}";
    var constellation = ${c.solarsystem.constellationID}
    var map = document.getElementById("map");
    draw_systems(url, map, {'constellation': 20000425, 'text': true, 'size': 10, 'line-width': 3, 'font': '12px sans-serif', 'padding': 20})
    
    //draw_systems(map_1, {'text': false, 'padding': 50, size: 2, 'line-width': 1})
    //draw_systems(map_2, {'region': 10000035, 'text': false, 'padding': 20, 'line-width': 1})
})
</script>
