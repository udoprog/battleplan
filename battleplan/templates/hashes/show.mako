<%inherit file="/layout/main.mako" />

<h2>Latest Intel by <em>#${c.hash.name}</em></h2>

<ul id="latest-reports" class="reports">
    <li>Loading Reports...</li>
</ul>

<script type="text/javascript">
$(function() {
    var options = {
        'url.reports': "${url('latest.json')}",
        'url.check': "${url('check.json')}",
        'url.system_base': "${url('solarsystems')}",
        'url.report_base': "${url('reports')}",
        'flashing': 20,
        'hash': "${c.hash.id.hex}"
    }

    dynamic_reports("#latest-reports", options);
});
</script>
