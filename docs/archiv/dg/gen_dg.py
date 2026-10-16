import json,subprocess
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
I=S+'/dg/page/img/'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
style=b[b.index('<style>')+7:b.index('</style>')]
def size(f): return tuple(map(int,subprocess.run(['identify','-format','%w %h',I+f],capture_output=True,text=True).stdout.split()))
def T(de,en): return f'<span class="l-de">{de}</span><span class="l-en" lang="en">{en}</span>'
G={}
def zb(g,src,alt,full=None,cls=''):
    G.setdefault(g,[]).append((full or src,alt)); n=len(G[g])-1
    return f'<button class="zoom {cls}" data-gallery="{g}" data-n="{n}" aria-label="{alt} gross ansehen"><img src="img/{src}" alt="{alt}" loading="lazy"></button>'
def sec(n,id,t,intro,inner):
    return f'<section class="cat" id="{id}"><div class="chead"><span class="num">{n:02d}</span><div><h2>{T(*t)}</h2><p>{T(*intro)}</p></div></div>{inner}</section>'
CP='CP Pump Systems'; GO='GOLDINGER Immobilien'; A='https://claude.ai/artifact/'

# 1 Website
web=[('w_home.jpg','Startseite','Home page'),('w_messen.jpg','Messekalender mit Standnummern','Trade fair calendar with stand numbers'),
     ('w_news.jpg','News und Blog','News and blog'),('w_post_dk.jpg','Messebeitrag DK HUB GLOBAL','Trade fair post DK HUB GLOBAL'),
     ('w_post_prod.jpg','Produktbeitrag','Product post'),('w_downloads.jpg','Download-Bibliothek','Download library')]
brw=lambda f,a: f'<figure class="brw"><div class="bar"><i></i><i></i><i></i><span>cp-pumps.com</span></div>{zb("web",f,a)}</figure>'
s1=sec(1,'website',('Website','Website'),('Inhaltliche Pflege der Website von CP Pump Systems in Craft CMS, in Deutsch, Englisch, Französisch und Chinesisch.','Content management for the CP Pump Systems website in Craft CMS, in German, English, French and Chinese.'),
 f'''<div class="lead">{brw(web[0][0],web[0][1])}<div class="txt"><span class="client">{CP}</span><h3>{T("Die Website lebendig halten","Keeping the website alive")}</h3>
<p>{T("Technisch betreut eine Agentur die Website. Ich bin für die Inhalte verantwortlich: Ich schreibe Beiträge, halte Seiten und Downloads aktuell und sorge dafür, dass Website, Newsletter und Social Media dieselbe Geschichte erzählen.","An agency looks after the technical side. I am responsible for the content: I write posts, keep pages and downloads up to date and make sure website, newsletter and social media tell the same story.")}</p>
<div class="chips"><span>Craft CMS</span><span>Content</span><span>{T("Mehrsprachig","Multilingual")}</span></div></div></div>
<div class="wgrid">{"".join(f'<div>{brw(f,de)}<small>{T(de,en)}</small></div>' for f,de,en in web[1:])}</div>
<div class="blocks"><div><h4>{T("News und Blog","News and blog")}</h4><p>{T("Beiträge zu Messen, Produkten und Unternehmensthemen, inklusive Messekalender mit Standnummern und Gratis-Tickets.","Posts on trade fairs, products and company topics, including a trade fair calendar with stand numbers and free tickets.")}</p></div>
<div><h4>{T("Downloads","Downloads")}</h4><p>{T("Broschüren, Factsheets und Explosionszeichnungen in allen Sprachen laufend erneuern.","Continuously updating brochures, factsheets and exploded drawings in all languages.")}</p></div>
<div><h4>{T("Unternehmen und Karriere","Company and careers")}</h4><p>{T("Weltkarte und Kontaktseiten pro Land aktualisieren, Stellenanzeigen aufschalten und wieder entfernen, neue Mitarbeitende vorstellen.","Updating the world map and country contact pages, publishing and removing job ads, introducing new team members.")}</p></div>
<div><h4>{T("Ein Thema, viele Kanäle","One topic, many channels")}</h4><p>{T("Eine Messe taucht an mehreren Orten auf: im Messekalender, als Blogbeitrag, im Newsletter, auf LinkedIn und im E-Mail-Banner.","A trade fair appears in several places: in the calendar, as a blog post, in the newsletter, on LinkedIn and in the email banner.")}</p></div></div>''')

# 2 Newsletter / Mailings
mails=[('mail1_de','Einladung','Invitation'),('mail2_de','Mailing 2','Mailing 2'),('mail3_de','Mailing 3','Mailing 3'),('dank_de','Dankesmail nach der Messe','Thank-you mail after the fair')]
s2=sec(2,'newsletter',('Newsletter und Mailings','Newsletter and Mailings'),('Mailings rund um die ACHEMA 2024, versendet über Zoho: von der Einladung bis zum Dank nach der Messe.','Mailings around ACHEMA 2024, sent via Zoho: from the invitation to the thank-you after the fair.'),
 '<div class="mgrid4">'+''.join(f'<div class="ml">{zb("mail"+str(i),"c_"+f+".jpg",de,f+".jpg","tall")}<b>{T(de,en)}</b></div>' for i,(f,de,en) in enumerate(mails))+'</div>')

# 3 E-Mail-Banner
EB=[('achema','ACHEMA 2024'),('pv25','Pumps & Valves 2025'),('tfs25','The Fertilizer Show 2025'),('cru25','Sulphur + Sulphuric Acid 2025'),('pv26','Pumps & Valves 2026'),('fla26','Fertilizer Latino Americano 2026'),('dahej26','Dahej 2026'),('petro26','Petrochymia 2026'),('uk26','CHEMUK 2026'),('dk26','DK HUB GLOBAL 2026'),('cheme26','ChemE Show 2026'),('tfs26','The Fertilizer Show 2026'),('cru26','Sulphur + Sulphuric Acid 2026')]
s3=sec(3,'banner',('E-Mail-Banner','Email Banners'),('Zu jeder Messe ein Banner für die E-Mails des ganzen Teams, meist mit Link zum Gratis-Ticket.','For every trade fair a banner for the whole team\'s emails, usually linking to a free ticket.'),
 '<div class="bgrid">'+''.join(f'<figure>{zb("eb",f"e_{k}_vor0.jpg",n,cls="flat")}<figcaption>{n}</figcaption></figure>' for k,n in EB)+'</div>')

# 4 Web-Banner
s4=sec(4,'webbanner',('Web-Banner','Web Banners'),('Banner für Websites und Newsletter von Veranstaltern und für den eigenen Messeüberblick.','Banners for organisers\' websites and newsletters and for our own trade fair overview.'),
 f'''<div class="bgrid two"><figure>{zb("wb1","b90.png","Web-Banner Petrochymia 2026, 1000 × 90",cls="flat")}<figcaption>{T("Petrochymia 2026, Format 1000 × 90","Petrochymia 2026, 1000 × 90 format")}</figcaption></figure>
<figure>{zb("wb2","salons.jpg","Banner «Nos prochains salons»",cls="flat")}<figcaption>{T("«Nos prochains salons», Übersicht der nächsten Messen","«Nos prochains salons», overview of upcoming fairs")}</figcaption></figure></div>''')

# 5 LinkedIn
li=json.load(open(S+'/me/li.json'))
pick=[('pv26',0),('fla26',0),('uk26',0),('cheme26',0)]
def post(k,i):
    p=li[k][i]; t=p['text'].strip().replace('\n','<br>')
    return f'<article class="lic"><div class="lih"><span class="av">cp</span><div><b>CP Pump Systems</b><small>LinkedIn · {p["date"][:7].replace("-","/") if p["date"] else ""}</small></div></div>{zb("li"+k,p["images"][0],"LinkedIn-Beitrag "+k)}<p>{t}</p></article>'
s5=sec(5,'linkedin',('LinkedIn','LinkedIn'),('Beiträge vor, während und nach den Messen: Ankündigung mit Stand und Ticket, erster Messetag, Rückblick. Hier eine Auswahl der Ankündigungen.','Posts before, during and after trade fairs: announcement with stand and ticket, first day, recap. Here a selection of announcements.'),
 '<div class="ligrid">'+''.join(post(*x) for x in pick)+f'</div><p class="more2"><a class="lnk" href="{A}NcW3BUdbXA5pKkgtA91Zvi" target="_blank" rel="noopener">{T("Alle Beiträge pro Messe unter «Messen»","All posts per fair under «Trade Fairs»")} ↗</a></p>')

# 6 Instagram GOLDINGER
s6=sec(6,'instagram',('Instagram GOLDINGER','Instagram GOLDINGER'),('Feed-Beiträge für GOLDINGER Immobilien, alle von mir gestaltet: Ratgeber-Serien, Prozessgrafiken, Infoabende und das Hausmagazin.','Feed posts for GOLDINGER Immobilien, all designed by me: advice series, process graphics, information evenings and the customer magazine.'),
 f'''<div class="lead ig"><div class="phone"><div class="ph-top"><b>goldinger.ch</b></div><div class="igrid">{"".join(zb("ig",f"ig{n:02d}.jpg",f"Instagram-Beitrag {n+1}") for n in range(12))}</div></div>
<div class="txt"><span class="client">{GO}</span><h3>{T("Kanäle regelmässig bespielen","Keeping channels active")}</h3>
<p>{T("GOLDINGER war auf Instagram, Facebook, LinkedIn und YouTube präsent. Die Kanäle sollten Vertrauen in die Fachleute aufbauen und Objekte, Infoabende und das Hausmagazin bekannt machen. Ich betreute Redaktionsplan, Gestaltung der Beiträge, Fotografie und Video bis zum Schnitt.","GOLDINGER was present on Instagram, Facebook, LinkedIn and YouTube. The channels were meant to build trust in the experts and promote properties, information evenings and the customer magazine. I handled the editorial plan, post design, photography and video through to editing.")}</p>
<p>{T("Beiträge zu Themen wie Tipps für Käufer, Steuern beim Verkauf oder Immobilie im Alter, dazu Storys mit Umfragen und Countdowns zu den Infoabenden.","Posts on topics such as tips for buyers, taxes when selling or property in old age, plus stories with polls and countdowns to the information evenings.")}</p>
<div class="chips"><span>Social Media</span><span>{T("Redaktionsplanung","Editorial planning")}</span><span>TYPO3</span></div>
<div class="acts"><a class="lnk" href="{A}AWzk8y7iyFhZyJJQF4gszF" target="_blank" rel="noopener">{T("Immobilien-Reels ansehen","Watch property reels")} ↗</a></div></div></div>''')

css=r'''
html[lang=en] .l-de,html:not([lang=en]) .l-en{display:none}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:12px}
.lang{display:flex;gap:4px}.lang button{all:unset;cursor:pointer;font:700 .8rem var(--font);padding:6px 11px;border-radius:99px;border:1px solid var(--line)}.lang button[aria-pressed=true]{background:var(--accent);color:#fff;border-color:var(--accent)}
.cat{display:grid;gap:26px;padding:56px 0;border-top:1px solid var(--line)}
.chead{display:grid;grid-template-columns:90px minmax(0,1fr);gap:20px}.num{font:700 2.8rem/1 var(--font);color:var(--accent);opacity:.3}.chead p{color:var(--muted);margin-top:8px;max-width:62ch}
.client{font:700 .66rem var(--font);letter-spacing:.09em;text-transform:uppercase;color:var(--accent)}
.txt{display:grid;gap:10px;align-content:center}.txt h3{font-size:1.35rem}
.chips{display:flex;flex-wrap:wrap;gap:6px}.chips span{font-size:.75rem;border:1px solid var(--line);border-radius:99px;padding:3px 10px;color:var(--muted)}
.lnk{color:var(--ink);font-weight:700;text-decoration:none;border-bottom:1px solid var(--line)}
.zoom{all:unset;cursor:zoom-in;display:block;position:relative}.zoom img{display:block;width:100%;height:auto}
.zoom:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.lead{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:36px;align-items:center}
.brw{margin:0;border-radius:10px;overflow:hidden;box-shadow:0 14px 34px rgba(0,0,0,.18);background:#2a2e33}
.brw .bar{display:flex;align-items:center;gap:6px;padding:8px 12px}.brw .bar i{width:9px;height:9px;border-radius:50%;background:#6b7178}.brw .bar span{margin-left:12px;flex:1;background:#3a3f45;color:#c9ced4;font-size:.72rem;border-radius:6px;padding:3px 10px}
.wgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:26px 22px}.wgrid small{display:block;margin-top:8px;color:var(--muted);font-size:.85rem}
.blocks{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px}.blocks h4{font-size:.95rem;margin-bottom:6px}.blocks p{color:var(--muted);font-size:.95rem}
.mgrid4{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:24px}
.ml{display:grid;gap:10px}.ml .zoom{background:var(--tint);border-radius:12px;padding:16px;aspect-ratio:4/5;overflow:hidden}.ml .zoom img{box-shadow:0 10px 24px rgba(0,0,0,.18);border-radius:2px}
.ml .zoom::after{content:"";position:absolute;left:16px;right:16px;bottom:0;height:40%;background:linear-gradient(rgba(0,0,0,0),var(--tint))}
.ml b{font-size:.92rem}
.bgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px}.bgrid.two{grid-template-columns:repeat(auto-fit,minmax(320px,1fr))}
.bgrid figure{margin:0;display:grid;gap:8px}.bgrid .zoom{background:var(--tint);border-radius:12px;padding:18px}.bgrid .zoom img{box-shadow:0 6px 16px rgba(0,0,0,.14)}
.bgrid figcaption{color:var(--muted);font-size:.85rem}
.ligrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:22px;align-items:start}
.lic{background:var(--bg);border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:0 8px 22px rgba(0,0,0,.08);display:grid}
.lih{display:flex;gap:10px;align-items:center;padding:12px 14px}.lih b{display:block;font-size:.88rem}.lih small{color:var(--muted);font-size:.75rem}
.av{width:34px;height:34px;border-radius:50%;background:#1f6fb5;color:#fff;display:grid;place-items:center;font:700 .85rem var(--font)}
.lic p{padding:12px 14px 16px;font-size:.84rem;color:var(--muted);display:-webkit-box;-webkit-line-clamp:7;-webkit-box-orient:vertical;overflow:hidden}
.more2{margin-top:-6px}
.lead.ig{grid-template-columns:minmax(0,420px) minmax(0,1fr)}
.phone{background:#15181b;border-radius:34px;padding:14px;box-shadow:0 18px 40px rgba(0,0,0,.25)}
.ph-top{background:#fff;border-radius:22px 22px 0 0;padding:12px 14px;font-size:.85rem}
.igrid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#fff;border-radius:0 0 22px 22px;overflow:hidden;padding-bottom:12px}
.igrid .zoom img{aspect-ratio:1;object-fit:cover}
#lb{border:0;padding:0;max-width:none;max-height:none;width:100vw;height:100vh;background:rgba(236,238,242,.55);-webkit-backdrop-filter:blur(22px) saturate(1.2);backdrop-filter:blur(22px) saturate(1.2);color:#15181b}
#lb::backdrop{background:transparent}
.vw{display:grid;grid-template-rows:auto 1fr auto;height:100%;gap:10px;padding:14px 18px;box-sizing:border-box}
.vwtop{display:flex;align-items:center;gap:16px}.vwtop #vwC{opacity:.7;font-size:.85rem}
#close{all:unset;cursor:pointer;font-size:1.4rem;padding:4px 10px;margin-left:auto}
.vwstage{display:grid;grid-template-columns:48px minmax(0,1fr) 48px;align-items:center;min-height:0}
#prev,#next{all:unset;cursor:pointer;font-size:2.6rem;text-align:center;opacity:.8}#prev[hidden],#next[hidden]{visibility:hidden;display:block}
.sp{display:flex;justify-content:center;align-items:center;height:100%;min-height:0;overflow:auto}
.sp img{max-height:calc(100vh - 150px);max-width:100%;object-fit:contain;box-shadow:0 3px 8px rgba(0,0,0,.1),0 24px 50px rgba(0,0,0,.22)}
.sp.tall{align-items:flex-start}.sp.tall img{max-height:none;width:min(720px,100%)}
#thumbs{display:flex;gap:6px;overflow-x:auto;justify-content:center}#thumbs button{all:unset;cursor:pointer;opacity:.5;flex:0 0 auto}#thumbs button[aria-current=true]{opacity:1;outline:2px solid #15181b}#thumbs img{height:48px;display:block}
@media (max-width:760px){.chead{grid-template-columns:minmax(0,1fr);gap:4px}.lead,.lead.ig{grid-template-columns:minmax(0,1fr)}.bgrid{grid-template-columns:minmax(0,1fr)}}
'''
js='const G='+json.dumps({k:[["img/"+s,a] for s,a in v] for k,v in G.items()},ensure_ascii=False)+r''';
let cur=[],i=0;const d=document.getElementById('lb'),sp=document.getElementById('sp'),th=document.getElementById('thumbs');
function show(){const [s,a]=cur[i];const im=new Image();im.src=s;im.alt=a;sp.innerHTML='';sp.appendChild(im);
 im.onload=()=>sp.classList.toggle('tall',im.naturalHeight>im.naturalWidth*2);if(im.complete)im.onload();
 document.getElementById('vwT').textContent=a;document.getElementById('vwC').textContent=cur.length>1?`${i+1} / ${cur.length}`:'';
 document.getElementById('prev').hidden=document.getElementById('next').hidden=cur.length<2;
 th.innerHTML=cur.length>1?cur.map(([s,a],k)=>`<button data-k="${k}" aria-label="${a}" aria-current="${k===i}"><img src="${s}" alt=""></button>`).join(''):'';sp.scrollTop=0;}
document.querySelectorAll('[data-gallery]').forEach(b=>b.addEventListener('click',()=>{cur=G[b.dataset.gallery];i=+b.dataset.n;show();d.showModal()}));
document.getElementById('prev').onclick=()=>{i=(i-1+cur.length)%cur.length;show()};document.getElementById('next').onclick=()=>{i=(i+1)%cur.length;show()};
document.getElementById('close').onclick=()=>d.close();th.onclick=e=>{const b=e.target.closest('button');if(b){i=+b.dataset.k;show()}};
d.addEventListener('click',e=>{if(e.target===d||e.target===sp)d.close()});
d.addEventListener('keydown',e=>{if(cur.length>1&&e.key==='ArrowRight')document.getElementById('next').click();if(cur.length>1&&e.key==='ArrowLeft')document.getElementById('prev').click()});
function setLang(l){document.documentElement.lang=l;document.querySelectorAll('[data-lang]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.lang===l));try{localStorage.setItem('ys-lang',l)}catch(e){}}
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));try{const l=localStorage.getItem('ys-lang');if(l)setLang(l)}catch(e){}
'''
head=f'''<header class="wrap"><div class="topbar"><span class="client">yanasenn.ch · {T("Arbeiten","Work")}</span><div class="lang"><button data-lang="de" aria-pressed="true">DE</button><button data-lang="en" aria-pressed="false">EN</button></div></div>
<h1>{T("Digital und Social Media","Digital and Social Media")}</h1><p class="sub0">{T("Website, Newsletter, Banner und Social Media: Inhalte pflegen, gestalten und über alle Kanäle abstimmen.","Website, newsletter, banners and social media: maintaining, designing and aligning content across all channels.")}</p></header>'''
dlg='<dialog id="lb" aria-label="Ansicht"><div class="vw"><div class="vwtop"><b id="vwT"></b><span id="vwC"></span><button id="close" aria-label="Schliessen">✕</button></div><div class="vwstage"><button id="prev" aria-label="Zurück">‹</button><div class="sp" id="sp"></div><button id="next" aria-label="Weiter">›</button></div><div id="thumbs"></div></div></dialog>'
out=f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Digital und Social Media</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap"><style>{style}{css}
header.wrap,main.wrap{{max-width:1180px;margin:0 auto;padding:0 20px}}header.wrap{{padding-top:28px;padding-bottom:20px;display:grid;gap:14px}}.sub0{{color:var(--muted);max-width:62ch}}</style></head>
<body>{head}<main class="wrap">{s1}{s2}{s3}{s4}{s5}{s6}</main>{dlg}<script>{js}</script></body></html>'''
open(S+'/dg/page/digital.html','w',encoding='utf-8').write(out)
print('ok',sum(len(v) for v in G.values()))
