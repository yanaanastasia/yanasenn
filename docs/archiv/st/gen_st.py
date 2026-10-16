S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
BASE=b[b.index('<style>')+7:b.index('</style>')]
A='https://claude.ai/artifact/'
def T(de,en): return f'<span class="l-de">{de}</span><span class="l-en" lang="en">{en}</span>'

HL=[('XWP2ub9yg6MDibVE8ZQZ2c','p_achema.jpg','Messen','Trade fairs','ACHEMA 2024 in Frankfurt','ACHEMA 2024 in Frankfurt','Messeauftritt mit Gesamtverantwortung','Trade fair presence with overall responsibility'),
('1ub6RRXMbhZQRUq33avRvH','p_xmas.jpg','Grafik & Print','Graphic & Print','Weihnachten 2026','Christmas 2026','Karten, Texte und Geschenke für drei Zielgruppen','Cards, copy and gifts for three audiences'),
('5CenZNzAZtaKJN37GonvR1','p_usa.jpg','Messen','Trade fairs','Mobiler Messestand für die USA','Mobile trade fair stand for the USA','Standbox nach Mass, eigene Möbel, Lager vor Ort','Custom stand box, own furniture, local storage'),
('6CM4QZGbNhy5bjxvvMbnbc','p_bro.jpg','Grafik & Print','Graphic & Print','Broschüren in neun Sprachen','Brochures in nine languages','Ein einheitlicher Aufbau für alle Broschüren','One consistent structure for all brochures'),
('AWzk8y7iyFhZyJJQF4gszF','p_reels.jpg','Social Media','Social media','Immobilien-Reels','Property reels','Objekte in kurzen Videos für Instagram','Properties in short videos for Instagram'),
('3YqAhMFfdAX84mYeGeTHFW','p_marke.jpg','Corporate Design & Raum','Corporate design & space','Die Marke im eigenen Gebäude','The brand in its own building','Zwei Sitzungszimmer und Beschilderung','Two meeting rooms and signage')]

# id, url, titleDE, titleEN, descDE, descEN, imgs, sections[(id,de,en)], projects[(url,de,en)]
CAT=[
('messen','NcW3BUdbXA5pKkgtA91Zvi','Messen','Trade fairs','Messeauftritte in Europa, den USA und Indien: Planung, Standdesign, Logistik und Kommunikation.','Trade fair presences in Europe, the USA and India: planning, stand design, logistics and communication.',['m2.jpg'],
 [('international','International','International'),('partner','Am Stand eines Partners','At a partner\'s stand'),('schweiz','Schweiz','Switzerland')],
 [('XWP2ub9yg6MDibVE8ZQZ2c','ACHEMA 2024','ACHEMA 2024'),('5CenZNzAZtaKJN37GonvR1','Mobiler Messestand USA','Mobile stand USA')]),
('print','GZFTrhEhSPs7GJyEAEEvNi','Grafik & Print','Graphic & Print','Alles, was gedruckt wird: von der Broschüre über Inserate bis zur Messewand.','Everything that gets printed: from brochures and ads to trade fair walls.',['g1.jpg','g2.jpg','g3.jpg'],
 [('broschueren','Broschüren und Magazin','Brochures and magazine'),('flyer','Flyer','Flyers'),('inserate','Inserate','Ads'),('infoblaetter','Infoblätter','Info sheets'),('grusskarten','Grusskarten','Greeting cards'),('messegrafik','Messegrafik','Trade fair graphics'),('infografiken','Infografiken','Infographics'),('redesigns','Redesigns','Redesigns')],
 [('6CM4QZGbNhy5bjxvvMbnbc','Broschüren in neun Sprachen','Brochures in nine languages'),('1ub6RRXMbhZQRUq33avRvH','Weihnachten 2026','Christmas 2026')]),
('corporate','PvoLUQgLQFMc4gD6bygMcb','Corporate Design & Raum','Corporate design & space','Erscheinungsbild und Räume: die Marke im eigenen Gebäude und eine komplette Markenidentität.','Identity and spaces: the brand in its own building and a complete brand identity.',['c1.jpg','c2.jpg','c3.jpg'],
 [('raum','Raumgestaltung','Interior design'),('marke','Markenidentität','Brand identity'),('redesigns','Redesigns','Redesigns')],
 [('3YqAhMFfdAX84mYeGeTHFW','Die Marke im eigenen Gebäude','The brand in its own building')]),
('social','9pLQefB7tUVEDh7QPpWNy6','Social Media','Social media','Feed-Design, Storys, Reels, Feiertagsgrafiken und LinkedIn für zwei sehr unterschiedliche Marken.','Feed design, stories, reels, holiday graphics and LinkedIn for two very different brands.',['s1.jpg','s2.jpg','s3.jpg'],
 [('raster','Feed-Design','Feed design'),('storys','Storys','Stories'),('reels','Reels','Reels'),('anlaesse','Anlässe','Occasions'),('linkedin','LinkedIn','LinkedIn')],
 [('AWzk8y7iyFhZyJJQF4gszF','Immobilien-Reels','Property reels')]),
('digital','PdvNqJCMVj6QRj1SDPPNTW','Website und E-Mail','Website and email','Website-Pflege in Craft CMS, Newsletter und Mailings, E-Mail-Banner zu jeder Messe.','Website content in Craft CMS, newsletters and mailings, email banners for every trade fair.',['w1.jpg','w2.jpg','w3.jpg'],
 [('website','Website','Website'),('newsletter','Newsletter und Mailings','Newsletter and mailings'),('banner','E-Mail-Banner','Email banners')],[]),
('foto','9yWsuDQj8HqKbDUfF7j4vK','Foto & Video','Photo & video','Firmenshooting, Reportagen und animierte Erklärvideos.','Company shoots, reportage and animated explainer videos.',['f1.jpg','f2.jpg','f3.jpg'],
 [('erklaervideos','Erklärvideos','Explainer videos'),('halloween','Halloween-Videoflyer','Halloween video flyer'),('shooting','Mitarbeitende bei der Arbeit','Employees at work'),('reportage','Reportage Maschinenlieferung','Machine delivery'),('immobilienvideos','Immobilienvideos','Property videos')],[('AWzk8y7iyFhZyJJQF4gszF','Immobilien-Reels','Property reels')]),
('werbeartikel','J5R7HvN9ixfCbeDmSsdBEf','Werbeartikel','Promotional items','Giveaways, Geschenke für Kunden und Mitarbeitende, Kleidung mit Logo.','Giveaways, gifts for clients and staff, branded clothing.',['k1.jpg'],
 [('giveaways','Giveaways','Giveaways'),('katalog','Katalog','Catalogue'),('goldinger','Fruchtgummis GOLDINGER','Fruit gums GOLDINGER'),('kleidung','Arbeits- und Messekleidung','Clothing')],[('XWP2ub9yg6MDibVE8ZQZ2c','ACHEMA 2024','ACHEMA 2024'),('1ub6RRXMbhZQRUq33avRvH','Weihnachten 2026','Christmas 2026')]),
]

CSS=r'''
html[lang=en] .l-de,html:not([lang=en]) .l-en{display:none}
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:12px;padding-top:22px;padding-bottom:22px}
.crumb{font:700 .7rem var(--font);letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}.crumb b{color:var(--accent)}
.lang{display:flex;gap:4px}.lang button{all:unset;cursor:pointer;font:700 .8rem var(--font);padding:6px 11px;border-radius:99px;border:1px solid var(--line)}.lang button[aria-pressed=true]{background:var(--accent);color:#fff;border-color:var(--accent)}
.kick{font:700 .7rem var(--font);letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.intro{padding:24px 0 40px;max-width:760px}.intro h1{font-size:clamp(2.4rem,5vw,3.8rem);line-height:1.04;letter-spacing:-.02em;margin-top:8px}.intro p{color:var(--muted);font-size:1.1rem;margin-top:14px}
.jump{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}.jump a{font:700 .8rem var(--font);text-decoration:none;color:var(--ink);border:1px solid var(--line);border-radius:99px;padding:7px 14px}.jump a:hover{border-color:var(--accent);color:var(--accent)}
h2.sh{font-size:clamp(1.6rem,3vw,2.2rem)}.shead{display:flex;justify-content:space-between;align-items:end;gap:16px;margin-bottom:22px}.shead p{color:var(--muted);max-width:56ch;margin-top:6px}
section.blk{padding:48px 0;border-top:1px solid var(--line)}
.hl{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:22px}
.hl a{grid-column:span 2;text-decoration:none;color:var(--ink);display:grid;gap:12px}

.hl .pic{position:relative;overflow:hidden;border-radius:16px;aspect-ratio:4/3;background:var(--tint)}

.hl .pic img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}
.hl a:hover .pic img{transform:scale(1.04)}
.hl .tag{position:absolute;left:12px;top:12px;background:rgba(255,255,255,.92);color:#15181b;font:700 .66rem var(--font);letter-spacing:.08em;text-transform:uppercase;border-radius:99px;padding:5px 10px}
.hl b{font-size:1.15rem}.hl small{color:var(--muted);font-size:.92rem;display:block;margin-top:2px}
.hl a:focus-visible .pic{outline:3px solid var(--accent);outline-offset:3px}
.cats{display:grid;gap:22px}
.cat{display:grid;grid-template-columns:minmax(0,420px) minmax(0,1fr);gap:36px;align-items:center;background:var(--tint);border-radius:20px;padding:26px}
.cat .vis{display:flex;align-items:center;justify-content:center;height:300px;padding:0 10px}
.cat .vis img{display:block;height:auto;width:auto;max-height:200px;max-width:44%;border-radius:3px;box-shadow:0 14px 30px rgba(0,0,0,.2);transition:transform .4s;position:relative}
.cat .vis img:nth-child(2){max-height:250px;max-width:58%;z-index:2;margin:0 -26px}
.cat .vis img:only-child{max-height:260px;max-width:100%;margin:0}
.cat .vis:hover img{transform:translateY(-4px)}
.cat .num{font:700 .8rem var(--font);color:var(--accent);letter-spacing:.08em}
.cat h3{font-size:1.7rem;margin-top:4px}.cat p{color:var(--muted);margin-top:8px;max-width:58ch}
.cat .lbl{font:700 .66rem var(--font);letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin-top:18px;display:block}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.chips a{font-size:.82rem;text-decoration:none;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:99px;padding:5px 12px}
.chips a:hover{border-color:var(--accent);color:var(--accent)}
.chips a.proj{background:var(--ink);color:var(--bg);border-color:var(--ink)}.chips a.proj::after{content:" ↗"}
.cta{margin-top:20px;display:inline-flex;gap:10px;align-items:center;background:var(--accent);color:#fff;text-decoration:none;font:700 .9rem var(--font);border-radius:99px;padding:11px 20px}
.cat.soon{opacity:.75}.cat.soon .vis img{filter:grayscale(.3)}
.badge{display:inline-block;margin-top:20px;font:700 .75rem var(--font);border:1px dashed var(--muted);color:var(--muted);border-radius:99px;padding:8px 16px}
.legend{display:flex;gap:18px;flex-wrap:wrap;color:var(--muted);font-size:.82rem;margin-top:10px}.legend span{display:inline-flex;gap:6px;align-items:center}.legend i{display:inline-block;width:22px;height:12px;border-radius:99px;border:1px solid var(--line);background:var(--bg)}.legend i.p{background:var(--ink);border-color:var(--ink)}
footer{padding:30px 0 60px;color:var(--muted);font-size:.85rem}
@media (prefers-reduced-motion:reduce){.hl .pic img,.cat .vis img{transition:none}}
@media (max-width:860px){.hl a,.hl a:nth-child(1),.hl a:nth-child(2){grid-column:span 6}.cat{grid-template-columns:minmax(0,1fr);padding:18px}.cat .vis{height:230px}.cat .vis img{max-height:150px}.cat .vis img:nth-child(2){max-height:190px;margin:0 -18px}.shead{display:block}}
'''
def link(u,sec=''): return f'{A}{u}{"#"+sec if sec else ""}'
hl='<div class="hl">'+''.join(f'<a href="{link(u)}" target="_blank" rel="noopener"><div class="pic"><img src="img/{im}" alt="" loading="lazy"><span class="tag">{T(cd,ce)}</span></div><div><b>{T(td,te)}</b><small>{T(dd,de)}</small></div></a>' for u,im,cd,ce,td,te,dd,de in HL)+'</div>'
cats=''
for n,(cid,u,td,te,dd,de,ims,secs,projs) in enumerate(CAT,1):
    vis_cls='vis'
    imgs=''.join(f'<img src="img/{i}" alt="" loading="lazy">' for i in ims)
    vis=f'<a class="{vis_cls}" href="{link(u)}" target="_blank" rel="noopener" aria-label="{td} öffnen">{imgs}</a>' if u else f'<div class="{vis_cls}">{imgs}</div>'
    body=f'<span class="num">{n:02d}</span><h3>{T(td,te)}</h3><p>{T(dd,de)}</p>'
    if u:
        body+=f'<span class="lbl">{T("Auf dieser Seite","On this page")}</span><div class="chips">'+''.join(f'<a href="{link(u,s)}" target="_blank" rel="noopener">{T(a,b2)}</a>' for s,a,b2 in secs)+'</div>'
        if projs: body+=f'<span class="lbl">{T("Eigene Projektseiten","Own project pages")}</span><div class="chips">'+''.join(f'<a class="proj" href="{link(pu)}" target="_blank" rel="noopener">{T(a,b2)}</a>' for pu,a,b2 in projs)+'</div>'
        body+=f'<a class="cta" href="{link(u)}" target="_blank" rel="noopener">{T("Seite öffnen","Open page")} ↗</a>'
    else:
        body+=f'<span class="badge">{T("In Arbeit","In progress")}</span>'
    cats+=f'<article class="cat{"" if u else " soon"}" id="{cid}"><div>{vis}</div><div>{body}</div></article>'
jump=''.join(f'<a href="#{c[0]}">{T(c[2],c[3])}</a>' for c in CAT)
body=f'''<div class="wrap topbar"><span class="crumb">yanasenn.ch / <b>{T("Arbeiten","Work")}</b></span><div class="lang"><button data-lang="de" aria-pressed="true">DE</button><button data-lang="en" aria-pressed="false">EN</button></div></div>
<main class="wrap"><div class="intro"><span class="kick">{T("Portfolio","Portfolio")}</span><h1>{T("Arbeiten","Work")}</h1><p>{T("Marketing, Gestaltung und Kommunikation für Industrie und Immobilien: zuerst ausgewählte Projekte mit der ganzen Geschichte, darunter alle Arbeiten nach Kategorien.","Marketing, design and communication for industry and real estate: first selected projects with the full story, then all work by category.")}</p></div>
<section class="blk" id="projekte"><div class="shead"><div><span class="kick">{T("Ausgewählte Projekte","Selected projects")}</span><h2 class="sh">{T("Die ganze Geschichte","The full story")}</h2><p>{T("Sechs Projekte mit eigener Seite, von der Idee bis zur Umsetzung.","Six projects with their own page, from idea to execution.")}</p></div></div>{hl}</section>
<section class="blk" id="alle"><div class="shead"><div><span class="kick">{T("Alle Arbeiten","All work")}</span><h2 class="sh">{T("Nach Kategorien","By category")}</h2><p>{T("Jede Kategorie ist eine Seite. Die Stichworte springen direkt zum passenden Abschnitt.","Each category is one page. The tags jump straight to the matching section.")}</p>
<div class="legend"><span><i></i>{T("Abschnitt auf der Kategorieseite","Section on the category page")}</span><span><i class="p"></i>{T("Eigene Projektseite","Own project page")}</span></div></div></div>
<nav class="jump" aria-label="Kategorien" style="margin:0 0 22px">{jump}</nav><div class="cats">{cats}</div></section>
<footer>{T("Entwurf zur Diskussion · Links öffnen die Entwurfsseiten in einem neuen Fenster.","Draft for discussion · links open the draft pages in a new window.")}</footer></main>'''
JS='''function setLang(l){document.documentElement.lang=l;document.querySelectorAll('[data-lang]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.lang===l));try{localStorage.setItem('ys-lang',l)}catch(e){}}
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));try{const l=localStorage.getItem('ys-lang');if(l)setLang(l)}catch(e){}'''
out=f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Portfolio-Struktur yanasenn.ch</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap"><style>{BASE}{CSS}</style></head><body>{body}<script>{JS}</script></body></html>'''
open(S+'/st/page/struktur.html','w',encoding='utf-8').write(out);print('ok')
