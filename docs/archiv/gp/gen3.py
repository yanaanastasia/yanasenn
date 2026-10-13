import re,subprocess,glob,os
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
I=S+'/gp/page/img/'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
style=b[b.index('<style>'):b.index('</style>')+8]
style=style.replace('/* Layout: Projektseite Broschüren','/* Layout: Kategorie Grafik & Print v3',1)
def size(f): return tuple(map(int,subprocess.run(['identify','-format','%w %h',I+f],capture_output=True,text=True).stdout.split()))
G={}
def zb(g,s,c,cls='page'):
    G.setdefault(g,[]).append((s,c)); n=len(G[g])-1
    return f'<button class="zoom {cls}" data-gallery="{g}" data-n="{n}" aria-label="{c} gross ansehen"><img src="img/{s}" alt="{c}"></button>'
CP='CP Pump Systems'; GO='GOLDINGER Immobilien'; A='https://claude.ai/artifact/'
RID=[0]
def gallery(g,title,files,w=120):
    W,H=size(files[0])
    return f'<div class="pages" style="--r:{W}/{H};--w:{w}px">'+''.join(f'<figure>{zb(g,f,f"{title}, Seite {i+1}")}</figure>' for i,f in enumerate(files))+'</div>'
def row(client,title,intro,cover,chips=(),more='',link=None,small=False,btn='Mehr erfahren',gal=None):
    RID[0]+=1; rid=f'r{RID[0]}'; g='g'+rid
    W,H=size(cover); cov=zb(g if not gal else gal,cover,title,'page' if H>W*0.9 else 'plan')
    ch=''.join(f'<span>{c}</span>' for c in chips)
    acts=''
    if more: acts+=f'<button class="tog" aria-expanded="false" aria-controls="{rid}">{btn}</button>'
    if link: acts+=f'<a class="lnk" href="{A}{link[1]}" target="_blank" rel="noopener">{link[0]} ↗</a>'
    mb=f'<div class="more" id="{rid}" hidden>{more}</div>' if more else ''
    return f'<article class="row{" sm" if small else ""}"><div class="vis" style="--r:{W}/{H}">{cov}</div><div class="txt"><span class="client">{client}</span><h3>{title}</h3><p>{intro}</p><div class="chips">{ch}</div><div class="acts">{acts}</div></div>{mb}</article>'
def blocks(*pairs): return '<div class="blocks">'+''.join(f'<div><h4>{h}</h4>{p if p.startswith("<") else "<p>"+p+"</p>"}</div>' for h,p in pairs)+'</div>'
def ul(*xs): return '<ul>'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'
def ba(a,b2,cap):
    W,H=size(a)
    return f'<figure class="babox"><div class="ba" style="--r:{W}/{H}"><img src="img/{a}" alt="Vorher: {cap}"><img class="after" src="img/{b2}" alt="Nachher: {cap}"><span class="bar"></span><span class="lbl l1">Vorher</span><span class="lbl l2">Nachher</span><input type="range" min="0" max="100" value="50" aria-label="Vorher und Nachher vergleichen: {cap}"></div><figcaption class="tag">{cap}</figcaption></figure>'
P=lambda pre,n: [f'b_{pre}-{i:02d}.jpg' for i in range(1,n+1)]
SEC=[]
# 01
prod=[('MKP · MKP-S · MKTP','Magnetgekuppelte Kreiselpumpen aus Edelstahl: effizient, robust, sicher.','mkp',20,'Deutsch'),
('MKPL · MKPL-S','PFA-ausgekleidete Magnetkupplungspumpen: korrosionsbeständig und vakuumfest.','mkpl',16,'Englisch'),
('MKP-Bio','Magnetkupplungspumpe für sterile Prozesse, EHEDG-konform.','bio',12,'Englisch'),
('MSKP · MSKPP · MSKS','Magnetkupplungspumpen aus Vollkunststoff PTFE, permeationsbeständig.','mskp',16,'Englisch'),
('MKPP · SZMK','Platzsparende Inline-Pumpen aus Edelstahl.','mkpp',16,'Englisch'),
('EB','PFA-ausgekleidete Pumpe mit doppelt wirkender Gleitringdichtung.','eb',12,'Englisch'),
('ET','Keramik-ausgekleidete Pumpe, abrasionsbeständig.','et',12,'Englisch'),
('ZMP','Zerkleinerungspumpe aus Edelstahl: massiv, langlebig, sicher.','zmp',12,'Englisch')]
prodrows=''.join(row(CP,'Produktbroschüre '+t,d,f'b_{k}-01.jpg',(f'{n} Seiten','A4',l+' (gezeigt)'),more=gallery('p'+k,t,P(k,n),110),small=True,btn='Alle Seiten') for t,d,k,n,l in prod)
SEC.append(('broschueren','Broschüren und Magazin','Von der Firmenbroschüre bis zum Hausmagazin: Ich entwickle Konzepte, gestalte Layouts und begleite Sprachfassungen und Druck.',
 row(CP,'Company Profile','Die Firmenbroschüre stellt CP Pump Systems vor: Geschichte, Standorte, Kompetenzen und Produkte, als Grundlage für Kundentermine und Messen weltweit.','b_cp-01.jpg',('16 Seiten','A4','9 Sprachen'),
   more=blocks(('Ausgangslage','Die Broschüren von CP waren über die Jahre gewachsen: unterschiedlich aufgebaut, teils mit Einklappfalte und je nach Sprache mit anderen Inhalten. Das machte Pflege und Übersetzung aufwendig.'),
     ('Was ich gemacht habe','Ich habe das Company Profile intensiv überarbeitet und neue Grafiken entwickelt, darunter die Weltkarte der Standorte und den Zeitstrahl zur Firmengeschichte. Die Sprachfassungen entstanden mit einem Übersetzungsbüro, dazu eine eigene US-Version im Letter-Format.'),
     ('Ergebnis','Die Broschüre wird gedruckt und vom Verkauf weltweit genutzt, bei Kundenterminen und an Messen. Online steht sie als Download bereit; diese Versionen halte ich laufend aktuell.'))+gallery('pcp','Company Profile',P('cp',16),110),
   link=('Projekt «Broschüren in neun Sprachen»','6CM4QZGbNhy5bjxvvMbnbc'))
 +row(CP,'Sortimentsbroschüre','Die Übersicht über alle Kreiselpumpen für herausfordernde Medien: «Mit Schweizer Qualität sichern Sie jeden Prozess.»','b_so-01.jpg',('8 Seiten','A4','Deutsch (gezeigt)'),
   more=blocks(('Inhalt','Hochsichere, hermetisch dichte und effiziente Kreiselpumpen im Überblick, mit den Herausforderungen der Kundschaft, den Baureihen und Service.'),('Was ich gemacht habe','Intensive Überarbeitung von Aufbau, Inhalt und Gestaltung, im einheitlichen System aller Broschüren.'))+gallery('pso','Sortimentsbroschüre',P('so',8),110))
 +'<div class="sub"><h4>Produktbroschüren</h4><p>Acht Broschüren, eine pro Baureihe, alle im gleichen Aufbau: Titel mit Kernnutzen, Anwendungen, Technik, Werkstoffe und Kennlinien.</p></div>'+prodrows
 +row(CP,'Broschüre Molten Sulphur','Acht Seiten zu Pumpen, die flüssigen Schwefel fördern: Gelb, Dreiecksmuster und die Schnittzeichnung der beheizten Pumpe ziehen sich durch die ganze Reihe aus Inserat, Messewand, Factsheet und Flyer.','ms_bro-1.jpg',('8 Seiten','A4','Englisch'),
   more=blocks(('Was ich gemacht habe','Konzept und Gestaltung der Broschüre; die Texte basieren auf bestehendem Material und sind mit dem Verkauf abgestimmt.'))+gallery('pms','Broschüre Molten Sulphur',[f'ms_bro-{i}.jpg' for i in range(1,9)],110))
 +row(GO,'Hausmagazin «Die IMMO-EXPERTEN»','GOLDINGER Immobilien gab zweimal im Jahr ein eigenes Magazin heraus. Es zeigte aktuelle Immobilien und Neubauprojekte, lud zu den Infoabenden ein und lag Zeitungen in der Ostschweiz bei.','hm-01.jpg',('12 Seiten','A4','Ausgabe Februar 2023'),
   more=blocks(('Meine Rolle','Ich gestaltete das Magazin und schrieb die Texte gemeinsam mit dem Verkaufsteam. Die Inhalte legten wir zusammen mit meinem Vorgesetzten fest; Bilder und Objektangaben kamen von den Standorten. Zudem organisierte ich die Verteilung: In welchen Zeitungen erreichen wir unsere Zielgruppe, und wo wird das Magazin gestreut?'),
     ('Aufbau der Ausgabe',ul('Titel: Ausblick auf das Jahr 2023 mit Editorial','News: Infoabende an sieben Standorten, mit QR-Code','Premium-Objekte, Kaufen und Neubauprojekte auf acht Seiten','Gutschein für eine kostenlose Wertermittlung und Anmeldetalon')),
     ('Gestaltung','Fester Seitenkopf mit blauer Linie und Rubrik in Versalien, ein klares Objektraster und viel Bild.'))
   +'<button class="btn" data-open="ghm">Magazin durchblättern</button>'+gallery('ghm','Hausmagazin',[f'hm-{i:02d}.jpg' for i in range(1,13)],110))))
# 02 Flyer
SEC.append(('flyer','Flyer','Flyer für Veranstaltungen, Neubauprojekte und Messen, gestaltet für einen schnellen Überblick und eine klare Handlung.',
 row(GO,'Infoabende','Einladung zu den Infoabenden für private Immobilieneigentümer: Termine an mehreren Standorten, die Themen des Abends und Anmeldung per QR-Code.','g_info23-1.jpg',('A5 quer','2 Seiten'),more=gallery('fi','Infoabende',['g_info23-1.jpg','g_info23-2.jpg'],260))
 +row(GO,'Gutschein Wertermittlung','Klappkarte mit Gutschein für eine kostenlose Immobilienbewertung und Antwortkarte zum Zurücksenden.','g_gutschein-3.jpg',('A5 quer','4 Seiten'),more=gallery('fg','Gutschein',[f'g_gutschein-{i}.jpg' for i in range(1,5)],230))
 +row(GO,'Neubauprojekt Sonnenhof','Flyer zu einem Neubauprojekt mit Eigentumswohnungen: Lage, Wohnungsmix und Ausstattung auf einen Blick.','g_sonnenhof-1.jpg',('A5','2 Seiten'),more=gallery('fs','Sonnenhof',['g_sonnenhof-1.jpg','g_sonnenhof-2.jpg'],160))
 +row(GO,'Tag der offenen Tür','Einladung zur Besichtigung eines Neubauprojekts mit Datum, Ort und QR-Code.','g_gruenblick.jpg',('A5',))
 +row(CP,'Molten Sulphur für die USA','Zweiseitiger Flyer im US-Letter-Format für die Messen in den USA.','ms_us-1.jpg',('US-Letter','2 Seiten','Englisch'),more=gallery('fu','Flyer USA',['ms_us-1.jpg','ms_us-2.jpg'],160))))
# 03 Inserate
SEC.append(('inserate','Inserate','Inserate müssen in Sekunden wirken. Für CP in Fachzeitschriften und Messekatalogen, in der Sprache des Zielmarkts; für GOLDINGER in Magazinen und Regionalzeitungen.',
 row(CP,'World Fertilizer','Halbseitiges Inserat in einer internationalen Fachzeitschrift der Düngemittelindustrie: «Sulphur at the perfect temperature».','anzeige.jpg',('Fachzeitschrift','Englisch'))
 +row(CP,'Messekataloge','Inserate in den Katalogen der Fachmessen, jeweils in der Sprache des Messelandes und abgestimmt auf die ausgestellten Pumpen.','i_petro.jpg',('4 Inserate','Französisch und Englisch'),more=gallery('ik','Katalog-Inserat',['i_petro.jpg','i_dk.jpg','i_chemuk.jpg','i_tfs.jpg'],180),btn='Alle Inserate')
 +row(GO,'Hauseigentümer-Magazin','Ganzseitige Inserate zur neuen Website, zum 35-Jahr-Jubiläum und zu den Ratgebern für Eigentümer.','g_hev23.jpg',('A4','2 Inserate'),more=gallery('ih','Inserat',['g_hev23.jpg','g_hev22.jpg'],170),btn='Beide Inserate')
 +row(GO,'Infoabende in Regionalzeitungen','Eine Serie in mehreren Formaten für verschiedene Regionalausgaben.','g_sgkb.jpg',('3 Formate',),more=gallery('ir','Inserat Infoabende',['g_sgkb.jpg','g_kreuz.jpg','g_tkb.jpg'],260),btn='Alle Formate')
 +row(GO,'Messe WEGA','Inserat mit dem Angebot, den Wert der eigenen Immobilie direkt am Messestand schätzen zu lassen.','g_wega.jpg')
 +row(GO,'Clubmagazin','Inserat im Magazin eines Sportclubs.','sck.jpg')))
# 04 Infoblätter
SEC.append(('infoblaetter','Infoblätter','Kompakte Informationen zu Produkten und Angeboten, für Messen, Kundentermine und als Download.',
 row(CP,'Factsheet Molten Sulphur','Zwei Seiten zu beheizten Pumpen für flüssigen Schwefel. Komplett von mir gestaltet; die Texte basieren auf bestehendem Material und sind mit dem Verkauf abgestimmt.','ms_fact-1.jpg',('A4','2 Seiten','Englisch'),more=gallery('if','Factsheet',['ms_fact-1.jpg','ms_fact-2.jpg'],160))
 +row(CP,'Sofort verfügbare Pumpensysteme','Übersicht über Pumpensysteme ab Lager mit kurzer Lieferzeit.','f_lead.jpg',('A4','Deutsch und Englisch'))))
# 05 Grusskarten
SEC.append(('grusskarten','Grusskarten','Karten zu Weihnachten und zum thailändischen Neujahr, von der Idee über Gestaltung und Text bis zum Druck.',
 row(CP,'Weihnachtskarten 2026','Rentiere ziehen einen Schlitten mit einer CP-Pumpe durch den Nachthimmel über verschneite Berge, dazu «Merry Christmas» und der Claim «cleaner pumps, cleaner planet™».','x_karteA-2.jpg',('3 Zielgruppen','Deutsch, Englisch, Französisch','Sie- und Du-Form'),
   more=blocks(('Idee','Jedes Geschenk erzählt etwas über CP: Die Picknickdecke für A-Kunden ist «leakproof», sie hält dicht wie die dichtungslosen Pumpen. Der Kartenhalter für B-Kunden schützt mit einem RFID-Blocker, «Sicherheit, die man nicht sieht, aber spürt».'),
     ('Die Karten','Auf der Innenseite ein Zahlen-verbinden-Rätsel: «Strich für Strich zur Lösung.» Eigene Texte für A-Kunden («Zeit für Dankbarkeit»), B-Kunden («Die schönste Zeit des Jahres») und Mitarbeitende («Gemeinsam stark»), personalisiert im Seriendruck.'),
     ('Meine Rolle','Gestaltung und alle Texte der Karten, Druckvorbereitung mit der Druckerei (Karten, Adressetiketten, Couverts), Offerten, Bestellung und Koordination der Lieferanten.'))
   +gallery('gx','Weihnachtskarte',['x_karteA-2.jpg','x_karteA-3.jpg','x_karteA-1.jpg','x_karteA-4.jpg','x_karteA-5.jpg'],150),link=('Ganze Kampagne','1ub6RRXMbhZQRUq33avRvH'))
 +row(CP,'Songkran-Grusskarte','Zum thailändischen Neujahrsfest, einem Fest des Wassers: zwei Pagoden mit der thailändischen und der Schweizer Flagge, dazu Wasserspritzer, Wellen und Blüten auf einem Verlauf von Gelb zu Blau.','karte-1.jpg',('A5','Englisch'),
   more=blocks(('Für wen','CP Pump Systems hat in Thailand eine Niederlassung. Zum Fest ging die Karte an Kundschaft und weitere Kontakte vor Ort.'),('Von der Skizze zur Karte','Am Anfang standen sechs Skizzen, daraus entstanden zwei Entwürfe. Ideen, Skizzen, Gestaltung, Druckvorbereitung und Bestellung lagen komplett bei mir.'))
   +gallery('gs','Songkran',['karte-1.jpg','karte-2.jpg','skizze.jpg'],160))))
# 06 Messegrafik
W8=[('Petrochymia 2026','Paneele mit Anlagenfoto, der neuen Weltkarte und Swiss-Made-Zeichen.','m_petro26.jpg','Französisch'),('ChemUK 2026','Rückwand mit Weltkarte und Kernbotschaft.','m_chemuk.jpg','Englisch, 6 m'),('CRU Sulphur + Sulphuric Acid Berlin 2026','«Keep Your Molten Sulphur Flowing», drei Paneele.','ms_wand.jpg','Englisch'),('DK Hub Dunkerque 2026','Paneele und Tür der Standkabine.','m_dk.jpg','Französisch'),('Fertilizer Latino Americano 2026','Rückwand mit Birkenwald und Claim.','m_fla.jpg','Englisch'),('Pumps & Valves Dortmund 2025','Zwei Wände eines Eckstands.','m_pv25.jpg','Englisch'),('Pétro+Chimie Le Havre 2025','Design der Petrochymia 2024 weitergeführt.','m_lehavre.jpg','Französisch'),('Petrochymia 2024','Sechs Paneele mit Weltkarte und Wassermotiv.','m_petro24.jpg','Französisch')]
walls=''.join(f'<article class="wallrow"><div class="wt"><span class="client">CP Pump Systems</span><h3>{t}</h3><p>{d}</p><div class="chips"><span>{l}</span></div></div><div class="vis wide">{zb("wm",f,t,"plan")}</div></article>' for t,d,f,l in W8)
SEC.append(('messegrafik','Messegrafik','Rückwände, Blenden und Folien für die Messestände, abgestimmt auf Standgrösse, Messeland und Sprache. Die neuesten zuerst.',
 walls+row(CP,'Blenden und Folien','Blenden über den Ständen mit Logo und Claim, dazu Folien für Theken.','f_p26.jpg',('4 Blenden','1 Folie'),more='<div class="pages" style="--r:10/1;--w:420px">'+''.join(f'<figure>{zb("wb",f,c,"plan")}<figcaption class="tag">{c}</figcaption></figure>' for f,c in [('f_p26.jpg','Petrochymia 2026'),('f_uk_fascia.jpg','ChemUK 2026'),('f_dk.jpg','DK Hub 2026'),('f_p24_fac6.jpg','Petrochymia 2024')])+'</div>'+gallery('wf','Folie Theke ACHEMA 2024',['m_achema.jpg'],180),btn='Alle ansehen')))
# 07 Infografiken
SEC.append(('infografiken','Infografiken','Grafiken, die komplexe Inhalte auf einen Blick zeigen und in Broschüren, auf Messewänden und auf der Website wiederverwendet werden.',
 row(CP,'Weltkarte der Standorte','Standorte, Tochterfirmen und Niederlassungen sowie Mitarbeitende in weiteren Ländern, mit einer Legende für CP Pump Systems und Partner.','neu.jpg',('2 Formate','mehrere Sprachen'),
   more=blocks(('Final','Ein Punktraster mit geordneten Beschriftungen in zwei Formaten: breit für die Messewände, im Hochformat für die Broschüren.'),('Vorher','Die ursprüngliche Karte war grau; in einer ersten Überarbeitung entstand eine flächige Fassung in CP-Blau für die Messewände.'))+gallery('kw','Weltkarte',['neu.jpg','neu_en.jpg','bro_neu.jpg','bro_grau.jpg','alt_blau.jpg'],200))
 +row(CP,'Firmengeschichte als Zeitstrahl','Zwei A4-Seiten im Company Profile, «passioniert – swiss made – innovativ»: Meilensteine als Schlangenlinie mit Bildern von Produkten, Maschinen, Gebäuden und Flaggen für neue Märkte.','zs_spread.jpg',('7 Sprachfassungen',),more=gallery('kz','Zeitstrahl',['zs_spread.jpg','zs_spread_en.jpg'],320),btn='Deutsch und Englisch')))
# 08 Redesigns
SEC.append(('redesigns','Redesigns','Bei GOLDINGER habe ich bestehende Werbemittel neu gestaltet: klares Blau und Weiss, grosse Bilder, wenig Text. Den Regler ziehen, um alt und neu zu vergleichen.',
 '<div class="bagrid">'+ba('wand_alt.jpg','wand_neu.jpg','Messewand WEGA')+ba('mappe22-1.jpg','mappe23-1.jpg','Faltmappe, Aussenseite')+ba('mappe22-2.jpg','mappe23-2.jpg','Faltmappe, Innenseite')+ba('g_info22-1.jpg','g_info23-1.jpg','Flyer Infoabende, Vorderseite')+ba('g_info22-2.jpg','g_info23-2.jpg','Flyer Infoabende, Rückseite')+'</div>'))
toc=''.join(f'<a href="#{k}"><span>{i:02d}</span>{t}</a>' for i,(k,t,_,_) in enumerate(SEC,1))
secs=''.join(f'<section class="cat" id="{k}"><div class="chead"><span class="num">{i:02d}</span><div><h2>{t}</h2><p>{intro}</p></div></div><div class="list">{html}</div></section>' for i,(k,t,intro,html) in enumerate(SEC,1))
body=f'<div class="wrap"><p class="note">Entwurf «Grafik &amp; Print»: «Mehr erfahren» klappt die Details auf, Bilder lassen sich vergrössern.</p><header class="hero"><p class="crumb">Arbeiten</p><h1>Grafik &amp; Print</h1><p class="lead">Broschüren, Flyer, Inserate, Karten und Messegrafik für CP Pump Systems und GOLDINGER Immobilien, vom Konzept bis zur fertigen Druckdatei.</p><nav class="toc">{toc}</nav></header>{secs}</div>'
style=style.replace('</style>','''
:root{--tint:#eceff3}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--tint:#232a27}}
:root[data-theme="dark"]{--tint:#232a27}
.crumb{font-size:.8rem;color:var(--muted);margin:0}
.toc{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:4px}.toc a{color:var(--ink);text-decoration:none;font-weight:700;font-size:.92rem}.toc a span{color:var(--accent);font-size:.72rem;margin-right:6px}
.cat{display:grid;gap:30px;padding-top:56px;border-top:1px solid var(--line);scroll-margin-top:16px}
.chead{display:grid;grid-template-columns:90px minmax(0,1fr);gap:20px}.num{font:700 2.8rem/1 var(--font);color:var(--accent);opacity:.3}
.chead p{color:var(--muted);margin-top:8px;max-width:62ch}
.list{display:grid;gap:22px}
.row{display:grid;grid-template-columns:300px minmax(0,1fr);gap:34px;align-items:center}
.row.sm{grid-template-columns:150px minmax(0,1fr);gap:24px}
.vis{background:var(--tint);border-radius:14px;padding:22px;display:grid;place-items:center}
.row.sm .vis{padding:14px;border-radius:10px}
.vis .zoom{aspect-ratio:var(--r);max-height:340px;width:auto;background:transparent!important;border:0!important;box-shadow:none!important;overflow:visible}
.vis .zoom img{box-shadow:0 10px 26px rgba(0,0,0,.18);border-radius:2px;object-fit:contain}
.row.sm .vis .zoom{max-height:170px}
.vis.wide .zoom{max-height:none;width:100%}
.txt{display:grid;gap:10px;align-content:center}
.client{font:700 .66rem var(--font);letter-spacing:.09em;text-transform:uppercase;color:var(--accent)}
.txt h3{font-size:1.35rem}.row.sm .txt h3{font-size:1.05rem}.row.sm .txt p{font-size:.92rem}
.chips{display:flex;flex-wrap:wrap;gap:6px}.chips span{font-size:.75rem;border:1px solid var(--line);border-radius:99px;padding:3px 10px;color:var(--muted)}
.acts{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.tog{all:unset;cursor:pointer;font-weight:700;color:var(--accent);display:inline-flex;gap:8px;align-items:center}
.tog::after{content:"+";font-size:1.15rem}.tog[aria-expanded=true]::after{content:"–"}
.tog:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.lnk{color:var(--ink);font-weight:700;text-decoration:none;border-bottom:1px solid var(--line)}
.more{grid-column:1/-1;display:grid;gap:22px;padding:26px 0 8px;border-top:1px dashed var(--line);animation:pin .3s ease}.more[hidden]{display:none}
.blocks{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px}.blocks h4{font-size:.95rem;margin-bottom:6px}.blocks p,.blocks li{color:var(--muted);font-size:.95rem}.blocks ul{margin:0;padding-left:18px}
.pages{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(min(var(--w,120px),100%),var(--w,120px)))}
.pages .zoom{aspect-ratio:var(--r)}
.btn{all:unset;cursor:pointer;background:var(--accent);color:#fff;border-radius:99px;padding:9px 18px;font:700 .88rem var(--font);justify-self:start}
.sub{padding:18px 0 0;border-top:1px solid var(--line)}.sub h4{font-size:1.1rem}.sub p{color:var(--muted);margin-top:4px}
.wallrow{display:grid;gap:14px}.wt{display:grid;gap:6px;max-width:62ch}
.bagrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.ba{position:relative;border-radius:12px;overflow:hidden;background:var(--tint);aspect-ratio:var(--r)}
.ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}
.ba .after{clip-path:inset(0 0 0 var(--p,50%))}
.ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.ba .bar{position:absolute;top:0;bottom:0;left:var(--p,50%);width:3px;background:var(--accent);transform:translateX(-50%);pointer-events:none}
.ba .bar::after{content:"⇆";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:var(--accent);color:#fff;border-radius:99px;padding:6px 9px;font-size:.9rem}
.ba .lbl{position:absolute;top:10px;font:700 .68rem var(--font);letter-spacing:.08em;text-transform:uppercase;background:rgba(0,0,0,.6);color:#fff;padding:4px 9px;border-radius:99px;pointer-events:none}.ba .l1{left:10px}.ba .l2{right:10px;background:var(--accent)}
@keyframes pin{from{opacity:0;transform:translateY(-6px)}}
@media (prefers-reduced-motion:reduce){.more{animation:none}}
@media (max-width:760px){.chead{grid-template-columns:minmax(0,1fr);gap:4px}.row,.row.sm{grid-template-columns:minmax(0,1fr);gap:14px}.row.sm{grid-template-columns:100px minmax(0,1fr)}.row.sm .more{grid-column:1/-1}.bagrid{grid-template-columns:minmax(0,1fr)}.vis .zoom{max-height:300px}}
</style>''')
NAV="""
// Aufklappen, Durchblättern, Vorher/Nachher
document.querySelectorAll('.tog').forEach(t=>t.addEventListener('click',()=>{const m=document.getElementById(t.getAttribute('aria-controls'));const o=t.getAttribute('aria-expanded')==='true';t.setAttribute('aria-expanded',!o);m.hidden=o;}));
document.querySelectorAll('[data-open]').forEach(b=>b.addEventListener('click',()=>document.querySelector('.zoom[data-gallery="'+b.dataset.open+'"][data-n="0"]').click()));
document.querySelectorAll('.ba input').forEach(r=>r.addEventListener('input',()=>r.parentElement.style.setProperty('--p',r.value+'%')));
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
