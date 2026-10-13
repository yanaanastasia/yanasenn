import re
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
style=b[b.index('<style>'):b.index('</style>')+8]
style=style.replace('/* Layout: Projektseite Broschüren','/* Layout: Projektseite Infografiken (abgeleitet von Broschüren)',1)
extra='''
.rneu{aspect-ratio:2400/920}.rA4p{aspect-ratio:1241/1754}.final{display:grid;grid-template-columns:2.609fr .7075fr;gap:20px;align-items:start}
.final figure{gap:10px}
.final .zoom{border-radius:10px}
.tag{display:flex;gap:10px;align-items:baseline;font-size:.85rem;color:var(--muted)}
.tag b{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--green)}
.past{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;max-width:680px}
.past .zoom{aspect-ratio:16/10;background:#fff}
.past .zoom.plan img{padding:18px}
.past img{filter:saturate(.9)}
.badge{display:inline-block;font:700 .7rem var(--font);letter-spacing:.08em;text-transform:uppercase;padding:4px 10px;border-radius:99px;background:var(--green);color:#fff}
.badge.old{background:var(--line);color:var(--muted)}
.head{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
@media (max-width:760px){.final,.past{grid-template-columns:minmax(0,1fr)}.final figure:last-child{max-width:260px}}
.sw{display:grid;gap:10px}
.steps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.steps .zoom{aspect-ratio:16/10}
.use{display:grid;grid-template-columns:minmax(0,1fr) 240px;gap:40px;align-items:start}
@media (max-width:640px){.use{grid-template-columns:minmax(0,1fr)}.use figure{max-width:240px}}
.steps .zoom.plan img{padding:18px}
.steps figcaption{font-size:.85rem;color:var(--muted);display:flex;gap:8px;align-items:baseline}
.steps figcaption b{color:var(--ink);font-weight:700}
@media (max-width:640px){.steps{grid-template-columns:minmax(0,1fr)}}.sw .zoom[hidden]{display:none}.rmap{aspect-ratio:2400/1233}.ra4{aspect-ratio:1400/1897}.rsq{aspect-ratio:1600/1584}.rsp{aspect-ratio:2400/1696}
.thumbrow{display:grid;grid-template-columns:repeat(auto-fill,200px);gap:12px}
.thumbrow figcaption{font-size:.78rem;color:var(--muted);line-height:1.35}
.thumbrow.sm{grid-template-columns:repeat(auto-fill,150px)}
@media (max-width:520px){.thumbrow,.thumbrow.sm{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>'''
style=style.replace('</style>',extra)
def th(g,n,src,cap,ratio,cls='plan'):
    return f'<figure><button class="zoom {cls} {ratio}" data-gallery="{g}" data-n="{n}" aria-label="{cap} gross ansehen"><img src="img/{src}" alt="{cap}"></button><figcaption>{cap}</figcaption></figure>'
G={
 'fin':[('neu.jpg','Finale Weltkarte für Messewände, Deutsch'),('neu_en.jpg','Finale Weltkarte für Messewände, Englisch'),('bro_neu.jpg','Finale Weltkarte für Broschüren, Company Profile')],
 'evo':[('bro_grau.jpg','Ursprüngliche Karte'),('alt_blau.jpg','Erste Überarbeitung für Messewände')],
 'zs':[('zs_spread.jpg','Firmengeschichte, Deutsch'),('zs_spread_en.jpg','Firmengeschichte, Englisch')],
}
evo=''.join(f'<figure><button class="zoom plan" data-gallery="evo" data-n="{i}" aria-label="{c} gross ansehen"><img src="img/{s}" alt="{c}"></button><figcaption class="tag">{c}</figcaption></figure>' for i,(s,c) in enumerate(G['evo']))
def sw(g,ratio,cls,alt,cap):
    a,b=G[g][:2]
    return (f'<figure class="sw"><div class="langTabs" role="group" aria-label="Sprache wählen"><button type="button" data-sw="{g}" data-i="0" aria-pressed="true">DE</button><button type="button" data-sw="{g}" data-i="1" aria-pressed="false">EN</button></div>'
     f'<button class="zoom {cls} {ratio}" data-gallery="{g}" data-n="0" aria-label="{a[1]} gross ansehen"><img src="img/{a[0]}" alt="{alt}, Deutsch"></button>'
     f'<button class="zoom {cls} {ratio}" data-gallery="{g}" data-n="1" aria-label="{b[1]} gross ansehen" hidden><img src="img/{b[0]}" alt="{alt}, Englisch" loading="lazy"></button>'
     f'<figcaption class="cap">{cap}</figcaption></figure>')
zs=sw('zs','rsp','page','Zeitstrahl Firmengeschichte über zwei A4-Seiten','Firmengeschichte, Doppelseite im Company Profile')
fin=('<div class="final">'
 '<figure><button class="zoom plan rneu" data-gallery="fin" data-n="0" aria-label="Finale Weltkarte für Messewände gross ansehen"><img src="img/neu.jpg" alt="Finale Weltkarte als grünes Punktraster, breites Format für Messewände"></button><figcaption class="tag"><b>Messewand</b>breites Format</figcaption></figure>'
 '<figure><button class="zoom page rA4p" data-gallery="fin" data-n="2" aria-label="Finale Weltkarte für Broschüren gross ansehen"><img src="img/bro_neu.jpg" alt="Finale Weltkarte als Punktraster auf der Seite Locations im Company Profile"></button><figcaption class="tag"><b>Broschüre</b>Hochformat A4</figcaption></figure>'
 '</div>')
body=f'''
<div class="wrap">
  <p class="note">Entwurf zur Anordnung. Alle Bilder lassen sich anklicken und gross ansehen.</p>

  <header class="hero">
    <p class="eyebrow">Grafik · CP Pump Systems</p>
    <h1>Infografiken &amp; Karten</h1>
    <p class="lead">CP Pump Systems ist mit Standorten, Tochterfirmen und Partnern weltweit tätig und blickt auf eine lange Firmengeschichte zurück. Beides sollte auf einen Blick verständlich sein, in mehreren Sprachen und für ganz unterschiedliche Formate. Ich entwickelte dafür die Weltkarte und den Zeitstrahl, von den ersten Entwürfen bis zu den fertigen Sprachversionen.</p>
  </header>

  <section class="chapter">
    <p class="eyebrow">1 · Weltkarte</p>
    <div class="text">
      <h2>Weltkarte der Standorte</h2>
      <p>Die Karte zeigt die Standorte, Tochterfirmen und Niederlassungen von CP Pump Systems sowie Mitarbeitende in weiteren Ländern, mit einer Legende für CP Pump Systems und Partner. Die finale Fassung ist ein Punktraster mit geordneten Beschriftungen, in zwei Formaten: breit für die Messewände und im Hochformat für die Broschüren.</p>
    </div>
    <div class="grpbox"><div class="head"><span class="badge">Final</span></div>{fin}</div>
    <div class="grpbox"><div class="head"><span class="badge old">Vorher</span><span class="cap">Ursprünglich grau, danach eine erste Überarbeitung in CP-Blau</span></div><div class="past">{evo}</div></div>
  </section>

  <section class="chapter">
    <p class="eyebrow">2 · Zeitstrahl</p>
    <div class="text">
      <h2>Firmengeschichte als Zeitstrahl</h2>
      <p>Für das Company Profile gestaltete ich die Firmengeschichte als Zeitstrahl über zwei A4-Seiten, unter dem Motto «passioniert – swiss made – innovativ». Die Meilensteine von der Gründung bis heute folgen einer Schlangenlinie, mit grünen Jahreszahlen und Bildern von Produkten, Maschinen, Gebäuden und Flaggen für neue Märkte.</p>
      <p>Den Zeitstrahl gibt es auf Deutsch, Englisch, Französisch, Italienisch, Polnisch und Chinesisch sowie in einer US-Version.</p>
    </div>
    {zs}
  </section>

  <section class="chapter">
    <p class="eyebrow">Meine Aufgaben</p>
    <ul class="tasks"><li>Konzept und Gestaltung</li><li>Farbvarianten</li><li>Sprachversionen</li><li>Anpassung bei neuen Standorten</li></ul>
  </section>
</div>
'''
SWJS='''
// DE/EN-Umschalter\ndocument.querySelectorAll('[data-sw]').forEach(btn=>btn.addEventListener('click',()=>{const g=btn.dataset.sw,i=btn.dataset.i;document.querySelectorAll('[data-sw="'+g+'"]').forEach(x=>x.setAttribute('aria-pressed',x===btn));document.querySelectorAll('.zoom[data-gallery="'+g+'"]').forEach(z=>z.hidden=z.dataset.n!==i);}));
'''
d=b[b.index('<dialog id="lb"'):b.index('</dialog>')+9]
scr=b[b.index('<script>'):b.index('</script>')+9]
gjs='const G={\n'+',\n'.join(f" {k}:["+','.join(f'["img/{s}","{c}"]' for s,c in v)+"]" for k,v in G.items())+'\n};'
scr=re.sub(r'const G=\{.*?\n\};',lambda m:gjs,scr,flags=re.S)
i=scr.find('// Sprachen-Umschalter')
if i>0: scr=scr[:i]+'</script>'
scr=scr[:scr.rindex('</script>')]+SWJS+'</script>'
out='<title>Infografiken und Karten</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/karten/page/infografiken.html','w',encoding='utf-8').write(out)
print('ok', out.count('data-gallery'))
