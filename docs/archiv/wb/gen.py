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
CP='CP Pump Systems'; GO='GOLDINGER Immobilien'
MQ1=['anzeige.jpg','ms_bro-1.jpg','i_petro.jpg','g_hev23.jpg','g_info23-1.jpg','b_aug.jpg','ms_fact-1.jpg','g_sonnenhof-1.jpg']
MQ2=['m_petro26.jpg','g_gutschein-3.jpg','i_tfs.jpg','f_lead.jpg','mappe23-1.jpg','i_chemuk.jpg','ms_bro-6.jpg','g_gruenblick.jpg']
row=lambda L,c='':f'<div class="mrow {c}" aria-hidden="true">'+''.join(f'<img src="img/{f}" alt="">' for f in L+L)+'</div>'
hero=f'<div class="marquee">{row(MQ1)}{row(MQ2,"rev")}</div>'
ms=(item('anz','Anzeige',CP,'Fachzeitschrift World Fertilizer, halbe Seite quer',['anzeige.jpg'],420)
   +item('wand','Messe-Rückwand',CP,'«Keep Your Molten Sulphur Flowing», drei Paneele',['ms_wand.jpg'],420)
   +item('bro','Broschüre',CP,'A4, acht Seiten, Englisch',[f'ms_bro-{i}.jpg' for i in range(1,9)])
   +item('fact','Factsheet',CP,'A4, zwei Seiten',['ms_fact-1.jpg','ms_fact-2.jpg'])
   +item('us','Flyer für die USA',CP,'US-Letter, zwei Seiten',['ms_us-1.jpg','ms_us-2.jpg']))
ins_cp=''.join(fig('ins',f,c,'plan') for f,c in [('i_tfs.jpg','The Fertilizer Show, Messekatalog'),('i_petro.jpg','Petrochymia, Messekatalog'),('i_chemuk.jpg','ChemUK, Messekatalog')])
ins_go=''.join(fig('ins',f,c,'plan') for f,c in [('g_hev22.jpg','Hauseigentümer-Magazin: neue Website und 35 Jahre'),('g_hev23.jpg','Hauseigentümer-Magazin: Ratgeber'),('g_wega.jpg','Messe WEGA'),('g_sgkb.jpg','Infoabende, Regionalzeitungen'),('sck.jpg','Clubmagazin eines Sportclubs')])
fl=(item('lead','Sofort verfügbare Pumpensysteme',CP,'A4, Deutsch und Englisch',['f_lead.jpg'])
   +item('info22','Infoabende',GO,'A5 quer, zwei Seiten',['g_info22-1.jpg','g_info22-2.jpg'],200)
   +item('info23','Infoveranstaltungen',GO,'A5 quer, zwei Seiten',['g_info23-1.jpg','g_info23-2.jpg'],200)
   +item('gut','Gutschein Wertermittlung',GO,'A5 quer, vier Seiten',[f'g_gutschein-{i}.jpg' for i in range(1,5)],200)
   +item('sonne','Neubauprojekt Sonnenhof',GO,'A5, zwei Seiten',['g_sonnenhof-1.jpg','g_sonnenhof-2.jpg'])
   +item('gruen','Tag der offenen Tür',GO,'Flyer zu einem Neubauprojekt',['g_gruenblick.jpg']))
mg=''.join(item(g,ti,CP,me,[f],900).replace('class="item"','class="item wide"') for g,ti,me,f in [('w24','Petrochymia 2024','Rückwand aus sechs Paneelen, Französisch','m_petro24.jpg'),('wuk','ChemUK 2026','Rückwand 6 m, Englisch','m_chemuk.jpg'),('w26','Petrochymia 2026','Rückwand mit Anlagenfoto und neuer Weltkarte','m_petro26.jpg')])
def ba(a,b,la,lb,cap):
    from subprocess import run
    W,H=map(int,run(['identify','-format','%w %h',I+a],capture_output=True,text=True).stdout.split())
    return f'<figure class="babox"><div class="ba" style="--r:{W}/{H}"><img src="img/{a}" alt="Vorher: {cap}"><img class="after" src="img/{b}" alt="Nachher: {cap}"><span class="bar"></span><span class="lbl l1">{la}</span><span class="lbl l2">{lb}</span><input type="range" min="0" max="100" value="50" aria-label="Vorher und Nachher vergleichen: {cap}"></div><figcaption class="tag">{cap}</figcaption></figure>'
vn=ba('wand_alt.jpg','wand_neu.jpg','Vorher','Nachher','Messewand WEGA')+ba('mappe22-1.jpg','mappe23-1.jpg','Vorher','Nachher','Faltmappe, Aussenseite')+ba('mappe22-2.jpg','mappe23-2.jpg','Vorher','Nachher','Faltmappe, Innenseite')
weitere=''.join(fig('wei',f,c,'plan') for f,c in [('g_fruchtgummi.jpg','Verpackung Fruchtgummi'),('g_auto.jpg','Autoaufkleber')])
ban=''.join(fig('ban',f,c,'plan') for f,c in [('b_cru_banner.jpg','CRU Sulphur + Sulphuric Acid'),('b_tfs_banner.jpg','The Fertilizer Show'),('b_fla.jpg','Fertilizer Latino Americano'),('b_pv.jpg','Pumps & Valves'),('b_dk.jpg','DK Hub'),('b_petro.jpg','Petrochymia')])
soc=''.join(fig('soc',f,c,'plan') for f,c in [('b_sammel_de.jpg','Sammelbanner aller Messen'),('b_fla_social.jpg','LinkedIn: Fertilizer Latino Americano'),('b_aug.jpg','LinkedIn: 1. August')])
body=f'''
<div class="wrap">
  <p class="note">Entwurf zur Anordnung. Alle Bilder lassen sich anklicken und gross ansehen.</p>
  <header class="hero">
    <p class="eyebrow">Grafik · CP Pump Systems und GOLDINGER Immobilien</p>
    <h1>Werbung: Print &amp; Digital</h1>
    {hero}
    <p class="lead" style="margin-top:8px">Fachleute aus Chemie, Düngemittel- und Prozessindustrie informieren sich in Fachzeitschriften, Messekatalogen, auf Fachportalen und per E-Mail; Immobilieneigentümer in Regionalzeitungen, Magazinen und über Flyer. Jede Anzeige muss in Sekunden zeigen, worum es geht.</p>
    <p>Ich gestalte Anzeigen, Flyer und digitale Werbemittel bis zur Druckdatei und passe sie für jedes Format und jede Sprache an.</p>
  </header>

  <section class="chapter">
    <p class="eyebrow">1 · Molten Sulphur</p>
    <div class="text"><h2>Eine Botschaft, viele Formate</h2>
      <p>Für Pumpen, die flüssigen Schwefel fördern, entstand eine Reihe zusammengehöriger Werbemittel, von der Anzeige oben über die Messe-Rückwand bis zur Broschüre. Gelb, das Dreiecksmuster und die Schnittzeichnung der beheizten Pumpe verbinden alle Formate. Die Texte basieren auf bestehendem Material und sind mit dem Verkauf abgestimmt.</p></div>
    {ms}
  </section>

  <section class="chapter">
    <p class="eyebrow">2 · Inserate</p>
    <div class="text"><h2>Inserate in Katalogen, Magazinen und Zeitungen</h2>
      <p>Für CP in den Katalogen der Fachmessen, jeweils in der Sprache des Messelandes; für GOLDINGER im Hauseigentümer-Magazin, zur Messe WEGA und als Serie zu den Infoabenden in mehreren Regionalzeitungen.</p></div>
    <p class="sub">CP Pump Systems</p><div class="grid4">{ins_cp}</div>
    <p class="sub">GOLDINGER Immobilien</p><div class="grid4">{ins_go}</div>
  </section>

  <section class="chapter">
    <p class="eyebrow">3 · Flyer</p>
    <div class="text"><h2>Flyer und weitere Drucksachen</h2></div>
    {fl}
    <p class="sub">Weitere Drucksachen</p><div class="grid4">{weitere}</div>
  </section>

  <section class="chapter">
    <p class="eyebrow">4 · Messegrafik</p>
    <div class="text"><h2>Rückwände für Messestände</h2>
      <p>Für die Messestände gestalte ich die Rückwände und Blenden, jeweils in der Sprache des Messelandes und abgestimmt auf die Standgrösse.</p></div>
    {mg}
  </section>

  <section class="chapter">
    <p class="eyebrow">5 · Vorher / Nachher</p>
    <div class="text"><h2>Neu gestaltet bei GOLDINGER</h2>
      <p>Bei GOLDINGER habe ich bestehende Werbemittel neu gestaltet: klares Blau und Weiss, grosse Bilder, wenig Text. Den Regler ziehen, um alt und neu zu vergleichen.</p></div>
    {vn}
  </section>

  <section class="chapter">
    <p class="eyebrow">6 · Digital</p>
    <div class="text"><h2>Banner und Social Media</h2>
      <p>Zu jeder Messe entstehen E-Mail- und Web-Banner für Einladungen und Messeportale, dazu ein Sammelbanner mit allen kommenden Messen in Deutsch, Englisch und Französisch sowie Grafiken für LinkedIn.</p></div>
    <p class="sub">E-Mail- und Web-Banner</p><div class="grid2">{ban}</div>
    <p class="sub">Sammelbanner und LinkedIn</p><div class="grid4">{soc}</div>
  </section>

  <section class="chapter">
    <p class="eyebrow">7 · Anwendungsbericht</p>
    <div class="text"><h2>Ein Referenzprojekt als Bericht</h2>
      <p>Den Anwendungsbericht verfasste ich mit fachlicher Unterstützung des Verkaufsteams und veröffentlichte ihn in drei Sprachen auf der Website. Aufbau: Ausgangslage, Lösung, Gründe und technische Kennwerte.</p></div>
    <div class="report"><div class="rl"><small>Anwendungsbericht · Düngemittelproduktion</small><b>Dichtungslose Magnetkupplungspumpen für die Förderung von saurem Prozesswasser</b><p>Für ein neues Rückführungssystem von Pondwasser in einem Düngemittelwerk brauchte es eine dichte, korrosionsbeständige Lösung. Drei Magnetkupplungspumpen fördern das saure Wasser zurück in den Prozess.</p><div class="langs"><i>DE</i><i>EN</i><i>FR</i></div></div>
    <div class="rr"><div><strong>3</strong><span>Pumpen MKP 200-150-500</span></div><div><strong>682 m³/h</strong><span>Förderstrom gesamt</span></div><div><strong>72,6 %</strong><span>hydraulischer Wirkungsgrad</span></div></div></div>
  </section>

  <section class="chapter">
    <p class="eyebrow">Meine Aufgaben</p>
    <ul class="tasks"><li>Headlines und Texte</li><li>Gestaltung</li><li>Druckdaten</li><li>Sprachversionen</li><li>Banner und Social Media</li><li>Anwendungsbericht</li></ul>
  </section>
</div>
'''
d=b[b.index('<dialog id="lb"'):b.index('</dialog>')+9]
scr=b[b.index('<script>'):b.index('</script>')+9]
gjs='const G={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in G.items())+'\n};'
scr=re.sub(r'const G=\{.*?\n\};',lambda m:gjs,scr,flags=re.S)
SWJS="\n// Vorher/Nachher\ndocument.querySelectorAll('.ba input').forEach(r=>r.addEventListener('input',()=>r.parentElement.style.setProperty('--p',r.value+'%')));\n"
i=scr.find('// Sprachen-Umschalter')
if i>0: scr=scr[:i]+'</script>'
scr=scr[:scr.rindex('</script>')]+SWJS+'</script>'
out='<title>Werbung Print und Digital</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/wb/page/werbung.html','w',encoding='utf-8').write(out)
print('ok',sum(len(v) for v in G.values()))
