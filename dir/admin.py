# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import IntegrityError, models
from dir.models import *
from dir.crawler import CrawlSingleUrl
from dir.utils import MoveSiteTo, RemoveURLsForDomain, MarkURLContentsAsSpam, SetDomainLanguage, SetDomainInfixLanguage, GenerateSearchReport, PornBlock, RequeueRankedKeywordsForDomain, CalculateDomainSuffixStats
from urllib.parse import urlparse
from dir.indexer import BuildIndexForTerm
from django.core.exceptions import ObjectDoesNotExist


def LanguageBlock(siteinfo, language=None):
    parsedurl = urlparse(siteinfo.url)
    # If you try to language block an unblockable domain (i.e. YouTube), it just deletes the URL
    # and continues on its way.
    try:
        domain = DomainInfo.objects.get(url=parsedurl.netloc)
        if domain.is_unblockable:
            siteinfo.delete()
            return
    except ObjectDoesNotExist:
        # Always create domain info if the domain doesn't exist yet.
        domain = DomainInfo()
        domain.url = parsedurl.netloc
        domain.save()
    try:
        BlockedSite.objects.get(url=parsedurl.netloc)
        # If the domain is already blocked, the URL must have been added erroneously.
        # in that case, just delete it.
        RemoveURLsForDomain(siteinfo.rooturl)
    except ObjectDoesNotExist:
        site = BlockedSite()
        site.url = parsedurl.netloc
        # (34, 'Unindexed Language - Azerbaijani'),
        if language == 'az':
            site.reason = 34
        # (32, 'Unindexed Language - Georgian'),
        elif language == 'ge':
            site.reason = 32
        # (20, 'Unindexed Language - Arabic or Farsi'),
        elif language == 'ar':
            site.reason = 20
        # (21, 'Unindexed Language - Chinese'),
        elif language == 'zh':
            site.reason = 21
        # (31, 'Unindexed Language - Georgian'),
        elif language == 'ge':
            site.reason = 31
        # (22, 'Unindexed Language - Hebrew'),
        elif language == 'he':
            site.reason = 22
        # (23, 'Unindexed Language - Hindi'),
        elif language == 'hi':
            site.reason = 23
        # (24, 'Unindexed Language - Indonesian or Similar'),
        elif language == 'in':
            site.reason = 24
        # (25, 'Unindexed Language - Japanese'),
        elif language == 'ja':
            site.reason = 25
        # (26, 'Unindexed Language - Khmer'),
        elif language == 'km':
            site.reason = 26
        # (27, 'Unindexed Language - Korean'),
        elif language == 'ko':
            site.reason = 27
        # (28, 'Unindexed Language - Russian or Other Cyrillic'),
        elif language == 'ru':
            site.reason = 28
        # (33, 'Unindexed Language - Serbian'),
        elif language == 'sr':
            site.reason = 30
        # (30, 'Unindexed Language - Thai'),
        elif language == 'th':
            site.reason = 30
        # (29, 'Unindexed Language - Vietnamese'),
        elif language == 'vn':
            site.reason = 29
        # Generic "unindexed language" reason.
        else:
            site.reason = 8
        try:
            site.save()
        except IntegrityError:
            # The only reason we would get an integrity error is if we
            # violate the unique key constraint of the database. If we
            # did that, it means that the site is already in blocked and we
            # can safely move on.
            connection._rollback()
    RequeueRankedKeywordsForDomain(parsedurl.netloc)

    if language is not None:
        domain.language_association = language
        domain.save()


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
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag')
    search_fields = ('rooturl',)
    show_full_result_count = False
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '132'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 132})},
    }

    def block_domain_wrong_language(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item)

    block_domain_wrong_language.short_description = "Block the selected domains due to unindexed language."

    def block_domain_language_am(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'am')

    block_domain_language_am.short_description = "Block the selected domains (Armenian language)."

    def block_domain_language_ar(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'ar')

    block_domain_language_ar.short_description = "Block the selected domains (Arabic/Farsi language)."

    def block_domain_language_az(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'az')

    block_domain_language_az.short_description = "Block the selected domains (Azerbaijani language)."

    def block_domain_language_cn(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'zh')

    block_domain_language_cn.short_description = "Block the selected domains (Chinese language)."

    def block_domain_language_ge(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'ge')

    block_domain_language_ge.short_description = "Block the selected domains (Georgian language)."

    def block_domain_language_hi(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'hi')

    block_domain_language_hi.short_description = "Block the selected domains (Hindi language)."

    def block_domain_language_il(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'he')

    block_domain_language_il.short_description = "Block the selected domains (Hebrew language)."

    def block_domain_language_km(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'km')

    block_domain_language_km.short_description = "Block the selected domains (Khmer language)."

    def block_domain_language_in(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'in')

    block_domain_language_in.short_description = "Block the selected domains (Indonesian or similar language)."

    def block_domain_language_ja(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'ja')

    block_domain_language_ja.short_description = "Block the selected domains (Japanese language)."

    def block_domain_language_ko(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'ko')

    block_domain_language_ko.short_description = "Block the selected domains (Korean language)."

    def block_domain_language_ru(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'ru')

    block_domain_language_ru.short_description = "Block the selected domains (Russian language)."

    def block_domain_language_sr(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'sr')

    block_domain_language_sr.short_description = "Block the selected domains (Serbian language)."

    def block_domain_language_th(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'th')

    block_domain_language_th.short_description = "Block the selected domains (Thai language)."

    def block_domain_language_vn(modeladmin, request, queryset):
        for item in queryset:
            LanguageBlock(item, 'vn')

    block_domain_language_vn.short_description = "Block the selected domains (Vietnamese language)."

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
                BlockedSite.objects.get(url=parsedurl.netloc)
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
                BlockedSite.objects.get(url=parsedurl.netloc)
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
                BlockedSite.objects.get(url=parsedurl.netloc)
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
                BlockedSite.objects.get(url=parsedurl.netloc)
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
                BlockedSite.objects.get(url=parsedurl.netloc)
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
                BlockedSite.objects.get(url=parsedurl.netloc)
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
                BlockedSite.objects.get(url=parsedurl.netloc)
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

    def move_to_aragonese(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'an')

    move_to_aragonese.short_description = "Move these to Aragonese."

    def move_to_basque(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'eu')

    move_to_basque.short_description = "Move these to Basque."

    def move_to_catalan(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ca')

    move_to_catalan.short_description = "Move these to Catalan."

    def move_to_czech(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'cs')

    move_to_czech.short_description = "Move these to Czech."

    def move_to_croatian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'hr')

    move_to_croatian.short_description = "Move these to Croatian."

    def move_to_dutch(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'nl')

    move_to_dutch.short_description = "Move these to Dutch."

    def move_to_english(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'en')

    move_to_english.short_description = "Move these to English."

    def move_to_estonian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'et')

    move_to_estonian.short_description = "Move these to Estonian."

    def move_to_finnish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'fi')

    move_to_finnish.short_description = "Move these to Finnish."

    def move_to_french(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'fr')

    move_to_french.short_description = "Move these to French."

    def move_to_galician(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'gl')

    move_to_galician.short_description = "Move these to Galician."

    def move_to_german(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'de')

    move_to_german.short_description = "Move these to German."

    def move_to_greek(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'el')

    move_to_greek.short_description = "Move these to Greek."

    def move_to_hausa(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ha')

    move_to_hausa.short_description = "Move these to Hausa."

    def move_to_hungarian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'hu')

    move_to_hungarian.short_description = "Move these to Hungarian."

    def move_to_italian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'it')

    move_to_italian.short_description = "Move these to Italian."

    def move_to_latvian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'lv')

    move_to_latvian.short_description = "Move these to Latvian."

    def move_to_lithuanian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'lt')

    move_to_lithuanian.short_description = "Move these to Lithuanian."

    def move_to_norwegian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'no')

    move_to_norwegian.short_description = "Move these to Norwegian."

    def move_to_polish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'pl')

    move_to_polish.short_description = "Move these to Polish."

    def move_to_portuguese(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'pt')

    move_to_portuguese.short_description = "Move these to Portuguese."

    def move_to_romanian(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'ro')

    move_to_romanian.short_description = "Move these to Romanian."

    def move_to_rwandan(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'rw')

    move_to_rwandan.short_description = "Move these to Rwandan."

    def move_to_shona(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sn')

    move_to_shona.short_description = "Move these to Shona."

    def move_to_slovene(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sl')

    move_to_slovene.short_description = "Move these to Slovene."

    def move_to_somali(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'so')

    move_to_somali.short_description = "Move these to Somali."

    def move_to_spanish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'es')

    move_to_spanish.short_description = "Move these to Spanish."

    def move_to_swahili(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sw')

    move_to_swahili.short_description = "Move these to Swahili."

    def move_to_swedish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'sv')

    move_to_swedish.short_description = "Move these to Swedish."

    def move_to_turkish(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'tr')

    move_to_turkish.short_description = "Move these to Turkish."

    def move_to_welsh(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'cy')

    move_to_welsh.short_description = "Move these to Welsh."

    def move_to_wolof(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'wo')

    move_to_wolof.short_description = "Move these to Wolof."

    def move_to_yoruba(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'yo')

    move_to_yoruba.short_description = "Move these to Yoruba."

    def move_to_xhosa(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'xh')

    move_to_xhosa.short_description = "Move these to Xhosa."

    def move_to_zulu(modeladmin, request, queryset):
        for item in queryset:
            MoveSiteTo(item, 'zu')

    move_to_zulu.short_description = "Move these to Zulu."

    actions = [block_domain_wrong_language, block_domain_porn, block_domain_gambling, block_domain_piracy, block_domain_shortener,
               block_domain_adserver, block_domain_nocontent, block_domain_spam, block_domain_social, tag_as_english, tag_as_language_infix,
               recrawl_this_url, move_to_aragonese, move_to_basque, move_to_catalan, move_to_croatian,
               move_to_czech, move_to_dutch,
               move_to_estonian, move_to_finnish, move_to_french, move_to_galician, move_to_german,
               move_to_greek, move_to_hausa, move_to_hungarian, move_to_italian, move_to_latvian,
               move_to_lithuanian, move_to_portuguese, move_to_polish, move_to_romanian,
               move_to_rwandan, move_to_shona, move_to_slovene, move_to_somali, move_to_spanish, move_to_swahili,
               move_to_swedish, move_to_turkish, move_to_welsh, move_to_wolof, move_to_yoruba,
               move_to_xhosa, move_to_zulu,
               block_domain_language_am, block_domain_language_ar,
               block_domain_language_az, block_domain_language_cn, block_domain_language_ge, block_domain_language_il,
               block_domain_language_hi, block_domain_language_in,
               block_domain_language_ja, block_domain_language_km, block_domain_language_ko,
               block_domain_language_ru, block_domain_language_sr, block_domain_language_th, block_domain_language_vn,
               move_to_english]


class SearchReportAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'language', 'total_searches')
    search_fields = ('year', 'language')

    def rebuild_this_report(modelAdmin, request, queryset):
        for item in queryset:
            report = GenerateSearchReport(False, month=item.month, year=item.year, lang=item.language)
            item.delete()
            report.save()

    rebuild_this_report.short_description = "Rebuild this report."

    actions = [rebuild_this_report, ]


class PendingUrlAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

    def recrawl_this_url(modelAdmin, request, queryset):
        for item in queryset:
            CrawlSingleUrl(item.url)

    recrawl_this_url.short_description = "Crawl this URL."

    actions = [recrawl_this_url, ]


class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'result_count', 'search_time', 'ip', 'last_search', 'search_id', 'indexed', 'is_bot')
    search_fields = ('keywords', 'ip', 'search_id')

    def block_these_terms(modeladmin, request, queryset):
        for item in queryset:
            try:
                BadQuery.objects.get(keywords=item.keywords)
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
    list_display = ('keywords', 'date_indexed', 'num_pages', 'index_time', 'actively_blocked', 'refused')
    search_fields = ('keywords',)
    fields = [('keywords', 'term_weight'), ('date_indexed', 'index_time'), 'page_rankings', ('num_pages', 'num_results'), 'search_results',
             ('actively_blocked', 'refused', 'show_ad', 'verified_english'), ('is_language', 'typo_for')]

    def reindex_these_terms(modeladmin, request, queryset):
        for item in queryset:
            name = item.__class__.__name__
            if name == 'IndexTerm':
                lang = 'en'
            else:
                lang = name[-2:]
            BuildIndexForTerm(item.keywords, lang=lang, type='logdivide')

    reindex_these_terms.short_description = "Reindex these term(s). (may time out)"

    def delete_these_index_terms(modeladmin, request, queryset):
        for item in queryset:
            ranking_model = KeywordRanking
            if item.is_language:
                ranking_model = GetKeywordRankingModelFromLanguage(item.is_language)
            ranking_model.objects.filter(keywords=item.keywords).delete()
            item.delete()

    delete_these_index_terms.short_description = "Delete these index terms and their keyword ranks."

    actions = [delete_these_index_terms, reindex_these_terms]


class EnglishIndexTermAdmin(IndexTermAdmin):
    list_display = ('keywords', 'date_indexed', 'num_pages', 'index_time', 'actively_blocked', 'refused', 'show_ad', 'typo_for', 'is_language')


class BadQueryAdmin(admin.ModelAdmin):
    list_display = ('keywords',)
    search_fields = ('keywords',)


class PendingIndexAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'date_added', 'reason')
    search_fields = ('keywords',)

    def index_these_terms(modeladmin, request, queryset):
        for item in queryset:
            name = item.__class__.__name__
            if name == 'PendingIndex':
                lang = 'en'
            else:
                lang = name[-2:]
            BuildIndexForTerm(item.keywords, lang=lang, type='logdivide')
            item.delete()

    index_these_terms.short_description = "Index these term(s). (may time out)"

    def block_these_terms(modeladmin, request, queryset):
        for item in queryset:
            try:
                BadQuery.objects.get(keywords=item.keywords)
            except ObjectDoesNotExist:
                bad = BadQuery()
                bad.keywords = item.keywords
                bad.save()
            item.delete()

    block_these_terms.short_description = "Add terms to bad query list and delete."

    def delete_all_moved_terms(modeladmin, request, queryset):
        for item in queryset:
            if ' moved to ' in item.reason:
                item.delete()

    delete_all_moved_terms.short_description = "Delete all of these terms with 'moved to' as a reason."

    def delete_all_blocked_terms(modeladmin, request, queryset):
        for item in queryset:
            if ' blocked and it ' in item.reason:
                item.delete()

    delete_all_blocked_terms.short_description = "Delete all of these terms with 'blocked' as a reason."

    actions = [index_these_terms, block_these_terms, delete_all_moved_terms, delete_all_blocked_terms]


class FeedbackItemAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'num_search_results', 'date_added', 'language', 'processed', 'ip')
    search_fields = ('keywords',)

    def spam_block(modeladmin, request, queryset):
        for item in queryset:
            MarkURLContentsAsSpam(item.comment, item.ip)
            item.delete()

    spam_block.short_description = "Block the contents of these items as spam."

    actions = [spam_block, ]


class DomainInfoAdmin(admin.ModelAdmin):
    list_display = ('url', 'language_association', 'alexa_rank', 'majestic_rank', 'domcop_pagerank')
    search_fields = ('url',)
    fields = ['url', ('language_association', 'rank_adjustment', 'rank_reason'),
              ('is_unblockable', 'verified_notporn'),
              ('uses_language_subdirs', 'uses_language_query_parameter', 'uses_langid'),
              ('domains_linking_in', 'domains_linking_in_last_updated', 'favicons_last_updated'),
              ('alexa_rank', 'alexa_rank_date', 'majestic_rank', 'majestic_refsubnets', 'majestic_rank_date'),
              ('quantcast_rank', 'quantcast_rank_date', 'domcop_rank', 'domcop_pagerank', 'domcop_pagerank_date'),
              ('alexa_outdated', 'majestic_outdated', 'quantcast_outdated', 'domcop_pagerank_outdated'),
              ('domain_created', 'domain_expires', 'domain_updated', 'whois_last_updated'),
              ('num_urls', 'num_urls_last_updated', 'num_keywords_ranked', 'num_keywords_last_updated'),
              ('whois_registrar', 'whois_name', 'whois_country', 'whois_state'),
              ('whois_city', 'whois_address', 'whois_zipcode', 'whois_org'),
              ('whois_nameservers', 'whois_emails'),
              ('robots_ip', 'robots_last_updated'),
              ('robots_txt', 'notes')]
    show_full_result_count = False


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name', 'value')


class ExtendedSiteInfoAdmin(SiteInfoAdmin):
    list_display = ('rooturl', 'url', 'pagetitle', 'pagefirstheadtag', 'pagefirsth2tag', 'pagefirsth3tag')


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


class DomainSuffixAdmin(admin.ModelAdmin):
    list_display = ('extension', 'num_known', 'num_crawled', 'num_blocked', 'default_language', 'blocked_to_crawled_ratio', 'last_updated')

    def generate_stats(modeladmin, request, queryset):
        for item in queryset:
            CalculateDomainSuffixStats(item.extension)

    generate_stats.short_description = "Generate stats for this domain suffix."

    actions = [generate_stats, ]


admin.site.register(BlockedSite, ExcludedSiteAdmin)
admin.site.register(SiteInfo, SiteInfoAdmin)
admin.site.register(SiteInfoFull, ExtendedSiteInfoAdmin)
admin.site.register(SiteInfo_cs, SiteInfoAdmin)
admin.site.register(SiteInfo_de, SiteInfoAdmin)
admin.site.register(SiteInfo_el, SiteInfoAdmin)
admin.site.register(SiteInfo_es, SiteInfoAdmin)
admin.site.register(SiteInfo_fi, SiteInfoAdmin)
admin.site.register(SiteInfo_fr, SiteInfoAdmin)
admin.site.register(SiteInfo_hu, SiteInfoAdmin)
admin.site.register(SiteInfo_it, SiteInfoAdmin)
admin.site.register(SiteInfo_nl, SiteInfoAdmin)
admin.site.register(SiteInfo_pl, SiteInfoAdmin)
admin.site.register(SiteInfo_pt, SiteInfoAdmin)
admin.site.register(SiteInfo_sv, SiteInfoAdmin)
admin.site.register(SiteInfo_tr, SiteInfoAdmin)
admin.site.register(DomainInfo, DomainInfoAdmin)
admin.site.register(SearchLog, SearchLogAdmin)
admin.site.register(SearchLog_cs, SearchLogAdmin)
admin.site.register(SearchLog_da, SearchLogAdmin)
admin.site.register(SearchLog_de, SearchLogAdmin)
admin.site.register(SearchLog_el, SearchLogAdmin)
admin.site.register(SearchLog_es, SearchLogAdmin)
admin.site.register(SearchLog_fi, SearchLogAdmin)
admin.site.register(SearchLog_fr, SearchLogAdmin)
admin.site.register(SearchLog_hu, SearchLogAdmin)
admin.site.register(SearchLog_is, SearchLogAdmin)
admin.site.register(SearchLog_it, SearchLogAdmin)
admin.site.register(SearchLog_nl, SearchLogAdmin)
admin.site.register(SearchLog_no, SearchLogAdmin)
admin.site.register(SearchLog_pl, SearchLogAdmin)
admin.site.register(SearchLog_pt, SearchLogAdmin)
admin.site.register(SearchLog_sk, SearchLogAdmin)
admin.site.register(SearchLog_sv, SearchLogAdmin)
admin.site.register(SearchLog_tr, SearchLogAdmin)
admin.site.register(PendingIndex, PendingIndexAdmin)
admin.site.register(PendingIndex_cs, PendingIndexAdmin)
admin.site.register(PendingIndex_de, PendingIndexAdmin)
admin.site.register(PendingIndex_el, PendingIndexAdmin)
admin.site.register(PendingIndex_es, PendingIndexAdmin)
admin.site.register(PendingIndex_fi, PendingIndexAdmin)
admin.site.register(PendingIndex_fr, PendingIndexAdmin)
admin.site.register(PendingIndex_hu, PendingIndexAdmin)
admin.site.register(PendingIndex_it, PendingIndexAdmin)
admin.site.register(PendingIndex_nl, PendingIndexAdmin)
admin.site.register(PendingIndex_pl, PendingIndexAdmin)
admin.site.register(PendingIndex_pt, PendingIndexAdmin)
admin.site.register(PendingIndex_sv, PendingIndexAdmin)
admin.site.register(PendingIndex_tr, PendingIndexAdmin)
admin.site.register(IndexTerm, EnglishIndexTermAdmin)
admin.site.register(IndexTerm_cs, IndexTermAdmin)
admin.site.register(IndexTerm_de, IndexTermAdmin)
admin.site.register(IndexTerm_el, IndexTermAdmin)
admin.site.register(IndexTerm_es, IndexTermAdmin)
admin.site.register(IndexTerm_fi, IndexTermAdmin)
admin.site.register(IndexTerm_fr, IndexTermAdmin)
admin.site.register(IndexTerm_hu, IndexTermAdmin)
admin.site.register(IndexTerm_it, IndexTermAdmin)
admin.site.register(IndexTerm_nl, IndexTermAdmin)
admin.site.register(IndexTerm_pl, IndexTermAdmin)
admin.site.register(IndexTerm_pt, IndexTermAdmin)
admin.site.register(IndexTerm_sv, IndexTermAdmin)
admin.site.register(IndexTerm_tr, IndexTermAdmin)
admin.site.register(FeedbackItem, FeedbackItemAdmin)
admin.site.register(ChangelogItem)
admin.site.register(DomainSuffix, DomainSuffixAdmin)
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
admin.site.register(IPSearchLog, SearchLogAdmin)
admin.site.register(NewsSite)
admin.site.register(AutoComplete, AutoCompleteAdmin)
admin.site.register(AutoComplete_cs, AutoCompleteAdmin)
admin.site.register(AutoComplete_de, AutoCompleteAdmin)
admin.site.register(AutoComplete_el, AutoCompleteAdmin)
admin.site.register(AutoComplete_es, AutoCompleteAdmin)
admin.site.register(AutoComplete_fi, AutoCompleteAdmin)
admin.site.register(AutoComplete_fr, AutoCompleteAdmin)
admin.site.register(AutoComplete_hu, AutoCompleteAdmin)
admin.site.register(AutoComplete_it, AutoCompleteAdmin)
admin.site.register(AutoComplete_nl, AutoCompleteAdmin)
admin.site.register(AutoComplete_pl, AutoCompleteAdmin)
admin.site.register(AutoComplete_pt, AutoCompleteAdmin)
admin.site.register(AutoComplete_tr, AutoCompleteAdmin)
admin.site.register(ResultClick, ResultClickAdmin)
admin.site.register(ResultClick_cs, ResultClickAdmin)
admin.site.register(ResultClick_da, ResultClickAdmin)
admin.site.register(ResultClick_de, ResultClickAdmin)
admin.site.register(ResultClick_el, ResultClickAdmin)
admin.site.register(ResultClick_es, ResultClickAdmin)
admin.site.register(ResultClick_fi, ResultClickAdmin)
admin.site.register(ResultClick_fr, ResultClickAdmin)
admin.site.register(ResultClick_hu, ResultClickAdmin)
admin.site.register(ResultClick_is, ResultClickAdmin)
admin.site.register(ResultClick_it, ResultClickAdmin)
admin.site.register(ResultClick_nl, ResultClickAdmin)
admin.site.register(ResultClick_no, ResultClickAdmin)
admin.site.register(ResultClick_pl, ResultClickAdmin)
admin.site.register(ResultClick_pt, ResultClickAdmin)
admin.site.register(ResultClick_sk, ResultClickAdmin)
admin.site.register(ResultClick_sv, ResultClickAdmin)
admin.site.register(ResultClick_tr, ResultClickAdmin)
admin.site.register(Screenshot)
admin.site.register(APISubscription, APISubscriptionAdmin)
admin.site.register(APIUsage, APIUsageAdmin)
admin.site.register(APIToken)
admin.site.register(APIUser)
admin.site.register(CrawlableUrl)
admin.site.register(Favicon)

# Conditional languages, enabled in language_list in models.py.
if 'an' in language_list:
    admin.site.register(SiteInfo_an, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_an, IndexTermAdmin)
    admin.site.register(PendingIndex_an, PendingIndexAdmin)
    admin.site.register(SearchLog_an, SearchLogAdmin)
    admin.site.register(AutoComplete_an, AutoCompleteAdmin)
    admin.site.register(ResultClick_an, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'ca' in language_list:
    admin.site.register(SiteInfo_ca, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_ca, IndexTermAdmin)
    admin.site.register(PendingIndex_ca, PendingIndexAdmin)
    admin.site.register(SearchLog_ca, SearchLogAdmin)
    admin.site.register(AutoComplete_ca, AutoCompleteAdmin)
    admin.site.register(ResultClick_ca, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'cy' in language_list:
    admin.site.register(SiteInfo_cy, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_cy, IndexTermAdmin)
    admin.site.register(PendingIndex_cy, PendingIndexAdmin)
    admin.site.register(SearchLog_cy, SearchLogAdmin)
    admin.site.register(AutoComplete_cy, AutoCompleteAdmin)
    admin.site.register(ResultClick_cy, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'et' in language_list:
    admin.site.register(SiteInfo_et, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_et, IndexTermAdmin)
    admin.site.register(PendingIndex_et, PendingIndexAdmin)
    admin.site.register(SearchLog_et, SearchLogAdmin)
    admin.site.register(AutoComplete_et, AutoCompleteAdmin)
    admin.site.register(ResultClick_et, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'eu' in language_list:
    admin.site.register(SiteInfo_eu, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_eu, IndexTermAdmin)
    admin.site.register(PendingIndex_eu, PendingIndexAdmin)
    admin.site.register(SearchLog_eu, SearchLogAdmin)
    admin.site.register(AutoComplete_eu, AutoCompleteAdmin)
    admin.site.register(ResultClick_eu, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'gl' in language_list:
    admin.site.register(SiteInfo_gl, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_gl, IndexTermAdmin)
    admin.site.register(PendingIndex_gl, PendingIndexAdmin)
    admin.site.register(SearchLog_gl, SearchLogAdmin)
    admin.site.register(AutoComplete_gl, AutoCompleteAdmin)
    admin.site.register(ResultClick_gl, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'ha' in language_list:
    admin.site.register(SiteInfo_ha, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_ha, IndexTermAdmin)
    admin.site.register(PendingIndex_ha, PendingIndexAdmin)
    admin.site.register(SearchLog_ha, SearchLogAdmin)
    admin.site.register(AutoComplete_ha, AutoCompleteAdmin)
    admin.site.register(ResultClick_ha, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'hr' in language_list:
    admin.site.register(SiteInfo_hr, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_hr, IndexTermAdmin)
    admin.site.register(PendingIndex_hr, PendingIndexAdmin)
    admin.site.register(SearchLog_hr, SearchLogAdmin)
    admin.site.register(AutoComplete_hr, AutoCompleteAdmin)
    admin.site.register(ResultClick_hr, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'lt' in language_list:
    admin.site.register(SiteInfo_lt, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_lt, IndexTermAdmin)
    admin.site.register(PendingIndex_lt, PendingIndexAdmin)
    admin.site.register(SearchLog_lt, SearchLogAdmin)
    admin.site.register(AutoComplete_lt, AutoCompleteAdmin)
    admin.site.register(ResultClick_lt, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'lv' in language_list:
    admin.site.register(SiteInfo_lv, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_lv, IndexTermAdmin)
    admin.site.register(PendingIndex_lv, PendingIndexAdmin)
    admin.site.register(SearchLog_lv, SearchLogAdmin)
    admin.site.register(AutoComplete_lv, AutoCompleteAdmin)
    admin.site.register(ResultClick_lv, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'ro' in language_list:
    admin.site.register(SiteInfo_ro, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_ro, IndexTermAdmin)
    admin.site.register(PendingIndex_ro, PendingIndexAdmin)
    admin.site.register(SearchLog_ro, SearchLogAdmin)
    admin.site.register(AutoComplete_ro, AutoCompleteAdmin)
    admin.site.register(ResultClick_ro, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'rw' in language_list:
    admin.site.register(SiteInfo_rw, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_rw, IndexTermAdmin)
    admin.site.register(PendingIndex_rw, PendingIndexAdmin)
    admin.site.register(SearchLog_rw, SearchLogAdmin)
    admin.site.register(AutoComplete_rw, AutoCompleteAdmin)
    admin.site.register(ResultClick_rw, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'sl' in language_list:
    admin.site.register(SiteInfo_sl, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_sl, IndexTermAdmin)
    admin.site.register(PendingIndex_sl, PendingIndexAdmin)
    admin.site.register(SearchLog_sl, SearchLogAdmin)
    admin.site.register(AutoComplete_sl, AutoCompleteAdmin)
    admin.site.register(ResultClick_sl, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'sn' in language_list:
    admin.site.register(SiteInfo_sn, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_sn, IndexTermAdmin)
    admin.site.register(PendingIndex_sn, PendingIndexAdmin)
    admin.site.register(SearchLog_sn, SearchLogAdmin)
    admin.site.register(AutoComplete_sn, AutoCompleteAdmin)
    admin.site.register(ResultClick_sn, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'so' in language_list:
    admin.site.register(SiteInfo_so, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_so, IndexTermAdmin)
    admin.site.register(PendingIndex_so, PendingIndexAdmin)
    admin.site.register(SearchLog_so, SearchLogAdmin)
    admin.site.register(AutoComplete_so, AutoCompleteAdmin)
    admin.site.register(ResultClick_so, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'sw' in language_list:
    admin.site.register(SiteInfo_sw, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_sw, IndexTermAdmin)
    admin.site.register(PendingIndex_sw, PendingIndexAdmin)
    admin.site.register(SearchLog_sw, SearchLogAdmin)
    admin.site.register(AutoComplete_sw, AutoCompleteAdmin)
    admin.site.register(ResultClick_sw, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'wo' in language_list:
    admin.site.register(SiteInfo_wo, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_wo, IndexTermAdmin)
    admin.site.register(PendingIndex_wo, PendingIndexAdmin)
    admin.site.register(SearchLog_wo, SearchLogAdmin)
    admin.site.register(AutoComplete_wo, AutoCompleteAdmin)
    admin.site.register(ResultClick_wo, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'xh' in language_list:
    admin.site.register(SiteInfo_xh, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_xh, IndexTermAdmin)
    admin.site.register(PendingIndex_xh, PendingIndexAdmin)
    admin.site.register(SearchLog_xh, SearchLogAdmin)
    admin.site.register(AutoComplete_xh, AutoCompleteAdmin)
    admin.site.register(ResultClick_xh, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'yo' in language_list:
    admin.site.register(SiteInfo_yo, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_yo, IndexTermAdmin)
    admin.site.register(PendingIndex_yo, PendingIndexAdmin)
    admin.site.register(SearchLog_yo, SearchLogAdmin)
    admin.site.register(AutoComplete_yo, AutoCompleteAdmin)
    admin.site.register(ResultClick_yo, ResultClickAdmin)
    # We don't register KeywordRanking.
if 'zu' in language_list:
    admin.site.register(SiteInfo_zu, ExtendedSiteInfoAdmin)
    admin.site.register(IndexTerm_zu, IndexTermAdmin)
    admin.site.register(PendingIndex_zu, PendingIndexAdmin)
    admin.site.register(SearchLog_zu, SearchLogAdmin)
    admin.site.register(AutoComplete_zu, AutoCompleteAdmin)
    admin.site.register(ResultClick_zu, ResultClickAdmin)
    # We don't register KeywordRanking.
