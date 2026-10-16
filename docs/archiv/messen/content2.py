# Messen v2: ruhige Übersicht + Detailansicht pro Messe
exec(open(S+'/me/content.py',encoding='utf-8').read())
import json
IM=json.load(open(S+'/me/imgs3.json'))
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
TAGS={'e_achema_vor0.jpg':'banner','e_achema_vor1.jpg':'mail','e_achema_vor2.jpg':'gift','e_tfs25_vor1.jpg':'ad','e_dk26_vor1.jpg':'ad','e_uk26_vor1.jpg':'ad','e_petro26_vor1.jpg':'ad'}
TN={'banner':('E-Mail-Banner','e-mail banner'),'ad':('Inserat im Messekatalog','ad in the fair catalogue'),'mail':('Einladungs-Mailing','invitation mailing'),'gift':('Kundengeschenke zur Auswahl','customer gifts to choose from')}
def _list(xs,de=True):
    xs=[TN[x][0 if de else 1] for x in xs]
    return xs[0] if len(xs)==1 else ', '.join(xs[:-1])+(' und ' if de else ' and ')+xs[-1]
import re as _re
def _li(t): return _re.sub(r'(#\w+)',r'<span class="ht">\1</span>',t).replace('\n','<br>')
POSTS=json.load(open(S+'/me/li.json',encoding='utf-8'))
SPEC={
('tfs25','vor'):('Das Inserat im Messekatalog trägt den Titel «Swiss Pump Technology for Sustainable and Decarbonized Fertilizer Production». Der E-Mail-Banner lud mit Gratis-Ticket zur Messe ein.','The catalogue ad is titled “Swiss Pump Technology for Sustainable and Decarbonized Fertilizer Production”. The e-mail banner invited visitors with a free ticket.'),
('dk26','vor'):('Das ganzseitige Inserat im Katalog stellt die drei ausgestellten Baureihen vor, der E-Mail-Banner lud zum Besuch am Stand C12 ein.','The full-page catalogue ad presents the three product series on show; the e-mail banner invited visitors to booth C12.'),
('uk26','vor'):('Das Inserat setzt auf zwei Argumente: Schweizer Qualität und geringer Wartungsaufwand. Dazu der E-Mail-Banner mit Gratis-Ticket.','The ad focuses on two arguments: Swiss quality and low maintenance. Plus the e-mail banner with a free ticket.'),
('achema','vor'):('E-Mail-Banner und Einladungs-Mailing: Kundinnen und Kunden wählten vorab ein Geschenk, das sie am Stand abholten: SIGG-Flasche, Badetuch oder Fussball im CP-Stil.','E-mail banner and invitation mailing: customers chose a gift in advance and collected it at the booth: SIGG bottle, bath towel or a football in CP style.'),
('tps','design'):('Statt Mobiliar zu mieten, entstand ein eigenes Messesystem für die USA: eine aufklappbare Standbox mit Rundum-Design und eine Box für die Möbel.','Instead of renting furniture, a booth system for the USA was created: a fold-out booth box with all-round design and a box for the furniture.'),
('achema','design'):('Standdesign und Standbau lagen bei einer Agentur. Von mir: die Infostelen zu den Exponaten.','Booth design and construction were by an agency. My part: the info columns for the exhibits.'),
}
BRIEF={'achema':37,'tps':14,'petro24':12,'pv25':15,'fla26':13,'pv26':20,'dk26':21,'uk26':15,'cheme26':17,'cru26':20}
def cover(k): return (IM.get(k,{}).get('hero') or [None])[0]
GTXT=[('GOLDINGER war jedes Jahr an der WEGA und an der Immozionale vertreten. Der bisherige Stand stammte aus früheren Jahren und zeigte vor allem viele kleine Objektplakate. Gleichzeitig sollte die eher ältere Zielgruppe schon vor der Messe erfahren, dass sie am Stand ihre Immobilie bewerten lassen kann.','GOLDINGER exhibited at WEGA and Immozionale every year. The existing booth dated from earlier years and mainly showed many small property posters. At the same time, the rather older target group was to learn before the fair that they could have their property valued at the booth.'),
 ('Königsblaue Paneele mit klaren Botschaften wie «Jetzt Immobilie direkt am Stand bewerten» ersetzten die kleinen Objektplakate.','Royal blue panels with clear messages such as “Have your property valued right at the booth” replaced the small property posters.')]
GTK=('Ich gestaltete die Messewände neu, entwarf ein Mockup des Stands und plante die Werbung vor der Messe.','I redesigned the booth walls, created a mockup of the booth and planned the advertising before the fair.')
SW=[('wega','WEGA',('Weinfelden, Thurgau','Weinfelden, Thurgau'),('2022 und 2023','2022 and 2023'),None,[],(),GTXT,GTK,None),
    ('immo','Immozionale',('Thurgau','Thurgau'),('2022','2022'),None,[],(),GTXT,GTK,None)]
F2=F+SW
IM.update({'wega':{'hero':['wand_neu.jpg'],'design':['wand_neu.jpg'],'vor':['g_wega.jpg']},'immo':{'hero':['wand_neu.jpg'],'design':['wand_neu.jpg']}})
TAGS['g_wega.jpg']='adz'
TN['adz']=('Inserat in den Wochen vor der Messe, mit dem Angebot einer Immobilien-Bewertung in fünf Minuten am Stand','ad in the weeks before the fair, offering a five-minute property valuation at the booth')
FACT['wega']=[('Messe','Fair','Die Thurgauer Messe','The Thurgau fair'),('Auftraggeber','Client','GOLDINGER Immobilien','GOLDINGER Immobilien'),('WEGA 2023','WEGA 2023','28.9.–2.10.2023','28 Sep–2 Oct 2023')]
FACT['immo']=[('Messe','Fair','Immobilienmesse im Thurgau','Real estate fair in Thurgau'),('Auftraggeber','Client','GOLDINGER Immobilien','GOLDINGER Immobilien')]
SPEC[('wega','design')]=('Die neuen Messewände in Königsblau. Vorher und nachher im Vergleich unten.','The new booth walls in royal blue. Before and after compared below.')
SPEC[('immo','design')]=('Die neu gestalteten Messewände kamen auch an der Immozionale zum Einsatz.','The redesigned booth walls were also used at Immozionale.')
ORDER=[f[0] for f in F2]
LOGO={'wega':'wega','immo':'immo','achema':'achema','tps':'tps','petro24':'petro','petro26':'petro','pv25':'pv','pv26':'pv','tfs25':'tfs','tfs26':'tfs','leuna25':'leuna','cru25':'cru','cru26':'cru','lh25':'lh','fla26':'fla','dk26':'dk','uk26':'chemuk','cheme26':'cheme','dahej26':'dahej'}
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
    I_=IM.get(k,{})
    def tiles(gid,fs,lab,fit):
        G[gid]=[(x,f'{name} · {lab}') for x in fs]
        return ''.join(f'<button class="gt{" fit" if fit else ""}" data-gallery="{gid}" data-n="{i}"><img src="img/{x}" alt="{name}, {lab} {i+1}"></button>' for i,x in enumerate(fs))
    dz,st=I_.get('design',[]),I_.get('stand',[])
    if dz or st:
        bl=SPEC.get((k,'design'),('Vom Entwurf zum fertigen Stand: oben geplant, darunter vor Ort.','From design to finished booth: planned above, on site below.'))
        if not dz: bl=('So sah der Stand vor Ort aus.','How the booth looked on site.')
        if not st: bl=SPEC.get((k,'design'),('Das Standdesign. Fotos vom fertigen Stand folgen nach der Messe.','The booth design. Photos of the finished booth will follow after the fair.') if k in ('cru26','tfs26','petro26','dahej26') else ('Das Standdesign.','The booth design.'))
        sub=''
        if dz: sub+=f'<div class="gsub"><h5>{T("Entwurf","Design")}</h5><div class="gg">{tiles(f"f_{k}_d",dz,"Standdesign",True)}</div></div>'
        if st: sub+=f'<div class="gsub"><h5>{T("Vor Ort","On site")}</h5><div class="gg">{tiles(f"f_{k}_s",st,"Vor Ort",False)}</div></div>'
        gal+=f'<section class="gsec"><div class="gh"><h4>{T("Standdesign und Umsetzung","Booth design and result")}</h4><p>{T(*bl)}</p></div>{sub}</section>'
    if I_.get('messe'):
        gal+=f'<section class="gsec"><div class="gh"><h4>{T("Die Messe","The fair")}</h4><p>{T("Eindrücke der Veranstaltung. Bilder: Veranstalter.","Impressions of the event. Images: organiser.")}</p></div><div class="gg">{tiles(f"f_{k}_m",I_["messe"],"Messe",False)}</div></section>'
    vo=I_.get('vor',[])
    if vo or k in POSTS:
        if vo:
            types=list(dict.fromkeys(TAGS.get(x,'banner') for x in vo))
            bl=SPEC.get((k,'vor'),(f'Gezeigt: {_list(types)}.',f'Shown: {_list(types,False)}.'))
            gal+=f'<section class="gsec"><div class="gh"><h4>{T("Werbung und Kommunikation","Advertising and communication")}</h4><p>{T(*bl)}</p></div><div class="gg">{tiles(f"f_{k}_v",vo,"Werbung",True)}</div></section>'
        if k in POSTS:
            def _card(q):
                ims=q['images'];g=f'li_{k}_'+(q['date'] or 'x').replace('-',''); G[g]=[(x,'LinkedIn') for x in ims]
                im=''.join(f'<button data-gallery="{g}" data-n="{i}"><img src="img/{x}" alt=""></button>' for i,x in enumerate(ims[:4]))
                dd=T(*q['datelabel']) if q.get('datelabel') else '.'.join(reversed(q['date'].split('-')))
                return f'<article class="li"><header><img src="img/t_cplogo.png" alt=""><div><b>CP Pumpen AG</b><small>LinkedIn · {dd}</small></div></header><div class="lit"><p>{_li(q["text"])}</p></div><button class="limore">{T("mehr","more")}</button><div class="limg n{min(len(ims),4)}">{im}</div><footer><span>👍 Gefällt mir</span><span>💬 Kommentieren</span><span>↗ Teilen</span></footer></article>'
            n=len(POSTS[k])
            bl=('Der Beitrag auf dem LinkedIn-Kanal von CP.','The post on CP’s LinkedIn channel.') if n==1 else (f'{n} Beiträge auf dem LinkedIn-Kanal von CP rund um die Messe.',f'{n} posts on CP’s LinkedIn channel around the fair.')
            gal+=f'<section class="gsec"><div class="gh"><h4>LinkedIn</h4><p>{T(*bl)}</p></div><div class="lig">{"".join(_card(q) for q in POSTS[k])}</div></section>'
    if k=='wega':
        gal+=f'<section class="gsec"><div class="gh"><h4>{T("Vorher und nachher","Before and after")}</h4><p>{T("Den Regler ziehen, um den alten und den neuen Stand zu vergleichen.","Drag the slider to compare the old and the new booth.")}</p></div><div class="rdi">{ba("wand_alt.jpg","wand_neu.jpg",("Messewand WEGA",))}</div></section>'
    br=I_.get('brief',[])
    if br:
        tot=BRIEF.get(k)
        bl=(f'Vor jeder Messe erstelle ich ein Briefing für das Standteam. Hier ein Auszug: {len(br)} von {tot} Seiten.',f'Before every fair I create a briefing for the booth team. An excerpt: {len(br)} of {tot} pages.') if tot else ('Vor jeder Messe erstelle ich ein Briefing für das Standteam. Hier ein Auszug.','Before every fair I create a briefing for the booth team. An excerpt.')
        gal+=f'<section class="gsec"><div class="gh"><h4>{T("Auszug aus dem Messebriefing","Excerpt from the fair briefing")}</h4><p>{T(*bl)}</p></div><div class="gg">{tiles(f"f_{k}_b",br,"Briefing",True)}</div></section>'
    c=cover(k)
    heroh=(f'<button class="sh-hero" data-gallery="h_{k}" data-n="0"><img src="img/{c}" alt="{name}"></button>' if c else '')
    if c: G[f'h_{k}']=[(c,name)]
    lk=f'<a class="lnk" href="{A}{link}" target="_blank" rel="noopener">{T("Ganze Projektseite ansehen","View the full project page")} ↗</a>' if link else ''
    i=ORDER.index(k); pv=ORDER[i-1] if i>0 else None; nx=ORDER[i+1] if i+1<len(ORDER) else None
    nm={f[0]:f[1] for f in F2}
    nav='<nav class="sh-nav">'+(f'<button data-fair="{pv}">‹ {nm[pv]}</button>' if pv else '<span></span>')+(f'<button data-fair="{nx}">{nm[nx]} ›</button>' if nx else '')+'</nav>'
    return (f'<article class="sheet" id="fs-{k}" hidden><p class="crumb">{T("Messen","Trade fairs")} · {T("Schweiz","Switzerland") if k in ("wega","immo") else "International"}</p><div class="sh-head"><div><h2>{name}</h2><p class="sh-sub">{T(*dat)} · {T(*ort)}</p></div><img class="sh-logo" src="img/t_{LOGO[k]}.jpg" alt="Logo {name}"></div>{heroh}'
            f'<dl class="facts">{facts}</dl><div class="sh-body"><div class="sh-text">{body}{lk}</div><aside>{tasks(*tk)}</aside></div>{gal}{nav}</article>')
yrs=[('2026',[f for f in F if '2026' in f[1]]),('2025',[f for f in F if '2025' in f[1]]),('2024',[f for f in F if '2024' in f[1]])]
intl=''.join(f'<div class="yr"><h4>{y}</h4></div><div class="fgrid">'+''.join(card(f) for f in fs)+'</div>' for y,fs in yrs)
SEC[0]=('international',('International','International'),('Messeauftritte von CP Pump Systems in Europa, den USA und Indien. Eine Messe anklicken, um Stand, Standdesign und Kommunikation im Detail zu sehen.','Trade fairs of CP Pump Systems in Europe, the USA and India. Click a fair to see the booth, booth design and communication in detail.'),intl)
for i_,x_ in enumerate(SEC):
    if x_[0]=='schweiz': SEC[i_]=('schweiz',('Schweiz','Switzerland'),('Regionale Publikumsmessen im Thurgau für GOLDINGER Immobilien.','Regional consumer fairs in Thurgau for GOLDINGER Immobilien.'),'<div class="fgrid">'+''.join(card(f) for f in SW)+'</div>')
EXTRA='<dialog id="fair" aria-label="Messe"><div class="fwrap"><button class="fclose" id="fclose" aria-label="Schliessen">✕</button>'+''.join(sheet(f) for f in F2)+'</div></dialog>'
