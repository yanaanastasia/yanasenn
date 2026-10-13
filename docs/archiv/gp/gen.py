import re,subprocess
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
I=S+'/gp/page/img/'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
style=b[b.index('<style>'):b.index('</style>')+8]
style=style.replace('/* Layout: Projektseite Broschüren','/* Layout: Kategorie Grafik & Print (abgeleitet von Broschüren)',1)
style=style.replace('</style>','''
.fgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
.fcard{display:grid;gap:8px;text-decoration:none;color:var(--ink)}
.fimg{aspect-ratio:4/3;border-radius:12px;border:1px solid var(--line);background:#fff;overflow:hidden;display:block}
.fimg img{width:100%;height:100%;object-fit:contain;padding:12px;transition:transform .3s}
.fcard:hover .fimg img{transform:scale(1.04)}
.fcard b{font-size:1.05rem}.fcard small{color:var(--muted);font-size:.82rem}
.fview{display:grid;gap:28px}.fview[hidden]{display:none}
.back{color:var(--accent);text-decoration:none;font-weight:700;font-size:.9rem}
.crumb{font-size:.8rem;color:var(--muted)}
.entry{display:grid;grid-template-columns:260px minmax(0,1fr);gap:32px;padding-top:28px;border-top:1px solid var(--line)}
.entry .cover .zoom{aspect-ratio:var(--r)}
.client{display:inline-block;font:700 .68rem var(--font);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.entry h3{font-size:1.3rem;margin:4px 0 8px}
.entry .txt{display:grid;gap:12px;align-content:start}
.facts2{display:flex;flex-wrap:wrap;gap:6px}.facts2 span{font-size:.78rem;border:1px solid var(--line);border-radius:99px;padding:3px 10px;color:var(--muted)}
details.more summary{cursor:pointer;font-weight:700;color:var(--accent);list-style:none;display:inline-flex;gap:6px;align-items:center}
details.more summary::-webkit-details-marker{display:none}
details.more summary::after{content:"+";font-size:1.1rem}details.more[open] summary::after{content:"–"}
details.more .inner{display:grid;gap:14px;margin-top:14px}
.pages{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(min(var(--w,120px),100%),var(--w,120px)))}
.pages .zoom{aspect-ratio:var(--r)}
.btn{display:inline-block;background:var(--accent);color:#fff;border:0;border-radius:99px;padding:9px 16px;font:700 .88rem var(--font);text-decoration:none;cursor:pointer;justify-self:start}
.btn.ghost{background:transparent;color:var(--accent);border:1px solid var(--accent)}
.wall .zoom{aspect-ratio:var(--r)}
@media (max-width:760px){.fgrid{grid-template-columns:repeat(2,minmax(0,1fr))}.entry{grid-template-columns:minmax(0,1fr);gap:14px}.entry .cover{max-width:260px}}
@media (prefers-reduced-motion:reduce){.fcard .fimg img{transition:none}}
</style>''')
def size(f): return tuple(map(int,subprocess.run(['identify','-format','%w %h',I+f],capture_output=True,text=True).stdout.split()))
G={}
def zb(g,s,c,cls='page'):
    G.setdefault(g,[]).append((s,c)); n=len(G[g])-1
    return f'<button class="zoom {cls}" data-gallery="{g}" data-n="{n}" aria-label="{c} gross ansehen"><img src="img/{s}" alt="{c}"></button>'
CP='CP Pump Systems'; GO='GOLDINGER Immobilien'
A='https://claude.ai/artifact/'
def entry(g,client,title,intro,files,facts=(),more='',w=120,cover_w=None,extra='',open_label='Mehr Infos'):
    W,H=size(files[0])
    cov=zb(g,files[0],f'{title}'+(', Seite 1' if len(files)>1 else ''),'page' if H>W*0.9 else 'plan')
    pages=''.join(f'<figure>{zb(g,f,f"{title}, Seite {i+2}")}</figure>' for i,f in enumerate(files[1:]))
    pw,ph=size(files[1]) if len(files)>1 else (W,H)
    fc=''.join(f'<span>{x}</span>' for x in facts)
    inner=''
    if len(files)>1: inner+=f'<div class="pages" style="--r:{pw}/{ph};--w:{w}px">{pages}</div>'
    if more: inner+=more
    det=f'<details class="more"><summary>{open_label}</summary><div class="inner">{inner}</div></details>' if inner else ''
    return f'<article class="entry"><div class="cover" style="--r:{W}/{H}">{cov}</div><div class="txt"><span class="client">{client}</span><h3>{title}</h3><p>{intro}</p><div class="facts2">{fc}</div>{extra}{det}</div></article>'
def wall(g,client,title,intro,f,facts=()):
    W,H=size(f); fc=''.join(f'<span>{x}</span>' for x in facts)
    return f'<article class="entry" style="grid-template-columns:minmax(0,1fr)"><div class="txt"><span class="client">{client}</span><h3>{title}</h3><p>{intro}</p><div class="facts2">{fc}</div></div><div class="wall" style="--r:{W}/{H}">{zb(g,f,title,"plan")}</div></article>'
F={}
# 1 Broschüren und Magazin
hm=[f'hm-{i:02d}.jpg' for i in range(1,13)]
F['broschueren']=('Broschüren und Magazin','cover_01.jpg','Produkt- und Firmenbroschüren für CP Pump Systems und das Hausmagazin von GOLDINGER Immobilien.',
 entry('bro9',CP,'Broschüren in neun Sprachen','Ein einheitliches Konzept für alle Firmen- und Produktbroschüren: gleicher Aufbau, ein zentrales Masterdokument, Sprachversionen bis ins Chinesische und Polnische.',[f'cover_{i:02d}.jpg' for i in range(1,11)],('Company Profile','Sortimentsbroschüre','8 Produktbroschüren','9 Sprachen'),extra=f'<a class="btn" href="{A}6CM4QZGbNhy5bjxvvMbnbc" target="_blank" rel="noopener">Zum Projekt ↗</a>',open_label='Alle Titelseiten')
 +entry('msb',CP,'Broschüre Molten Sulphur','Acht Seiten zu Pumpen, die flüssigen Schwefel fördern: Gelb, Dreiecksmuster und die Schnittzeichnung der beheizten Pumpe. Die Texte basieren auf bestehendem Material und sind mit dem Verkauf abgestimmt.',[f'ms_bro-{i}.jpg' for i in range(1,9)],('A4','8 Seiten','Englisch'),open_label='Alle Seiten')
 +entry('hm',GO,'Hausmagazin «Die IMMO-EXPERTEN»','GOLDINGER gab zweimal im Jahr ein eigenes Magazin heraus, mit aktuellen Immobilien, Neubauprojekten und der Einladung zu den Infoabenden; es lag auch Zeitungen in der Ostschweiz bei. Ich gestaltete das Magazin, schrieb die Texte gemeinsam mit dem Verkaufsteam und organisierte die Verteilung als Zeitungsbeilage.',hm,('A4','12 Seiten','Ausgabe Februar 2023'),extra='<button class="btn" data-open="hm">Magazin durchblättern</button>',open_label='Alle Seiten',w=110))
# 2 Flyer
F['flyer']=('Flyer','g_sonnenhof-1.jpg','Flyer für Veranstaltungen, Neubauprojekte und Angebote.',
 entry('f1',GO,'Infoabende','Einladung zu den Infoabenden für private Immobilieneigentümer, mit Terminen an mehreren Standorten und Anmeldung per QR-Code.',['g_info23-1.jpg','g_info23-2.jpg'],('A5 quer','2 Seiten'),w=220)
 +entry('f2',GO,'Gutschein Wertermittlung','Klappkarte mit Gutschein für eine kostenlose Immobilienbewertung und Antwortkarte.',[f'g_gutschein-{i}.jpg' for i in range(1,5)],('A5 quer','4 Seiten'),w=200)
 +entry('f3',GO,'Neubauprojekt Sonnenhof','Flyer zu einem Neubauprojekt mit Eigentumswohnungen.',['g_sonnenhof-1.jpg','g_sonnenhof-2.jpg'],('A5','2 Seiten'))
 +entry('f4',GO,'Tag der offenen Tür','Einladung zur Besichtigung eines Neubauprojekts.',['g_gruenblick.jpg'],('A5',))
 +entry('f5',CP,'Molten Sulphur für die USA','Zweiseitiger Flyer im US-Letter-Format für die Messen in den USA.',['ms_us-1.jpg','ms_us-2.jpg'],('US-Letter','2 Seiten','Englisch')))
# 3 Inserate
ins=lambda L:'<div class="pages" style="--r:1/1;--w:180px">'+''.join(f'<figure>{zb(g,f,c,"plan")}<figcaption class="tag">{c}</figcaption></figure>' for g,f,c in L)+'</div>'
F['inserate']=('Inserate','i_petro.jpg','Inserate in Fachzeitschriften, Messekatalogen, Magazinen und Regionalzeitungen.',
 entry('i1',CP,'World Fertilizer','Halbseitiges Inserat in einer internationalen Fachzeitschrift für die Düngemittelindustrie.',['anzeige.jpg'],('Fachzeitschrift','Englisch'))
 +entry('i2',CP,'Messekataloge','Inserate in den Katalogen der Fachmessen, jeweils in der Sprache des Messelandes und abgestimmt auf die ausgestellten Pumpen.',['i_petro.jpg','i_dk.jpg','i_chemuk.jpg','i_tfs.jpg'],('Französisch','Englisch'),w=150,open_label='Alle Inserate')
 +entry('i3',GO,'Hauseigentümer-Magazin','Inserate zur neuen Website, zum 35-Jahr-Jubiläum und zu den Ratgebern für Eigentümer.',['g_hev23.jpg','g_hev22.jpg'],('A4',),open_label='Weiteres Inserat')
 +entry('i4',GO,'Infoabende in Regionalzeitungen','Serie in mehreren Formaten für verschiedene Regionalausgaben.',['g_sgkb.jpg','g_kreuz.jpg','g_tkb.jpg'],('3 Formate',),w=220,open_label='Alle Formate')
 +entry('i5',GO,'Messe WEGA','Inserat mit dem Angebot, den Wert der eigenen Immobilie direkt am Messestand schätzen zu lassen.',['g_wega.jpg'])
 +entry('i6',GO,'Clubmagazin','Inserat im Magazin eines Sportclubs.',['sck.jpg']))
# 4 Infoblätter
F['infoblaetter']=('Infoblätter','ms_fact-1.jpg','Kompakte Informationen zu Produkten und Angeboten, für Messen, Kundentermine und als Download.',
 entry('ib1',CP,'Factsheet Molten Sulphur','Zwei Seiten zu beheizten Pumpen für flüssigen Schwefel. Komplett von mir gestaltet; die Texte basieren auf bestehendem Material und sind mit dem Verkauf abgestimmt.',['ms_fact-1.jpg','ms_fact-2.jpg'],('A4','2 Seiten','Englisch'))
 +entry('ib2',CP,'Sofort verfügbare Pumpensysteme','Übersicht über Pumpensysteme ab Lager mit kurzer Lieferzeit.',['f_lead.jpg'],('A4','Deutsch und Englisch')))
# 5 Grusskarten
F['grusskarten']=('Grusskarten','x_karteA-2.jpg','Karten zu Weihnachten und zum thailändischen Neujahr, für Kundschaft und Mitarbeitende.',
 entry('g1',CP,'Weihnachtskarten 2026','Rentiere ziehen einen Schlitten mit einer CP-Pumpe über verschneite Berge; innen ein Zahlen-verbinden-Rätsel. Karten für A- und B-Kunden und Mitarbeitende, in Deutsch, Englisch und Französisch, personalisiert im Seriendruck.',['x_karteA-2.jpg','x_karteA-3.jpg','x_karteA-1.jpg','x_karteA-4.jpg','x_karteA-5.jpg'],('3 Sprachen','Sie- und Du-Form'),extra=f'<a class="btn" href="{A}1ub6RRXMbhZQRUq33avRvH" target="_blank" rel="noopener">Ganze Kampagne ↗</a>',open_label='Weitere Seiten')
 +entry('g2',CP,'Songkran-Grusskarte','Zum thailändischen Neujahrsfest: zwei Pagoden mit der thailändischen und der Schweizer Flagge, dazu Wasserspritzer und Blüten. Die Karte ging an Kundschaft und weitere Kontakte in Thailand; Ideen, Skizzen, Gestaltung, Druckvorbereitung und Bestellung lagen bei mir.',['karte-1.jpg','karte-2.jpg','skizze.jpg'],('A5','Englisch'),open_label='Rückseite und Skizze'))
# 6 Messegrafik
F['messegrafik']=('Messegrafik','m_petro26.jpg','Rückwände, Blenden und Folien für die Messestände, jeweils in der Sprache des Messelandes und abgestimmt auf die Standgrösse.',
 wall('w1',CP,'Petrochymia 2026','Paneele mit Anlagenfoto, der neuen Weltkarte und Swiss-Made-Zeichen.','m_petro26.jpg',('Französisch',))
 +wall('w2',CP,'ChemUK 2026','Rückwand mit Weltkarte und Kernbotschaft.','m_chemuk.jpg',('6 m','Englisch'))
 +wall('w3',CP,'CRU Sulphur + Sulphuric Acid Berlin 2026','«Keep Your Molten Sulphur Flowing», drei Paneele.','ms_wand.jpg',('Englisch',))
 +wall('w4',CP,'DK Hub Dunkerque 2026','Paneele und Tür der Standkabine.','m_dk.jpg',('Französisch',))
 +wall('w5',CP,'Fertilizer Latino Americano 2026','Rückwand mit Birkenwald und Claim.','m_fla.jpg',('Englisch',))
 +wall('w6',CP,'Pumps & Valves Dortmund 2025','Zwei Wände eines Eckstands.','m_pv25.jpg',('Englisch',))
 +wall('w7',CP,'Pétro+Chimie Le Havre 2025','Design der Petrochymia 2024 weitergeführt.','m_lehavre.jpg',('Französisch',))
 +wall('w8',CP,'Petrochymia 2024','Sechs Paneele mit Weltkarte und Wassermotiv.','m_petro24.jpg',('Französisch',))
 +'<article class="entry" style="grid-template-columns:minmax(0,1fr)"><div class="txt"><span class="client">CP Pump Systems</span><h3>Blenden und Folien</h3></div><div class="pages" style="--r:10/1;--w:420px">'+''.join(f'<figure>{zb("bl",f,c,"plan")}<figcaption class="tag">{c}</figcaption></figure>' for f,c in [('f_p26.jpg','Blende Petrochymia 2026'),('f_uk_fascia.jpg','Blende ChemUK 2026'),('f_dk.jpg','Blende DK Hub 2026'),('f_p24_fac6.jpg','Blende Petrochymia 2024')])+'</div><div class="pages" style="--r:1161/1408;--w:160px"><figure>'+zb('bl2','m_achema.jpg','ACHEMA 2024: Folie für die Theke')+'<figcaption class="tag">Folie Theke, ACHEMA 2024</figcaption></figure></div></article>')
# 7 Infografiken
F['infografiken']=('Infografiken','neu.jpg','Weltkarte und Firmengeschichte als wiederverwendbare Grafiken für Broschüren, Messen und Website.',
 entry('k1',CP,'Weltkarte der Standorte','Standorte, Tochterfirmen und Niederlassungen sowie Mitarbeitende in weiteren Ländern. Die finale Fassung ist ein Punktraster in zwei Formaten: breit für die Messewände, im Hochformat für die Broschüren. Vorher: zuerst grau, dann eine erste Überarbeitung in CP-Blau.',['neu.jpg','neu_en.jpg','bro_neu.jpg','bro_grau.jpg','alt_blau.jpg'],('Deutsch, Englisch, Französisch u. a.',),w=200,open_label='Fassungen und Vorher')
 +entry('k2',CP,'Firmengeschichte als Zeitstrahl','Zwei A4-Seiten im Company Profile, «passioniert – swiss made – innovativ»: Meilensteine von der Gründung bis heute als Schlangenlinie mit Bildern von Produkten, Maschinen, Gebäuden und Flaggen für neue Märkte.',['zs_spread.jpg','zs_spread_en.jpg'],('7 Sprachfassungen',),w=300,open_label='Englische Fassung'))
ORDER=['broschueren','flyer','inserate','infoblaetter','grusskarten','messegrafik','infografiken']
N={'broschueren':'3 Arbeiten','flyer':'5 Arbeiten','inserate':'6 Arbeiten','infoblaetter':'2 Arbeiten','grusskarten':'2 Arbeiten','messegrafik':'9 Arbeiten','infografiken':'2 Arbeiten'}
cards=''.join(f'<a class="fcard" href="#{k}"><span class="fimg"><img src="img/{F[k][1]}" alt=""></span><b>{F[k][0]}</b><small>{N[k]}</small></a>' for k in ORDER)
over=f'<section id="overview" class="fview"><p class="crumb">Arbeiten</p><p class="eyebrow">Kategorie</p><h1>Grafik &amp; Print</h1><p class="lead">Broschüren, Flyer, Inserate, Karten und Messegrafik für CP Pump Systems und GOLDINGER Immobilien, vom Layout bis zur fertigen Druckdatei.</p><div class="fgrid">{cards}</div></section>'
views=''.join(f'<section class="fview" id="{k}" hidden><a class="back" href="#">← Grafik &amp; Print</a><p class="crumb">Arbeiten · Grafik &amp; Print</p><h1>{F[k][0]}</h1><p class="lead">{F[k][2]}</p>{F[k][3]}</section>' for k in ORDER)
body=f'<div class="wrap"><p class="note">Entwurf der Kategorie «Grafik &amp; Print»: Ordner anklicken, «Mehr Infos» aufklappen, Bilder vergrössern.</p>{over}{views}</div>'
NAV="""
// Ordner-Navigation
function route(){const h=location.hash.slice(1);document.querySelectorAll('.fview').forEach(s=>s.hidden=h?s.id!==h:s.id!=='overview');window.scrollTo(0,0);}
addEventListener('hashchange',route);route();
document.querySelectorAll('[data-open]').forEach(b=>b.addEventListener('click',()=>document.querySelector('.zoom[data-gallery="'+b.dataset.open+'"][data-n="0"]').click()));
"""
d=b[b.index('<dialog id="lb"'):b.index('</dialog>')+9]
scr=b[b.index('<script>'):b.index('</script>')+9]
gjs='const G={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in G.items())+'\n};'
scr=re.sub(r'const G=\{.*?\n\};',lambda m:gjs,scr,flags=re.S)
i=scr.find('// Sprachen-Umschalter')
if i>0: scr=scr[:i]+'</script>'
scr=scr[:scr.rindex('</script>')]+NAV+'</script>'
out='<title>Grafik und Print</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/gp/page/grafik-print.html','w',encoding='utf-8').write(out)
print('ok',sum(len(v) for v in G.values()))
