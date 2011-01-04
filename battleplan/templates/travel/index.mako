<%inherit file="/layout/main.mako"/>

<canvas id="map" width="300" height="300"></canvas>

<script>
function draw_jump(context, from, to, active, request) {
    var with_text = request["text"] || false
    var size = request["size"] || 4
    var padding = (request["padding"] || 50) + 0.5;
    var line_width = request["line-width"] || 2;

    context.lineWidth = line_width
    
    if (active) {
        context.strokeStyle = '#999'
    } else {
        context.strokeStyle = '#333'
    }
    
    context.beginPath();
    context.moveTo(from.x + padding, from.z + padding);
    context.lineTo(to.x + padding, to.z + padding);
    context.closePath();
    context.stroke();
}

function draw_system(context, s, request) {
    var with_text = request["text"] || false
    var size = request["size"] || 4
    var padding = (request["padding"] || 50) - size / 2 + 0.5;
    var font = request["font"] || '10px sans-serif'
    
    if (s.security > 8) {
        context.fillStyle = '#0f0'
    }
    else if (s.security > 6) {
        context.fillStyle = '#2d0'
    }
    else if (s.security > 4) {
        context.fillStyle = '#4b0'
    }
    else if (s.security > 2) {
        context.fillStyle = '#990'
    }
    else if (s.security > 0) {
        context.fillStyle = '#a70'
    }
    else if (s.security > -2) {
        context.fillStyle = '#c50'
    }
    else if (s.security > -4) {
        context.fillStyle = '#d20'
    }
    else {
        context.fillStyle = '#f00'
    }
    
    context.fillRect(s.x + padding, s.z + padding, size, size)
    
    if (with_text) {
        context.font = font
        context.fillText(s.name, s.x + padding + size / 2 + 8, s.z + padding)
    }
}

function draw_systems(canvas, request) {
    var request = request || {};

    var context = canvas.getContext("2d")

    var padding = request["padding"] || 50;
    
    request['resolution'] = (canvas.width > canvas.height ? canvas.height: canvas.width) - padding * 2;
    
    context.fillStyle = '#000000'
    context.fillRect(0,0,canvas.width,canvas.height)
    
    $.getJSON("${url('/map/systems')}", request, function(data){
        for (i in data.jumps) {
            var j = data.jumps[i];
            var from = data.systems[j[0]];
            var to = data.systems[j[1]];
            var active = j[2];
            draw_jump(context, from, to, active, request)
        }
        
        for (i in data.systems) {
            draw_system(context, data.systems[i], request);
        }
    });
}

$(document).ready(function() {
    //var map_1 = document.getElementById("map_1");
    //var map_2 = document.getElementById("map_2");
    var map = document.getElementById("map");
    
    //draw_systems(map_1, {'text': false, 'padding': 50, size: 2, 'line-width': 1})
    //draw_systems(map_2, {'region': 10000035, 'text': false, 'padding': 20, 'line-width': 1})
    draw_systems(map, {'constellation': 20000425, 'text': true, 'size': 10, 'line-width': 3, 'font': '12px sans-serif', 'padding': 20})
})
</script>
