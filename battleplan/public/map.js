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
    var padding = (request["padding"] || 50) + 0.5;
    var font = request["font"] || '10px sans-serif'

    if (s.highlight) {
        t_size = size * 1.8;

        context.strokeStyle = '#fff'
        context.beginPath();
        context.arc(s.x + padding, s.z + padding, (t_size + 1) / 2, 0, Math.PI*2, true); 
        context.closePath();
        context.stroke();
        
        context.fillStyle = '#000'
        context.beginPath();
        context.arc(s.x + padding, s.z + padding, (t_size) / 2, 0, Math.PI*2, true); 
        context.closePath();
        context.fill();
    }
    
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
    
    context.beginPath();
    context.arc(s.x + padding, s.z + padding, size / 2, 0, Math.PI*2, true); 
    context.closePath();
    context.fill();
    //context.fillRect(s.x + padding, s.z + padding, size, size)
    
    if (with_text) {
        context.font = font
        context.fillText(s.name, s.x + padding + size / 2 + 8, s.z + padding)
    }
}

function draw_systems(url, canvas, request) {
    var request = request || {};

    var context = canvas.getContext("2d")

    var padding = request["padding"] || 50;
    
    request['resolution'] = (canvas.width > canvas.height ? canvas.height: canvas.width) - padding * 2;
    
    context.fillStyle = '#000000'
    context.fillRect(0,0,canvas.width,canvas.height)
    
    $.getJSON(url, request, function(data){
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
