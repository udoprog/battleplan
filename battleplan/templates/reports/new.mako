<%inherit file="/layout/main.mako" />

${h.form(url('reports'), method="post")}
    System:<br />
    %if c.errors.solarSystemName:
        ${c.errors.solarSystemName}
    %endif
    ${h.text('solarSystemName', style='width: 200px;')}<br />
    Report:<br />
    %if c.errors.text:
        ${c.errors.text}
    %endif
    ${h.textarea('text', style='width: 200px; height: 160px;')}<br />
    ${h.submit('report','Report')}
${h.end_form()}

<script type="text/javascript">
$(document).ready(function() {
    $("#solarsystemname").autocomplete("${url('/map/complete')}")
});
</script>
