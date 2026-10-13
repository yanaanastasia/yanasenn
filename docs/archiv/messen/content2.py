# Messen v2: ruhige Übersicht + Detailansicht pro Messe
exec(open(S+'/me/content.py',encoding='utf-8').read())
import json
IM=json.load(open(S+'/me/imgs.json'))
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
CAT=[('stand',('Am Stand','At the booth')),('design',('Standdesign','Booth design')),('komm',('Kommunikation','Communication'))]
COVER={'petro24':'d_petro24_design0.jpg','fla26':'d_fla26_design0.jpg','cru26':'d_cru26_design0.jpg','tfs26':'d_tfs26_komm0.jpg','petro26':'d_petro26_design0.jpg','dahej26':'d_dahej26_komm0.jpg','tps':'d_tps_stand2.jpg'}
def cover(k):
    if k in COVER: return COVER[k]
    for c,_ in CAT:
        if IM.get(k,{}).get(c): return IM[k][c][0]
    return None
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
    allimgs=[]
    for c,lab in CAT:
        fs=IM.get(k,{}).get(c,[])
        if not fs: continue
        gid=f'f_{k}_{c}'; G[gid]=[(x,f'{name} · {lab[0]}') for x in fs]
        tiles=''.join(f'<button class="gt{" fit" if c!="stand" else ""}" data-gallery="{gid}" data-n="{i}"><img src="img/{x}" alt="{name}, {lab[0]} {i+1}"></button>' for i,x in enumerate(fs))
        gal+=f'<section class="gsec"><h4>{T(*lab)}</h4><div class="gg">{tiles}</div></section>'
        allimgs+=fs
    c=cover(k)
    heroh=(f'<div class="sh-hero{" fit" if c and ("design" in c or "komm" in c) else ""}"><img src="img/{c}" alt="{name}"></div>' if c else '')
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
