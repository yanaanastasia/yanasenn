# Messen v2: ruhige Übersicht + Detailansicht pro Messe
exec(open(S+'/me/content.py',encoding='utf-8').read())
import json
IM=json.load(open(S+'/me/imgs2.json'))
# Zusatzinfos pro Messe (aus content-plan.md, Kurz-Zeilen und Texte)
FACT={
'achema':[('Ort','Location','Messe Frankfurt','Messe Frankfurt'),('Rolle','Role','Projektleitung ab Frühling 2024','Project lead from spring 2024'),('Vor Ort','On site','im Standteam','in the booth team')],
'tps':[('Datum','Date','20.–22. August 2024','20–22 August 2024'),('Ort','Venue','George R. Brown Convention Center','George R. Brown Convention Center'),('Stand','Booth','2725','2725'),('Vor Ort','On site','im Standteam','in the booth team')],
'petro24':[('Datum','Date','27.–28. November 2024','27–28 November 2024'),('Stand','Booth','E8-F7','E8-F7'),('Fläche','Size','12 m², drei Seiten offen','12 m², open on three sides')],
'pv25':[('Datum','Date','19.–20. Februar 2025','19–20 February 2025'),('Stand','Booth','Halle 5, 5-I06','Hall 5, 5-I06'),('Fläche','Size','20 m² Eckstand','20 m² corner booth')],
'tfs25':[('Datum','Date','8.–10. April 2025','8–10 April 2025'),('Ort','Venue','Orange County Convention Center','Orange County Convention Center'),('Stand','Booth','WA2, 3014','WA2, 3014'),('Fläche','Size','600 sq ft, vier Seiten offen','600 sq ft, open on four sides')],
'leuna25':[('Datum','Date','24. April 2025','24 April 2025'),('Ort','Venue','cCe Kulturhaus Leuna','cCe Kulturhaus Leuna'),('Stand','Booth','D13, Komplettstand 9 m²','D13, complete booth 9 m²')],
'cru25':[('Datum','Date','3.–5. November 2025','3–5 November 2025'),('Ausgabe','Edition','41.','41st'),('Stand','Booth','37, Tischstand 3 × 2 m','37, tabletop 3 × 2 m')],
'lh25':[('Datum','Date','19.–20. November 2025','19–20 November 2025'),('Ort','Venue','Carré des Docks','Carré des Docks'),('Stand','Booth','D17-E20','D17-E20'),('Fläche','Size','18 m², drei Seiten offen','18 m², open on three sides')],
'fla26':[('Datum','Date','26.–28. Januar 2026','26–28 January 2026'),('Stand','Booth','22/23, Doppelstand','22/23, double booth')],
'pv26':[('Datum','Date','25.–26. Februar 2026','25–26 February 2026'),('Stand','Booth','Halle 7, 7238','Hall 7, 7238'),('Fläche','Size','6 × 3 m','6 × 3 m')],
'dk26':[('Datum','Date','20.–21. Mai 2026','20–21 May 2026'),('Ort','Venue','Kursaal','Kursaal'),('Stand','Booth','C12','C12')],
'uk26':[('Datum','Date','20.–21. Mai 2026','20–21 May 2026'),('Ort','Venue','NEC Birmingham, Halle 5','NEC Birmingham, Hall 5'),('Stand','Booth','G60','G60')],
'cheme26':[('Datum','Date','9.–10. Juni 2026','9–10 June 2026'),('Ort','Venue','George R. Brown Convention Center','George R. Brown Convention Center'),('Stand','Booth','507, 10 × 10 ft','507, 10 × 10 ft')],
'cru26':[('Datum','Date','3.–5. November 2026','3–5 November 2026'),('Ort','Venue','Estrel Berlin','Estrel Berlin'),('Stand','Booth','60, Tischstand 3 × 2 m','60, tabletop 3 × 2 m'),('Status','Status','bevorstehend','upcoming')],
'tfs26':[('Datum','Date','18.–19. November 2026','18–19 November 2026'),('Ort','Venue','Tampa Convention Center','Tampa Convention Center'),('Stand','Booth','1114, 400 sq ft','1114, 400 sq ft'),('Status','Status','bevorstehend','upcoming')],
'petro26':[('Datum','Date','25.–26. November 2026','25–26 November 2026'),('Ort','Venue','La Halle de Martigues','La Halle de Martigues'),('Stand','Booth','B4-C3, 18 m²','B4-C3, 18 m²'),('Status','Status','bevorstehend','upcoming')],
'dahej26':[('Datum','Date','16.–18. Dezember 2026','16–18 December 2026'),('Stand','Booth','Halle B, B35, 45 m²','Hall B, B35, 45 m²'),('Status','Status','bevorstehend','upcoming')],
}
MORE={
'pv25':[('Zur Vorbereitung gehörten die Standplanung, drei Exponate, Broschüren und Explosionszeichnungen auf Deutsch, Giveaways sowie der Versand über den Messespediteur, inklusive Einfuhr nach Deutschland. Ein Messebriefing und das Lead-Formular bereiteten das Standteam vor.','Preparation included booth planning, three exhibits, brochures and exploded drawings in German, giveaways and shipping via the fair forwarder, including import into Germany. A fair briefing and the lead form prepared the booth team.')],
'leuna25':[('Material, Exponate und Standausstattung entstanden in Abstimmung mit dem Verkauf in Deutschland und reisten aus der Schweiz an die Messe.','Material, exhibits and booth equipment were coordinated with sales in Germany and travelled from Switzerland to the fair.')],
'cru25':[('Das Mobiliar kam aus dem Lager in den USA; die englischen Broschüren wurden in der Schweiz gedruckt und reisten zusammen mit Giveaways und Schweizer Spezialitäten an die Messe. Ein Messebriefing und das Lead-Formular bereiteten das Team vor Ort vor.','The furniture came from the warehouse in the USA; the English brochures were printed in Switzerland and travelled to the fair with giveaways and Swiss specialities. A fair briefing and the lead form prepared the team on site.')],
'lh25':[('Broschüren, Explosionszeichnungen und Factsheets lagen auf Französisch bereit. Über das Kommunikationspaket des Veranstalters war CP zudem im Messekatalog und auf der Messe-Website präsent, mit eigens gestalteter Anzeige und eigenen Web-Bannern.','Brochures, exploded drawings and factsheets were available in French. Through the organiser’s communication package, CP was also present in the fair catalogue and on the fair website, with a custom ad and web banners.')],
'uk26':[('Im Vorfeld machten E-Mail-Banner, E-Mail-Signatur, ein Eintrag in den Show News und ein Social-Media-Beitrag die Teilnahme bekannt. Messebriefing und Lead-Formular bereiteten das Team vor.','Beforehand, e-mail banners, the e-mail signature, an entry in the Show News and a social media post announced the participation. A fair briefing and the lead form prepared the team.')],
'cheme26':[('Ein englisches Messebriefing bereitete das Team vor Ort vor: von den Fakten zur Messe über Hallenplan, Ausstellerliste und Programm bis zu Standausstattung, Dresscode und Giveaways.','An English fair briefing prepared the team on site: from fair facts, hall plan, exhibitor list and programme to booth equipment, dress code and giveaways.')],
'cru26':[('Gezeigt werden zwei Magnetkupplungspumpen der Baureihe MKP und eine MKTP. Im Vorfeld laden ein E-Mail-Banner mit Gratis-Ticket und die E-Mail-Signatur zur Messe ein.','Two MKP magnetic drive pumps and one MKTP will be on show. Beforehand, an e-mail banner with a free ticket and the e-mail signature invite visitors to the fair.')],
'petro26':[('Über das Kommunikationspaket des Veranstalters ist CP im Messekatalog und auf der Messe-Website präsent, mit einer Anzeige, die vier Baureihen vorstellt, und zwei Web-Bannern.','Through the organiser’s communication package, CP is present in the fair catalogue and on the fair website, with an ad presenting four product series and two web banners.')],
'dahej26':[('Gezeigt werden drei Magnetkupplungspumpen aus den Baureihen MKP, MKP-S und MKPL. Vor Ort betreut das Verkaufsteam den Stand.','Three magnetic drive pumps from the MKP, MKP-S and MKPL series are on show. On site, the sales team runs the booth.')],
}
CAT=[('design',('Standdesign','Booth design'),('Rückwände, Blenden und Grafik für den Stand.','Back walls, fascias and graphics for the booth.')),
('stand',('Am Stand','At the booth'),('So sah der Auftritt vor Ort aus.','How the booth looked on site.')),
('vor',('Vor der Messe','Before the fair'),('E-Mail-Signatur, Banner, Inserate und Social Media machen die Teilnahme im Vorfeld bekannt.','E-mail signature, banners, ads and social media announce the participation beforehand.')),
('brief',('Briefing fürs Team','Briefing for the team'),('Vor jeder Messe erstelle ich ein Messebriefing für das Standteam: Fakten zur Messe, Standplan, Ablauf und Dresscode.','Before every fair I create a briefing for the booth team: fair facts, booth plan, schedule and dress code.')),
('lead',('Leads','Leads'),('Mit dem Lead-Formular hält das Team jedes Gespräch am Stand fest: Branche, Einsatzbereich, Produktinteresse und nächste Schritte. Das Formular erstelle ich für jede Messe.','With the lead form the team records every conversation at the booth: industry, application, product interest and next steps. I create the form for every fair.'))]
import re as _re
def _li(t): return _re.sub(r'(#\w+)',r'<span class="ht">\1</span>',t).replace('\n','<br>')
POSTS=json.load(open(S+'/me/li.json',encoding='utf-8'))
SPEC={
('tfs25','vor'):('Die Anzeige im Messekatalog trug den Titel «Swiss Pump Technology for Sustainable and Decarbonized Fertilizer Production». Dazu kamen E-Mail-Banner mit Gratis-Ticket und drei Mailings; registrierte Kundinnen und Kunden holten ihr Geschenk am Stand ab.','The catalogue ad was titled “Swiss Pump Technology for Sustainable and Decarbonized Fertilizer Production”. E-mail banners with a free ticket and three mailings followed; registered customers collected their gift at the booth.'),
('pv25','vor'):('E-Mail-Banner luden zum kostenlosen Messeticket ein, LinkedIn-Beiträge kündigten den Auftritt an. Kundinnen und Kunden konnten sich vorab für ein Geschenk anmelden.','E-mail banners invited visitors to a free ticket and LinkedIn posts announced the booth. Customers could register for a gift in advance.'),
('dk26','vor'):('Ganzseitige Anzeige im Katalog mit den drei ausgestellten Baureihen, Web-Banner auf der Messe-Website und E-Mail-Banner. Am Eingang verteilte das Team Goodie-Bags, damit möglichst viele Besucher eine CP-Tasche durch die Messe trugen.','Full-page catalogue ad with the three product series on show, web banners on the fair website and e-mail banners. At the entrance the team handed out goodie bags so that many visitors carried a CP bag through the fair.'),
('uk26','vor'):('Die Anzeige setzte auf zwei Argumente: Schweizer Qualität und geringer Wartungsaufwand. E-Mail-Banner, E-Mail-Signatur und ein Social-Media-Beitrag machten die Teilnahme bekannt.','The ad focused on two arguments: Swiss quality and low maintenance. E-mail banners, the e-mail signature and a social media post announced the participation.'),
('achema','vor'):('Drei Mailings, ein Reminder und eine Dankesmail luden Kundinnen und Kunden ein, vorab ein Geschenk zu wählen: SIGG-Flasche, Badetuch oder Fussball im CP-Stil, passend zur Fussball-EM.','Three mailings, a reminder and a thank-you mail invited customers to choose a gift in advance: SIGG bottle, bath towel or a football in CP style, in time for the European Championship.'),
('tps','design'):('Statt Mobiliar zu mieten, entstand ein eigenes Messesystem für die USA: eine aufklappbare Standbox mit Rundum-Design und eine Box für die Möbel. Beide lagern zwischen den Messen in den USA.','Instead of renting furniture, a booth system for the USA was created: a fold-out booth box with all-round design and a box for the furniture. Both are stored in the USA between fairs.'),
('tps','lead'):('Nach der Messe gingen die Leads an die zuständigen Verkäufer und wurden zentral abgelegt.','After the fair, the leads went to the responsible sales staff and were stored centrally.'),
}
def cover(k): return (IM.get(k,{}).get('hero') or [None])[0]
ORDER=[f[0] for f in F]
LOGO={'achema':'achema','tps':'tps','petro24':'petro','petro26':'petro','pv25':'pv','pv26':'pv','tfs25':'tfs','tfs26':'tfs','leuna25':'leuna','cru25':'cru','cru26':'cru','lh25':'lh','fla26':'fla','dk26':'dk','uk26':'chemuk','cheme26':'cheme','dahej26':'dahej'}
def card(f):
    k,name,ort,dat=f[:4]
    vis=f'<img src="img/t_{LOGO[k]}.jpg" alt="Logo {name}">'; fit=''
    up='<span class="up">'+T('bevorstehend','upcoming')+'</span>' if k in ('cru26','tfs26','petro26','dahej26') else ''
    return f'<button class="fc" data-fair="{k}"><span class="fv">{vis}{up}</span><span class="fm">{T(*dat)} · {T(*ort)}</span><b class="fn">{name}</b></button>'
def sheet(f):
    k,name,ort,dat,hero,more,chips,txt,tk,link=f
    facts=''.join(f'<div><dt>{T(a,b)}</dt><dd>{T(c,d)}</dd></div>' for a,b,c,d in FACT.get(k,[]))
    body=P(*(list(txt)+MORE.get(k,[])))
    gal=''
    for n_,(c,lab,blurb) in enumerate(CAT,1):
        fs=IM.get(k,{}).get(c,[])
        if not fs: continue
        if (k,c) in SPEC: blurb=SPEC[(k,c)]
        if k=='achema' and c=='design': blurb=('Standdesign und Standbau lagen bei einer Agentur. Von mir: die Infostelen zu den Exponaten.','Booth design and construction were by an agency. My part: the info columns for the exhibits.')
        gid=f'f_{k}_{c}'; G[gid]=[(x,f'{name} · {lab[0]}') for x in fs]
        tiles=''.join(f'<button class="gt{" fit" if c!="stand" else ""}" data-gallery="{gid}" data-n="{i}"><img src="img/{x}" alt="{name}, {lab[0]} {i+1}"></button>' for i,x in enumerate(fs))
        gal+=f'<section class="gsec"><div class="gh"><h4>{T(*lab)}</h4><p>{T(*blurb)}</p></div><div class="gg">{tiles}</div></section>'
        if c=='vor' and k in POSTS:
            def _card(q):
                ims=q['images'];g=f'li_{k}_'+q['date'].replace('-',''); G[g]=[(x,'LinkedIn') for x in ims]
                im=''.join(f'<button data-gallery="{g}" data-n="{i}"><img src="img/{x}" alt=""></button>' for i,x in enumerate(ims[:4]))
                dd='.'.join(reversed(q['date'].split('-')))
                return f'<article class="li"><header><img src="img/t_cplogo.png" alt=""><div><b>CP Pumpen AG</b><small>LinkedIn · {dd}</small></div></header><div class="lit"><p>{_li(q["text"])}</p></div><button class="limore">{T("mehr","more")}</button><div class="limg n{min(len(ims),4)}">{im}</div><footer><span>👍 Gefällt mir</span><span>💬 Kommentieren</span><span>↗ Teilen</span></footer></article>'
            cards=''.join(_card(q) for q in POSTS[k])
            gal+=f'<section class="gsec"><div class="gh"><h4>LinkedIn</h4><p>{T("Die Beiträge auf dem LinkedIn-Kanal von CP: vor der Messe als Einladung, während der Messe mit Bildern vom Stand und danach als Rückblick.","The posts on CP’s LinkedIn channel: an invitation before the fair, pictures from the booth during the fair and a recap afterwards.")}</p></div><div class="lig">{cards}</div></section>'
    c=cover(k)
    heroh=(f'<button class="sh-hero" data-gallery="h_{k}" data-n="0"><img src="img/{c}" alt="{name}"></button>' if c else '')
    if c: G[f'h_{k}']=[(c,name)]
    lk=f'<a class="lnk" href="{A}{link}" target="_blank" rel="noopener">{T("Ganze Projektseite ansehen","View the full project page")} ↗</a>' if link else ''
    i=ORDER.index(k); pv=ORDER[i-1] if i>0 else None; nx=ORDER[i+1] if i+1<len(ORDER) else None
    nm={f[0]:f[1] for f in F}
    nav='<nav class="sh-nav">'+(f'<button data-fair="{pv}">‹ {nm[pv]}</button>' if pv else '<span></span>')+(f'<button data-fair="{nx}">{nm[nx]} ›</button>' if nx else '')+'</nav>'
    return (f'<article class="sheet" id="fs-{k}" hidden><p class="crumb">{T("Messen","Trade fairs")} · International</p><div class="sh-head"><div><h2>{name}</h2><p class="sh-sub">{T(*dat)} · {T(*ort)}</p></div><img class="sh-logo" src="img/t_{LOGO[k]}.jpg" alt="Logo {name}"></div>{heroh}'
            f'<dl class="facts">{facts}</dl><div class="sh-body"><div class="sh-text">{body}{lk}</div><aside>{tasks(*tk)}</aside></div>{gal}{nav}</article>')
yrs=[('2026',[f for f in F if '2026' in f[1]]),('2025',[f for f in F if '2025' in f[1]]),('2024',[f for f in F if '2024' in f[1]])]
intl=''.join(f'<div class="yr"><h4>{y}</h4></div><div class="fgrid">'+''.join(card(f) for f in fs)+'</div>' for y,fs in yrs)
SEC[0]=('international',('International','International'),('Messeauftritte von CP Pump Systems in Europa, den USA und Indien. Eine Messe anklicken, um Stand, Standdesign und Kommunikation im Detail zu sehen.','Trade fairs of CP Pump Systems in Europe, the USA and India. Click a fair to see the booth, booth design and communication in detail.'),intl)
EXTRA='<dialog id="fair" aria-label="Messe"><div class="fwrap"><button class="fclose" id="fclose" aria-label="Schliessen">✕</button>'+''.join(sheet(f) for f in F)+'</div></dialog>'
