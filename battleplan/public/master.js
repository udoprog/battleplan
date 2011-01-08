/**
 * Create a list of reports and keep it updated.
 *
 * Notable css-selectors are:
 * .flash - when a report is highlighted
 */
function dynamic_reports(selector, options) {
    var $reports = $(selector);
    
    var opts = $.extend({
        "flashing": 120,
        "flash-class": "flash",
        "hash": null,
        "limit": 25
    }, options);

    var latest_id = null;
    
    function setup_report(r) {
        var c = r.created;
        r.created = new Date(c[0], c[1], c[2], c[3], c[4], c[5]);
        var created = $.format.date(r.created, "HH:mm:ss");
        
        var $report = $("<li />").attr('id', r.id);
        var $time = $("<span>").text(created).addClass("time")
        var $a_system = $("<a>")
            .attr('href', opts["url.system_base"] + "/" + r['solarSystem.solarSystemID'])
            .text("@" + r["solarSystem.solarSystemName"]);
        var $solarsystem = $("<span>").append($a_system).addClass("solarsystem")
        
        var $a_text = $("<a>")
            .attr('href', opts["url.report_base"] + "/" + r.id)
            .text(r.title);
        
        var $text = $("<span>")
            .append($a_text)
            .addClass("title")

        var level_p = "level-" + r.priority;
        
        $time.appendTo($report);
        $solarsystem.appendTo($report);
        $text.appendTo($report);

        $("<div>").css('clear', 'both').appendTo($report)
            
        if (r.diff < opts["flashing"]) {
            var self = $report.get(0);
            
            self.interval = setInterval(function(){
                $report.toggleClass(opts["flash-class"]);
                $report.toggleClass(level_p);
            }, 750 + Math.round(50 * Math.random()));
            
            self.timeout = setTimeout(function(){
                clearInterval(self.interval);
                $report.removeClass(opts["flash-class"]);
                $report.removeClass(level_p)
            }, (opts["flashing"] - r.diff) * 1000);
            
            $report.click(function(){
                clearInterval(self.interval);
                clearTimeout(self.timeout);
                $report.removeClass(opts["flash-class"]);
                $report.removeClass(level_p)
                self.interval = null;
                self.timeout = null;
            });
        }
        
        return $report
    }

    function reports_check() {
        if (latest_id == null) return;

        var request = {
            "latest_id": latest_id
        }
        
        if (opts['hash']) request['hash'] = opts['hash']
        
        $.getJSON(opts["url.check"], request, function(data){
            if (data.result) {
                latest_id = null;
                reports_update();
            }
        });
    }
    
    function reports_update() {
        var request = {
            "limit": opts['limit']
        };
        
        if (opts['hash']) request['hash'] = opts['hash']

        $.getJSON(opts["url.reports"], request, function(data){
            $reports.children().each(function(){
                if (this.timeout) clearTimeout(this.timeout);
                if (this.interval) clearInterval(this.interval);
                $(this).remove();
            });
            
            if (data.error) {
                $("<li>", {"class": "error"}).text(data.error).appendTo($reports);
                return;
            }

            if (data.result.length == 0) {
                $("<li>", {"class": "notice"}).text("No available reports").appendTo($reports);
                return;
            }
            
            for (i in data.result) {
                var r = data.result[i];
                var $report = setup_report(r)
                
                $report.appendTo($reports);
                
                if (!latest_id) {
                    latest_id = r.id;
                }
            }
        });
    }

    reports_update();
    setInterval(reports_check, 5000);
}
