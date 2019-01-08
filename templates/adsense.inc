{% with [1, 2, 3, 4]|random as section %}
{% if section == 1 %}
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
{% elif section == 2 %}
<!-- RevenueHits -->
<script data-cfasync='false' type='text/javascript' src='//p134532.clksite.com/adServe/banners?tid=134532_231433_0'></script>
{% elif section == 3 %}
<!-- Bidvertiser -->
<!-- Begin BidVertiser code -->
<SCRIPT data-cfasync="false" SRC="//bdv.bidvertiser.com/BidVertiser.dbm?pid=724857&bid=1800308" TYPE="text/javascript"></SCRIPT>
<!-- End BidVertiser code -->
{% else %}
<!-- Clicksor -->
<script type="text/javascript"> 
clicksor_enable_adhere = false; 
clicksor_default_url = '';
clicksor_banner_border = '#99CC33'; 
clicksor_banner_ad_bg = '#FFFFFF';
clicksor_banner_link_color = '#000000'; 
clicksor_banner_text_color = '#666666';
clicksor_layer_border_color = '';
clicksor_layer_ad_bg = ''; 
clicksor_layer_ad_link_color = '';
clicksor_layer_ad_text_color = ''; 
clicksor_text_link_bg = '';
clicksor_text_link_color = ''; 
clicksor_enable_text_link = false;
clicksor_banner_text_banner = true;
clicksor_banner_image_banner = true; 
clicksor_enable_layer_pop = false;
clicksor_enable_pop = false;
</script>
 <script type="text/javascript" src="http://b.clicksor.net/show.php?nid=1&amp;pid=372059&amp;adtype=1&amp;sid=659252"></script>
{% endif %}
