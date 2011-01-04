<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
    <head>
        <script src="${url('/jquery-1.4.4.min.js')}" type="text/javascript"></script>
        <script src="${url('/jquery.autocomplete.js')}" type="text/javascript"></script>
        <script src="${url('/jquery.color.js')}" type="text/javascript"></script>
        <script src="${url('/map.js')}" type="text/javascript"></script>
        <link href="${url('/main.css')}" type="text/css" rel="stylesheet" />
        <link href="${url('/jquery.autocomplete.css')}" type="text/css" rel="stylesheet" />
        ${self.headtags()}
    </head>
    <body>
        <div id="navigation">
            ${h.link_to("Intel", url('reports'))}
            ${h.link_to("Travel", url('travel_index'))}
        </div>
        ${next.body()}
    </body>
</html>
<%def name="headtags()"></%def>
