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

def T(de,en): return f'<span class="l-de">{de}</span><span class="l-en" lang="en">{en}</span>'
def row(client,title,intro,cover,chips=(),more='',link=None,small=False,btn=('Mehr erfahren','Learn more'),gal=None):
    RID[0]+=1; rid=f'r{RID[0]}'; g='g'+rid
    W,H=size(cover); tt=title[0] if isinstance(title,tuple) else title
    n,cnt=take(g,cover,tt)
    badge=f'<span class="cnt">{cnt} {T("Seiten","pages")} · {T("blättern","flip through")}</span>' if cnt>1 else ''
    cov=f'<button class="zoom {"page" if H>W*0.9 else "plan"}" data-gallery="{g}" data-n="{n}" aria-label="{tt} öffnen"><img src="img/{cover}" alt="{tt}">{badge}</button>'
    ti=T(*title) if isinstance(title,tuple) else title
    ch=''.join(f'<span>{T(*c) if isinstance(c,tuple) else c}</span>' for c in chips)
    acts=''
    if more: acts+=f'<button class="tog" aria-expanded="false" aria-controls="{rid}">{T(*btn)}</button>'
    if link: acts+=f'<a class="lnk" href="{A}{link[2]}" target="_blank" rel="noopener">{T(link[0],link[1])} ↗</a>'
    mb=f'<div class="more" id="{rid}" hidden>{more}</div>' if more else ''
    return f'<article class="row{" sm" if small else ""}"><div class="vis" style="--r:{W}/{H}">{cov}</div><div class="txt"><span class="client">{client}</span><h3>{ti}</h3><p>{T(*intro)}</p><div class="chips">{ch}</div><div class="acts">{acts}</div></div>{mb}</article>'
def blocks(*items): return '<div class="blocks">'+''.join(f'<div><h4>{T(h1,h2)}</h4><p>{T(p1,p2)}</p></div>' for h1,h2,p1,p2 in items)+'</div>'
PEND=[];PEN=[];GEN={}
def gallery(g,title,files,w=120,en=None):
    PEND.extend((f,f"{title}, {i+1}") for i,f in enumerate(files))
    if en: PEN.extend((f,f"{title}, {i+1}") for i,f in enumerate(en))
    return ''
def take(g,cover,title):
    global PEND,PEN
    pages=PEND or [(cover,title)]
    if cover not in [p[0] for p in pages]: pages=[(cover,title)]+pages
    G[g]=pages; n=[p[0] for p in pages].index(cover)
    if PEN: GEN[g]=PEN
    PEND=[];PEN=[]
    return n,len(pages)
def ba(a,b2,cap,l1=('Vorher','Before'),l2=('Nachher','After')):
    W,H=size(a)
    return f'<div class="ba" style="--r:{W}/{H}"><img src="img/{a}" alt="{cap[0]}"><img class="after" src="img/{b2}" alt="{cap[0]}"><span class="bar"></span><span class="lbl l1">{T(*l1)}</span><span class="lbl l2">{T(*l2)}</span><input type="range" min="0" max="100" value="50" aria-label="{cap[0]}"></div>'
def tabs(name,items):
    # items: (labelDE,labelEN,html)
    btns=''.join(f'<button class="tab" role="tab" aria-selected="{"true" if i==0 else "false"}" data-tab="{name}-{i}">{T(a,b2)}</button>' for i,(a,b2,_) in enumerate(items))
    pans=''.join(f'<div class="tabp" id="{name}-{i}" {"" if i==0 else "hidden"}>{h}</div>' for i,(a,b2,h) in enumerate(items))
    return f'<div class="tabs"><div class="tabbar" role="tablist">{btns}</div>{pans}</div>'
def rd(title,intro,client,inner):
    return f'<article class="rdi"><div class="txt"><span class="client">{client}</span><h3>{T(*title)}</h3><p>{T(*intro)}</p></div>{inner}</article>'
P=lambda pre,n: [f'b_{pre}-{i:02d}.jpg' for i in range(1,n+1)]
SEC=[]
# 01 Broschüren
prod=[('MKP · MKP-S · MKTP','Magnetgekuppelte Kreiselpumpen aus Edelstahl','Stainless steel magnetic drive pumps','mkp',20),
('MKPL · MKPL-S','PFA-ausgekleidet, korrosionsbeständig','PFA lined, corrosion-proof','mkpl',16),
('MKP-Bio','Für sterile Prozesse, EHEDG-konform','For sterile processes, EHEDG-compliant','bio',12),
('MSKP · MSKPP · MSKS','Vollkunststoff PTFE','Solid PTFE','mskp',16),
('MKPP · SZMK','Platzsparende Inline-Pumpen','Space-saving in-line pumps','mkpp',16),
('EB','Mit doppelter Gleitringdichtung','Double mechanical seal','eb',12),
('ET','Keramik-ausgekleidet','Ceramic lined','et',12),
('ZMP','Zerkleinerungspumpe','Grinder pump','zmp',12)]
for t_,de,en,k,n in prod: G['p'+k]=[(f,f"{t_}, {i+1}") for i,f in enumerate(P(k,n))]
GEN['pmkp']=[(f'be_mkp-{i:02d}.jpg',f'MKP, {i}') for i in range(1,21)]
covers=''.join(f'<button class="pcov" data-gallery="p{k}" data-n="0"><span class="vis"><img src="img/b_{k}-01.jpg" alt="{t}"><span class="cnt">{n} {T("Seiten","pages")}</span></span><b>{t}</b><small>{T(de,en)}</small></button>' for t,de,en,k,n in prod)
ppan=''
SEC.append(('broschueren',('Broschüren und Magazin','Brochures and Magazine'),('Von der Firmenbroschüre bis zum Hausmagazin: Ich entwickle Konzepte, gestalte Layouts und begleite Sprachfassungen und Druck.','From the company brochure to the customer magazine: I develop concepts, design layouts and manage language versions and printing.'),
 row(CP,('Company Profile','Company Profile'),('Die Firmenbroschüre stellt CP Pump Systems vor: Geschichte, Standorte, Kompetenzen und Produkte, als Grundlage für Kundentermine und Messen weltweit.','The company brochure introduces CP Pump Systems: history, locations, expertise and products, used at customer meetings and trade fairs worldwide.'),'b_cp-01.jpg',(('16 Seiten','16 pages'),'A4',('9 Sprachen','9 languages')),
   more=blocks(('Ausgangslage','Starting point','Die Broschüren waren über die Jahre gewachsen: unterschiedlich aufgebaut, teils mit Einklappfalte und je nach Sprache mit anderen Inhalten.','Over the years the brochures had grown apart: different structures, some with fold-in flaps and different content per language.'),
     ('Meine Arbeit','My work','Ich habe das Company Profile intensiv überarbeitet und neue Grafiken entwickelt, darunter die Weltkarte der Standorte und den Zeitstrahl zur Firmengeschichte. Die Sprachfassungen entstanden mit einem Übersetzungsbüro, dazu eine US-Version im Letter-Format.','I thoroughly revised the Company Profile and created new graphics, including the world map of locations and the company timeline. Language versions were produced with a translation agency, plus a US Letter version.'),
     ('Ergebnis','Result','Die Broschüre wird gedruckt und vom Verkauf weltweit genutzt. Online steht sie als Download bereit; diese Versionen halte ich laufend aktuell.','The brochure is printed and used by sales worldwide. It is also available for download online, and I keep these versions up to date.'))+gallery('pcp','Company Profile',P('cp',16),110),
   link=('Projekt «Broschüren in neun Sprachen»','Project “Brochures in nine languages”','6CM4QZGbNhy5bjxvvMbnbc'))
 +row(CP,('Sortimentsbroschüre','Product range brochure'),('Die Übersicht über alle Kreiselpumpen für herausfordernde Medien: «Mit Schweizer Qualität sichern Sie jeden Prozess.»','An overview of all centrifugal pumps for challenging media: “Swiss quality to secure every process.”'),'b_so-01.jpg',(('8 Seiten','8 pages'),'A4'),
   more=gallery('pso','Sortiment',P('so',8),110,en=[f'be_so-{i:02d}.jpg' for i in range(1,9)]))
 +f'<div class="sub"><h4>{T("Produktbroschüren","Product brochures")}</h4><p>{T("Acht Broschüren, eine pro Baureihe, alle im gleichen Aufbau. Titelseite anklicken und blättern.","Eight brochures, one per product line, all with the same structure. Click a cover to flip through.")}</p><div class="pgrid">{covers}</div>{ppan}</div>'
 +row(CP,('Broschüre Molten Sulphur','Molten Sulphur brochure'),('Acht Seiten zu Pumpen, die flüssigen Schwefel fördern: Gelb, Dreiecksmuster und die Schnittzeichnung der beheizten Pumpe verbinden die ganze Reihe aus Inserat, Messewand, Factsheet und Flyer.','Eight pages on pumps for molten sulphur: yellow, a triangle pattern and the cutaway of the heated pump link the whole series of ad, booth wall, factsheet and flyer.'),'ms_bro-1.jpg',(('8 Seiten','8 pages'),'A4',('Englisch','English')),
   more=gallery('pms','Molten Sulphur',[f'ms_bro-{i}.jpg' for i in range(1,9)],110))
 +row(GO,('Hausmagazin «Die IMMO-EXPERTEN»','Customer magazine “Die IMMO-EXPERTEN”'),('GOLDINGER Immobilien gab zweimal im Jahr ein eigenes Magazin heraus, mit aktuellen Immobilien, Neubauprojekten und der Einladung zu den Infoabenden. Es lag Zeitungen in der Ostschweiz bei.','GOLDINGER Immobilien published its own magazine twice a year, with current properties, new-build projects and an invitation to its information evenings. It was inserted into newspapers in Eastern Switzerland.'),'hm-01.jpg',(('12 Seiten','12 pages'),'A4',('Februar 2023','February 2023')),
   more=blocks(('Meine Rolle','My role','Ich gestaltete das Magazin und schrieb die Texte gemeinsam mit dem Verkaufsteam. Die Inhalte legten wir mit meinem Vorgesetzten fest. Zudem plante ich die Verteilung: In welchen Zeitungen erreichen wir unsere Zielgruppe?','I designed the magazine and wrote the texts together with the sales team, defining the content with my manager. I also planned distribution: which newspapers reach our audience?'),
     ('Inhalt','Content','Ausblick auf das Jahr mit Editorial, News zu den Infoabenden an sieben Standorten, acht Seiten Immobilien und Neubauprojekte, Gutschein für eine kostenlose Wertermittlung.','An outlook on the year with editorial, news on information evenings at seven locations, eight pages of properties and new builds, and a voucher for a free valuation.'),
     ('Gestaltung','Design','Fester Seitenkopf mit blauer Linie und Rubrik in Versalien, ein klares Objektraster und viel Bild.','A fixed page header with a blue rule and section titles in capitals, a clear property grid and plenty of imagery.'))
   +f'<button class="btn" data-open="ghm">{T("Magazin durchblättern","Browse the magazine")}</button>'+gallery('ghm','Hausmagazin',[f'hm-{i:02d}.jpg' for i in range(1,13)],110))))
# 02 Flyer
SEC.append(('flyer',('Flyer','Flyers'),('Flyer für Veranstaltungen, Neubauprojekte und Messen, gestaltet für einen schnellen Überblick und eine klare Handlung.','Flyers for events, new-build projects and trade fairs, designed for a quick overview and a clear call to action.'),
 row(GO,('Infoabende','Information evenings'),('Einladung zu den Infoabenden für private Immobilieneigentümer: Termine an mehreren Standorten, die Themen des Abends und Anmeldung per QR-Code.','Invitation to information evenings for private property owners: dates at several locations, the topics and registration via QR code.'),'g_info23-1.jpg',('A5',('2 Seiten','2 pages')),more=gallery('fi','Infoabende',['g_info23-1.jpg','g_info23-2.jpg'],260))
 +row(GO,('Gutschein Wertermittlung','Valuation voucher'),('Klappkarte mit Gutschein für eine kostenlose Immobilienbewertung und Antwortkarte.','Folded card with a voucher for a free property valuation and a reply card.'),'g_gutschein-3.jpg',('A5',('4 Seiten','4 pages')),more=gallery('fg','Gutschein',[f'g_gutschein-{i}.jpg' for i in range(1,5)],230))
 +row(GO,('Neubauprojekt Sonnenhof','New-build project Sonnenhof'),('Flyer zu einem Neubauprojekt mit Eigentumswohnungen: Lage, Wohnungsmix und Ausstattung auf einen Blick.','Flyer for a new-build project with owner-occupied flats: location, mix and features at a glance.'),'g_sonnenhof-1.jpg',('A5',('2 Seiten','2 pages')),more=gallery('fs','Sonnenhof',['g_sonnenhof-1.jpg','g_sonnenhof-2.jpg'],160))
 +row(GO,('Tag der offenen Tür','Open house'),('Einladung zur Besichtigung eines Neubauprojekts mit Datum, Ort und QR-Code.','Invitation to view a new-build project, with date, place and QR code.'),'g_gruenblick.jpg',('A5',))
 +row(CP,('Molten Sulphur für die USA','Molten Sulphur for the US'),('Zweiseitiger Flyer im US-Letter-Format für die Messen in den USA.','Two-page flyer in US Letter format for trade fairs in the United States.'),'ms_us-1.jpg',('US Letter',('2 Seiten','2 pages')),more=gallery('fu','Flyer USA',['ms_us-1.jpg','ms_us-2.jpg'],160))))
# 03 Inserate
SEC.append(('inserate',('Inserate','Advertisements'),('Inserate müssen in Sekunden wirken. Für CP in Fachzeitschriften und Messekatalogen, in der Sprache des Zielmarkts; für GOLDINGER in Magazinen und Regionalzeitungen.','Ads have to work in seconds. For CP in trade journals and fair catalogues, in the language of the market; for GOLDINGER in magazines and regional newspapers.'),
 row(CP,('World Fertilizer','World Fertilizer'),('Halbseitiges Inserat in einer internationalen Fachzeitschrift der Düngemittelindustrie: «Sulphur at the perfect temperature».','Half-page ad in an international fertilizer industry journal: “Sulphur at the perfect temperature”.'),'anzeige.jpg',(('Fachzeitschrift','Trade journal'),))
 +row(CP,('Messekataloge','Trade fair catalogues'),('Inserate in den Katalogen der Fachmessen, jeweils in der Sprache des Messelandes und abgestimmt auf die ausgestellten Pumpen.','Ads in trade fair catalogues, in the language of the host country and tailored to the pumps on show.'),'kat_mag.png',(('4 Inserate','4 ads'),),more=gallery('ik','Katalog',['i_petro.jpg','i_dk.jpg','i_chemuk.jpg','i_tfs.jpg'],180))
 +row(GO,('Hauseigentümer-Magazin','Homeowners’ magazine'),('Ganzseitige Inserate zur neuen Website, zum 35-Jahr-Jubiläum und zu den Ratgebern für Eigentümer.','Full-page ads on the new website, the 35th anniversary and guides for owners.'),'g_hev23.jpg',('A4',),more=gallery('ih','Inserat',['g_hev23.jpg','g_hev22.jpg'],170))
 +row(GO,('Infoabende in Regionalzeitungen','Information evenings in regional papers'),('Serie in mehreren Formaten für verschiedene Regionalausgaben, hier ein Beispiel.','A series in several formats for different regional editions; one example shown.'),'g_sgkb.jpg')
 +row(GO,('Messe WEGA','WEGA fair'),('Inserat mit dem Angebot, den Wert der eigenen Immobilie direkt am Messestand schätzen zu lassen.','Ad offering visitors a property valuation right at the booth.'),'g_wega.jpg')
 +row(GO,('Clubmagazin','Club magazine'),('Inserat im Magazin eines Sportclubs.','Ad in a sports club magazine.'),'sck.jpg')))
# 04
SEC.append(('infoblaetter',('Infoblätter','Information sheets'),('Kompakte Informationen zu Produkten und Angeboten, für Messen, Kundentermine und als Download.','Compact information on products and offers, for trade fairs, customer meetings and download.'),
 row(CP,('Factsheet Molten Sulphur','Molten Sulphur factsheet'),('Zwei Seiten zu beheizten Pumpen für flüssigen Schwefel. Komplett von mir gestaltet; die Texte basieren auf bestehendem Material und sind mit dem Verkauf abgestimmt.','Two pages on heated pumps for molten sulphur. Designed entirely by me; texts based on existing material and agreed with sales.'),'ms_fact-1.jpg',('A4',('2 Seiten','2 pages')),more=gallery('if','Factsheet',['ms_fact-1.jpg','ms_fact-2.jpg'],160))
 +row(CP,('Sofort verfügbare Pumpensysteme','Pump systems available now'),('Übersicht über Pumpensysteme ab Lager mit kurzer Lieferzeit.','Overview of pump systems in stock with short delivery times.'),'f_lead.jpg',('A4',('Deutsch und Englisch','German and English')))))
# 05 Grusskarten
xfold='<div class="fold" tabindex="0" role="button" aria-pressed="false" aria-label="Karte öffnen"><img class="in-r" src="img/x_karteA-1.jpg" alt="Innenseite mit Grusstext"><div class="cover"><img class="f" src="img/x_karteA-3.jpg" alt="Vorderseite: Rentiere ziehen einen Schlitten mit einer CP-Pumpe"><img class="b" src="img/x_karteA-4.jpg" alt="Innenseite mit Rätsel"></div></div>'
sflip='<div class="flip" tabindex="0" role="button" aria-pressed="false" aria-label="Karte umdrehen"><div class="cover"><img class="f" src="img/karte-1.jpg" alt="Vorderseite Songkran-Karte"><img class="b" src="img/karte-2.jpg" alt="Rückseite mit Grusstext"></div></div>'
def card(vis,client,title,intro,chips,more,link=None,hint=('Klick öffnet die Karte, zweiter Klick zeigt sie gross','Click to open the card, click again to view it large')):
    RID[0]+=1; rid=f'r{RID[0]}'
    ch=''.join(f'<span>{T(*c) if isinstance(c,tuple) else c}</span>' for c in chips)
    lk=f'<a class="lnk" href="{A}{link[2]}" target="_blank" rel="noopener">{T(link[0],link[1])} ↗</a>' if link else ''
    gid='c'+rid; first=PEND[0][0] if PEND else None
    if first: take(gid,first,title[0]); vis=vis.replace('tabindex="0"',f'tabindex="0" data-g="{gid}"',1)
    return f'<article class="row card"><div class="vis cardvis">{vis}<small class="hint">{T(*hint)}</small></div><div class="txt"><span class="client">{client}</span><h3>{T(*title)}</h3><p>{T(*intro)}</p><div class="chips">{ch}</div><div class="acts"><button class="tog" aria-expanded="false" aria-controls="{rid}">{T("Mehr erfahren","Learn more")}</button>{lk}</div></div><div class="more" id="{rid}" hidden>{more}</div></article>'
SEC.append(('grusskarten',('Grusskarten','Greeting cards'),('Karten zu Weihnachten und zum thailändischen Neujahr: Ich entwickle die Idee, gestalte die Karte, schreibe die Texte und begleite den Druck.','Cards for Christmas and Thai New Year: I develop the idea, design the card, write the texts and see it through to print.'),
 card(xfold,CP,('Weihnachtskarten 2026','Christmas cards 2026'),('Rentiere ziehen einen Schlitten mit einer CP-Pumpe durch den Nachthimmel, über verschneite Berge. Innen wartet ein Rätsel: «Strich für Strich zur Lösung.»','Reindeer pull a sleigh carrying a CP pump through the night sky over snowy mountains. Inside, a puzzle: “Every line reveals more.”'),(('3 Zielgruppen','3 audiences'),('3 Sprachen','3 languages'),('Sie- und Du-Form','formal and informal')),
   blocks(('Die Idee','The idea','Jedes Geschenk erzählt etwas über CP: Die Picknickdecke für A-Kunden ist «leakproof» und hält dicht wie die dichtungslosen Pumpen. Der Kartenhalter für B-Kunden schützt mit einem RFID-Blocker, «Sicherheit, die man nicht sieht, aber spürt». Die Karte bringt diese Geschichte auf den Punkt.','Every gift tells something about CP: the picnic blanket for key customers is “leakproof”, as sealed as the sealless pumps. The card holder for other customers protects with an RFID blocker, “security you can’t see but can feel”. The card sums up this story.'),
     ('Was ich gemacht habe','What I did','Ich habe die Karten gestaltet und alle Texte geschrieben: für A-Kunden «Zeit für Dankbarkeit», für B-Kunden «Die schönste Zeit des Jahres» und für die Mitarbeitenden «Gemeinsam stark». Jede Karte gibt es auf Deutsch, Englisch und Französisch, persönlich adressiert im Seriendruck.','I designed the cards and wrote all texts: “Time for Gratitude” for key customers, “The Most Wonderful Time of the Year” for other customers and “Stronger Together” for employees. Each card exists in German, English and French, personally addressed via mail merge.'),
     ('Bis zum Versand','Through to dispatch','Druckvorbereitung mit der Druckerei für Karten, Adressetiketten und Couverts, Offerten, Bestellung der Geschenke und Koordination der Lieferanten.','Prepress with the printer for cards, address labels and envelopes, quotes, ordering the gifts and coordinating suppliers.'))
   +gallery('gx','Weihnachtskarte',['x_karteA-3.jpg','x_karteA-4.jpg','x_karteA-5.jpg','x_karteA-2.jpg'],150,en=['x_karteA-3.jpg','x_karteA-4.jpg','x_karteA-1.jpg','x_karteA-2.jpg']),link=('Ganze Kampagne','Full campaign','1ub6RRXMbhZQRUq33avRvH'))
 +card(sflip,CP,('Songkran-Grusskarte','Songkran greeting card'),('Zum thailändischen Neujahrsfest, einem Fest des Wassers: zwei Pagoden mit der thailändischen und der Schweizer Flagge verbinden die beiden Länder, dazu Wasserspritzer, Wellen und Blüten.','For Thai New Year, a festival of water: two pagodas with the Thai and Swiss flags link the two countries, with splashes, waves and blossoms.'),('A5',('Englisch','English')),
   blocks(('Für wen','For whom','CP Pump Systems hat in Thailand eine Niederlassung. Zum Fest ging die Karte an Kundinnen und Kunden und weitere Kontakte vor Ort.','CP Pump Systems has a branch in Thailand. For the festival, the card went to customers and other local contacts.'),
     ('Von der Skizze zur Karte','From sketch to card','Die Karte lag komplett bei mir. Ich begann mit sechs Bleistiftskizzen, entwickelte daraus zwei Entwürfe und wählte das Motiv mit den Pagoden. Danach folgten Reinzeichnung, Druckvorbereitung und Bestellung.','The card was entirely my project. I started with six pencil sketches, developed two drafts and chose the pagoda motif, followed by final artwork, prepress and ordering.'))
   +gallery('gs','Songkran',['karte-1.jpg','karte-2.jpg','skizze.jpg'],160),hint=('Klick dreht die Karte, zweiter Klick zeigt sie gross','Click to turn the card, click again to view it large'))))
# 06 Messegrafik
W8=[('ChemUK 2026','Rückwand mit Weltkarte und Kernbotschaft.','Back wall with world map and key message.','m_chemuk.jpg','f_uk_fascia.jpg'),('CRU Sulphur + Sulphuric Acid Berlin 2026','«Keep Your Molten Sulphur Flowing», drei Paneele.','“Keep Your Molten Sulphur Flowing”, three panels.','ms_wand.jpg',None),('DK Hub Dunkerque 2026','Paneele, Tür der Standkabine und Blende.','Panels, booth cabin door and fascia.','m_dk.jpg','f_dk.jpg'),('Fertilizer Latino Americano 2026','Rückwand mit Birkenwald und Claim.','Back wall with birch forest and claim.','m_fla.jpg',None),('Pumps & Valves Dortmund 2025','Zwei Wände eines Eckstands.','Two walls of a corner booth.','m_pv25.jpg',None),('Pétro+Chimie Le Havre 2025','Design der Petrochymia 2024 weitergeführt.','Continuing the Petrochymia 2024 design.','m_lehavre.jpg',None),('Petrochymia 2024','Sechs Paneele mit Weltkarte und Wassermotiv, dazu die Blende über dem Stand.','Six panels with world map and water motif, plus the fascia above the booth.','m_petro24.jpg','f_p24_fac6.jpg')]
walls=''
for t_,de,en,f,bl in W8:
    gallery('x',t_,[f]+([bl] if bl else []))
    RID[0]+=1; g='w'+str(RID[0]); take(g,f,t_)
    walls+=f'<button class="mt" data-gallery="{g}" data-n="0"><span class="mi"><img src="img/{f}" alt="{t_}">'+(f'<span class="cnt">{T("+ Blende","+ fascia")}</span>' if bl else '')+f'</span><b>{t_}</b><small>{T(de,en)}</small></button>'
gallery('x','Petrochymia 2026',['m_petro26.jpg','f_p26.jpg'])
feat=row(CP,('Petrochymia 2026','Petrochymia 2026'),('Der aktuelle Auftritt: Paneele mit grossformatigem Anlagenfoto, der neuen Weltkarte und Swiss-Made-Zeichen, darüber die Blende mit Logo und Claim.','The latest booth: panels with a large plant photo, the new world map and the Swiss Made mark, topped by the fascia with logo and claim.'),'m_petro26.jpg',(('Französisch','French'),('mit Blende','with fascia'))).replace('class="row"','class="row feat"')
gallery('x','ACHEMA 2024',['achema_mock.jpg','achema_front.jpg'])
RID[0]+=1; take('w'+str(RID[0]),'achema_mock.jpg','ACHEMA 2024')
walls+=f'<button class="mt" data-gallery="w{RID[0]}" data-n="0"><span class="mi st"><img src="img/achema_mock.jpg" alt="Stele ACHEMA 2024"></span><b>{T("Stele ACHEMA 2024","Display column ACHEMA 2024")}</b><small>{T("Vorne bedruckte Folie zu Service und Ersatzteilen, sonst weiss.","Printed foil on the front about service and spare parts, white elsewhere.")}</small></button>'
theke='';_x=(CP,('Stele ACHEMA 2024','Display column ACHEMA 2024'),('Freistehende Stele am Stand: vorne die bedruckte Folie zu Service und Ersatzteilen, hinten weiss.','Free-standing column at the booth: printed foil on the front about service and spare parts, white at the back.'),'achema_mock.jpg',(('Folie 1800 × 2200 mm','foil 1800 × 2200 mm'),))
SEC.append(('messegrafik',('Messegrafik','Exhibition graphics'),('Rückwände, Blenden und Folien für die Messestände, abgestimmt auf Standgrösse, Messeland und Sprache. Die Wände bestehen aus einzelnen Paneelen, hier nebeneinander gezeigt. Bild anklicken, um es gross zu sehen.','Back walls, fascias and foils for trade fair booths, tailored to booth size, country and language. Walls consist of individual panels, shown side by side. Click an image to view it large.'),
 feat+f'<div class="sub"><h4>{T("Weitere Messen","More trade fairs")}</h4></div>'+'<div class="mgrid">'+walls+'</div>'))
# 07 Infografiken
SEC.append(('infografiken',('Infografiken','Infographics'),('Grafiken, die komplexe Inhalte auf einen Blick zeigen und in Broschüren, auf Messewänden und auf der Website wiederverwendet werden.','Graphics that show complex content at a glance and are reused in brochures, on booth walls and on the website.'),
 row(CP,('Weltkarte der Standorte','World map of locations'),('Standorte, Tochterfirmen und Niederlassungen sowie Mitarbeitende in weiteren Ländern, als Punktraster mit geordneten Beschriftungen, in zwei Formaten: breit für Messewände, im Hochformat für Broschüren.','Locations, subsidiaries and branches plus employees in further countries, as a dot grid with ordered labels, in two formats: wide for booth walls, portrait for brochures.'),'k_neu.jpg',(('2 Formate','2 formats'),('mehrere Sprachen','several languages')),
   more=gallery('kw','Weltkarte',['k_neu.jpg','k_bro.jpg'],300,en=['neu_en.jpg','k_bro.jpg']))
 +row(CP,('Firmengeschichte als Zeitstrahl','Company history timeline'),('Zwei A4-Seiten im Company Profile, «passioniert – swiss made – innovativ»: Meilensteine als Schlangenlinie mit Bildern von Produkten, Maschinen, Gebäuden und Flaggen für neue Märkte.','Two A4 pages in the Company Profile, “passionate – swiss made – innovative”: milestones along a winding line with images of products, machines, buildings and flags for new markets.'),'zs_spread.jpg',(('7 Sprachen','7 languages'),),more=gallery('kz','Zeitstrahl',['zs_spread.jpg'],320,en=['zs_spread_en.jpg']))))
# 08 Redesigns
map3=tabs('wk',[('Ursprünglich','Original',f'<div class="frame">{zb("rw","k_bro_grau.jpg","Ursprüngliche Weltkarte","plan")}</div>'),('1. Erneuerung','1st redesign',f'<div class="frame">{zb("rw","k_alt_blau.jpg","Erste Erneuerung","plan")}</div>'),('2. Erneuerung','2nd redesign',f'<div class="frame">{zb("rw","k_neu.jpg","Zweite Erneuerung","plan")}</div>')])
mappe=tabs('fm',[('Aussenseite','Outside',ba('mappe22-1.jpg','mappe23-1.jpg',('Faltmappe aussen',))),('Innenseite','Inside',ba('mappe22-2.jpg','mappe23-2.jpg',('Faltmappe innen',)))])
info=tabs('ia',[('Vorderseite','Front',ba('g_info22-1.jpg','g_info23-1.jpg',('Flyer Infoabende vorne',))),('Rückseite','Back',ba('g_info22-2.jpg','g_info23-2.jpg',('Flyer Infoabende hinten',)))])
SEC.append(('redesigns',('Redesigns','Redesigns'),('Bestehendes neu gestaltet: klarer, bildstärker und einheitlicher. Den Regler ziehen oder die Stufen anklicken, um alt und neu zu vergleichen.','Existing materials redesigned: clearer, more visual and more consistent. Drag the slider or click the steps to compare old and new.'),
 rd(('Weltkarte in zwei Schritten','World map in two steps'),('Von der grauen Karte über eine flächige Fassung in CP-Blau zum finalen Punktraster mit geordneten Beschriftungen.','From the grey map via a solid version in CP blue to the final dot grid with ordered labels.'),CP,map3)
 +rd(('Messestand Petrochymia: 2024 und 2026','Petrochymia booth: 2024 and 2026'),('Vom Wassermotiv mit blauer Karte zum grossformatigen Anlagenfoto mit neuer Weltkarte.','From the water motif with a blue map to a large plant photo with the new world map.'),CP,ba('r_p24.jpg','r_p26.jpg',('Petrochymia',),('2024','2024'),('2026','2026')))
 +rd(('Messewand WEGA','WEGA booth wall'),('Vom waagrechten Band mit kleinen Kacheln zu hochformatigen, bildstarken Paneelen in Blau und Weiss.','From a horizontal band with small tiles to bold portrait panels in blue and white.'),GO,ba('wand_alt.jpg','wand_neu.jpg',('Messewand WEGA',)))
 +rd(('Faltmappe','Presentation folder'),('Statt einzelner Felder mit verschiedenen Bildern ein durchgehendes Panoramabild und klare Textspalten.','Instead of separate panels with different images, one continuous panorama and clear text columns.'),GO,mappe)
 +rd(('Flyer Infoabende 2022 und 2023','Information evening flyer 2022 and 2023'),('Vom weissen Flyer mit Siegel zum Gebäudefoto mit blauer Diagonale, «Eintritt frei» und QR-Anmeldung.','From a white flyer with a seal to a building photo with a blue diagonal, “free entry” and QR registration.'),GO,info)))
toc=''.join(f'<a href="#{k}"><span>{i:02d}</span>{T(*t)}</a>' for i,(k,t,_,_) in enumerate(SEC,1))
secs=''.join(f'<section class="cat" id="{k}"><div class="chead"><span class="num">{i:02d}</span><div><h2>{T(*t)}</h2><p>{T(*intro)}</p></div></div><div class="list">{html}</div></section>' for i,(k,t,intro,html) in enumerate(SEC,1))
body=f'<div class="wrap"><div class="topbar"><p class="note">{T("Entwurf «Grafik &amp; Print»","Draft “Graphic &amp; Print”")}</p><div class="lang" role="group" aria-label="Sprache"><button data-lang="de" aria-pressed="true">DE</button><button data-lang="en" aria-pressed="false">EN</button></div></div><header class="hero"><p class="crumb">{T("Arbeiten","Work")}</p><h1>{T("Grafik &amp; Print","Graphic &amp; Print")}</h1><p class="lead">{T("Broschüren, Flyer, Inserate, Karten und Messegrafik für CP Pump Systems und GOLDINGER Immobilien, vom Konzept bis zur fertigen Druckdatei.","Brochures, flyers, ads, cards and exhibition graphics for CP Pump Systems and GOLDINGER Immobilien, from concept to print-ready file.")}</p><nav class="toc">{toc}</nav></header>{secs}</div>'
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

html[lang=en] .l-de,html:not([lang=en]) .l-en{display:none}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:12px}
.lang{display:flex;gap:4px}.lang button{all:unset;cursor:pointer;font:700 .8rem var(--font);padding:6px 11px;border-radius:99px;border:1px solid var(--line)}.lang button[aria-pressed=true]{background:var(--accent);color:#fff;border-color:var(--accent)}
.pgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:16px}
.pcov{all:unset;cursor:pointer;display:grid;gap:6px}.pcov .vis{padding:14px}.pcov img{width:100%;box-shadow:0 8px 20px rgba(0,0,0,.16)}
.pcov b{font-size:.92rem}.pcov small{color:var(--muted);font-size:.8rem}
.pcov[aria-expanded=true] .vis{outline:2px solid var(--accent)}.pcov:focus-visible .vis{outline:3px solid var(--accent)}
.sub .more{margin-top:18px}
.cardvis{gap:12px;perspective:1600px}.hint{color:var(--muted);font-size:.78rem}
.row.card{grid-template-columns:600px minmax(0,1fr)}.cardvis{overflow:hidden}.fold{position:relative;width:min(250px,40vw);aspect-ratio:875/1241;cursor:pointer;transform:translateX(0);transition:transform .7s}
.fold.open{transform:translateX(50%)}
.fold .in-r{position:absolute;inset:0;width:100%;height:100%;box-shadow:0 10px 24px rgba(0,0,0,.18)}
.fold .cover,.flip .cover{position:absolute;inset:0;transform-style:preserve-3d;transition:transform .9s cubic-bezier(.4,.1,.2,1)}
.fold .cover{transform-origin:left center}
.fold.open .cover{transform:rotateY(-180deg)}
.cover img{position:absolute;inset:0;width:100%;height:100%;backface-visibility:hidden;box-shadow:0 10px 24px rgba(0,0,0,.18)}
.cover .b{transform:rotateY(180deg)}
.flip{position:relative;width:min(300px,60vw);aspect-ratio:1166/1654;cursor:pointer}
.flip.open .cover{transform:rotateY(180deg)}
.fold:focus-visible,.flip:focus-visible{outline:3px solid var(--accent);outline-offset:6px}
.card .vis{min-height:480px}
.vis .zoom.page{transform:none}
.vis .zoom.page img{box-shadow:0 2px 4px rgba(0,0,0,.08),0 14px 34px rgba(0,0,0,.2);border-radius:1px 3px 3px 1px}
.vis .zoom.page::before{content:"";position:absolute;inset:0 auto 0 0;width:5%;background:linear-gradient(90deg,rgba(0,0,0,.14),rgba(0,0,0,0));z-index:1;pointer-events:none}
.row.feat{grid-template-columns:minmax(0,1fr)}.row.feat .vis .zoom{max-height:none;width:100%}
.row.sm .vis .zoom.plan{max-height:120px;width:100%}
.blenden{display:grid;gap:14px}.blende .zoom{aspect-ratio:auto}.blende img{height:auto}
.rdi{display:grid;gap:16px}.rdi .ba,.rdi .tabs{max-width:760px}.rdi .frame{max-width:760px}
.tabbar{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}.tab{all:unset;cursor:pointer;font:700 .82rem var(--font);padding:6px 12px;border-radius:99px;border:1px solid var(--line)}.tab[aria-selected=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.tabp[hidden]{display:none}.frame{background:var(--tint);border-radius:12px;padding:20px}.frame .zoom{aspect-ratio:2100/1100;background:transparent!important;border:0!important}
#lb{border:0;padding:0;max-width:none;max-height:none;width:100vw;height:100vh;background:rgba(236,238,242,.55);-webkit-backdrop-filter:blur(22px) saturate(1.2);backdrop-filter:blur(22px) saturate(1.2);color:#15181b}
#lb::backdrop{background:transparent}
.vw{display:grid;grid-template-rows:auto 1fr auto;height:100%;gap:10px;padding:14px 18px}
.vwtop{display:flex;align-items:center;gap:16px}.vwtop b{font-size:1rem}.vwtop #vwC{opacity:.7;font-size:.85rem}
.vwl{display:flex;gap:4px;margin-left:auto}.vwl[hidden]{display:none}.vwl button{all:unset;cursor:pointer;font:700 .8rem var(--font);padding:5px 11px;border-radius:99px;border:1px solid rgba(0,0,0,.25)}.vwl button[aria-pressed=true]{background:#15181b;color:#fff}
#close{all:unset;cursor:pointer;font-size:1.4rem;padding:4px 10px;margin-left:8px}.vwl[hidden]+#close{margin-left:auto}
.vwstage{display:grid;grid-template-columns:48px minmax(0,1fr) 48px;align-items:center;min-height:0}
#prev,#next{all:unset;cursor:pointer;font-size:2.6rem;text-align:center;opacity:.8}#prev:hover,#next:hover{opacity:1}
.spread{display:flex;justify-content:center;align-items:center;height:100%;min-height:0;gap:0}
.spread{position:relative}.spread img{max-height:calc(100vh - 170px);max-width:100%;object-fit:contain;box-shadow:0 3px 8px rgba(0,0,0,.1),0 24px 50px rgba(0,0,0,.22);border-radius:1px 3px 3px 1px}
.spread.two img{max-width:50%;box-shadow:0 24px 50px rgba(0,0,0,.22)}.spread.two img:first-child{border-radius:3px 0 0 3px;-webkit-mask-image:linear-gradient(90deg,#000 92%,rgba(0,0,0,.82))}.spread.two img:last-child{border-radius:0 3px 3px 0;-webkit-mask-image:linear-gradient(90deg,rgba(0,0,0,.82),#000 8%)}
.bk{position:relative;display:flex;max-width:100%;max-height:100%}.spread.two .bk::after{content:"";position:absolute;left:50%;top:0;bottom:0;width:60px;transform:translateX(-50%);background:linear-gradient(90deg,rgba(0,0,0,0),rgba(0,0,0,.16) 48%,rgba(0,0,0,.16) 52%,rgba(0,0,0,0));pointer-events:none}
.vis .zoom img[src$="kat_mag.png"]{box-shadow:none}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:26px 22px}
.mt{all:unset;cursor:pointer;display:grid;gap:6px;align-content:start}.mt .mi{position:relative;display:grid;place-items:center;aspect-ratio:16/10;background:var(--tint);border-radius:12px;padding:16px;overflow:hidden}
.mt .mi img{position:absolute;inset:16px;width:calc(100% - 32px);height:calc(100% - 32px);object-fit:contain;transition:transform .3s}.mt:hover .mi img{transform:scale(1.03)}.mt .mi.st img{mix-blend-mode:multiply}
.mt b{font-size:.95rem;margin-top:4px}.mt small{color:var(--muted);font-size:.85rem}.mt:focus-visible .mi{outline:3px solid var(--accent);outline-offset:3px}
#thumbs{display:flex;gap:6px;overflow-x:auto;justify-content:center;padding-bottom:4px}#thumbs button{all:unset;cursor:pointer;opacity:.5;flex:0 0 auto}#thumbs button[aria-current=true]{opacity:1;outline:2px solid #15181b}#thumbs img{box-shadow:0 2px 6px rgba(0,0,0,.2)}#thumbs img{height:52px;width:auto;display:block}
.zoom .cnt,.pcov .cnt,.mt .cnt{z-index:2;position:absolute;left:10px;bottom:10px;background:rgba(0,0,0,.72);color:#fff;font:700 .7rem var(--font);padding:4px 9px;border-radius:99px}
.pcov .vis{position:relative}
.lnk2{all:unset;cursor:pointer;font-weight:700;color:var(--ink);border-bottom:1px solid var(--line)}
@media (prefers-reduced-motion:reduce){.fold,.fold .cover,.flip .cover{transition:none}}
@media (max-width:760px){.vis .zoom.page{transform:none}.row.card{grid-template-columns:minmax(0,1fr)}.card .vis{min-height:340px}.pgrid{grid-template-columns:repeat(2,minmax(0,1fr))}.fold.open{transform:translateX(45%)}.card .vis{min-height:300px}}
</style>''')
VIEW=r'''
let base=[],alt=null,cur=[],i=0,lng='de',gid='';const d=document.getElementById('lb'),sp=document.getElementById('sp'),th=document.getElementById('thumbs'),vl=document.getElementById('vwL');
const wide=()=>innerWidth>900;
function pagesOf(){return lng==='en'&&alt?alt:base}
function show(){cur=pagesOf();if(i>=cur.length)i=cur.length-1;let idx=[i];
 const portrait=im=>true;
 if(wide()&&cur.length>2&&i>0){const L=i%2?i:i-1;idx=[L];if(L+1<cur.length)idx.push(L+1);}
 sp.innerHTML='<div class="bk">'+idx.map(k=>`<img src="${cur[k][0]}" alt="${cur[k][1]}">`).join('')+'</div>';sp.classList.toggle('two',idx.length>1);
 document.getElementById('vwC').textContent=cur.length>1?`${idx.map(k=>k+1).join('–')} / ${cur.length}`:'';
 th.innerHTML=cur.length>1?cur.map(([s,a],k)=>`<button data-k="${k}" aria-label="${a}" aria-current="${idx.includes(k)}"><img src="${s}" alt=""></button>`).join(''):'';
 vl.hidden=!alt;vl.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.vl===lng));}
function step(dir){let L=i===0?0:(i%2?i:i-1);if(dir>0){L=L===0?1:L+2}else{L=L<=1?0:L-2}if(L<cur.length){i=L}show();}
window.ysOpen=(g,n)=>open(g,n);function open(g,n){gid=g;base=G[g];alt=GEN[g]||null;lng=document.documentElement.lang==='en'&&alt?'en':'de';i=n||0;document.getElementById('vwT').textContent=(base[0][1]||'').replace(/, \d+$/,'');show();d.showModal();}
document.querySelectorAll('[data-gallery]').forEach(b=>b.addEventListener('click',()=>open(b.dataset.gallery,+(b.dataset.n||0))));
document.getElementById('prev').onclick=()=>{if(wide()&&cur.length>2){step(-1)}else{i=Math.max(0,i-1);show()}};
document.getElementById('next').onclick=()=>{if(wide()&&cur.length>2){step(1)}else{i=Math.min(cur.length-1,i+1);show()}};
document.getElementById('close').onclick=()=>d.close();
vl.onclick=e=>{const b=e.target.closest('[data-vl]');if(b){lng=b.dataset.vl;show()}};
th.onclick=e=>{const b=e.target.closest('button');if(b){i=+b.dataset.k;show()}};
d.addEventListener('click',e=>{if(e.target===d)d.close()});
d.addEventListener('keydown',e=>{if(e.key==='ArrowRight')document.getElementById('next').click();if(e.key==='ArrowLeft')document.getElementById('prev').click()});
'''
NAV="""
// Sprache, Aufklappen, Karten, Tabs, Vorher/Nachher
function setLang(l){document.documentElement.lang=l;document.querySelectorAll('[data-lang]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.lang===l));try{localStorage.setItem('ys-lang',l)}catch(e){}}
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));
try{const l=localStorage.getItem('ys-lang');if(l)setLang(l)}catch(e){}
document.querySelectorAll('.tog').forEach(t=>t.addEventListener('click',()=>{const m=document.getElementById(t.getAttribute('aria-controls'));const o=t.getAttribute('aria-expanded')==='true';
 if(t.classList.contains('pcov')){t.closest('.sub').querySelectorAll('.pcov').forEach(x=>x.setAttribute('aria-expanded','false'));t.closest('.sub').querySelectorAll('.more').forEach(x=>x.hidden=true);}
 t.setAttribute('aria-expanded',!o);m.hidden=o;}));
document.querySelectorAll('.fold,.flip').forEach(c=>{const f=()=>{if(c.classList.contains('open')&&c.dataset.g){window.ysOpen(c.dataset.g,0);return}c.classList.add('open');c.setAttribute('aria-pressed',true)};c.addEventListener('click',f);c.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();f()}})});
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',()=>{const bar=t.parentElement;bar.querySelectorAll('.tab').forEach(x=>{x.setAttribute('aria-selected',x===t);document.getElementById(x.dataset.tab).hidden=x!==t;});}));
document.querySelectorAll('[data-open]').forEach(b=>b.addEventListener('click',()=>document.querySelector('.zoom[data-gallery="'+b.dataset.open+'"][data-n="0"]').click()));
document.querySelectorAll('.ba input').forEach(r=>r.addEventListener('input',()=>r.parentElement.style.setProperty('--p',r.value+'%')));
"""
d='<dialog id="lb" aria-label="Ansicht"><div class="vw"><div class="vwtop"><b id="vwT"></b><span id="vwC"></span><div class="vwl" id="vwL"><button data-vl="de">DE</button><button data-vl="en">EN</button></div><button id="close" aria-label="Schliessen">✕</button></div><div class="vwstage"><button id="prev" aria-label="Zurück">‹</button><div class="spread" id="sp"></div><button id="next" aria-label="Weiter">›</button></div><div class="thumbs" id="thumbs"></div></div></dialog>'
scr=b[b.index('<script>'):b.index('</script>')+9]
gjs='const G={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in G.items())+'\n};'
gje='const GEN={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in GEN.items())+'\n};'
scr='<script>\n'+gjs+'\n'+gje+VIEW+'\n</script>'
scr=scr[:scr.rindex('</script>')]+NAV+'</script>'
out='<title>Grafik und Print</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/gp/page/grafik-print.html','w',encoding='utf-8').write(out)
print('ok',sum(len(v) for v in G.values()))
