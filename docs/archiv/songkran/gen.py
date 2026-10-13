import re
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
style=b[b.index('<style>'):b.index('</style>')+8]
style=style.replace('/* Layout: Projektseite Broschüren','/* Layout: Projektseite Songkran (abgeleitet von Broschüren)',1)
style=style.replace('</style>','''
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;max-width:860px}
.pair .zoom,.sk .zoom{aspect-ratio:1166/1654}
.sk{display:grid;grid-template-columns:200px;gap:16px}
.sk .zoom{aspect-ratio:874/1240}
.tag{font-size:.85rem;color:var(--muted)}
@media (max-width:560px){.pair{grid-template-columns:minmax(0,1fr)}.sk{grid-template-columns:200px}}
</style>''')
G={'karte':[('karte-1.jpg','Vorderseite'),('karte-2.jpg','Rückseite mit Grusstext')],
   'sk':[('skizze.jpg','Skizze mit den zwei Pagoden')]}
def fig(g,i,s,c,cls):
    return f'<figure><button class="zoom {cls}" data-gallery="{g}" data-n="{i}" aria-label="{c} gross ansehen"><img src="img/{s}" alt="{c}"></button><figcaption class="tag">{c}</figcaption></figure>'
pair=''.join(fig('karte',i,s,c,'page') for i,(s,c) in enumerate(G['karte']))
sk=''.join(fig('sk',i,s,c,'page') for i,(s,c) in enumerate(G['sk']))
body=f'''
<div class="wrap">
  <p class="note">Entwurf zur Anordnung. Alle Bilder lassen sich anklicken und gross ansehen.</p>
  <header class="hero">
    <p class="eyebrow">Grafik · CP Pump Systems</p>
    <h1>Songkran-Grusskarte</h1>
    <div class="pair">{pair}</div>
    <p class="lead">Songkran ist das thailändische Neujahrsfest im April und ein Fest des Wassers. CP Pump Systems hat in Thailand eine Niederlassung. Zum Fest verschickte sie eine Grusskarte an ihre Kundinnen und Kunden und an weitere Kontakte vor Ort.</p>
    <p>Die Karte lag komplett bei mir: Ideen und Skizzen, Gestaltung, Druckvorbereitung und Bestellung.</p>
  </header>
  <section class="chapter">
    <p class="eyebrow">Von der Skizze zur Karte</p>
    <div class="text">
      <h2>Zwei Pagoden, zwei Länder</h2>
      <p>Am Anfang standen sechs Skizzen, daraus entstanden zwei Entwürfe. Das finale Motiv zeigt zwei Pagoden mit der thailändischen und der Schweizer Flagge, die Thailand und die Schweiz verbinden. Dazu kommen Wasserspritzer, Wellen und Blüten auf einem Verlauf von Gelb zu Blau, mit CP-Logo und «Happy Songkran Festival». Gedruckt wurde die Karte im Format A5 über eine Online-Druckerei.</p>
    </div>
    <div class="grpbox"><p class="grp">Skizze</p><div class="sk">{sk}</div></div>
  </section>
  <section class="chapter">
    <p class="eyebrow">Meine Aufgaben</p>
    <ul class="tasks"><li>Ideen und Skizzen</li><li>Gestaltung</li><li>Druckvorbereitung</li><li>Bestellung</li></ul>
  </section>
</div>
'''
d=b[b.index('<dialog id="lb"'):b.index('</dialog>')+9]
scr=b[b.index('<script>'):b.index('</script>')+9]
gjs='const G={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in G.items())+'\n};'
scr=re.sub(r'const G=\{.*?\n\};',lambda m:gjs,scr,flags=re.S)
i=scr.find('// Sprachen-Umschalter')
if i>0: scr=scr[:i]+'</script>'
out='<title>Songkran-Grusskarte</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/songkran/page/songkran.html','w',encoding='utf-8').write(out)
print('ok')
