# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from models import *
from crawler import CrawlSingleUrl
from utils import MoveSiteTo, RemoveURLsForDomain, MarkURLContentsAsSpam, SetDomainLanguage, SetDomainInfixLanguage, GetRootDomain, GenerateSearchReport, PornBlock, RequeueRankedKeywordsForDomain
from urlparse import urlparse
from indexer import BuildIndexForTerm
from django.core.exceptions import ObjectDoesNotExist

class QueryParameterAdmin(admin.ModelAdmin):
    list_display = ('domain', 'parameter', 'remove_before_crawl')
    search_fields = ('domain', 'parameter')

class ExcludedSiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'reason')
    search_fields = ('url',)

class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip', 'spam_commenter')
    search_fields = ('ip',)

class SiteInfoAdmin(admin.ModelAdmin):
    list_per_page = 200
    list_display = ('rooturl', 'url', 'pagetitle')
    search_fields = ('rooturl',)
    show_full_result_count = False
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '132'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 132})},
    }

    def block_domain_wrong_language(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            # If you try to language block an unblockable domain (i.e. YouTube), it just deletes the URL
            # and continues on its way.
            try:
                domain = DomainInfo.objects.get(url=parsedurl.netloc)
                if domain.is_unblockable:
                    item.delete()
                    continue
            except ObjectDoesNotExist:
                # Always create domain info if the domain doesn't exist yet.
                domain = DomainInfo()
                domain.url = parsedurl.netloc
                domain.save()
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 8
                site.save()

            RequeueRankedKeywordsForDomain(parsedurl.netloc)

    block_domain_wrong_language.short_description = "Block the selected domains (lang)."

    def block_domain_porn(modeladmin, request, queryset):
        for item in queryset:
            PornBlock(item)

    block_domain_porn.short_description = "Block the selected domains (porn)."

    def block_domain_gambling(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            try:
                domain = DomainInfo.objects.get(url=parsedurl.netloc)
                if domain.is_unblockable:
                    item.delete()
                    continue
            except ObjectDoesNotExist:
                # Always create domain info if the domain doesn't exist yet.
                domain = DomainInfo()
                domain.url = parsedurl.netloc
                domain.save()
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 6
                site.save()

    block_domain_gambling.short_description = "Block the selected domains (gambling)."

    def block_domain_piracy(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            try:
                domain = DomainInfo.objects.get(url=parsedurl.netloc)
                if domain.is_unblockable:
                    item.delete()
                    continue
            except ObjectDoesNotExist:
                # Always create domain info if the domain doesn't exist yet.
                domain = DomainInfo()
                domain.url = parsedurl.netloc
                domain.save()
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 9
                site.save()

    block_domain_piracy.short_description = "Block the selected domains (piracy)."

    def block_domain_shortener(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            try:
                domain = DomainInfo.objects.get(url=parsedurl.netloc)
                if domain.is_unblockable:
                    item.delete()
                    continue
            except ObjectDoesNotExist:
                # Always create domain info if the domain doesn't exist yet.
                domain = DomainInfo()
                domain.url = parsedurl.netloc
                domain.save()
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 12
                site.save()

    block_domain_shortener.short_description = "Block the selected domains (shortener)."

    def block_domain_adserver(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            try:
                domain = DomainInfo.objects.get(url=parsedurl.netloc)
                if domain.is_unblockable:
                    item.delete()
                    continue
            except ObjectDoesNotExist:
                # Always create domain info if the domain doesn't exist yet.
                domain = DomainInfo()
                domain.url = parsedurl.netloc
                domain.save()
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 11
                site.save()

    block_domain_adserver.short_description = "Block the selected domains (ad server)."

    def block_domain_nocontent(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 13
                site.save()

    block_domain_nocontent.short_description = "Block the selected domains (no content)."

    def block_domain_spam(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            try:
                domain = DomainInfo.objects.get(url=parsedurl.netloc)
                if domain.is_unblockable:
                    item.delete()
                    continue
            except ObjectDoesNotExist:
                # Always create domain info if the domain doesn't exist yet.
                domain = DomainInfo()
                domain.url = parsedurl.netloc
                domain.save()
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 7
                site.save()

    block_domain_spam.short_description = "Block the selected domains (spam)."

    def block_domain_social(modeladmin, request, queryset):
        for item in queryset:
            parsedurl = urlparse(item.url)
            try:
                domain = DomainInfo.objects.get(url=parsedurl.netloc)
                if domain.is_unblockable:
                    item.delete()
                    continue
            except ObjectDoesNotExist:
                # Always create domain info if the domain doesn't exist yet.
                domain = DomainInfo()
                domain.url = parsedurl.netloc
                domain.save()
            try:
                existing = BlockedSite.objects.get(url=parsedurl.netloc)
                # If the domain is already blocked, the URL must have been added erroneously.
                # in that case, just delete it.
                RemoveURLsForDomain(item.rooturl)
            except ObjectDoesNotExist:
                site = BlockedSite()
                site.url = parsedurl.netloc
                site.reason = 2
                site.save()

    block_domain_social.short_description = "Block the selected domains (social)."

    def recrawl_this_url(modelAdmin, request, queryset):
        for item in queryset:
            CrawlSingleUrl(item.url)

    recrawl_this_url.short_description = "Recrawl this URL."

    def tag_as_english(modeladmin, request, queryset):
        for item in queryset:
            SetDomainLanguage(item.rooturl, 'en')

    tag_as_english.short_description = "Tag these sites as English."

    def tag_as_language_infix(modeladmin, request, queryset):
        for item in queryset:
            SetDomainInfixLanguage(item.rooturl)

    tag_as_language_infix.short_description = "Tag these sites as Language infix, like /fr/."

    def move_to_german(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'de')

    move_to_german.short_description = "Move these to German."

    def move_to_spanish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'es')

    move_to_spanish.short_description = "Move these to Spanish."

    def move_to_french(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'fr')

    move_to_french.short_description = "Move these to French."

    def move_to_italian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'it')

    move_to_italian.short_description = "Move these to Italian."

    def move_to_polish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'pl')

    move_to_polish.short_description = "Move these to Polish."

    def move_to_portuguese(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'pt')

    move_to_portuguese.short_description = "Move these to Portuguese."

    def move_to_swedish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sv')

    move_to_swedish.short_description = "Move these to Swedish."

    def move_to_norwegian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'no')

    move_to_norwegian.short_description = "Move these to Norwegian."

    def move_to_finnish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'fi')

    move_to_finnish.short_description = "Move these to Finnish."

    def move_to_icelandic(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'is')

    move_to_icelandic.short_description = "Move these to Icelandic."

    def move_to_dutch(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'nl')

    move_to_dutch.short_description = "Move these to Dutch."

    def move_to_czech(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'cs')

    move_to_czech.short_description = "Move these to Czech."

    def move_to_swahili(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sw')

    move_to_swahili.short_description = "Move these to Swahili."

    def move_to_romanian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ro')

    move_to_romanian.short_description = "Move these to Romanian."

    def move_to_danish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'da')

    move_to_danish.short_description = "Move these to Danish."

    def move_to_greek(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'el')

    move_to_greek.short_description = "Move these to Greek."

    def move_to_hungarian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'hu')

    move_to_hungarian.short_description = "Move these to Hungarian."

    def move_to_croatian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'hr')

    move_to_croatian.short_description = "Move these to Croatian."

    def move_to_turkish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'tr')

    move_to_turkish.short_description = "Move these to Turkish."

    def move_to_lithuanian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'lt')

    move_to_lithuanian.short_description = "Move these to Lithuanian."

    def move_to_latvian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'lv')

    move_to_latvian.short_description = "Move these to Latvian."

    def move_to_slovak(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sk')

    move_to_slovak.short_description = "Move these to Slovak."

    def move_to_estonian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'et')

    move_to_estonian.short_description = "Move these to Estonian."

    def move_to_esperanto(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'eo')

    move_to_esperanto.short_description = "Move these to Esperanto."

    def move_to_basque(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'eu')

    move_to_basque.short_description = "Move these to Basque."

    def move_to_slovene(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sl')

    move_to_slovene.short_description = "Move these to Slovene."

    def move_to_yoruba(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'yo')

    move_to_yoruba.short_description = "Move these to Yoruba."

    def move_to_rwandan(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'rw')

    move_to_rwandan.short_description = "Move these to Rwandan."

    def move_to_zulu(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'zu')

    move_to_zulu.short_description = "Move these to Zulu."

    def move_to_shona(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sn')

    move_to_shona.short_description = "Move these to Shona."

    def move_to_afrikaans(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'af')

    move_to_afrikaans.short_description = "Move these to Afrikaans."

    def move_to_akan(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ak')

    move_to_akan.short_description = "Move these to Akan."

    def move_to_igbo(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ig')

    move_to_igbo.short_description = "Move these to Igbo."

    def move_to_lingala(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ln')

    move_to_lingala.short_description = "Move these to Lingala."

    def move_to_wolof(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'wo')

    move_to_wolof.short_description = "Move these to Wolof."

    def move_to_kongo(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'kg')

    move_to_kongo.short_description = "Move these to Kongo."

    def move_to_bambara(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'bm')

    move_to_bambara.short_description = "Move these to Bambara."

    def move_to_breton(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'br')

    move_to_breton.short_description = "Move these to Breton."

    def move_to_ewe(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ee')

    move_to_ewe.short_description = "Move these to Ewe."

    def move_to_fulani(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ff')

    move_to_fulani.short_description = "Move these to Fulani."

    def move_to_hausa(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ha')

    move_to_hausa.short_description = "Move these to Hausa."

    def move_to_kikuyu(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ki')

    move_to_kikuyu.short_description = "Move these to Kikuyu."

    def move_to_luganda(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'lg')

    move_to_luganda.short_description = "Move these to Luganda."

    def move_to_northernsotho(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'nso')

    move_to_northernsotho.short_description = "Move these to Northern Sotho."

    def move_to_nyanja(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ny')

    move_to_nyanja.short_description = "Move these to Nyanja."

    def move_to_oromo(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'om')

    move_to_oromo.short_description = "Move these to Oromo."

    def move_to_kirundi(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'rn')

    move_to_kirundi.short_description = "Move these to Kirundi."

    def move_to_somali(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'so')

    move_to_somali.short_description = "Move these to Somali."

    def move_to_swati(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ss')

    move_to_swati.short_description = "Move these to Swati."

    def move_to_sesotho(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'st')

    move_to_sesotho.short_description = "Move these to Sesotho."

    def move_to_tswana(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'tn')

    move_to_tswana.short_description = "Move these to Tswana."

    def move_to_tsonga(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ts')

    move_to_tsonga.short_description = "Move these to Tsonga."

    def move_to_venda(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 've')

    move_to_venda.short_description = "Move these to Venda."

    def move_to_xhosa(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'xh')

    move_to_xhosa.short_description = "Move these to Xhosa."

    def move_to_occitan(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'oc')

    move_to_occitan.short_description = "Move these to Occitan."

    def move_to_neapolitan(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'nap')

    move_to_neapolitan.short_description = "Move these to Neapolitan."

    def move_to_frisian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'fy')

    move_to_frisian.short_description = "Move these to West Frisian."

    def move_to_faroese(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'fo')

    move_to_faroese.short_description = "Move these to Faroese."

    def move_to_piedmontese(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'pms')

    move_to_piedmontese.short_description = "Move these to Piedmontese."

    def move_to_sardinian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sc')

    move_to_sardinian.short_description = "Move these to Sardinian."

    def move_to_sicilian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'scn')

    move_to_sicilian.short_description = "Move these to Sicilian."

    def move_to_venetian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'vec')

    move_to_venetian.short_description = "Move these to Venetian."

    def move_to_cymraeg(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'cy')

    move_to_cymraeg.short_description = "Move these to Cymraeg (Welsh)."

    def move_to_latin(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'la')

    move_to_latin.short_description = "Move these to Latin."

    def move_to_galician(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'gl')

    move_to_galician.short_description = "Move these to Galician."

    def move_to_catalan(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ca')

    move_to_catalan.short_description = "Move these to Catalan."

    def move_to_english(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'en')

    move_to_english.short_description = "Move these to English."

    actions = [block_domain_wrong_language, block_domain_porn, block_domain_gambling, block_domain_piracy, block_domain_shortener, 
               block_domain_adserver, block_domain_nocontent, block_domain_spam, block_domain_social, tag_as_english, tag_as_language_infix, 
               recrawl_this_url, move_to_german,
               move_to_spanish, move_to_french, move_to_italian, move_to_portuguese, move_to_polish, move_to_swedish, move_to_norwegian,
               move_to_finnish, move_to_icelandic, move_to_dutch, move_to_czech, move_to_swahili, move_to_romanian, move_to_danish,
               move_to_greek, move_to_hungarian, move_to_croatian, move_to_turkish, move_to_lithuanian, move_to_latvian, move_to_slovak,
               move_to_estonian, move_to_slovene, move_to_yoruba, move_to_rwandan, move_to_zulu, move_to_shona, move_to_afrikaans,
               move_to_akan, move_to_igbo, move_to_lingala, move_to_wolof, move_to_kongo, 
               move_to_bambara, move_to_breton, move_to_ewe, move_to_fulani, move_to_hausa, move_to_kikuyu,
               move_to_luganda, move_to_northernsotho, move_to_nyanja, move_to_oromo, move_to_kirundi, move_to_somali, move_to_swati,
               move_to_sesotho, move_to_tswana, move_to_tsonga, move_to_venda, move_to_xhosa, move_to_basque, 
               move_to_occitan, move_to_neapolitan, move_to_frisian, move_to_faroese, move_to_piedmontese, move_to_sardinian,
               move_to_esperanto, move_to_sicilian, move_to_venetian, move_to_cymraeg, move_to_latin, 
               move_to_galician, move_to_catalan, move_to_english]

class SearchReportAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'language', 'total_searches')
    search_fields = ('year', 'language')

    def rebuild_this_report(modelAdmin, request, queryset):
        for item in queryset:
            report = GenerateSearchReport(False, month=item.month, year=item.year, lang=item.language)
            item.delete()
            report.save()

    rebuild_this_report.short_description = "Rebuild this report."

    actions = [rebuild_this_report,]

class PendingUrlAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

    def recrawl_this_url(modelAdmin, request, queryset):
        for item in queryset:
            CrawlSingleUrl(item.url)

    recrawl_this_url.short_description = "Crawl this URL."

    actions = [recrawl_this_url,]

class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'result_count', 'search_time', 'ip', 'last_search', 'indexed', 'is_bot')
    search_fields = ('keywords', 'ip')

    def block_these_terms(modeladmin, request, queryset):
        for item in queryset:
            try:
                existing = BadQuery.objects.get(keywords=item.keywords)
            except ObjectDoesNotExist:
                bad = BadQuery()
                bad.keywords = item.keywords
                bad.save()
            item.is_bot = True
            item.save()
    
    block_these_terms.short_description = "Add terms to bad query list and mark as bot queries."

    def mark_as_bot(modeladmin, request, queryset):
        for item in queryset:
            item.is_bot = True
            item.save()
    
    mark_as_bot.short_description = "Mark these queries as bot queries."
    
    actions = [block_these_terms, mark_as_bot]

class IndexTermAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'date_indexed', 'num_results', 'index_time', 'actively_blocked', 'refused')
    search_fields = ('keywords',)

    def reindex_these_terms(modeladmin, request, queryset):
        for item in queryset:
            name = item.__class__.__name__
            if name is 'IndexTerm':
                lang = 'en'
            else:
                lang = name[-2:]
            BuildIndexForTerm(item.keywords, lang=lang, type='fourthrootandlog')
    
    reindex_these_terms.short_description = "Reindex these term(s). (may time out)"
    
    actions = [reindex_these_terms,]

class EnglishIndexTermAdmin(IndexTermAdmin):
    list_display = ('keywords', 'date_indexed', 'num_results', 'index_time', 'actively_blocked', 'refused', 'show_ad', 'typo_for', 'is_language')

class BadQueryAdmin(admin.ModelAdmin):
    list_display = ('keywords',)
    search_fields = ('keywords',)

class PendingIndexAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'date_added', 'reason')
    search_fields = ('keywords',)

    def index_these_terms(modeladmin, request, queryset):
        for item in queryset:
            name = item.__class__.__name__
            if name is 'PendingIndex':
                lang = 'en'
            else:
                lang = name[-2:]
            BuildIndexForTerm(item.keywords, lang=lang, type='fourthrootandlog')
            item.delete()
    
    index_these_terms.short_description = "Index these term(s). (may time out)"

    def block_these_terms(modeladmin, request, queryset):
        for item in queryset:
            name = item.__class__.__name__
            if name is 'PendingIndex':
                lang = 'en'
            else:
                lang = name[-2:]
            try:
                existing = BadQuery.objects.get(keywords=item.keywords)
            except ObjectDoesNotExist:
                bad = BadQuery()
                bad.keywords = item.keywords
                bad.save()
            item.delete()
    
    block_these_terms.short_description = "Add terms to bad query list and delete."
    
    actions = [index_these_terms, block_these_terms]

class FeedbackItemAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'num_search_results', 'date_added', 'language', 'processed', 'ip')
    search_fields = ('keywords',)

    def spam_block(modeladmin, request, queryset):
        for item in queryset:
            MarkURLContentsAsSpam(item.comment, item.ip)
            item.delete()
    
    spam_block.short_description = "Block the contents of these items as spam."
    
    actions = [spam_block,]

class DomainInfoAdmin(admin.ModelAdmin):
    list_display = ('url', 'language_association', 'alexa_rank')
    search_fields = ('url',)
    show_full_result_count = False

class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name', 'value')

class SiteInfoAfterZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZZZZZZZ')

class SiteInfoH1AfterZAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagefirstheadtag__gt='ZZZZZZZZZZ')

class SiteInfoH2AfterZAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagefirsth2tag__gt='ZZZZZZZZZZ')

class SiteInfoH3AfterZAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagefirsth3tag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagefirsth3tag__gt='ZZZZZZZZZZ')

class SiteInfoGreekAlphabetAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='Α', pagetitle__lt='ΩΩΩΩΩ')

class SiteInfoH1GreekAlphabetAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagefirstheadtag__gt='Α', pagefirstheadtag__lt='ΩΩΩΩΩ')

class SiteInfoBeforeZeroAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__lt='0', pagetitle__gt=' ')

class SiteInfoH1BeforeZeroAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagefirstheadtag__lt='0', pagefirstheadtag__gt=' ')

class SiteInfoH2BeforeZeroAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagefirsth2tag__lt='0', pagefirsth2tag__gt=' ')

class SiteInfoH3BeforeZeroAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagefirsth3tag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagefirsth3tag__lt='0', pagefirsth3tag__gt=' ')

class SiteInfoEndingInADAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ad')

class SiteInfoEndingInAEAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ae')

class SiteInfoEndingInAEROAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.aero')

class SiteInfoEndingInAFAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.af')

class SiteInfoEndingInAIAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ai')

class SiteInfoEndingInALAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.al')

class SiteInfoEndingInAMAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.am')

class SiteInfoEndingInANAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.an')

class SiteInfoEndingInAOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ao')

class SiteInfoEndingInAQAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.aq')

class SiteInfoEndingInARAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ar')

class SiteInfoEndingInASIAAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.asia')

class SiteInfoEndingInATAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.at')

class SiteInfoEndingInAUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.au')

class SiteInfoEndingInAWAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.aw')

class SiteInfoEndingInAZAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.az')

class SiteInfoEndingInBAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ba')

class SiteInfoEndingInBBAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bb')

class SiteInfoEndingInBDAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bd')

class SiteInfoEndingInBEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.be')

class SiteInfoEndingInBERLINAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.berlin')

class SiteInfoEndingInBFAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bf')

class SiteInfoEndingInBGAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bg')

class SiteInfoEndingInBHAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bh')

class SiteInfoEndingInBIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bi')

class SiteInfoEndingInBIZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.biz')

class SiteInfoEndingInBJAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bj')

class SiteInfoEndingInBNAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bn')

class SiteInfoEndingInBOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bo')

class SiteInfoEndingInBRAdmin(SiteInfoAdmin):
    pass

class SiteInfoEndingInBSAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bs')

class SiteInfoEndingInBTAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bt')

class SiteInfoEndingInBWAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bw')

class SiteInfoEndingInBYAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.by')

class SiteInfoEndingInBZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.bz')

class SiteInfoEndingInCAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ca')

class SiteInfoEndingInCATAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cat')

class SiteInfoEndingInCCAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cc')

class SiteInfoEndingInCDAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cd')

class SiteInfoEndingInCFAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cf')

class SiteInfoEndingInCGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cg')

class SiteInfoEndingInCHAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ch')

class SiteInfoEndingInCIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ci')

class SiteInfoEndingInCKAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ck')

class SiteInfoEndingInCLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cl')

class SiteInfoEndingInCOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.co')

class SiteInfoEndingInCOMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.com')

class SiteInfoEndingInCUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cu')

class SiteInfoEndingInCVAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cv')

class SiteInfoEndingInCWAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cw')

class SiteInfoEndingInCMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cm')

class SiteInfoEndingInCNAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cn')

class SiteInfoEndingInCRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cr')

class SiteInfoEndingInCUAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cu')

class SiteInfoEndingInCVAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cv')

class SiteInfoEndingInCXAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cx')

class SiteInfoEndingInCYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cy')

class SiteInfoEndingInCZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.cz')

class SiteInfoEndingInDEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.de')

class SiteInfoEndingInDJAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.dj')

class SiteInfoEndingInDKAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.dk')

class SiteInfoEndingInDMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.dm')

class SiteInfoEndingInDOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.do')

class SiteInfoEndingInDZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.dz')

class SiteInfoEndingInECAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ec')

class SiteInfoEndingInEDUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.edu')

class SiteInfoEndingInEEAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ee')

class SiteInfoEndingInETAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.et')

class SiteInfoEndingInEGAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.eg')

class SiteInfoEndingInERAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.er')

class SiteInfoEndingInESAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.es')

class SiteInfoEndingInEUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.eu')

class SiteInfoEndingInEUSAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.eus')

class SiteInfoEndingInFIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.fi')

class SiteInfoEndingInFJAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.fj')

class SiteInfoEndingInFKAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.fk')

class SiteInfoEndingInFRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.fr')

class SiteInfoEndingInFRLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.frl')

class SiteInfoEndingInFOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.fo')

class SiteInfoEndingInGAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ga')

class SiteInfoEndingInGALAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gal')

class SiteInfoEndingInGDAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gd')

class SiteInfoEndingInGEAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ge')

class SiteInfoEndingInGFAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gf')

class SiteInfoEndingInGHAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gh')

class SiteInfoEndingInGIAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gi')

class SiteInfoEndingInGLAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gl')

class SiteInfoEndingInGMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gm')

class SiteInfoEndingInGNAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gn')

class SiteInfoEndingInGQAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gq')

class SiteInfoEndingInGRAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gr')

class SiteInfoEndingInGTAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gt')

class SiteInfoEndingInGUAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gu')

class SiteInfoEndingInGURUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.guru')

class SiteInfoEndingInGWAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gw')

class SiteInfoEndingInGYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.gy')

class SiteInfoEndingInHKAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.hk')

class SiteInfoEndingInHNAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.hn')

class SiteInfoEndingInHMAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.hm')

class SiteInfoEndingInHRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.hr')

class SiteInfoEndingInHUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.hu')

class SiteInfoEndingInHTAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ht')

class SiteInfoEndingInIDAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.id')

class SiteInfoEndingInILAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.il')

class SiteInfoEndingInINAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.in')

class SiteInfoEndingInINFOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.info')

class SiteInfoEndingInIQAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.iq')

class SiteInfoEndingInIRAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ir')

class SiteInfoEndingInISAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.is')

class SiteInfoEndingInITAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.it')

class SiteInfoEndingInJOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.jo')

class SiteInfoEndingInJPAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.jp')

class SiteInfoEndingInKEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ke')

class SiteInfoEndingInKGAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.kg')

class SiteInfoEndingInKHAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.kh')

class SiteInfoEndingInKIAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ki')

class SiteInfoEndingInKOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ko')

class SiteInfoEndingInKMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.km')

class SiteInfoEndingInKNAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.kn')

class SiteInfoEndingInKPAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.kp')

class SiteInfoEndingInKRAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.kr')

class SiteInfoEndingInKWAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.kw')

class SiteInfoEndingInKZAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.kz')

class SiteInfoEndingInLAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.la')

class SiteInfoEndingInLBAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.lb')

class SiteInfoEndingInLCAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.lc')

class SiteInfoEndingInLIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.li')

class SiteInfoEndingInLKAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.lk')

class SiteInfoEndingInLRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.lr')

class SiteInfoEndingInLSAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ls')

class SiteInfoEndingInLUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.lu')

class SiteInfoEndingInLTAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.lt')

class SiteInfoEndingInLVAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.lv')

class SiteInfoEndingInMAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ma')

class SiteInfoEndingInMCAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mc')

class SiteInfoEndingInMDAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.md')

class SiteInfoEndingInMEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.me')

class SiteInfoEndingInMGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mg')

class SiteInfoEndingInMKAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mk')

class SiteInfoEndingInMLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ml')

class SiteInfoEndingInMMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mm')

class SiteInfoEndingInMNAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mn')

class SiteInfoEndingInMOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mo')

class SiteInfoEndingInMOBIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mobi')

class SiteInfoEndingInMQAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mq')

class SiteInfoEndingInMRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mr')

class SiteInfoEndingInMUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mu')

class SiteInfoEndingInMVAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mv')

class SiteInfoEndingInMWAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mw')

class SiteInfoEndingInMXAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mx')

class SiteInfoEndingInMYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.my')

class SiteInfoEndingInMZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.mz')

class SiteInfoEndingInNAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.na')

class SiteInfoEndingInNEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ne')

class SiteInfoEndingInNETAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.net')

class SiteInfoEndingInNGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ng')

class SiteInfoEndingInNIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ni')

class SiteInfoEndingInNINJAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ninja')

class SiteInfoEndingInNLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.nl')

class SiteInfoEndingInNOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.no')

class SiteInfoEndingInNUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.nu')

class SiteInfoEndingInNZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.nz')

class SiteInfoEndingInOMAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.om')

class SiteInfoEndingInORGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.org')

class SiteInfoEndingInPAAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pa')

class SiteInfoEndingInPARISAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.paris')

class SiteInfoEndingInPEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pe')

class SiteInfoEndingInPFAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pf')

class SiteInfoEndingInPGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pg')

class SiteInfoEndingInPHAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ph')

class SiteInfoEndingInPICSAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pics')

class SiteInfoEndingInPLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pl')

class SiteInfoEndingInPMAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pm')

class SiteInfoEndingInPNAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pn')

class SiteInfoEndingInNPAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.po')

class SiteInfoEndingInPORNAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.porn')

class SiteInfoEndingInPRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pr')

class SiteInfoEndingInPTAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.pt')

class SiteInfoEndingInPYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.py')

class SiteInfoEndingInQAAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.qa')

class SiteInfoEndingInROAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ro')

class SiteInfoEndingInRSAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.rs')

class SiteInfoEndingInRUAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ru')

class SiteInfoEndingInRWAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.rw')

class SiteInfoEndingInSAAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sa')

class SiteInfoEndingInSBAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sb')

class SiteInfoEndingInSCAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sc')

class SiteInfoEndingInSDAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sd')

class SiteInfoEndingInSEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.se')

class SiteInfoEndingInSEXYAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sexy')

class SiteInfoEndingInSGAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sg')

class SiteInfoEndingInSIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.si')

class SiteInfoEndingInSKAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sk')

class SiteInfoEndingInSLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sl')

class SiteInfoEndingInSMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sm')

class SiteInfoEndingInSNAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sn')

class SiteInfoEndingInSOAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.so')

class SiteInfoEndingInSRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sr')

class SiteInfoEndingInSTAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.st')

class SiteInfoEndingInSUAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.su')

class SiteInfoEndingInSVAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sv')

class SiteInfoEndingInSYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sy')

class SiteInfoEndingInSXAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sx')

class SiteInfoEndingInSZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.sz')

class SiteInfoEndingInTDAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.td')

class SiteInfoEndingInTGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tg')

class SiteInfoEndingInTHAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.th')

class SiteInfoEndingInTJAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tj')

class SiteInfoEndingInTKAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tk')

class SiteInfoEndingInTLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tl')

class SiteInfoEndingInTMAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tm')

class SiteInfoEndingInTOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.to')

class SiteInfoEndingInTPAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tp')

class SiteInfoEndingInTRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tr')

class SiteInfoEndingInTRAVELAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.travel')

class SiteInfoEndingInTTAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tt')

class SiteInfoEndingInTVAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tv')

class SiteInfoEndingInTWAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tw')

class SiteInfoEndingInTZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.tz')

class SiteInfoEndingInUAAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ua')

class SiteInfoEndingInUGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ug')

class SiteInfoEndingInUKAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.uk')

class SiteInfoEndingInUSAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.us')

class SiteInfoEndingInUYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.uy')

class SiteInfoEndingInUZAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.uz')

class SiteInfoEndingInVAAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.va')

class SiteInfoEndingInVEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ve')

class SiteInfoEndingInVNAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.vn')

class SiteInfoEndingInWFAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.wf')

class SiteInfoEndingInWSAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ws')

class SiteInfoEndingInXMLAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(url__endswith='.xml')

class SiteInfoEndingInXXXAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.xxx')

class SiteInfoEndingInYEAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.ye')

class SiteInfoEndingInYTAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.yt')

class SiteInfoEndingInZAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.za')

class SiteInfoEndingInZMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.zm')

class SiteInfoEndingInZWAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(rooturl__endswith='.zw')

class SiteInfoAfterZEndingInAMAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag')
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.am')

class SiteInfoAfterZEndingInAEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ae')

class SiteInfoAfterZEndingInASIAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.asia')

class SiteInfoAfterZEndingInAZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.az')

class SiteInfoAfterZEndingInBGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.bg')

class SiteInfoAfterZEndingInBHAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.bh')

class SiteInfoAfterZEndingInBIZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.biz')

class SiteInfoAfterZEndingInBYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.by')

class SiteInfoAfterZEndingInBZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.bz')

class SiteInfoAfterZEndingInCNAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.cn')

class SiteInfoAfterZEndingInCOMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.com')

class SiteInfoAfterZEndingInDZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.dz')

class SiteInfoAfterZEndingInEEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ee')

class SiteInfoAfterZEndingInEGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.eg')

class SiteInfoAfterZEndingInFMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.fm')

class SiteInfoAfterZEndingInGEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ge')

class SiteInfoAfterZEndingInHKAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.hk')

class SiteInfoAfterZEndingInILAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.il')

class SiteInfoAfterZEndingInINAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.in')

class SiteInfoAfterZEndingInINFOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.info')

class SiteInfoAfterZEndingInIQAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.iq')

class SiteInfoAfterZEndingInIRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ir')

class SiteInfoAfterZEndingInJOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.jo')

class SiteInfoAfterZEndingInJPAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.jp')

class SiteInfoAfterZEndingInKGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.kg')

class SiteInfoAfterZEndingInKRAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.kr')

class SiteInfoAfterZEndingInKWAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.kw')

class SiteInfoAfterZEndingInKZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.kz')

class SiteInfoAfterZEndingInLAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.la')

class SiteInfoAfterZEndingInLBAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.lb')

class SiteInfoAfterZEndingInLIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.li')

class SiteInfoAfterZEndingInLYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ly')

class SiteInfoAfterZEndingInMAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ma')

class SiteInfoAfterZEndingInMDAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.md')

class SiteInfoAfterZEndingInMEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.me')

class SiteInfoAfterZEndingInMKAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.mk')

class SiteInfoAfterZEndingInMOBIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.mobi')

class SiteInfoAfterZEndingInMYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.my')

class SiteInfoAfterZEndingInOMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.om')

class SiteInfoAfterZEndingInORGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.org')

class SiteInfoAfterZEndingInNETAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.net')

class SiteInfoAfterZEndingInPROAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.pro')

class SiteInfoAfterZEndingInPSAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ps')

class SiteInfoAfterZEndingInQAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.qa')

class SiteInfoAfterZEndingInRSAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.rs')

class SiteInfoAfterZEndingInRUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ru')

class SiteInfoAfterZEndingInSAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.sa')

class SiteInfoAfterZEndingInSDAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.sd')

class SiteInfoAfterZEndingInSGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.sg')

class SiteInfoAfterZEndingInSTAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.st')

class SiteInfoAfterZEndingInSUAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.su')

class SiteInfoAfterZEndingInSYAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.sy')

class SiteInfoAfterZEndingInTJAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.tj')

class SiteInfoAfterZEndingInTKAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.tk')

class SiteInfoAfterZEndingInTMAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.tm')

class SiteInfoAfterZEndingInTNAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.tn')

class SiteInfoAfterZEndingInTOAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.to')

class SiteInfoAfterZEndingInTVAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.tv')

class SiteInfoAfterZEndingInTWAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.tw')

class SiteInfoAfterZEndingInUAAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ua')

class SiteInfoAfterZEndingInUSAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.us')

class SiteInfoAfterZEndingInUZAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.uz')

class SiteInfoAfterZEndingInVGAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.vg')

class SiteInfoAfterZEndingInWSAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ws')

class SiteInfoAfterZEndingInYEAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='.ye')

class SiteInfoAfterZEndingInP1AIAdmin(SiteInfoAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(pagetitle__gt='ZZZZ', rooturl__endswith='--p1ai')

class DMCANoticeAdmin(admin.ModelAdmin):
    list_display = ('sender', 'date')
    search_fields = ('sender', 'contents')

class AutoCompleteAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'score')
    search_fields = ('keywords',)

class ResultClickAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'position', 'url', 'ip', 'search_id', 'click_time')
    search_fields = ('keywords',)

class APISubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'monthly_calls', 'expires')
    search_fields = ('user__username',)

class APIUsageAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'year', 'calls_used')
    search_fields = ('user__username',)

admin.site.register(BlockedSite, ExcludedSiteAdmin)
admin.site.register(SiteInfo, SiteInfoAdmin)
admin.site.register(SiteInfoEndingInAD, SiteInfoEndingInADAdmin)
admin.site.register(SiteInfoEndingInAE, SiteInfoEndingInAEAdmin)
admin.site.register(SiteInfoEndingInAERO, SiteInfoEndingInAEROAdmin)
admin.site.register(SiteInfoEndingInAF, SiteInfoEndingInAFAdmin)
admin.site.register(SiteInfoEndingInAI, SiteInfoEndingInAIAdmin)
admin.site.register(SiteInfoEndingInAL, SiteInfoEndingInALAdmin)
admin.site.register(SiteInfoEndingInAM, SiteInfoEndingInAMAdmin)
admin.site.register(SiteInfoEndingInAN, SiteInfoEndingInANAdmin)
admin.site.register(SiteInfoEndingInAO, SiteInfoEndingInAOAdmin)
admin.site.register(SiteInfoEndingInAQ, SiteInfoEndingInAQAdmin)
admin.site.register(SiteInfoEndingInAR, SiteInfoEndingInARAdmin)
admin.site.register(SiteInfoEndingInASIA, SiteInfoEndingInASIAAdmin)
admin.site.register(SiteInfoEndingInAT, SiteInfoEndingInATAdmin)
admin.site.register(SiteInfoEndingInAU, SiteInfoEndingInAUAdmin)
admin.site.register(SiteInfoEndingInAW, SiteInfoEndingInAWAdmin)
admin.site.register(SiteInfoEndingInAZ, SiteInfoEndingInAZAdmin)
admin.site.register(SiteInfoEndingInBA, SiteInfoEndingInBAAdmin)
admin.site.register(SiteInfoEndingInBB, SiteInfoEndingInBBAdmin)
admin.site.register(SiteInfoEndingInBD, SiteInfoEndingInBDAdmin)
admin.site.register(SiteInfoEndingInBE, SiteInfoEndingInBEAdmin)
admin.site.register(SiteInfoEndingInBERLIN, SiteInfoEndingInBERLINAdmin)
admin.site.register(SiteInfoEndingInBF, SiteInfoEndingInBFAdmin)
admin.site.register(SiteInfoEndingInBG, SiteInfoEndingInBGAdmin)
admin.site.register(SiteInfoEndingInBH, SiteInfoEndingInBHAdmin)
admin.site.register(SiteInfoEndingInBI, SiteInfoEndingInBIAdmin)
admin.site.register(SiteInfoEndingInBIZ, SiteInfoEndingInBIZAdmin)
admin.site.register(SiteInfoEndingInBJ, SiteInfoEndingInBJAdmin)
admin.site.register(SiteInfoEndingInBN, SiteInfoEndingInBNAdmin)
admin.site.register(SiteInfoEndingInBO, SiteInfoEndingInBOAdmin)
admin.site.register(SiteInfoEndingInBR, SiteInfoEndingInBRAdmin)
admin.site.register(SiteInfoEndingInBS, SiteInfoEndingInBSAdmin)
admin.site.register(SiteInfoEndingInBT, SiteInfoEndingInBTAdmin)
admin.site.register(SiteInfoEndingInBW, SiteInfoEndingInBWAdmin)
admin.site.register(SiteInfoEndingInBY, SiteInfoEndingInBYAdmin)
admin.site.register(SiteInfoEndingInBZ, SiteInfoEndingInBZAdmin)
admin.site.register(SiteInfoEndingInCA, SiteInfoEndingInCAAdmin)
admin.site.register(SiteInfoEndingInCAT, SiteInfoEndingInCATAdmin)
admin.site.register(SiteInfoEndingInCC, SiteInfoEndingInCCAdmin)
admin.site.register(SiteInfoEndingInCD, SiteInfoEndingInCDAdmin)
admin.site.register(SiteInfoEndingInCF, SiteInfoEndingInCFAdmin)
admin.site.register(SiteInfoEndingInCG, SiteInfoEndingInCGAdmin)
admin.site.register(SiteInfoEndingInCH, SiteInfoEndingInCHAdmin)
admin.site.register(SiteInfoEndingInCI, SiteInfoEndingInCIAdmin)
admin.site.register(SiteInfoEndingInCK, SiteInfoEndingInCKAdmin)
admin.site.register(SiteInfoEndingInCL, SiteInfoEndingInCLAdmin)
admin.site.register(SiteInfoEndingInCM, SiteInfoEndingInCMAdmin)
admin.site.register(SiteInfoEndingInCN, SiteInfoEndingInCNAdmin)
admin.site.register(SiteInfoEndingInCO, SiteInfoEndingInCOAdmin)
admin.site.register(SiteInfoEndingInCOM, SiteInfoEndingInCOMAdmin)
admin.site.register(SiteInfoEndingInCR, SiteInfoEndingInCRAdmin)
admin.site.register(SiteInfoEndingInCU, SiteInfoEndingInCUAdmin)
admin.site.register(SiteInfoEndingInCV, SiteInfoEndingInCVAdmin)
admin.site.register(SiteInfoEndingInCW, SiteInfoEndingInCWAdmin)
admin.site.register(SiteInfoEndingInCY, SiteInfoEndingInCYAdmin)
admin.site.register(SiteInfoEndingInCX, SiteInfoEndingInCXAdmin)
admin.site.register(SiteInfoEndingInCZ, SiteInfoEndingInCZAdmin)
admin.site.register(SiteInfoEndingInDE, SiteInfoEndingInDEAdmin)
admin.site.register(SiteInfoEndingInDK, SiteInfoEndingInDKAdmin)
admin.site.register(SiteInfoEndingInDJ, SiteInfoEndingInDJAdmin)
admin.site.register(SiteInfoEndingInDM, SiteInfoEndingInDMAdmin)
admin.site.register(SiteInfoEndingInDO, SiteInfoEndingInDOAdmin)
admin.site.register(SiteInfoEndingInDZ, SiteInfoEndingInDZAdmin)
admin.site.register(SiteInfoEndingInEC, SiteInfoEndingInECAdmin)
admin.site.register(SiteInfoEndingInEDU, SiteInfoEndingInEDUAdmin)
admin.site.register(SiteInfoEndingInEE, SiteInfoEndingInEEAdmin)
admin.site.register(SiteInfoEndingInEG, SiteInfoEndingInEGAdmin)
admin.site.register(SiteInfoEndingInER, SiteInfoEndingInERAdmin)
admin.site.register(SiteInfoEndingInES, SiteInfoEndingInESAdmin)
admin.site.register(SiteInfoEndingInET, SiteInfoEndingInETAdmin)
admin.site.register(SiteInfoEndingInEU, SiteInfoEndingInEUAdmin)
admin.site.register(SiteInfoEndingInEUS, SiteInfoEndingInEUSAdmin)
admin.site.register(SiteInfoEndingInFI, SiteInfoEndingInFIAdmin)
admin.site.register(SiteInfoEndingInFJ, SiteInfoEndingInFJAdmin)
admin.site.register(SiteInfoEndingInFK, SiteInfoEndingInFKAdmin)
admin.site.register(SiteInfoEndingInFO, SiteInfoEndingInFOAdmin)
admin.site.register(SiteInfoEndingInFR, SiteInfoEndingInFRAdmin)
admin.site.register(SiteInfoEndingInFRL, SiteInfoEndingInFRLAdmin)
admin.site.register(SiteInfoEndingInGA, SiteInfoEndingInGAAdmin)
admin.site.register(SiteInfoEndingInGAL, SiteInfoEndingInGALAdmin)
admin.site.register(SiteInfoEndingInGD, SiteInfoEndingInGDAdmin)
admin.site.register(SiteInfoEndingInGE, SiteInfoEndingInGEAdmin)
admin.site.register(SiteInfoEndingInGF, SiteInfoEndingInGFAdmin)
admin.site.register(SiteInfoEndingInGH, SiteInfoEndingInGHAdmin)
admin.site.register(SiteInfoEndingInGI, SiteInfoEndingInGIAdmin)
admin.site.register(SiteInfoEndingInGM, SiteInfoEndingInGMAdmin)
admin.site.register(SiteInfoEndingInGL, SiteInfoEndingInGLAdmin)
admin.site.register(SiteInfoEndingInGN, SiteInfoEndingInGNAdmin)
admin.site.register(SiteInfoEndingInGQ, SiteInfoEndingInGQAdmin)
admin.site.register(SiteInfoEndingInGR, SiteInfoEndingInGRAdmin)
admin.site.register(SiteInfoEndingInGT, SiteInfoEndingInGTAdmin)
admin.site.register(SiteInfoEndingInGU, SiteInfoEndingInGUAdmin)
admin.site.register(SiteInfoEndingInGURU, SiteInfoEndingInGURUAdmin)
admin.site.register(SiteInfoEndingInGY, SiteInfoEndingInGYAdmin)
admin.site.register(SiteInfoEndingInGW, SiteInfoEndingInGWAdmin)
admin.site.register(SiteInfoEndingInHK, SiteInfoEndingInHKAdmin)
admin.site.register(SiteInfoEndingInHM, SiteInfoEndingInHMAdmin)
admin.site.register(SiteInfoEndingInHN, SiteInfoEndingInHNAdmin)
admin.site.register(SiteInfoEndingInHR, SiteInfoEndingInHRAdmin)
admin.site.register(SiteInfoEndingInHT, SiteInfoEndingInHTAdmin)
admin.site.register(SiteInfoEndingInHU, SiteInfoEndingInHUAdmin)
admin.site.register(SiteInfoEndingInID, SiteInfoEndingInIDAdmin)
admin.site.register(SiteInfoEndingInIL, SiteInfoEndingInILAdmin)
admin.site.register(SiteInfoEndingInIN, SiteInfoEndingInINAdmin)
admin.site.register(SiteInfoEndingInINFO, SiteInfoEndingInINFOAdmin)
admin.site.register(SiteInfoEndingInIQ, SiteInfoEndingInIQAdmin)
admin.site.register(SiteInfoEndingInIR, SiteInfoEndingInIRAdmin)
admin.site.register(SiteInfoEndingInIS, SiteInfoEndingInISAdmin)
admin.site.register(SiteInfoEndingInIT, SiteInfoEndingInITAdmin)
admin.site.register(SiteInfoEndingInJO, SiteInfoEndingInJOAdmin)
admin.site.register(SiteInfoEndingInJP, SiteInfoEndingInJPAdmin)
admin.site.register(SiteInfoEndingInKE, SiteInfoEndingInKEAdmin)
admin.site.register(SiteInfoEndingInKG, SiteInfoEndingInKGAdmin)
admin.site.register(SiteInfoEndingInKH, SiteInfoEndingInKHAdmin)
admin.site.register(SiteInfoEndingInKI, SiteInfoEndingInKIAdmin)
admin.site.register(SiteInfoEndingInKM, SiteInfoEndingInKMAdmin)
admin.site.register(SiteInfoEndingInKN, SiteInfoEndingInKNAdmin)
admin.site.register(SiteInfoEndingInKO, SiteInfoEndingInKOAdmin)
admin.site.register(SiteInfoEndingInKP, SiteInfoEndingInKPAdmin)
admin.site.register(SiteInfoEndingInKR, SiteInfoEndingInKRAdmin)
admin.site.register(SiteInfoEndingInKW, SiteInfoEndingInKWAdmin)
admin.site.register(SiteInfoEndingInKZ, SiteInfoEndingInKZAdmin)
admin.site.register(SiteInfoEndingInLA, SiteInfoEndingInLAAdmin)
admin.site.register(SiteInfoEndingInLB, SiteInfoEndingInLBAdmin)
admin.site.register(SiteInfoEndingInLC, SiteInfoEndingInLCAdmin)
admin.site.register(SiteInfoEndingInLI, SiteInfoEndingInLIAdmin)
admin.site.register(SiteInfoEndingInLK, SiteInfoEndingInLKAdmin)
admin.site.register(SiteInfoEndingInLR, SiteInfoEndingInLRAdmin)
admin.site.register(SiteInfoEndingInLS, SiteInfoEndingInLSAdmin)
admin.site.register(SiteInfoEndingInLT, SiteInfoEndingInLTAdmin)
admin.site.register(SiteInfoEndingInLU, SiteInfoEndingInLUAdmin)
admin.site.register(SiteInfoEndingInLV, SiteInfoEndingInLVAdmin)
admin.site.register(SiteInfoEndingInMA, SiteInfoEndingInMAAdmin)
admin.site.register(SiteInfoEndingInMC, SiteInfoEndingInMCAdmin)
admin.site.register(SiteInfoEndingInMD, SiteInfoEndingInMDAdmin)
admin.site.register(SiteInfoEndingInME, SiteInfoEndingInMEAdmin)
admin.site.register(SiteInfoEndingInMG, SiteInfoEndingInMGAdmin)
admin.site.register(SiteInfoEndingInMK, SiteInfoEndingInMKAdmin)
admin.site.register(SiteInfoEndingInML, SiteInfoEndingInMLAdmin)
admin.site.register(SiteInfoEndingInMM, SiteInfoEndingInMMAdmin)
admin.site.register(SiteInfoEndingInMN, SiteInfoEndingInMNAdmin)
admin.site.register(SiteInfoEndingInMO, SiteInfoEndingInMOAdmin)
admin.site.register(SiteInfoEndingInMOBI, SiteInfoEndingInMOBIAdmin)
admin.site.register(SiteInfoEndingInMQ, SiteInfoEndingInMQAdmin)
admin.site.register(SiteInfoEndingInMR, SiteInfoEndingInMRAdmin)
admin.site.register(SiteInfoEndingInMU, SiteInfoEndingInMUAdmin)
admin.site.register(SiteInfoEndingInMV, SiteInfoEndingInMVAdmin)
admin.site.register(SiteInfoEndingInMW, SiteInfoEndingInMWAdmin)
admin.site.register(SiteInfoEndingInMY, SiteInfoEndingInMYAdmin)
admin.site.register(SiteInfoEndingInMX, SiteInfoEndingInMXAdmin)
admin.site.register(SiteInfoEndingInMZ, SiteInfoEndingInMZAdmin)
admin.site.register(SiteInfoEndingInNA, SiteInfoEndingInNAAdmin)
admin.site.register(SiteInfoEndingInNE, SiteInfoEndingInNEAdmin)
admin.site.register(SiteInfoEndingInNET, SiteInfoEndingInNETAdmin)
admin.site.register(SiteInfoEndingInNG, SiteInfoEndingInNGAdmin)
admin.site.register(SiteInfoEndingInNI, SiteInfoEndingInNIAdmin)
admin.site.register(SiteInfoEndingInNINJA, SiteInfoEndingInNINJAAdmin)
admin.site.register(SiteInfoEndingInNO, SiteInfoEndingInNOAdmin)
admin.site.register(SiteInfoEndingInNP, SiteInfoEndingInNPAdmin)
admin.site.register(SiteInfoEndingInNL, SiteInfoEndingInNLAdmin)
admin.site.register(SiteInfoEndingInNU, SiteInfoEndingInNUAdmin)
admin.site.register(SiteInfoEndingInNZ, SiteInfoEndingInNZAdmin)
admin.site.register(SiteInfoEndingInOM, SiteInfoEndingInOMAdmin)
admin.site.register(SiteInfoEndingInORG, SiteInfoEndingInORGAdmin)
admin.site.register(SiteInfoEndingInPA, SiteInfoEndingInPAAdmin)
admin.site.register(SiteInfoEndingInPARIS, SiteInfoEndingInPARISAdmin)
admin.site.register(SiteInfoEndingInPE, SiteInfoEndingInPEAdmin)
admin.site.register(SiteInfoEndingInPF, SiteInfoEndingInPFAdmin)
admin.site.register(SiteInfoEndingInPG, SiteInfoEndingInPGAdmin)
admin.site.register(SiteInfoEndingInPH, SiteInfoEndingInPHAdmin)
admin.site.register(SiteInfoEndingInPICS, SiteInfoEndingInPICSAdmin)
admin.site.register(SiteInfoEndingInPL, SiteInfoEndingInPLAdmin)
admin.site.register(SiteInfoEndingInPM, SiteInfoEndingInPMAdmin)
admin.site.register(SiteInfoEndingInPN, SiteInfoEndingInPNAdmin)
admin.site.register(SiteInfoEndingInPORN, SiteInfoEndingInPORNAdmin)
admin.site.register(SiteInfoEndingInPR, SiteInfoEndingInPRAdmin)
admin.site.register(SiteInfoEndingInPT, SiteInfoEndingInPTAdmin)
admin.site.register(SiteInfoEndingInPY, SiteInfoEndingInPYAdmin)
admin.site.register(SiteInfoEndingInQA, SiteInfoEndingInQAAdmin)
admin.site.register(SiteInfoEndingInRO, SiteInfoEndingInROAdmin)
admin.site.register(SiteInfoEndingInRS, SiteInfoEndingInRSAdmin)
admin.site.register(SiteInfoEndingInRU, SiteInfoEndingInRUAdmin)
admin.site.register(SiteInfoEndingInRW, SiteInfoEndingInRWAdmin)
admin.site.register(SiteInfoEndingInSA, SiteInfoEndingInSAAdmin)
admin.site.register(SiteInfoEndingInSB, SiteInfoEndingInSBAdmin)
admin.site.register(SiteInfoEndingInSC, SiteInfoEndingInSCAdmin)
admin.site.register(SiteInfoEndingInSD, SiteInfoEndingInSDAdmin)
admin.site.register(SiteInfoEndingInSE, SiteInfoEndingInSEAdmin)
admin.site.register(SiteInfoEndingInSEXY, SiteInfoEndingInSEXYAdmin)
admin.site.register(SiteInfoEndingInSG, SiteInfoEndingInSGAdmin)
admin.site.register(SiteInfoEndingInSI, SiteInfoEndingInSIAdmin)
admin.site.register(SiteInfoEndingInSK, SiteInfoEndingInSKAdmin)
admin.site.register(SiteInfoEndingInSL, SiteInfoEndingInSLAdmin)
admin.site.register(SiteInfoEndingInSM, SiteInfoEndingInSMAdmin)
admin.site.register(SiteInfoEndingInSN, SiteInfoEndingInSNAdmin)
admin.site.register(SiteInfoEndingInSO, SiteInfoEndingInSOAdmin)
admin.site.register(SiteInfoEndingInSR, SiteInfoEndingInSRAdmin)
admin.site.register(SiteInfoEndingInST, SiteInfoEndingInSTAdmin)
admin.site.register(SiteInfoEndingInSU, SiteInfoEndingInSUAdmin)
admin.site.register(SiteInfoEndingInSV, SiteInfoEndingInSVAdmin)
admin.site.register(SiteInfoEndingInSX, SiteInfoEndingInSXAdmin)
admin.site.register(SiteInfoEndingInSY, SiteInfoEndingInSYAdmin)
admin.site.register(SiteInfoEndingInSZ, SiteInfoEndingInSZAdmin)
admin.site.register(SiteInfoEndingInTD, SiteInfoEndingInTDAdmin)
admin.site.register(SiteInfoEndingInTG, SiteInfoEndingInTGAdmin)
admin.site.register(SiteInfoEndingInTH, SiteInfoEndingInTHAdmin)
admin.site.register(SiteInfoEndingInTJ, SiteInfoEndingInTJAdmin)
admin.site.register(SiteInfoEndingInTK, SiteInfoEndingInTKAdmin)
admin.site.register(SiteInfoEndingInTL, SiteInfoEndingInTLAdmin)
admin.site.register(SiteInfoEndingInTM, SiteInfoEndingInTMAdmin)
admin.site.register(SiteInfoEndingInTO, SiteInfoEndingInTOAdmin)
admin.site.register(SiteInfoEndingInTP, SiteInfoEndingInTPAdmin)
admin.site.register(SiteInfoEndingInTR, SiteInfoEndingInTRAdmin)
admin.site.register(SiteInfoEndingInTRAVEL, SiteInfoEndingInTRAVELAdmin)
admin.site.register(SiteInfoEndingInTT, SiteInfoEndingInTTAdmin)
admin.site.register(SiteInfoEndingInTV, SiteInfoEndingInTVAdmin)
admin.site.register(SiteInfoEndingInTW, SiteInfoEndingInTWAdmin)
admin.site.register(SiteInfoEndingInTZ, SiteInfoEndingInTZAdmin)
admin.site.register(SiteInfoEndingInUA, SiteInfoEndingInUAAdmin)
admin.site.register(SiteInfoEndingInUG, SiteInfoEndingInUGAdmin)
admin.site.register(SiteInfoEndingInUK, SiteInfoEndingInUKAdmin)
admin.site.register(SiteInfoEndingInUS, SiteInfoEndingInUSAdmin)
admin.site.register(SiteInfoEndingInUY, SiteInfoEndingInUYAdmin)
admin.site.register(SiteInfoEndingInUZ, SiteInfoEndingInUZAdmin)
admin.site.register(SiteInfoEndingInVA, SiteInfoEndingInVAAdmin)
admin.site.register(SiteInfoEndingInVE, SiteInfoEndingInVEAdmin)
admin.site.register(SiteInfoEndingInVN, SiteInfoEndingInVNAdmin)
admin.site.register(SiteInfoEndingInWF, SiteInfoEndingInWFAdmin)
admin.site.register(SiteInfoEndingInWS, SiteInfoEndingInWSAdmin)
admin.site.register(SiteInfoEndingInXML, SiteInfoEndingInXMLAdmin)
admin.site.register(SiteInfoEndingInXXX, SiteInfoEndingInXXXAdmin)
admin.site.register(SiteInfoEndingInYE, SiteInfoEndingInYEAdmin)
admin.site.register(SiteInfoEndingInYT, SiteInfoEndingInYTAdmin)
admin.site.register(SiteInfoEndingInZA, SiteInfoEndingInZAAdmin)
admin.site.register(SiteInfoEndingInZM, SiteInfoEndingInZMAdmin)
admin.site.register(SiteInfoEndingInZW, SiteInfoEndingInZWAdmin)
admin.site.register(SiteInfoGreekAlphabet, SiteInfoGreekAlphabetAdmin)
admin.site.register(SiteInfoH1GreekAlphabet, SiteInfoH1GreekAlphabetAdmin)
admin.site.register(SiteInfoAfterZ, SiteInfoAfterZAdmin)
admin.site.register(SiteInfoH1AfterZ, SiteInfoH1AfterZAdmin)
admin.site.register(SiteInfoH2AfterZ, SiteInfoH2AfterZAdmin)
admin.site.register(SiteInfoH3AfterZ, SiteInfoH3AfterZAdmin)
admin.site.register(SiteInfoAfterZEndingInAE, SiteInfoAfterZEndingInAEAdmin)
admin.site.register(SiteInfoAfterZEndingInAM, SiteInfoAfterZEndingInAMAdmin)
admin.site.register(SiteInfoAfterZEndingInASIA, SiteInfoAfterZEndingInASIAAdmin)
admin.site.register(SiteInfoAfterZEndingInAZ, SiteInfoAfterZEndingInAZAdmin)
admin.site.register(SiteInfoAfterZEndingInBG, SiteInfoAfterZEndingInBGAdmin)
admin.site.register(SiteInfoAfterZEndingInBH, SiteInfoAfterZEndingInBHAdmin)
admin.site.register(SiteInfoAfterZEndingInBIZ, SiteInfoAfterZEndingInBIZAdmin)
admin.site.register(SiteInfoAfterZEndingInBY, SiteInfoAfterZEndingInBYAdmin)
admin.site.register(SiteInfoAfterZEndingInBZ, SiteInfoAfterZEndingInBZAdmin)
admin.site.register(SiteInfoAfterZEndingInCN, SiteInfoAfterZEndingInCNAdmin)
admin.site.register(SiteInfoAfterZEndingInCOM, SiteInfoAfterZEndingInCOMAdmin)
admin.site.register(SiteInfoAfterZEndingInDZ, SiteInfoAfterZEndingInDZAdmin)
admin.site.register(SiteInfoAfterZEndingInEE, SiteInfoAfterZEndingInEEAdmin)
admin.site.register(SiteInfoAfterZEndingInEG, SiteInfoAfterZEndingInEGAdmin)
admin.site.register(SiteInfoAfterZEndingInFM, SiteInfoAfterZEndingInFMAdmin)
admin.site.register(SiteInfoAfterZEndingInGE, SiteInfoAfterZEndingInGEAdmin)
admin.site.register(SiteInfoAfterZEndingInHK, SiteInfoAfterZEndingInHKAdmin)
admin.site.register(SiteInfoAfterZEndingInIL, SiteInfoAfterZEndingInILAdmin)
admin.site.register(SiteInfoAfterZEndingInIN, SiteInfoAfterZEndingInINAdmin)
admin.site.register(SiteInfoAfterZEndingInINFO, SiteInfoAfterZEndingInINFOAdmin)
admin.site.register(SiteInfoAfterZEndingInIQ, SiteInfoAfterZEndingInIQAdmin)
admin.site.register(SiteInfoAfterZEndingInIR, SiteInfoAfterZEndingInIRAdmin)
admin.site.register(SiteInfoAfterZEndingInJO, SiteInfoAfterZEndingInJOAdmin)
admin.site.register(SiteInfoAfterZEndingInJP, SiteInfoAfterZEndingInJPAdmin)
admin.site.register(SiteInfoAfterZEndingInKG, SiteInfoAfterZEndingInKGAdmin)
admin.site.register(SiteInfoAfterZEndingInKR, SiteInfoAfterZEndingInKRAdmin)
admin.site.register(SiteInfoAfterZEndingInKW, SiteInfoAfterZEndingInKWAdmin)
admin.site.register(SiteInfoAfterZEndingInKZ, SiteInfoAfterZEndingInKZAdmin)
admin.site.register(SiteInfoAfterZEndingInLA, SiteInfoAfterZEndingInLAAdmin)
admin.site.register(SiteInfoAfterZEndingInLB, SiteInfoAfterZEndingInLBAdmin)
admin.site.register(SiteInfoAfterZEndingInLI, SiteInfoAfterZEndingInLIAdmin)
admin.site.register(SiteInfoAfterZEndingInLY, SiteInfoAfterZEndingInLYAdmin)
admin.site.register(SiteInfoAfterZEndingInMA, SiteInfoAfterZEndingInMAAdmin)
admin.site.register(SiteInfoAfterZEndingInMD, SiteInfoAfterZEndingInMDAdmin)
admin.site.register(SiteInfoAfterZEndingInME, SiteInfoAfterZEndingInMEAdmin)
admin.site.register(SiteInfoAfterZEndingInMK, SiteInfoAfterZEndingInMKAdmin)
admin.site.register(SiteInfoAfterZEndingInMOBI, SiteInfoAfterZEndingInMOBIAdmin)
admin.site.register(SiteInfoAfterZEndingInMY, SiteInfoAfterZEndingInMYAdmin)
admin.site.register(SiteInfoAfterZEndingInNET, SiteInfoAfterZEndingInNETAdmin)
admin.site.register(SiteInfoAfterZEndingInOM, SiteInfoAfterZEndingInOMAdmin)
admin.site.register(SiteInfoAfterZEndingInORG, SiteInfoAfterZEndingInORGAdmin)
admin.site.register(SiteInfoAfterZEndingInPRO, SiteInfoAfterZEndingInPROAdmin)
admin.site.register(SiteInfoAfterZEndingInPS, SiteInfoAfterZEndingInPSAdmin)
admin.site.register(SiteInfoAfterZEndingInQA, SiteInfoAfterZEndingInQAAdmin)
admin.site.register(SiteInfoAfterZEndingInRS, SiteInfoAfterZEndingInRSAdmin)
admin.site.register(SiteInfoAfterZEndingInRU, SiteInfoAfterZEndingInRUAdmin)
admin.site.register(SiteInfoAfterZEndingInSA, SiteInfoAfterZEndingInSAAdmin)
admin.site.register(SiteInfoAfterZEndingInSD, SiteInfoAfterZEndingInSDAdmin)
admin.site.register(SiteInfoAfterZEndingInSG, SiteInfoAfterZEndingInSGAdmin)
admin.site.register(SiteInfoAfterZEndingInST, SiteInfoAfterZEndingInSTAdmin)
admin.site.register(SiteInfoAfterZEndingInSU, SiteInfoAfterZEndingInSUAdmin)
admin.site.register(SiteInfoAfterZEndingInSY, SiteInfoAfterZEndingInSYAdmin)
admin.site.register(SiteInfoAfterZEndingInTJ, SiteInfoAfterZEndingInTJAdmin)
admin.site.register(SiteInfoAfterZEndingInTK, SiteInfoAfterZEndingInTKAdmin)
admin.site.register(SiteInfoAfterZEndingInTM, SiteInfoAfterZEndingInTMAdmin)
admin.site.register(SiteInfoAfterZEndingInTN, SiteInfoAfterZEndingInTNAdmin)
admin.site.register(SiteInfoAfterZEndingInTO, SiteInfoAfterZEndingInTOAdmin)
admin.site.register(SiteInfoAfterZEndingInTV, SiteInfoAfterZEndingInTVAdmin)
admin.site.register(SiteInfoAfterZEndingInTW, SiteInfoAfterZEndingInTWAdmin)
admin.site.register(SiteInfoAfterZEndingInUA, SiteInfoAfterZEndingInUAAdmin)
admin.site.register(SiteInfoAfterZEndingInUS, SiteInfoAfterZEndingInUSAdmin)
admin.site.register(SiteInfoAfterZEndingInUZ, SiteInfoAfterZEndingInUZAdmin)
admin.site.register(SiteInfoAfterZEndingInVG, SiteInfoAfterZEndingInVGAdmin)
admin.site.register(SiteInfoAfterZEndingInWS, SiteInfoAfterZEndingInWSAdmin)
admin.site.register(SiteInfoAfterZEndingInYE, SiteInfoAfterZEndingInYEAdmin)
admin.site.register(SiteInfoAfterZEndingInP1AI, SiteInfoAfterZEndingInP1AIAdmin)
admin.site.register(SiteInfoBeforeZero, SiteInfoBeforeZeroAdmin)
admin.site.register(SiteInfoH1BeforeZero, SiteInfoH1BeforeZeroAdmin)
admin.site.register(SiteInfoH2BeforeZero, SiteInfoH2BeforeZeroAdmin)
admin.site.register(SiteInfoH3BeforeZero, SiteInfoH3BeforeZeroAdmin)
admin.site.register(SiteInfo_af, SiteInfoAdmin)
admin.site.register(SiteInfo_ak, SiteInfoAdmin)
admin.site.register(SiteInfo_bm, SiteInfoAdmin)
admin.site.register(SiteInfo_br, SiteInfoAdmin)
admin.site.register(SiteInfo_ca, SiteInfoAdmin)
admin.site.register(SiteInfo_cs, SiteInfoAdmin)
admin.site.register(SiteInfo_cy, SiteInfoAdmin)
admin.site.register(SiteInfo_da, SiteInfoAdmin)
admin.site.register(SiteInfo_de, SiteInfoAdmin)
admin.site.register(SiteInfo_ee, SiteInfoAdmin)
admin.site.register(SiteInfo_el, SiteInfoAdmin)
admin.site.register(SiteInfo_eo, SiteInfoAdmin)
admin.site.register(SiteInfo_es, SiteInfoAdmin)
admin.site.register(SiteInfo_et, SiteInfoAdmin)
admin.site.register(SiteInfo_eu, SiteInfoAdmin)
admin.site.register(SiteInfo_ff, SiteInfoAdmin)
admin.site.register(SiteInfo_fi, SiteInfoAdmin)
admin.site.register(SiteInfo_fo, SiteInfoAdmin)
admin.site.register(SiteInfo_fr, SiteInfoAdmin)
admin.site.register(SiteInfo_fy, SiteInfoAdmin)
admin.site.register(SiteInfo_gl, SiteInfoAdmin)
admin.site.register(SiteInfo_ha, SiteInfoAdmin)
admin.site.register(SiteInfo_hr, SiteInfoAdmin)
admin.site.register(SiteInfo_hu, SiteInfoAdmin)
admin.site.register(SiteInfo_ig, SiteInfoAdmin)
admin.site.register(SiteInfo_is, SiteInfoAdmin)
admin.site.register(SiteInfo_it, SiteInfoAdmin)
admin.site.register(SiteInfo_kg, SiteInfoAdmin)
admin.site.register(SiteInfo_ki, SiteInfoAdmin)
admin.site.register(SiteInfo_la, SiteInfoAdmin)
admin.site.register(SiteInfo_lg, SiteInfoAdmin)
admin.site.register(SiteInfo_ln, SiteInfoAdmin)
admin.site.register(SiteInfo_lt, SiteInfoAdmin)
admin.site.register(SiteInfo_lv, SiteInfoAdmin)
admin.site.register(SiteInfo_nap, SiteInfoAdmin)
admin.site.register(SiteInfo_nl, SiteInfoAdmin)
admin.site.register(SiteInfo_no, SiteInfoAdmin)
admin.site.register(SiteInfo_nso, SiteInfoAdmin)
admin.site.register(SiteInfo_ny, SiteInfoAdmin)
admin.site.register(SiteInfo_oc, SiteInfoAdmin)
admin.site.register(SiteInfo_om, SiteInfoAdmin)
admin.site.register(SiteInfo_pl, SiteInfoAdmin)
admin.site.register(SiteInfo_pms, SiteInfoAdmin)
admin.site.register(SiteInfo_pt, SiteInfoAdmin)
admin.site.register(SiteInfo_rn, SiteInfoAdmin)
admin.site.register(SiteInfo_ro, SiteInfoAdmin)
admin.site.register(SiteInfo_rw, SiteInfoAdmin)
admin.site.register(SiteInfo_sc, SiteInfoAdmin)
admin.site.register(SiteInfo_scn, SiteInfoAdmin)
admin.site.register(SiteInfo_sk, SiteInfoAdmin)
admin.site.register(SiteInfo_sl, SiteInfoAdmin)
admin.site.register(SiteInfo_sn, SiteInfoAdmin)
admin.site.register(SiteInfo_so, SiteInfoAdmin)
admin.site.register(SiteInfo_ss, SiteInfoAdmin)
admin.site.register(SiteInfo_st, SiteInfoAdmin)
admin.site.register(SiteInfo_sv, SiteInfoAdmin)
admin.site.register(SiteInfo_sw, SiteInfoAdmin)
admin.site.register(SiteInfo_tn, SiteInfoAdmin)
admin.site.register(SiteInfo_tr, SiteInfoAdmin)
admin.site.register(SiteInfo_ts, SiteInfoAdmin)
admin.site.register(SiteInfo_ve, SiteInfoAdmin)
admin.site.register(SiteInfo_vec, SiteInfoAdmin)
admin.site.register(SiteInfo_wo, SiteInfoAdmin)
admin.site.register(SiteInfo_xh, SiteInfoAdmin)
admin.site.register(SiteInfo_yo, SiteInfoAdmin)
admin.site.register(SiteInfo_zu, SiteInfoAdmin)
admin.site.register(DomainInfo, DomainInfoAdmin)
admin.site.register(SearchLog, SearchLogAdmin)
admin.site.register(SearchLog_af, SearchLogAdmin)
admin.site.register(SearchLog_ak, SearchLogAdmin)
admin.site.register(SearchLog_bm, SearchLogAdmin)
admin.site.register(SearchLog_br, SearchLogAdmin)
admin.site.register(SearchLog_ca, SearchLogAdmin)
admin.site.register(SearchLog_cs, SearchLogAdmin)
admin.site.register(SearchLog_cy, SearchLogAdmin)
admin.site.register(SearchLog_da, SearchLogAdmin)
admin.site.register(SearchLog_de, SearchLogAdmin)
admin.site.register(SearchLog_ee, SearchLogAdmin)
admin.site.register(SearchLog_el, SearchLogAdmin)
admin.site.register(SearchLog_eo, SearchLogAdmin)
admin.site.register(SearchLog_es, SearchLogAdmin)
admin.site.register(SearchLog_et, SearchLogAdmin)
admin.site.register(SearchLog_eu, SearchLogAdmin)
admin.site.register(SearchLog_ff, SearchLogAdmin)
admin.site.register(SearchLog_fi, SearchLogAdmin)
admin.site.register(SearchLog_fo, SearchLogAdmin)
admin.site.register(SearchLog_fr, SearchLogAdmin)
admin.site.register(SearchLog_fy, SearchLogAdmin)
admin.site.register(SearchLog_gl, SearchLogAdmin)
admin.site.register(SearchLog_ha, SearchLogAdmin)
admin.site.register(SearchLog_hr, SearchLogAdmin)
admin.site.register(SearchLog_hu, SearchLogAdmin)
admin.site.register(SearchLog_ig, SearchLogAdmin)
admin.site.register(SearchLog_is, SearchLogAdmin)
admin.site.register(SearchLog_it, SearchLogAdmin)
admin.site.register(SearchLog_kg, SearchLogAdmin)
admin.site.register(SearchLog_ki, SearchLogAdmin)
admin.site.register(SearchLog_la, SearchLogAdmin)
admin.site.register(SearchLog_lg, SearchLogAdmin)
admin.site.register(SearchLog_ln, SearchLogAdmin)
admin.site.register(SearchLog_lt, SearchLogAdmin)
admin.site.register(SearchLog_lv, SearchLogAdmin)
admin.site.register(SearchLog_nap, SearchLogAdmin)
admin.site.register(SearchLog_nl, SearchLogAdmin)
admin.site.register(SearchLog_no, SearchLogAdmin)
admin.site.register(SearchLog_nso, SearchLogAdmin)
admin.site.register(SearchLog_ny, SearchLogAdmin)
admin.site.register(SearchLog_oc, SearchLogAdmin)
admin.site.register(SearchLog_om, SearchLogAdmin)
admin.site.register(SearchLog_pl, SearchLogAdmin)
admin.site.register(SearchLog_pms, SearchLogAdmin)
admin.site.register(SearchLog_pt, SearchLogAdmin)
admin.site.register(SearchLog_rn, SearchLogAdmin)
admin.site.register(SearchLog_ro, SearchLogAdmin)
admin.site.register(SearchLog_rw, SearchLogAdmin)
admin.site.register(SearchLog_sc, SearchLogAdmin)
admin.site.register(SearchLog_scn, SearchLogAdmin)
admin.site.register(SearchLog_sk, SearchLogAdmin)
admin.site.register(SearchLog_sl, SearchLogAdmin)
admin.site.register(SearchLog_sn, SearchLogAdmin)
admin.site.register(SearchLog_so, SearchLogAdmin)
admin.site.register(SearchLog_ss, SearchLogAdmin)
admin.site.register(SearchLog_st, SearchLogAdmin)
admin.site.register(SearchLog_sv, SearchLogAdmin)
admin.site.register(SearchLog_sw, SearchLogAdmin)
admin.site.register(SearchLog_tn, SearchLogAdmin)
admin.site.register(SearchLog_tr, SearchLogAdmin)
admin.site.register(SearchLog_ts, SearchLogAdmin)
admin.site.register(SearchLog_ve, SearchLogAdmin)
admin.site.register(SearchLog_vec, SearchLogAdmin)
admin.site.register(SearchLog_wo, SearchLogAdmin)
admin.site.register(SearchLog_xh, SearchLogAdmin)
admin.site.register(SearchLog_yo, SearchLogAdmin)
admin.site.register(SearchLog_zu, SearchLogAdmin)
admin.site.register(PendingIndex, PendingIndexAdmin)
admin.site.register(PendingIndex_af, PendingIndexAdmin)
admin.site.register(PendingIndex_ak, PendingIndexAdmin)
admin.site.register(PendingIndex_bm, PendingIndexAdmin)
admin.site.register(PendingIndex_br, PendingIndexAdmin)
admin.site.register(PendingIndex_ca, PendingIndexAdmin)
admin.site.register(PendingIndex_cs, PendingIndexAdmin)
admin.site.register(PendingIndex_cy, PendingIndexAdmin)
admin.site.register(PendingIndex_da, PendingIndexAdmin)
admin.site.register(PendingIndex_de, PendingIndexAdmin)
admin.site.register(PendingIndex_ee, PendingIndexAdmin)
admin.site.register(PendingIndex_el, PendingIndexAdmin)
admin.site.register(PendingIndex_eo, PendingIndexAdmin)
admin.site.register(PendingIndex_es, PendingIndexAdmin)
admin.site.register(PendingIndex_et, PendingIndexAdmin)
admin.site.register(PendingIndex_eu, PendingIndexAdmin)
admin.site.register(PendingIndex_ff, PendingIndexAdmin)
admin.site.register(PendingIndex_fi, PendingIndexAdmin)
admin.site.register(PendingIndex_fo, PendingIndexAdmin)
admin.site.register(PendingIndex_fr, PendingIndexAdmin)
admin.site.register(PendingIndex_fy, PendingIndexAdmin)
admin.site.register(PendingIndex_gl, PendingIndexAdmin)
admin.site.register(PendingIndex_ha, PendingIndexAdmin)
admin.site.register(PendingIndex_hr, PendingIndexAdmin)
admin.site.register(PendingIndex_hu, PendingIndexAdmin)
admin.site.register(PendingIndex_ig, PendingIndexAdmin)
admin.site.register(PendingIndex_is, PendingIndexAdmin)
admin.site.register(PendingIndex_it, PendingIndexAdmin)
admin.site.register(PendingIndex_kg, PendingIndexAdmin)
admin.site.register(PendingIndex_ki, PendingIndexAdmin)
admin.site.register(PendingIndex_la, PendingIndexAdmin)
admin.site.register(PendingIndex_lg, PendingIndexAdmin)
admin.site.register(PendingIndex_ln, PendingIndexAdmin)
admin.site.register(PendingIndex_lt, PendingIndexAdmin)
admin.site.register(PendingIndex_lv, PendingIndexAdmin)
admin.site.register(PendingIndex_nap, PendingIndexAdmin)
admin.site.register(PendingIndex_nl, PendingIndexAdmin)
admin.site.register(PendingIndex_no, PendingIndexAdmin)
admin.site.register(PendingIndex_nso, PendingIndexAdmin)
admin.site.register(PendingIndex_ny, PendingIndexAdmin)
admin.site.register(PendingIndex_oc, PendingIndexAdmin)
admin.site.register(PendingIndex_om, PendingIndexAdmin)
admin.site.register(PendingIndex_pl, PendingIndexAdmin)
admin.site.register(PendingIndex_pms, PendingIndexAdmin)
admin.site.register(PendingIndex_pt, PendingIndexAdmin)
admin.site.register(PendingIndex_rn, PendingIndexAdmin)
admin.site.register(PendingIndex_ro, PendingIndexAdmin)
admin.site.register(PendingIndex_rw, PendingIndexAdmin)
admin.site.register(PendingIndex_sc, PendingIndexAdmin)
admin.site.register(PendingIndex_scn, PendingIndexAdmin)
admin.site.register(PendingIndex_sk, PendingIndexAdmin)
admin.site.register(PendingIndex_sl, PendingIndexAdmin)
admin.site.register(PendingIndex_sn, PendingIndexAdmin)
admin.site.register(PendingIndex_so, PendingIndexAdmin)
admin.site.register(PendingIndex_ss, PendingIndexAdmin)
admin.site.register(PendingIndex_st, PendingIndexAdmin)
admin.site.register(PendingIndex_sv, PendingIndexAdmin)
admin.site.register(PendingIndex_sw, PendingIndexAdmin)
admin.site.register(PendingIndex_tn, PendingIndexAdmin)
admin.site.register(PendingIndex_tr, PendingIndexAdmin)
admin.site.register(PendingIndex_ts, PendingIndexAdmin)
admin.site.register(PendingIndex_ve, PendingIndexAdmin)
admin.site.register(PendingIndex_vec, PendingIndexAdmin)
admin.site.register(PendingIndex_wo, PendingIndexAdmin)
admin.site.register(PendingIndex_xh, PendingIndexAdmin)
admin.site.register(PendingIndex_yo, PendingIndexAdmin)
admin.site.register(PendingIndex_zu, PendingIndexAdmin)
admin.site.register(IndexTerm, EnglishIndexTermAdmin)
admin.site.register(IndexTerm_af, IndexTermAdmin)
admin.site.register(IndexTerm_ak, IndexTermAdmin)
admin.site.register(IndexTerm_bm, IndexTermAdmin)
admin.site.register(IndexTerm_br, IndexTermAdmin)
admin.site.register(IndexTerm_ca, IndexTermAdmin)
admin.site.register(IndexTerm_cs, IndexTermAdmin)
admin.site.register(IndexTerm_cy, IndexTermAdmin)
admin.site.register(IndexTerm_da, IndexTermAdmin)
admin.site.register(IndexTerm_de, IndexTermAdmin)
admin.site.register(IndexTerm_ee, IndexTermAdmin)
admin.site.register(IndexTerm_el, IndexTermAdmin)
admin.site.register(IndexTerm_eo, IndexTermAdmin)
admin.site.register(IndexTerm_es, IndexTermAdmin)
admin.site.register(IndexTerm_et, IndexTermAdmin)
admin.site.register(IndexTerm_eu, IndexTermAdmin)
admin.site.register(IndexTerm_ff, IndexTermAdmin)
admin.site.register(IndexTerm_fi, IndexTermAdmin)
admin.site.register(IndexTerm_fo, IndexTermAdmin)
admin.site.register(IndexTerm_fr, IndexTermAdmin)
admin.site.register(IndexTerm_fy, IndexTermAdmin)
admin.site.register(IndexTerm_gl, IndexTermAdmin)
admin.site.register(IndexTerm_ha, IndexTermAdmin)
admin.site.register(IndexTerm_hr, IndexTermAdmin)
admin.site.register(IndexTerm_hu, IndexTermAdmin)
admin.site.register(IndexTerm_ig, IndexTermAdmin)
admin.site.register(IndexTerm_is, IndexTermAdmin)
admin.site.register(IndexTerm_it, IndexTermAdmin)
admin.site.register(IndexTerm_kg, IndexTermAdmin)
admin.site.register(IndexTerm_ki, IndexTermAdmin)
admin.site.register(IndexTerm_la, IndexTermAdmin)
admin.site.register(IndexTerm_lg, IndexTermAdmin)
admin.site.register(IndexTerm_ln, IndexTermAdmin)
admin.site.register(IndexTerm_lt, IndexTermAdmin)
admin.site.register(IndexTerm_lv, IndexTermAdmin)
admin.site.register(IndexTerm_nap, IndexTermAdmin)
admin.site.register(IndexTerm_nl, IndexTermAdmin)
admin.site.register(IndexTerm_no, IndexTermAdmin)
admin.site.register(IndexTerm_nso, IndexTermAdmin)
admin.site.register(IndexTerm_ny, IndexTermAdmin)
admin.site.register(IndexTerm_oc, IndexTermAdmin)
admin.site.register(IndexTerm_om, IndexTermAdmin)
admin.site.register(IndexTerm_pl, IndexTermAdmin)
admin.site.register(IndexTerm_pms, IndexTermAdmin)
admin.site.register(IndexTerm_pt, IndexTermAdmin)
admin.site.register(IndexTerm_rn, IndexTermAdmin)
admin.site.register(IndexTerm_ro, IndexTermAdmin)
admin.site.register(IndexTerm_rw, IndexTermAdmin)
admin.site.register(IndexTerm_sc, IndexTermAdmin)
admin.site.register(IndexTerm_scn, IndexTermAdmin)
admin.site.register(IndexTerm_sk, IndexTermAdmin)
admin.site.register(IndexTerm_sl, IndexTermAdmin)
admin.site.register(IndexTerm_sn, IndexTermAdmin)
admin.site.register(IndexTerm_so, IndexTermAdmin)
admin.site.register(IndexTerm_ss, IndexTermAdmin)
admin.site.register(IndexTerm_st, IndexTermAdmin)
admin.site.register(IndexTerm_sv, IndexTermAdmin)
admin.site.register(IndexTerm_sw, IndexTermAdmin)
admin.site.register(IndexTerm_tn, IndexTermAdmin)
admin.site.register(IndexTerm_tr, IndexTermAdmin)
admin.site.register(IndexTerm_ts, IndexTermAdmin)
admin.site.register(IndexTerm_ve, IndexTermAdmin)
admin.site.register(IndexTerm_vec, IndexTermAdmin)
admin.site.register(IndexTerm_wo, IndexTermAdmin)
admin.site.register(IndexTerm_xh, IndexTermAdmin)
admin.site.register(IndexTerm_yo, IndexTermAdmin)
admin.site.register(IndexTerm_zu, IndexTermAdmin)
admin.site.register(FeedbackItem, FeedbackItemAdmin)
admin.site.register(ChangelogItem)
admin.site.register(DomainSuffix)
admin.site.register(IPAddress, IPAddressAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(IndexStats)
admin.site.register(MonthlySearchReport, SearchReportAdmin)
admin.site.register(BadQuery, BadQueryAdmin)
admin.site.register(QueryParameter, QueryParameterAdmin)
admin.site.register(PageLink)
admin.site.register(PageIFrame)
admin.site.register(PageJavaScript)
admin.site.register(DMCANotice, DMCANoticeAdmin)
admin.site.register(DomainSearchLog, SearchLogAdmin)
admin.site.register(NewsSite)
admin.site.register(AutoComplete, AutoCompleteAdmin)
admin.site.register(AutoComplete_af, AutoCompleteAdmin)
admin.site.register(AutoComplete_ak, AutoCompleteAdmin)
admin.site.register(AutoComplete_bm, AutoCompleteAdmin)
admin.site.register(AutoComplete_br, AutoCompleteAdmin)
admin.site.register(AutoComplete_ca, AutoCompleteAdmin)
admin.site.register(AutoComplete_cs, AutoCompleteAdmin)
admin.site.register(AutoComplete_cy, AutoCompleteAdmin)
admin.site.register(AutoComplete_da, AutoCompleteAdmin)
admin.site.register(AutoComplete_de, AutoCompleteAdmin)
admin.site.register(AutoComplete_ee, AutoCompleteAdmin)
admin.site.register(AutoComplete_el, AutoCompleteAdmin)
admin.site.register(AutoComplete_eo, AutoCompleteAdmin)
admin.site.register(AutoComplete_es, AutoCompleteAdmin)
admin.site.register(AutoComplete_et, AutoCompleteAdmin)
admin.site.register(AutoComplete_eu, AutoCompleteAdmin)
admin.site.register(AutoComplete_ff, AutoCompleteAdmin)
admin.site.register(AutoComplete_fi, AutoCompleteAdmin)
admin.site.register(AutoComplete_fo, AutoCompleteAdmin)
admin.site.register(AutoComplete_fr, AutoCompleteAdmin)
admin.site.register(AutoComplete_fy, AutoCompleteAdmin)
admin.site.register(AutoComplete_gl, AutoCompleteAdmin)
admin.site.register(AutoComplete_ha, AutoCompleteAdmin)
admin.site.register(AutoComplete_hr, AutoCompleteAdmin)
admin.site.register(AutoComplete_hu, AutoCompleteAdmin)
admin.site.register(AutoComplete_ig, AutoCompleteAdmin)
admin.site.register(AutoComplete_is, AutoCompleteAdmin)
admin.site.register(AutoComplete_it, AutoCompleteAdmin)
admin.site.register(AutoComplete_kg, AutoCompleteAdmin)
admin.site.register(AutoComplete_ki, AutoCompleteAdmin)
admin.site.register(AutoComplete_la, AutoCompleteAdmin)
admin.site.register(AutoComplete_lg, AutoCompleteAdmin)
admin.site.register(AutoComplete_ln, AutoCompleteAdmin)
admin.site.register(AutoComplete_lt, AutoCompleteAdmin)
admin.site.register(AutoComplete_lv, AutoCompleteAdmin)
admin.site.register(AutoComplete_nap, AutoCompleteAdmin)
admin.site.register(AutoComplete_nl, AutoCompleteAdmin)
admin.site.register(AutoComplete_no, AutoCompleteAdmin)
admin.site.register(AutoComplete_nso, AutoCompleteAdmin)
admin.site.register(AutoComplete_ny, AutoCompleteAdmin)
admin.site.register(AutoComplete_oc, AutoCompleteAdmin)
admin.site.register(AutoComplete_om, AutoCompleteAdmin)
admin.site.register(AutoComplete_pl, AutoCompleteAdmin)
admin.site.register(AutoComplete_pms, AutoCompleteAdmin)
admin.site.register(AutoComplete_pt, AutoCompleteAdmin)
admin.site.register(AutoComplete_rn, AutoCompleteAdmin)
admin.site.register(AutoComplete_ro, AutoCompleteAdmin)
admin.site.register(AutoComplete_rw, AutoCompleteAdmin)
admin.site.register(AutoComplete_sc, AutoCompleteAdmin)
admin.site.register(AutoComplete_scn, AutoCompleteAdmin)
admin.site.register(AutoComplete_sk, AutoCompleteAdmin)
admin.site.register(AutoComplete_sl, AutoCompleteAdmin)
admin.site.register(AutoComplete_sn, AutoCompleteAdmin)
admin.site.register(AutoComplete_so, AutoCompleteAdmin)
admin.site.register(AutoComplete_ss, AutoCompleteAdmin)
admin.site.register(AutoComplete_st, AutoCompleteAdmin)
admin.site.register(AutoComplete_sv, AutoCompleteAdmin)
admin.site.register(AutoComplete_sw, AutoCompleteAdmin)
admin.site.register(AutoComplete_tn, AutoCompleteAdmin)
admin.site.register(AutoComplete_tr, AutoCompleteAdmin)
admin.site.register(AutoComplete_ts, AutoCompleteAdmin)
admin.site.register(AutoComplete_ve, AutoCompleteAdmin)
admin.site.register(AutoComplete_vec, AutoCompleteAdmin)
admin.site.register(AutoComplete_wo, AutoCompleteAdmin)
admin.site.register(AutoComplete_xh, AutoCompleteAdmin)
admin.site.register(AutoComplete_yo, AutoCompleteAdmin)
admin.site.register(AutoComplete_zu, AutoCompleteAdmin)
admin.site.register(ResultClick, ResultClickAdmin)
admin.site.register(ResultClick_af, ResultClickAdmin)
admin.site.register(ResultClick_ak, ResultClickAdmin)
admin.site.register(ResultClick_bm, ResultClickAdmin)
admin.site.register(ResultClick_br, ResultClickAdmin)
admin.site.register(ResultClick_ca, ResultClickAdmin)
admin.site.register(ResultClick_cs, ResultClickAdmin)
admin.site.register(ResultClick_cy, ResultClickAdmin)
admin.site.register(ResultClick_da, ResultClickAdmin)
admin.site.register(ResultClick_de, ResultClickAdmin)
admin.site.register(ResultClick_ee, ResultClickAdmin)
admin.site.register(ResultClick_el, ResultClickAdmin)
admin.site.register(ResultClick_eo, ResultClickAdmin)
admin.site.register(ResultClick_es, ResultClickAdmin)
admin.site.register(ResultClick_et, ResultClickAdmin)
admin.site.register(ResultClick_eu, ResultClickAdmin)
admin.site.register(ResultClick_ff, ResultClickAdmin)
admin.site.register(ResultClick_fi, ResultClickAdmin)
admin.site.register(ResultClick_fo, ResultClickAdmin)
admin.site.register(ResultClick_fr, ResultClickAdmin)
admin.site.register(ResultClick_fy, ResultClickAdmin)
admin.site.register(ResultClick_gl, ResultClickAdmin)
admin.site.register(ResultClick_ha, ResultClickAdmin)
admin.site.register(ResultClick_hr, ResultClickAdmin)
admin.site.register(ResultClick_hu, ResultClickAdmin)
admin.site.register(ResultClick_ig, ResultClickAdmin)
admin.site.register(ResultClick_is, ResultClickAdmin)
admin.site.register(ResultClick_it, ResultClickAdmin)
admin.site.register(ResultClick_kg, ResultClickAdmin)
admin.site.register(ResultClick_ki, ResultClickAdmin)
admin.site.register(ResultClick_la, ResultClickAdmin)
admin.site.register(ResultClick_lg, ResultClickAdmin)
admin.site.register(ResultClick_ln, ResultClickAdmin)
admin.site.register(ResultClick_lt, ResultClickAdmin)
admin.site.register(ResultClick_lv, ResultClickAdmin)
admin.site.register(ResultClick_nap, ResultClickAdmin)
admin.site.register(ResultClick_nl, ResultClickAdmin)
admin.site.register(ResultClick_no, ResultClickAdmin)
admin.site.register(ResultClick_nso, ResultClickAdmin)
admin.site.register(ResultClick_ny, ResultClickAdmin)
admin.site.register(ResultClick_oc, ResultClickAdmin)
admin.site.register(ResultClick_om, ResultClickAdmin)
admin.site.register(ResultClick_pl, ResultClickAdmin)
admin.site.register(ResultClick_pms, ResultClickAdmin)
admin.site.register(ResultClick_pt, ResultClickAdmin)
admin.site.register(ResultClick_rn, ResultClickAdmin)
admin.site.register(ResultClick_ro, ResultClickAdmin)
admin.site.register(ResultClick_rw, ResultClickAdmin)
admin.site.register(ResultClick_sc, ResultClickAdmin)
admin.site.register(ResultClick_scn, ResultClickAdmin)
admin.site.register(ResultClick_sk, ResultClickAdmin)
admin.site.register(ResultClick_sl, ResultClickAdmin)
admin.site.register(ResultClick_sn, ResultClickAdmin)
admin.site.register(ResultClick_so, ResultClickAdmin)
admin.site.register(ResultClick_ss, ResultClickAdmin)
admin.site.register(ResultClick_st, ResultClickAdmin)
admin.site.register(ResultClick_sv, ResultClickAdmin)
admin.site.register(ResultClick_sw, ResultClickAdmin)
admin.site.register(ResultClick_tn, ResultClickAdmin)
admin.site.register(ResultClick_tr, ResultClickAdmin)
admin.site.register(ResultClick_ts, ResultClickAdmin)
admin.site.register(ResultClick_ve, ResultClickAdmin)
admin.site.register(ResultClick_vec, ResultClickAdmin)
admin.site.register(ResultClick_wo, ResultClickAdmin)
admin.site.register(ResultClick_xh, ResultClickAdmin)
admin.site.register(ResultClick_yo, ResultClickAdmin)
admin.site.register(ResultClick_zu, ResultClickAdmin)
admin.site.register(APISubscription, APISubscriptionAdmin)
admin.site.register(APIUsage, APIUsageAdmin)
