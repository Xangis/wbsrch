# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from zetaweb import settings
from dir import views
from dir import api
from blog.views import *
admin.autodiscover()


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^domain/$', views.domain, name='domain'),
    url(r'^ip/$', views.ipaddry, name='ipaddry'),
    url(r'^go/$', views.go, name='go'),
    # url(r'^domainrank/$', views.domainrank, name='domainrank'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^philosophy/$', views.philosophy, name='philosophy'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^dmca/$', views.dmca, name='dmca'),
    url(r'^dmca-notices/$', views.dmca_notices, name='dmca-notices'),
    url(r'^howto/$', views.howto, name='howto'),
    url(r'^changelog/$', views.changelog, name='changelog'),
    url(r'^hardware/$', views.hardware, name='hardware'),
    url(r'^policy/$', views.policy, name='policy'),
    url(r'^wbrank/$', views.wbrank, name='wbrank'),
    url(r'^autocomplete/$', views.autocomplete, name='autocomplete'),
    # url(r'^popular-searches/(?P<year>\d+)/(?P<month>\d+)/$', views.popular_searches, name='popular-searches'),
    # url(r'^popular-searches/$', views.popular_searches, name='popular-searches'),
    url(r'^index-stats/$', views.index_stats, name='index-stats'),
    url(r'^tld-stats/$', views.tld_stats, name='tld-stats'),
    url(r'^most-linked-to-domains/$', views.most_linked_domains, name='most-linked-domains'),
    # url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^criteria/$', views.criteria, name='criteria'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^articles/$', articles),
    url(r'^article/(?P<post_url>[a-zA-Z0-9_-]+)/$', post_url),
    url(r'^article-category/(?P<category>[a-zA-Z0-9_-]+)/$', article_category),
    # Redirects to other sites.
    url(r'^ads/$', views.ads),
    url(r'^analytics/$', views.analytics),
    url(r'^apps/$', views.apps),
    url(r'^browser/$', views.browser),
    url(r'^images/$', views.images),
    url(r'^maps/$', views.maps),
    url(r'^news/$', views.news),
    url(r'^video/$', views.video),
    url(r'^stats/$', views.stats),
    url(r'^error/$', views.error),
    url(r'^email/$', views.email),
    # Admin panel views.
    url(r'^adminpanel/oldestcrawls/$', views.adminpanel_oldestcrawls, name='adminpanel-oldestcrawls'),
    url(r'^adminpanel/unclassified/$', views.adminpanel_unclassified, name='adminpanel-unclassified'),
    url(r'^adminpanel/blocksite/$', views.adminpanel_blocksite, name='adminpanel-blocksite'),
    url(r'^adminpanel/movesite/$', views.adminpanel_movesite, name='adminpanel-movesite'),
    url(r'^adminpanel/topsites/$', views.adminpanel_topsites, name='adminpanel-topsites'),
    url(r'^adminpanel/sitelimits/$', views.adminpanel_sitelimits, name='adminpanel-sitelimits'),
    url(r'^adminpanel/pagescore/$', views.adminpanel_pagescore, name='adminpanel-pagescore'),
    url(r'^adminpanel/searchlogs/$', views.adminpanel_searchlogs, name='adminpanel-searchlogs'),
    url(r'^adminpanel/$', views.adminpanel, name='adminpanel'),
    # API Methods
    url(r'^api/ip_to_country/$', api.ip_to_country, name='api_ip_to_country'),
    url(r'^api/domain_link_rank/$', api.domain_link_rank, name='api_domain_link_rank'),
    url(r'^api/domain_pages_in_index/$', api.domain_pages_in_index, name='api_domain_pages_in_index'),
    url(r'^api/domain_keywords_ranked/$', api.domain_keywords_ranked, name='api_domain_keywords_ranked'),
    url(r'^api/autocomplete/$', api.autocomplete, name='api_autocomplete'),
    url(r'^api/check_typo/$', api.check_typo, name='api_check_typo'),
    url(r'^api/get_page_details/$', api.get_page_details, name='get_page_details'),
    url(r'^api/get_ranks/$', api.get_ranks, name='api_get_ranks'),
    url(r'^api/get_whois_info/$', api.get_whois_info, name='api_get_whois_info'),
    url(r'^api/get_robots_info/$', api.get_robots_info, name='api_get_robots_info'),
    # End API methods
    # url(r'^admin-preview/$', views.admin_preview, name='admin_preview'),
    url(r'^adm/doc/', include('django.contrib.admindocs.urls')),
    url(r'^adm/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),)
