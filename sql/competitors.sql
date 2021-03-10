select url, domcop_pagerank, domcop_rank, alexa_rank, majestic_rank, domains_linking_in, num_urls, num_keywords_ranked from dir_domaininfo where url in ('mojeek.com', 'duckduckgo.com', 'bing.com', 'google.com', 'gigablast.com', 'startpage.com', 'teoma.com', 'ecosia.org', 'wbsrch.com', 'qwant.com', 'lycos.com', 'yippy.com', 'search.com', 'info.com', 'ixquick.com', 'mywebsearch.com', 'ask.com', 'dogpile.com', 'mywebsearch.com', 'infospace.com', 'alhea.com', 'yandex.com', 'excite.com', 'hotbot.com', 'metacrawler.com', 'webcrawler.com', 'yahoo.com', 'mojeek.co.uk', 'lycos.com', 'baidu.com', 'metager.de', 'millionshort.com', 'exalead.com', 'gibiru.com', 'iseek.com', 'meekd.com', 'carrot2.org', 'exactseek.com', 'amidalla.de', 'wiby.me', 'thunderstone.com', 'activesearchresults.com', 'ask.com', 'ezilon.com', 'alltheinternet.com') order by alexa_rank;
