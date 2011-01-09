<%inherit file="/layout/main.mako" />

<h2>Help</h2>

<div id="help">
    <p>
        topics: <a href="#posting">Posting</a>
        <a href="#hashes">Hashes</a>
    </p>

    <h3 id="posting">How to post Intel</h3>

    <p>Locate the 'New Intel' link - should be on top of the front page</p>

    <img src="${url('/help/posting.png')}" width="314" height="400" />

    <p>Fill out the form and post new intel</p>

    <img src="${url('/help/posting-form.png')}" width="314" height="400" />

    <h3 id="hashes">Hashes</h3>

    <p>
        Hashes are special markers which will add an anchor to your report, allowing people who filters their view to receive only the type of reports they are interested in.
    </p>
    <p>
        Anchors are marked with a <em>number sign</em> (e.g. <code>#hash</code>) and are read without case, meaning <em>foo</em> will be treated as the same anchor as <em>FOO</em>.
    </p>
</div>
