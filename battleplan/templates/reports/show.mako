<%inherit file="/layout/reports.mako" />

<h2>${c.report.title}</h2>
<code style="display: block; background-color: white; border: 1px solid #777777; padding: 4px;">${c.text}</code>
<p>
Reported for ${h.link_to(c.report.solarSystem.solarSystemName, url('solarsystem', id=c.report.solarSystem.solarSystemID))}<br />
Created at ${c.report.created}
</p>
