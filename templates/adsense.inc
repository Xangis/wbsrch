{% with '2 3 5 6' as numbers %}
{% with numbers.split|random as section %}
{% if section == '1' %}
<!-- Adcash -->
<script data-cfasync="false" type="text/javascript" src="https://www.geniusdexchange.com/a/display.php?r=2266815"></script>
{% elif section == '2' %}
<!-- RevenueHits -->
<script data-cfasync='false' type='text/javascript' src='//p134532.clksite.com/adServe/banners?tid=134532_231433_0'></script>
{% elif section == '3' %}
<!-- Bidvertiser -->
<!-- Begin BidVertiser code -->
<SCRIPT data-cfasync="false" SRC="//bdv.bidvertiser.com/BidVertiser.dbm?pid=724857&bid=1800308" TYPE="text/javascript"></SCRIPT>
<!-- End BidVertiser code -->
{% elif section == '4' %}
<!-- Yllix -->
<script type="text/javascript" src="//ylx-1.com/bnr.php?section=General&pub=518533&format=728x90&ga=g"></script>
<noscript><a href="https://yllix.com/publishers/518533" target="_blank"><img src="//ylx-aff.advertica-cdn.com/pub/728x90.png" style="border:none;margin:0;padding:0;vertical-align:baseline;" /></a></noscript>
{% elif section == '5' %}
<!-- Adsterra -->
<script type="text/javascript">
	atOptions = {
		'key' : '3763623866646538366439656231323162613130363535336364633438643161',
		'format' : 'iframe',
		'height' : 90,
		'width' : 728,
		'params' : {}
	};
	document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.gatetodisplaycontent.com/3763623866646538366439656231323162613130363535336364633438643161/invoke.js"></scr' + 'ipt>');
</script>
{% elif section == '6' %}
<!-- Media.net -->
<div id="471798331">
    <script type="text/javascript">
        try {
            window._mNHandle.queue.push(function (){
                window._mNDetails.loadTag("471798331", "728x90", "471798331");
            });
        }
        catch (error) {}
    </script>
</div>
{% else %}
<!-- Chitika -->
<script type="text/javascript">
  ( function() {
    if (window.CHITIKA === undefined) { window.CHITIKA = { 'units' : [] }; };
    var unit = {"calltype":"async[2]","publisher":"Xangis","width":728,"height":90,"sid":"Chitika Default"};
    var placement_id = window.CHITIKA.units.length;
    window.CHITIKA.units.push(unit);
    document.write('<div id="chitikaAdBlock-' + placement_id + '"></div>');
}());
</script>
<script type="text/javascript" src="//cdn.chitika.net/getads.js" async></script>
{% endif %}
{% endwith %}
{% endwith %}
