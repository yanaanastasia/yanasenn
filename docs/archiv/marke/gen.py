import re
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
style=b[b.index('<style>'):b.index('</style>')+8]
style=style.replace('/* Layout: Projektseite Broschüren','/* Layout: Projektseite Marke im Gebäude (abgeleitet von Broschüren)',1)
extra='''
.ph{border:1px dashed var(--line);border-radius:12px;padding:18px 20px;color:var(--muted);font-size:.9rem;background:color-mix(in srgb,var(--surface) 60%,transparent)}
.r169w{aspect-ratio:2051/1201}.r32{aspect-ratio:3/2}.r23{aspect-ratio:1078/1616}.r43m{aspect-ratio:4/3}
.thumbrow{display:grid;grid-template-columns:repeat(auto-fill,150px);gap:12px}
.thumbrow figcaption{font-size:.78rem;color:var(--muted);line-height:1.35}
:root #lb{border:0;padding:0;max-width:none;max-height:none;width:100vw;height:100vh;background:rgba(236,238,242,.6);-webkit-backdrop-filter:blur(22px);backdrop-filter:blur(22px);border-radius:0;box-shadow:none}
#lb::backdrop{background:transparent}#lb .lb{height:100%;box-sizing:border-box;grid-template-rows:1fr auto auto;padding:24px}
#lb .lbScroll{background:transparent;max-height:none;min-height:0}#lb .lbScroll img{max-height:calc(100vh - 140px);box-shadow:0 3px 8px rgba(0,0,0,.1),0 24px 50px rgba(0,0,0,.22)}
.split2{display:grid;grid-template-columns:5fr 7fr;gap:40px;align-items:start}
@media (max-width:860px){.split2{grid-template-columns:1fr}}
@media (max-width:520px){.thumbrow{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>'''
style=style.replace('</style>',extra)
def th(g,n,src,cap,ratio='r43m',cls='plan'):
    return f'<figure><button class="zoom {cls} {ratio}" data-gallery="{g}" data-n="{n}" aria-label="{cap} gross ansehen"><img src="img/{src}" alt="{cap}"></button><figcaption>{cap}</figcaption></figure>'
G={
 'hero':[('v2_2.jpg','Wandbild Birkenwald mit Claim, Druckdaten')],
 'var':[('v2_1.jpg','Wandbild mit Claim'),('v2_0.jpg','Logo und Claim im Fensterband')],
 'pan':[('pan_21.jpg','Technik und Entwicklung'),('pan_14.jpg','CAM'),('pan_2.jpg','Pumpenmontage'),('pan_24.jpg','Export'),('pan_25.jpg','Verkauf')],
 'rend':[('rend_lounge.jpg','Rendering der Möbelfirma: Lounge'),('rend_sitzung.jpg','Rendering der Möbelfirma: Sitzungszimmer')],
}
var=''.join(th('var',i,s,c) for i,(s,c) in enumerate(G['var']))
for i_,(s_,c_) in enumerate(G['pan']): G[f'pan{i_}']=[(s_,c_)]
G['smock']=[('sch_mock.jpg','Schild neben der Tür, Mockup')]
pan=th('smock',0,'sch_mock.jpg','Mockup: Schild neben der Tür','r23','visual')+''.join(th(f'pan{i}',0,s,c,'r23','visual') for i,(s,c) in enumerate(G['pan']))
del G['pan']
rend=''.join(th('rend',i,s,c,'r169','visual') for i,(s,c) in enumerate(G['rend']))
body=f'''
<div class="wrap">
  <p class="note">Entwurf zur Anordnung. Fotos der fertigen Räume folgen. Alle Bilder lassen sich anklicken und gross ansehen.</p>

  <header class="hero">
    <p class="eyebrow">Raum · CP Pump Systems</p>
    <h1>Die Marke im eigenen Gebäude</h1>
    <figure><button class="zoom visual r169w" data-gallery="hero" data-n="0" aria-label="Wandbild gross ansehen"><img src="img/v2_2.jpg" alt="Wandbild mit Birkenwald und dem Claim cleaner pumps, cleaner planet"></button><figcaption class="cap">Wandbild mit Birkenwald und Claim, Druckdaten</figcaption></figure>
    <p class="lead">Die Marke CP sollte nicht nur an Messen und in Broschüren sichtbar sein, sondern auch im eigenen Gebäude: dort, wo Kundschaft empfangen wird, und dort, wo die Mitarbeitenden täglich arbeiten.</p>
  </header>

  <section class="chapter">
    <p class="eyebrow">1 · Besprechungsräume</p>
    <div class="text">
      <h2>Zwei Besprechungsräume im CP-Design</h2>
      <p>Für die beiden Besprechungsräume gestaltete ich die Wände: ein Wandbild mit Birkenwald und dem Claim «cleaner pumps, cleaner planet™», umgesetzt als Digitaldruck-Tapete, dazu Paneele mit Logo und Claim im Fensterband. Die Entwürfe entstanden direkt auf Fotos der Räume, so liess sich die Wirkung vorab beurteilen.</p>
    </div>
    <div class="grpbox"><p class="grp">Finaler Entwurf</p><div class="thumbrow" style="grid-template-columns:repeat(auto-fill,150px)">{var}</div></div>
    <div class="text">
      <p>Die Einrichtung wählte ich zusammen mit der Möbelfirma nach Farbpaletten aus, nach einem Besuch im Showroom und anhand ihrer Renderings: Möbel in Grün- und Blautönen, passend zum Wandbild. Umgesetzt wurde die Einrichtung wie geplant, die Lieferung organisierte ich.</p>
    </div>
    <div class="grpbox"><p class="grp">Planung der Einrichtung</p><div class="thumbrow" style="grid-template-columns:repeat(auto-fill,150px)">{rend}</div></div>
    <p class="ph">Fotos der fertig eingerichteten Räume folgen.</p>
  </section>

  <section class="chapter">
    <p class="eyebrow">2 · Abteilungen</p>
    <div class="text">
      <h2>Schilder für die Abteilungen</h2>
      <p>Für die Abteilungen fotografierte ich die Mitarbeitenden bei der Arbeit, unter anderem bei der PFA-Auskleidung, im CAM sowie in Technik und Entwicklung. Die Fotos bearbeitete ich in Farbe und Schwarzweiss und kombinierte sie mit Produkt- und Betriebsbildern und Grafiken wie der Weltkarte zu Wandbildern und Paneelen.</p>
      <p>Jedes Paneel stellt eine Abteilung oder ein Thema vor, zweisprachig auf Deutsch und Englisch, mit grossem Bild und kurzen Fakten.</p>
    </div>
    <div class="grpbox"><p class="grp">Paneele, Auswahl</p><div class="thumbrow" style="grid-template-columns:repeat(auto-fill,150px)">{pan}</div></div>
  </section>

  <section class="chapter">
    <p class="eyebrow">Meine Aufgaben</p>
    <ul class="tasks"><li>Wandgestaltung und Layout-Varianten</li><li>Druckdaten</li><li>Auswahl der Einrichtung</li><li>Organisation der Lieferung</li><li>Fotografie der Mitarbeitenden</li><li>Wandbilder und Paneele</li></ul>
  </section>
</div>
'''
d=b[b.index('<dialog id="lb"'):b.index('</dialog>')+9]
scr=b[b.index('<script>'):b.index('</script>')+9]
gjs='const G={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in G.items())+'\n};'
scr=re.sub(r'const G=\{.*?\n\};',lambda m:gjs,scr,flags=re.S)
i=scr.find('// Sprachen-Umschalter')
if i>0: scr=scr[:i]+'</script>'
scr=scr.replace("function open(g,n){pages=G[g];i=n||0;","function open(g,n){pages=G[g];i=n||0;const one=pages.length<2;document.getElementById('prev').hidden=one;document.getElementById('next').hidden=one;th.style.display=one?'none':'';")
out='<title>Marke im Gebäude</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/marke/page/marke.html','w',encoding='utf-8').write(out)


print('ok', out.count('data-gallery'), 'function open(g,n){pages=G[g];i=n||0;const one' in out)
