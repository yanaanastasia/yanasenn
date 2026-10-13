import re,subprocess
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
I=S+'/wb/page/img/'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
style=b[b.index('<style>'):b.index('</style>')+8]
style=style.replace('/* Layout: Projektseite Broschüren','/* Layout: Projektseite Werbung (abgeleitet von Broschüren)',1)
style=style.replace('</style>','''
.item{display:grid;grid-template-columns:230px minmax(0,1fr);gap:28px;padding-top:22px;border-top:1px solid var(--line)}
.item h3{margin-bottom:6px}.item .meta{font-size:.85rem;color:var(--muted);margin:0}
.client{display:inline-block;font:700 .68rem var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:6px}
.pages{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(min(var(--w,130px),100%),var(--w,130px)))}
.pages .zoom{aspect-ratio:var(--r)}
.grid4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.grid4 .zoom{aspect-ratio:1/1}.grid4 .zoom.plan img{padding:12px}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.grid2 .zoom{aspect-ratio:5/1}.grid2 .zoom.plan img{padding:8px}
.tag{font-size:.82rem;color:var(--muted)}
.sub{font:700 .78rem var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:8px 0 -6px}
.marquee{overflow:hidden;display:grid;gap:14px;mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.mrow{display:flex;gap:14px;width:max-content;animation:mq 60s linear infinite}
.mrow.rev{animation-direction:reverse;animation-duration:70s}
.marquee:hover .mrow{animation-play-state:paused}
.mrow img{height:190px;width:auto;border-radius:6px;box-shadow:0 6px 18px rgba(0,0,0,.12);background:#fff}
@keyframes mq{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.mrow{animation:none;flex-wrap:wrap;width:auto}}
@media (max-width:760px){.mrow img{height:120px}}
.ba{position:relative;border-radius:10px;overflow:hidden;border:1px solid var(--line);background:#fff;aspect-ratio:var(--r)}
.ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}
.ba .after{clip-path:inset(0 0 0 var(--p,50%))}
.ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.ba .bar{position:absolute;top:0;bottom:0;left:var(--p,50%);width:3px;background:var(--accent);transform:translateX(-50%);pointer-events:none}
.ba .bar::after{content:"⇆";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:var(--accent);color:#fff;border-radius:99px;padding:6px 9px;font-size:.9rem}
.ba .lbl{position:absolute;top:10px;font:700 .7rem var(--font);letter-spacing:.08em;text-transform:uppercase;background:rgba(0,0,0,.6);color:#fff;padding:4px 9px;border-radius:99px;pointer-events:none}
.ba .l1{left:10px}.ba .l2{right:10px;background:var(--accent)}
.babox{display:grid;gap:8px}
.report{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);border-radius:12px;overflow:hidden;border:1px solid var(--line);background:var(--surface)}
.report .rl{padding:28px;display:grid;gap:12px;align-content:start}
.report .rl small{font:700 .7rem var(--font);letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.report .rl b{font:700 1.3rem/1.25 var(--font)}
.report .rr{background:#1f5fa8;color:#fff;padding:28px;display:grid;gap:18px;align-content:center}
.report .rr div{display:grid}.report .rr strong{font:700 2rem/1 var(--font)}.report .rr span{font-size:.85rem;opacity:.85}
.langs{display:flex;gap:6px}.langs i{font-style:normal;font:700 .72rem var(--font);border:1px solid var(--line);border-radius:99px;padding:3px 9px}
@media (max-width:760px){.report{grid-template-columns:minmax(0,1fr)}}
.wide .pages{grid-template-columns:minmax(0,1fr)}
@media (max-width:760px){.item{grid-template-columns:minmax(0,1fr);gap:12px}.grid4{grid-template-columns:repeat(2,minmax(0,1fr))}.grid2{grid-template-columns:minmax(0,1fr)}}
</style>''')
def size(f): return tuple(map(int,subprocess.run(['identify','-format','%w %h',I+f],capture_output=True,text=True).stdout.split()))
G={}
def fig(g,s,c,cls='page',cap=True):
    G.setdefault(g,[]).append((s,c)); n=len(G[g])-1
    fc=f'<figcaption class="tag">{c}</figcaption>' if cap else ''
    return f'<figure><button class="zoom {cls}" data-gallery="{g}" data-n="{n}" aria-label="{c} gross ansehen"><img src="img/{s}" alt="{c}"></button>{fc}</figure>'
def item(g,title,client,meta,files,w=130):
    W,H=size(files[0]); r=f'{W}/{H}'
    pg=''.join(fig(g,f,f'{title}, Seite {i+1}' if len(files)>1 else title,cap=False) for i,f in enumerate(files))
    return f'<div class="item"><div><span class="client">{client}</span><h3>{title}</h3><p class="meta">{meta}</p></div><div class="pages" style="--r:{r};--w:{w}px">{pg}</div></div>'

CP='CP Pump Systems'; GO='GOLDINGER Immobilien'; FR='Freelance'
def ba(a,b,cap):
    W,H=size(a)
    return f'<figure class="babox"><div class="ba" style="--r:{W}/{H}"><img src="img/{a}" alt="Vorher: {cap}"><img class="after" src="img/{b}" alt="Nachher: {cap}"><span class="bar"></span><span class="lbl l1">Vorher</span><span class="lbl l2">Nachher</span><input type="range" min="0" max="100" value="50" aria-label="Vorher und Nachher vergleichen: {cap}"></div><figcaption class="tag">{cap}</figcaption></figure>'
def grid(g,L,cls='grid4'): return f'<div class="{cls}">'+''.join(fig(g,f,c,'plan') for f,c in L)+'</div>'
WIDE=lambda g,ti,cl,me,f: item(g,ti,cl,me,[f],900).replace('class="item"','class="item wide"')
F={}  # key -> (category, title, cover, intro, html)
F['inserate']=('Grafik & Print','Inserate','i_petro.jpg','Inserate in Fachzeitschriften, Messekatalogen, Magazinen und Regionalzeitungen, jeweils in der Sprache des Zielpublikums.',
  '<p class="sub">CP Pump Systems</p>'+grid('ins1',[('anzeige.jpg','World Fertilizer, Fachzeitschrift'),('i_tfs.jpg','The Fertilizer Show, Katalog'),('i_dk.jpg','DK Hub, Katalog'),('i_petro.jpg','Petrochymia, Katalog'),('i_chemuk.jpg','ChemUK, Katalog')])
  +'<p class="sub">GOLDINGER Immobilien</p>'+grid('ins2',[('g_hev22.jpg','Hauseigentümer-Magazin: Website und 35 Jahre'),('g_hev23.jpg','Hauseigentümer-Magazin: Ratgeber'),('g_wega.jpg','Messe WEGA'),('g_sgkb.jpg','Infoabende, grosses Format'),('g_kreuz.jpg','Infoabende, kleines Format'),('g_tkb.jpg','Infoabende, Gesamtausgabe'),('sck.jpg','Clubmagazin eines Sportclubs')]))
F['flyer']=('Grafik & Print','Flyer','g_sonnenhof-1.jpg','Flyer für Veranstaltungen, Neubauprojekte und Angebote, mit allen Seiten.',
  item('gut','Gutschein Wertermittlung',GO,'A5 quer, vier Seiten',[f'g_gutschein-{i}.jpg' for i in range(1,5)],200)
  +item('sonne','Neubauprojekt Sonnenhof',GO,'A5, zwei Seiten',['g_sonnenhof-1.jpg','g_sonnenhof-2.jpg'])
  +item('gruen','Tag der offenen Tür',GO,'Flyer zu einem Neubauprojekt',['g_gruenblick.jpg'])
  +item('us','Molten Sulphur',CP,'US-Letter, zwei Seiten',['ms_us-1.jpg','ms_us-2.jpg']))
F['infoblaetter']=('Grafik & Print','Infoblätter','ms_fact-1.jpg','Kompakte Informationen zu Produkten und Angeboten, für Messen, Kundentermine und als Download.',
  item('fact','Factsheet Molten Sulphur',CP,'A4, zwei Seiten, Englisch',['ms_fact-1.jpg','ms_fact-2.jpg'])
  +item('lead','Sofort verfügbare Pumpensysteme',CP,'A4, Deutsch und Englisch',['f_lead.jpg']))
F['messegrafik']=('Grafik & Print','Messegrafik','m_petro26.jpg','Rückwände, Blenden und Folien für die Messestände, jeweils in der Sprache des Messelandes und abgestimmt auf die Standgrösse.',
  '<p class="sub">Rückwände</p>'
  +WIDE('mw1','Petrochymia 2024',CP,'Sechs Paneele, Französisch','m_petro24.jpg')
  +WIDE('mw2','Pumps & Valves Dortmund 2025',CP,'Zwei Wände eines Eckstands','m_pv25.jpg')
  +WIDE('mw3','Pétro+Chimie Le Havre 2025',CP,'Design der Petrochymia 2024 weitergeführt','m_lehavre.jpg')
  +WIDE('mw4','Fertilizer Latino Americano 2026',CP,'Rückwand, Englisch','m_fla.jpg')
  +WIDE('mw5','DK Hub Dunkerque 2026',CP,'Paneele und Kabinentür, Französisch','m_dk.jpg')
  +WIDE('mw6','ChemUK 2026',CP,'Rückwand 6 m, Englisch','m_chemuk.jpg')
  +WIDE('mw7','Petrochymia 2026',CP,'Paneele mit Anlagenfoto und neuer Weltkarte','m_petro26.jpg')
  +WIDE('mw8','CRU Sulphur + Sulphuric Acid Berlin 2026',CP,'«Keep Your Molten Sulphur Flowing», drei Paneele','ms_wand.jpg')
  +'<p class="sub">Blenden</p><div class="banners">'+''.join(fig('bl',f,c,'plan') for f,c in [('f_p24_fac6.jpg','Petrochymia 2024, 6 m'),('f_dk.jpg','DK Hub 2026'),('f_uk_fascia.jpg','ChemUK 2026, 6 m'),('f_p26.jpg','Petrochymia 2026, 6 m')])+'</div>'
  +'<p class="sub">Folien</p>'+grid('fo',[('m_achema.jpg','ACHEMA 2024: Folie für die Theke')]))
F['redesigns']=('Corporate Design & Raum','Redesigns','mappe23-1.jpg','Bei GOLDINGER habe ich bestehende Werbemittel neu gestaltet: klares Blau und Weiss, grosse Bilder, wenig Text. Den Regler ziehen, um alt und neu zu vergleichen.',
  ba('wand_alt.jpg','wand_neu.jpg','Messewand WEGA')+ba('mappe22-1.jpg','mappe23-1.jpg','Faltmappe, Aussenseite')+ba('mappe22-2.jpg','mappe23-2.jpg','Faltmappe, Innenseite')
  +ba('g_info22-1.jpg','g_info23-1.jpg','Flyer Infoabende, Vorderseite')+ba('g_info22-2.jpg','g_info23-2.jpg','Flyer Infoabende, Rückseite'))
F['website']=('Digital & Social Media','Website','web_report.jpg','Beiträge für die Website von CP Pump Systems.',
  '<div class="report"><div class="rl"><small>Anwendungsbericht · Düngemittelproduktion</small><b>Dichtungslose Magnetkupplungspumpen für die Förderung von saurem Prozesswasser</b><p>Für ein neues Rückführungssystem von Pondwasser in einem Düngemittelwerk brauchte es eine dichte, korrosionsbeständige Lösung. Drei Magnetkupplungspumpen fördern das saure Wasser zurück in den Prozess. Den Bericht verfasste ich mit fachlicher Unterstützung des Verkaufsteams und veröffentlichte ihn in drei Sprachen.</p><div class="langs"><i>DE</i><i>EN</i><i>FR</i></div></div><div class="rr"><div><strong>3</strong><span>Pumpen MKP 200-150-500</span></div><div><strong>682 m³/h</strong><span>Förderstrom gesamt</span></div><div><strong>72,6 %</strong><span>hydraulischer Wirkungsgrad</span></div></div></div>')
F['emailbanner']=('Digital & Social Media','E-Mail-Banner','b_tfs_banner.jpg','Zu jeder Messe ein Banner für Einladungen und E-Mail-Signaturen, dazu ein Sammelbanner mit allen kommenden Messen.',
  '<div class="banners">'+''.join(fig('eb',f,c,'plan') for f,c in [('b_cru_banner.jpg','CRU Sulphur + Sulphuric Acid'),('b_tfs_banner.jpg','The Fertilizer Show'),('b_fla.jpg','Fertilizer Latino Americano'),('b_pv.jpg','Pumps & Valves'),('b_dk.jpg','DK Hub'),('b_sammel_de.jpg','Sammelbanner aller Messen')])+'</div>')
F['webbanner']=('Digital & Social Media','Web-Banner','b_petro.jpg','Banner für die Websites der Messeveranstalter.',
  '<div class="banners">'+fig('wb','b_petro.jpg','Petrochymia, 1000 × 90','plan')+'</div>')
F['linkedin']=('Digital & Social Media','LinkedIn','b_aug.jpg','Grafiken für die LinkedIn-Seite von CP Pump Systems.',
  grid('li',[('b_aug.jpg','1. August'),('b_fla_social.jpg','Fertilizer Latino Americano')]))
A='https://claude.ai/artifact/'
N={'inserate':12,'flyer':4,'infoblaetter':2,'messegrafik':13,'redesigns':5,'website':1,'emailbanner':6,'webbanner':1,'linkedin':2}
HL=[('ACHEMA 2024 in Frankfurt','h_achema.jpg','XWP2ub9yg6MDibVE8ZQZ2c'),('Weihnachten 2026','h_xmas.jpg','1ub6RRXMbhZQRUq33avRvH'),('Mobiler Messestand für die USA','h_usa.jpg','5CenZNzAZtaKJN37GonvR1'),('Broschüren in neun Sprachen','h_bro.jpg','6CM4QZGbNhy5bjxvvMbnbc'),('Immobilien-Reels','h_reels.jpg','AWzk8y7iyFhZyJJQF4gszF'),('Die Marke im eigenen Gebäude','h_marke.jpg','3YqAhMFfdAX84mYeGeTHFW')]
hl=''.join(f'<a class="hcard" href="'+A+f'{u}" target="_blank" rel="noopener"><span class="himg"><img src="img/{img}" alt=""></span><b>{ti}</b></a>' for ti,img,u in HL)
# category -> list of (title, kind, target) kind: v=view, a=artifact, s=soon
CATS=[('Messen',[('International','s',''),('Schweiz','s','')]),
 ('Grafik & Print',[('Broschüren und Magazin','a','6CM4QZGbNhy5bjxvvMbnbc|h_bro.jpg'),('Flyer','v','flyer'),('Inserate','v','inserate'),('Infoblätter','v','infoblaetter'),('Grusskarten','a','Fb4PomaQSsp4yY18TA8Uks|h_song.jpg'),('Messegrafik','v','messegrafik'),('Infografiken','a','6FrfmXHa7BUcfu8ZvPWrZE|h_info.jpg')]),
 ('Corporate Design & Raum',[('Raumgestaltung','a','3YqAhMFfdAX84mYeGeTHFW|h_marke.jpg'),('Redesigns','v','redesigns'),('Markenidentität','s','')]),
 ('Digital & Social Media',[('Website','v','website'),('Newsletter','s',''),('E-Mail-Banner','v','emailbanner'),('Web-Banner','v','webbanner'),('LinkedIn','v','linkedin'),('Instagram','s','')]),
 ('Foto & Video',[('Firmenshooting','s',''),('Reportage','s',''),('Immobilienvideos','a','AWzk8y7iyFhZyJJQF4gszF|h_reels.jpg'),('Erklärvideos','s','')]),
 ('Werbeartikel',[('Giveaways','s',''),('Kunden- und Mitarbeitergeschenke','a','1ub6RRXMbhZQRUq33avRvH|h_xmas.jpg'),('Arbeits- und Messekleidung','s','')])]
PV={};SV={}
over=f'<section class="chapter"><p class="eyebrow">Ausgewählte Projekte</p><div class="hgrid">{hl}</div></section>'
for c,fs in CATS:
    cards=''
    for ti,k,tg in fs:
        if k=='v':
            v=F[tg]; cards+=f'<a class="fcard" href="#{tg}"><span class="fimg"><img src="img/{v[2]}" alt=""></span><b>{ti}</b><small>{N[tg]} {"Arbeit" if N[tg]==1 else "Arbeiten"}</small></a>'
        elif k=='a':
            u,img=tg.split('|'); key='p_'+u[:6]
            cards+=f'<a class="fcard" href="#{key}"><span class="fimg"><img src="img/{img}" alt=""></span><b>{ti}</b><small>1 Projekt</small></a>'
            PV[key]=(c,ti,u,img)
        else:
            key='s_'+str(len(SV)); SV[key]=(c,ti)
            cards+=f'<a class="fcard soon" href="#{key}"><span class="fimg"></span><b>{ti}</b><small>folgt</small></a>'
    over+=f'<section class="chapter"><p class="eyebrow">{c}</p><div class="fgrid">{cards}</div></section>'
PT={'6CM4QZ': 'Broschüren in neun Sprachen', 'Fb4Pom': 'Songkran-Grusskarte', '6FrfmX': 'Weltkarte und Zeitstrahl', '3YqAhM': 'Die Marke im eigenen Gebäude', 'AWzk8y': 'Immobilien-Reels', '1ub6RR': 'Weihnachten 2026'}
SVH=''.join(f'<section class="fview" id="{k}" hidden><a class="back" href="#">← Alle Arbeiten</a><p class="eyebrow">{c}</p><h1>{ti}</h1><p class="lead">Diese Seite folgt.</p></section>' for k,(c,ti) in SV.items())
views=''.join(f'<section class="fview" id="{k}" hidden><a class="back" href="#">← Alle Arbeiten</a><p class="eyebrow">{c}</p><h1>{ti}</h1><div class="hgrid"><a class="hcard" href="'+A+f'{u}" target="_blank" rel="noopener"><span class="himg"><img src="img/{img}" alt=""></span><b>{PT[u[:6]]} ↗</b></a></div><p class="meta">Weitere Arbeiten folgen.</p></section>' for k,(c,ti,u,img) in PV.items())+''.join(f'<section class="fview" id="{k}" hidden><a class="back" href="#">← Alle Arbeiten</a><p class="eyebrow">{v[0]}</p><h1>{v[1]}</h1><p class="lead">{v[3]}</p>{v[4]}</section>' for k,v in F.items())
style=style.replace('</style>',"""
.fgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.fcard{display:grid;gap:6px;text-decoration:none;color:var(--ink)}
.fimg{aspect-ratio:4/3;border-radius:10px;border:1px solid var(--line);background:#fff;overflow:hidden;display:block}
.fimg img{width:100%;height:100%;object-fit:contain;padding:10px;transition:transform .25s}
.fcard:hover .fimg img{transform:scale(1.04)}
.fcard small{color:var(--muted);font-size:.8rem}
.hgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.hcard{display:grid;gap:8px;text-decoration:none;color:var(--ink)}.himg{aspect-ratio:16/10;border-radius:12px;overflow:hidden;display:block;background:#eee}
.himg img{width:100%;height:100%;object-fit:cover;transition:transform .3s}.hcard:hover .himg img{transform:scale(1.04)}
.soon{opacity:.55}.soon .fimg{background:repeating-linear-gradient(45deg,var(--surface),var(--surface) 8px,var(--bg) 8px,var(--bg) 16px)}
@media (max-width:760px){.hgrid{grid-template-columns:minmax(0,1fr)}}
.fview{display:grid;gap:22px}.fview[hidden]{display:none}.back{color:var(--accent);text-decoration:none;font-weight:700}
@media (max-width:760px){.fgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (prefers-reduced-motion:reduce){.fcard .fimg img{transition:none}}
</style>""")
body=f'<div class="wrap"><p class="note">Entwurf der Seite «Arbeiten»: Projekte und Ordner anklicken. Ordner mit «folgt» sind noch in Arbeit.</p><div id="overview" class="fview"><h1>Arbeiten</h1>{over}</div>{views}{SVH}</div>'
NAVJS="""
// Ordner-Navigation und Vorher/Nachher
function route(){const h=location.hash.slice(1);document.querySelectorAll('.fview').forEach(s=>s.hidden=h?s.id!==h:s.id!=='overview');window.scrollTo(0,0);}
addEventListener('hashchange',route);route();
document.querySelectorAll('.ba input').forEach(r=>r.addEventListener('input',()=>r.parentElement.style.setProperty('--p',r.value+'%')));
"""
d=b[b.index('<dialog id="lb"'):b.index('</dialog>')+9]
scr=b[b.index('<script>'):b.index('</script>')+9]
gjs='const G={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in G.items())+'\n};'
scr=re.sub(r'const G=\{.*?\n\};',lambda m:gjs,scr,flags=re.S)
SWJS="\n// Vorher/Nachher\ndocument.querySelectorAll('.ba input').forEach(r=>r.addEventListener('input',()=>r.parentElement.style.setProperty('--p',r.value+'%')));\n"
i=scr.find('// Sprachen-Umschalter')
if i>0: scr=scr[:i]+'</script>'
scr=scr[:scr.rindex('</script>')]+NAVJS+'</script>'
out='<title>Arbeiten Übersicht</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/wb/page/ordner.html','w',encoding='utf-8').write(out)
print('ok',sum(len(v) for v in G.values()))
