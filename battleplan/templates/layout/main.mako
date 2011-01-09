<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
    <head>
        <script src="${url('/jquery-1.4.4.min.js')}" type="text/javascript"></script>
        <script src="${url('/jquery.dateFormat-1.0.js')}" type="text/javascript"></script>
        <script src="${url('/jquery.autocomplete.js')}" type="text/javascript"></script>
        <script src="${url('/jquery.color.js')}" type="text/javascript"></script>
        <script src="${url('/master.js')}" type="text/javascript"></script>
        <script src="${url('/map.js')}" type="text/javascript"></script>
        <link href="${url('/main.css')}" type="text/css" rel="stylesheet" />
        <link href="${url('/jquery.autocomplete.css')}" type="text/css" rel="stylesheet" />
        ${self.headtags()}
        <script>
            $(document).ready(function(){
                %if not c.eve.trusted:
                    if (window.CCPEVE) CCPEVE.requestTrust("${url('', qualified=True)}")
                %endif
            });
        </script>
    </head>
    <body>
        <ul class="nav">
            <li>
                ${h.link_to("Intel", url('reports'))}
            </li>
            
            <li>
                ${h.link_to("Hash", url('hashes'))}
            </li>
            
            %if not c.eve.trusted:
                <li class="notice">Trust Site<li>
            %else:
                <li>${h.link_to("Current", url('solarsystem', id="current"))}</li>
            %endif

            %if c.user:
                <li class="right">${h.link_to("Sign Out", url('auth_signout'))}</li>
            %endif
            
            <li class="right">${h.link_to("Help", url('help'))}</li>
        </ul>
        ${self.top()}
        <div id="main">
            ${next.body()}
        </div>
    </body>
</html>
<%def name="top()">
<%include file="/errors.mako" />
</%def>
<%def name="headtags()"></%def>
