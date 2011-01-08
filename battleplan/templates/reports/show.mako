<%inherit file="/layout/reports.mako" />

<h2>${c.report.title} @ ${h.link_to(c.report.solarSystem.solarSystemName, url('solarsystem', id=c.report.solarSystem.solarSystemID))}</h2>
<h4>${c.report.created}</h4>
<pre style="display: block; background-color: white; border: 1px solid #777777; padding: 4px;">${c.text}</pre>
