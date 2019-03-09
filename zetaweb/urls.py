# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from zetaweb import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dir.views.index', name='home'),
    url(r'^search/$', 'dir.views.search', name='search'),
    url(r'^domain/$', 'dir.views.domain', name='domain'),
    url(r'^ip/$', 'dir.views.ipaddry', name='ipaddry'),
    url(r'^go/$', 'dir.views.go', name='go'),
    #url(r'^domainrank/$', 'dir.views.domainrank', name='domainrank'),
    url(r'^privacy/$', 'dir.views.privacy', name='privacy'),
    url(r'^philosophy/$', 'dir.views.philosophy', name='philosophy'),
    url(r'^faq/$', 'dir.views.faq', name='faq'),
    url(r'^dmca/$', 'dir.views.dmca', name='dmca'),
    url(r'^dmca-notices/$', 'dir.views.dmca_notices', name='dmca-notices'),
    url(r'^howto/$', 'dir.views.howto', name='howto'),
    url(r'^changelog/$', 'dir.views.changelog', name='changelog'),
    url(r'^hardware/$', 'dir.views.hardware', name='hardware'),
    url(r'^policy/$', 'dir.views.policy', name='policy'),
    url(r'^wbrank/$', 'dir.views.wbrank', name='wbrank'),
    url(r'^autocomplete/$', 'dir.views.autocomplete', name='autocomplete'),
    #url(r'^popular-searches/(?P<year>\d+)/(?P<month>\d+)/$', 'dir.views.popular_searches', name='popular-searches'),
    #url(r'^popular-searches/$', 'dir.views.popular_searches', name='popular-searches'),
    url(r'^index-stats/$', 'dir.views.index_stats', name='index-stats'),
    url(r'^most-linked-to-domains/$', 'dir.views.most_linked_domains', name='most-linked-domains'),
    #url(r'^feedback/$', 'dir.views.feedback', name='feedback'),
    url(r'^criteria/$', 'dir.views.criteria', name='criteria'),
    url(r'^terms/$', 'dir.views.terms', name='terms'),
    url(r'^contact/$', 'dir.views.contact', name='contact'),
    url(r'^articles/$', 'blog.views.articles'),
    url(r'^article/(?P<post_url>[a-zA-Z0-9_-]+)/$', 'blog.views.post_url'),
    url(r'^article-category/(?P<category>[a-zA-Z0-9_-]+)/$', 'blog.views.article_category' ),
    # Redirects to other sites.
    url(r'^ads/$', 'dir.views.ads'),
    url(r'^analytics/$', 'dir.views.analytics'),
    url(r'^apps/$', 'dir.views.apps'),
    url(r'^browser/$', 'dir.views.browser'),
    url(r'^images/$', 'dir.views.images'),
    url(r'^maps/$', 'dir.views.maps'),
    url(r'^news/$', 'dir.views.news'),
    url(r'^video/$', 'dir.views.video'),
    url(r'^stats/$', 'dir.views.stats'),
    # Admin panel views.
    url(r'^adminpanel/oldestcrawls/$', 'dir.views.adminpanel_oldestcrawls', name='adminpanel-oldestcrawls'),
    url(r'^adminpanel/unclassified/$', 'dir.views.adminpanel_unclassified', name='adminpanel-unclassified'),
    url(r'^adminpanel/siteinfoendingin/$', 'dir.views.adminpanel_siteinfoendingin', name='adminpanel-siteinfoendingin'),
    url(r'^adminpanel/blocksite/$', 'dir.views.adminpanel_blocksite', name='adminpanel-blocksite'),
    url(r'^adminpanel/movesite/$', 'dir.views.adminpanel_movesite', name='adminpanel-movesite'),
    url(r'^adminpanel/topsites/$', 'dir.views.adminpanel_topsites', name='adminpanel-topsites'),
    url(r'^adminpanel/sitelimits/$', 'dir.views.adminpanel_sitelimits', name='adminpanel-sitelimits'),
    url(r'^adminpanel/index-stats/$', 'dir.views.index_stats', {'realtime': True}, name='index-stats-realtime' ),
    url(r'^adminpanel/urlrange/$', 'dir.views.adminpanel_urlrange', name='adminpanel-urlrange' ),
    url(r'^adminpanel/domainsafterz/$', 'dir.views.adminpanel_domainsafterz', name='adminpanel-domainsafterz' ),
    url(r'^adminpanel/pagescore/$', 'dir.views.adminpanel_pagescore', name='adminpanel-pagescore' ),
    url(r'^adminpanel/searchlogs/$', 'dir.views.adminpanel_searchlogs', name='adminpanel-searchlogs' ),
    url(r'^adminpanel/$', 'dir.views.adminpanel', name='adminpanel'),
    # API Methods
    url(r'^api/ip_to_country/$', 'dir.api.ip_to_country', name='api_ip_to_country'),
    url(r'^api/domain_link_rank/$', 'dir.api.domain_link_rank', name='api_domain_link_rank'),
    url(r'^api/domain_pages_in_index/$', 'dir.api.domain_pages_in_index', name='api_domain_pages_in_index'),
    url(r'^api/domain_keywords_ranked/$', 'dir.api.domain_keywords_ranked', name='api_domain_keywords_ranked'),
    url(r'^api/autocomplete/$', 'dir.api.autocomplete', name='api_autocomplete'),
    url(r'^api/check_typo/$', 'dir.api.check_typo', name='api_check_typo'),
    url(r'^api/get_page_details/$', 'dir.api.get_page_details', name='get_page_details'),
    url(r'^api/get_alexa_rank/$', 'dir.api.get_alexa_rank', name='api_get_alexa_rank'),
    url(r'^api/get_whois_info/$', 'dir.api.get_whois_info', name='api_get_whois_info'),
    url(r'^api/get_robots_info/$', 'dir.api.get_robots_info', name='api_get_robots_info'),
    # End API methods
    #url(r'^admin-preview/$', 'dir.views.admin_preview', name='admin_preview'),
    url(r'^adm/doc/', include('django.contrib.admindocs.urls')),
    url(r'^adm/', include(admin.site.urls)),
)

if settings.DEBUG == True:
    urlpatterns += patterns('', url(r'^(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),)
