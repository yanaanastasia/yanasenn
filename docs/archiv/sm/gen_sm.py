import json,subprocess,html,sys
WEBURL=open('weburl.txt').read().strip() if __import__('os').path.exists('weburl.txt') else '#'
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
P=S+'/sm/page/'
b=open(S+'/mockbro/broschueren.html',encoding='utf-8').read()
BASE=b[b.index('<style>')+7:b.index('</style>')]
def T(de,en): return f'<span class="l-de">{de}</span><span class="l-en" lang="en">{en}</span>'
A='https://claude.ai/artifact/'
G={}
def zb(g,src,alt,full=None,cls=''):
    G.setdefault(g,[]).append((full or src,alt)); n=len(G[g])-1
    return f'<button class="zoom {cls}" data-gallery="{g}" data-n="{n}" aria-label="{html.escape(alt)} gross ansehen"><img src="img/{src}" alt="{html.escape(alt)}" loading="lazy"></button>'
def sec(n,id,t,intro,inner,cls=''):
    return f'<section class="cat {cls}" id="{id}"><div class="chead"><span class="num">{n:02d}</span><div><h2>{T(*t)}</h2><p>{T(*intro)}</p></div></div>{inner}</section>'

CSS=r'''
html[lang=en] .l-de,html:not([lang=en]) .l-en{display:none}
body{background:var(--bg)}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:12px;padding-top:22px;padding-bottom:22px}.stage{overflow:hidden}
.crumb{font:700 .7rem var(--font);letter-spacing:.09em;text-transform:uppercase;color:var(--muted);text-decoration:none}.crumb b{color:var(--accent)}
.lang{display:flex;gap:4px}.lang button{all:unset;cursor:pointer;font:700 .8rem var(--font);padding:6px 11px;border-radius:99px;border:1px solid var(--line)}.lang button[aria-pressed=true]{background:var(--accent);color:#fff;border-color:var(--accent)}
.hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:40px;align-items:center;padding:20px 0 60px}
.hero h1{font-size:clamp(2.4rem,5vw,4rem);line-height:1.02;letter-spacing:-.02em}
.hero .lead{font-size:1.12rem;color:var(--muted);max-width:52ch;margin-top:16px}
.kick{font:700 .7rem var(--font);letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:18px}.chips span{font-size:.78rem;border:1px solid var(--line);border-radius:99px;padding:4px 11px;color:var(--muted)}
.stage{position:relative;height:520px}
.ph{position:absolute;background:#111;border-radius:30px;padding:9px;box-shadow:0 30px 60px rgba(0,0,0,.25)}
.ph>*{border-radius:22px;overflow:hidden;display:block;width:100%;height:100%;object-fit:cover;background:#fff}
.ph.a{width:230px;height:470px;left:0;top:30px}.ph.b{width:250px;height:510px;left:31%;top:0;z-index:2}.ph.c{width:230px;height:470px;right:0;top:40px}
.ph .feed{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;align-content:start;padding-top:34px;position:relative}
.ph .feed::before{content:"goldinger_immobilien";position:absolute;top:10px;left:12px;font:700 .72rem var(--font);color:#111}
.ph .feed img{width:100%;aspect-ratio:1;object-fit:cover;display:block}
.cat{display:grid;gap:28px;padding:64px 0;border-top:1px solid var(--line)}
.chead{display:grid;grid-template-columns:90px minmax(0,1fr);gap:20px}.num{font:700 2.8rem/1 var(--font);color:var(--accent);opacity:.3}.chead h2{font-size:clamp(1.6rem,3vw,2.2rem)}.chead p{color:var(--muted);margin-top:8px;max-width:64ch}
.zoom{all:unset;cursor:zoom-in;display:block;position:relative}.zoom img{display:block;width:100%;height:auto}
.zoom:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.duo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.brand{background:var(--tint);border-radius:16px;padding:28px;display:grid;gap:12px;align-content:start}
.brand h3{font-size:1.3rem}.brand p{color:var(--muted)}
.brand ul{margin:0;padding-left:18px;color:var(--muted)}.brand .client{font:700 .66rem var(--font);letter-spacing:.09em;text-transform:uppercase;color:var(--accent)}
.split{display:grid;grid-template-columns:minmax(0,400px) minmax(0,1fr);gap:44px;align-items:center}
.phone{background:#111;border-radius:36px;padding:12px;box-shadow:0 24px 50px rgba(0,0,0,.22)}
.phone .scr{background:#fff;border-radius:26px;overflow:hidden}
.phone .bar{display:flex;justify-content:space-between;padding:12px 16px;font:700 .8rem var(--font);color:#111}
.igrid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px}.igrid .zoom img{aspect-ratio:1;object-fit:cover}
.txt{display:grid;gap:12px}.txt h3{font-size:1.35rem}.txt p{color:var(--muted)}
.pts{display:grid;gap:14px;margin-top:6px}.pts div{border-left:3px solid var(--accent);padding:2px 0 2px 14px}.pts b{display:block;font-size:.95rem}.pts span{color:var(--muted);font-size:.92rem}
.rail{display:flex;gap:18px;overflow-x:auto;padding:6px 2px 18px;scroll-snap-type:x mandatory}
.rail::-webkit-scrollbar{height:8px}.rail::-webkit-scrollbar-thumb{background:var(--line);border-radius:9px}
.sto{flex:0 0 200px;scroll-snap-align:start;background:#111;border-radius:26px;padding:7px;box-shadow:0 14px 30px rgba(0,0,0,.18)}
.sto .zoom img{border-radius:20px;aspect-ratio:9/16;object-fit:cover}
.sto small{display:block;color:#bbb;font-size:.72rem;text-align:center;padding:6px 0 2px}
.reels{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:18px}
.reel{display:grid;gap:10px}.reel .frame{background:#111;border-radius:26px;padding:7px;box-shadow:0 14px 30px rgba(0,0,0,.18)}
.reel video{display:block;width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:20px;background:#000}
.reel b{font-size:.92rem}.reel small{color:var(--muted);font-size:.82rem}
.occ{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:18px}
.occ figure{margin:0;display:grid;gap:8px}.occ .zoom img{border-radius:10px;box-shadow:0 10px 24px rgba(0,0,0,.14);aspect-ratio:1;object-fit:cover}
.occ figcaption{font-size:.85rem;color:var(--muted)}.occ figcaption b{display:block;color:var(--ink);font-size:.9rem}
.lipre{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:44px;align-items:center}
.listack{position:relative;height:440px}
.listack .lic{position:absolute;width:300px}
.listack .lic:nth-child(1){left:0;top:40px;transform:rotate(-4deg)}.listack .lic:nth-child(2){left:22%;top:0;z-index:2}.listack .lic:nth-child(3){right:0;top:50px;transform:rotate(4deg)}
.lic{background:#fff;color:#111;border:1px solid #e3e6ea;border-radius:12px;overflow:hidden;box-shadow:0 10px 28px rgba(0,0,0,.12)}
.lih{display:flex;gap:10px;align-items:center;padding:12px 14px}.lih b{display:block;font-size:.88rem}.lih small{color:#6b7178;font-size:.74rem}
.av{width:36px;height:36px;border-radius:50%;background:#1f6fb5;color:#fff;display:grid;place-items:center;font:700 .85rem var(--font);flex:0 0 auto}
.lic p{padding:0 14px 12px;font-size:.86rem;line-height:1.45;white-space:pre-line}
.lic img{display:block;width:100%}
.lic .cut{display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
.lic .act{display:flex;justify-content:space-around;border-top:1px solid #e3e6ea;padding:8px;color:#6b7178;font-size:.78rem}
.btn{all:unset;cursor:pointer;background:var(--accent);color:#fff;border-radius:99px;padding:11px 20px;font:700 .9rem var(--font);display:inline-block}
.btn:focus-visible{outline:3px solid var(--ink);outline-offset:3px}
.lnk{color:var(--ink);font-weight:700;text-decoration:none;border-bottom:1px solid var(--line)}
#feed{border:0;padding:0;max-width:none;max-height:none;width:100vw;height:100vh;background:rgba(236,238,242,.55);-webkit-backdrop-filter:blur(22px);backdrop-filter:blur(22px)}
#feed::backdrop{background:transparent}
.fwrap{height:100%;overflow-y:auto;padding:0 16px 40px}
.fhead{position:sticky;top:0;z-index:3;display:flex;align-items:center;gap:12px;max-width:560px;margin:0 auto;padding:16px 0}
.fhead b{font-size:1rem}.fhead small{color:#555}.fhead button{all:unset;cursor:pointer;margin-left:auto;font-size:1.4rem;padding:4px 10px;background:#fff;border-radius:99px;box-shadow:0 2px 8px rgba(0,0,0,.12)}
.flist{max-width:560px;margin:0 auto;display:grid;gap:16px}
.ftabs{display:flex;gap:6px;flex-wrap:wrap;max-width:560px;margin:0 auto 14px}.ftabs button{all:unset;cursor:pointer;font:700 .78rem var(--font);padding:6px 12px;border-radius:99px;background:#fff;border:1px solid #d5d9de}.ftabs button[aria-pressed=true]{background:#111;color:#fff;border-color:#111}
.tools{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px}
.tools div{background:var(--tint);border-radius:14px;padding:22px}.tools h4{font-size:1rem;margin-bottom:6px}.tools p{color:var(--muted);font-size:.93rem}
.next{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:24px;align-items:center;background:var(--ink);color:var(--bg);border-radius:18px;padding:34px;margin:10px 0 70px;text-decoration:none}
.next h3{font-size:1.5rem;color:var(--bg)}.next p{opacity:.75;margin-top:6px}.next span.arr{font-size:2.4rem}
#lb{border:0;padding:0;max-width:none;max-height:none;width:100vw;height:100vh;background:rgba(236,238,242,.55);-webkit-backdrop-filter:blur(22px) saturate(1.2);backdrop-filter:blur(22px) saturate(1.2);color:#15181b}
#lb::backdrop{background:transparent}
.vw{display:grid;grid-template-rows:auto 1fr auto;height:100%;gap:10px;padding:14px 18px;box-sizing:border-box}
.vwtop{display:flex;align-items:center;gap:16px}.vwtop #vwC{opacity:.7;font-size:.85rem}
#close{all:unset;cursor:pointer;font-size:1.4rem;padding:4px 10px;margin-left:auto}
.vwstage{display:grid;grid-template-columns:48px minmax(0,1fr) 48px;align-items:center;min-height:0}
#prev,#next{all:unset;cursor:pointer;font-size:2.6rem;text-align:center;opacity:.8}#prev.off,#next.off{visibility:hidden}
.sp{display:flex;justify-content:center;align-items:center;height:100%;min-height:0;overflow:auto}
.sp img{max-height:calc(100vh - 150px);max-width:100%;object-fit:contain;box-shadow:0 3px 8px rgba(0,0,0,.1),0 24px 50px rgba(0,0,0,.22)}
.sp.tall{align-items:flex-start}.sp.tall img{max-height:none;width:min(720px,100%)}
#thumbs{display:flex;gap:6px;overflow-x:auto;justify-content:center}#thumbs button{all:unset;cursor:pointer;opacity:.5;flex:0 0 auto}#thumbs button[aria-current=true]{opacity:1;outline:2px solid #15181b}#thumbs img{height:48px;display:block}
/* website page */
.brw{margin:0;border-radius:10px;overflow:hidden;box-shadow:0 14px 34px rgba(0,0,0,.18);background:#2a2e33}
.brw .bb{display:flex;align-items:center;gap:6px;padding:8px 12px}.brw .bb i{width:9px;height:9px;border-radius:50%;background:#6b7178}.brw .bb span{margin-left:12px;flex:1;background:#3a3f45;color:#c9ced4;font-size:.72rem;border-radius:6px;padding:3px 10px}
.wlead{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:36px;align-items:center}
.wgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:26px 22px}.wgrid small{display:block;margin-top:8px;color:var(--muted);font-size:.85rem}
.blocks{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px}.blocks h4{font-size:.95rem;margin-bottom:6px}.blocks p{color:var(--muted);font-size:.95rem}
.mail{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:40px;align-items:start}
.mail .scrollbox{height:520px;overflow-y:auto;border-radius:14px;box-shadow:0 18px 40px rgba(0,0,0,.18);background:#fff}
.mail .scrollbox img{display:block;width:100%}
.mthumbs{display:flex;gap:10px;flex-wrap:wrap}.mthumbs button{all:unset;cursor:pointer;width:84px;border-radius:8px;overflow:hidden;opacity:.55;box-shadow:0 4px 10px rgba(0,0,0,.12)}.mthumbs button[aria-pressed=true]{opacity:1;outline:2px solid var(--accent)}.mthumbs img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.bgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px}
.bgrid figure{margin:0;display:grid;gap:8px}.bgrid .zoom{background:var(--tint);border-radius:12px;padding:18px}.bgrid .zoom img{box-shadow:0 6px 16px rgba(0,0,0,.14)}.bgrid figcaption{color:var(--muted);font-size:.85rem}
/* overview */
.ov{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px;padding-bottom:70px}
.ovc{display:grid;grid-template-rows:auto 1fr;border-radius:20px;overflow:hidden;background:var(--tint);text-decoration:none;color:var(--ink);transition:transform .3s}
.ovc:hover{transform:translateY(-4px)}.ovc:focus-visible{outline:3px solid var(--accent);outline-offset:4px}
.ovc .pic{height:300px;position:relative;overflow:hidden;background:#dfe4ea}
.ovc .pic img{position:absolute;box-shadow:0 14px 30px rgba(0,0,0,.22);border-radius:10px}
.ovc .body{padding:26px;display:grid;gap:10px;align-content:start}.ovc h2{font-size:1.6rem}.ovc p{color:var(--muted)}.ovc .go{font-weight:700;color:var(--accent)}
@media (prefers-reduced-motion:reduce){.ovc{transition:none}}
@media (max-width:860px){.hero,.split,.lipre,.wlead,.mail,.duo,.ov{grid-template-columns:minmax(0,1fr)}.stage{height:400px}.ph.a,.ph.c{width:170px;height:350px}.ph.b{width:190px;height:390px;left:26%}.reels{grid-template-columns:repeat(2,minmax(0,1fr))}.listack .lic{width:240px}.chead{grid-template-columns:minmax(0,1fr);gap:4px}.next{grid-template-columns:minmax(0,1fr)}.bgrid{grid-template-columns:minmax(0,1fr)}}
'''
JS=r'''
let cur=[],i=0;const d=document.getElementById('lb'),sp=document.getElementById('sp'),th=document.getElementById('thumbs');
function show(){const [s,a]=cur[i];const im=new Image();im.src=s;im.alt=a;sp.innerHTML='';sp.appendChild(im);
 const t=()=>sp.classList.toggle('tall',im.naturalHeight>im.naturalWidth*2);im.onload=t;if(im.complete)t();
 document.getElementById('vwT').textContent=a;document.getElementById('vwC').textContent=cur.length>1?`${i+1} / ${cur.length}`:'';
 ['prev','next'].forEach(x=>document.getElementById(x).classList.toggle('off',cur.length<2));
 th.innerHTML=cur.length>1?cur.map(([s,a],k)=>`<button data-k="${k}" aria-label="${a}" aria-current="${k===i}"><img src="${s}" alt=""></button>`).join(''):'';sp.scrollTop=0;}
document.querySelectorAll('[data-gallery]').forEach(b=>b.addEventListener('click',()=>{cur=G[b.dataset.gallery];i=+b.dataset.n;show();d.showModal()}));
document.getElementById('prev').onclick=()=>{i=(i-1+cur.length)%cur.length;show()};document.getElementById('next').onclick=()=>{i=(i+1)%cur.length;show()};
document.getElementById('close').onclick=()=>d.close();th.onclick=e=>{const b=e.target.closest('button');if(b){i=+b.dataset.k;show()}};
d.addEventListener('click',e=>{if(e.target===d||e.target===sp)d.close()});
d.addEventListener('keydown',e=>{if(cur.length>1&&e.key==='ArrowRight')document.getElementById('next').click();if(cur.length>1&&e.key==='ArrowLeft')document.getElementById('prev').click()});
function setLang(l){document.documentElement.lang=l;document.querySelectorAll('[data-lang]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.lang===l));try{localStorage.setItem('ys-lang',l)}catch(e){}}
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));try{const l=localStorage.getItem('ys-lang');if(l)setLang(l)}catch(e){}
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('video[data-auto]').forEach(v=>{if(rm){v.removeAttribute('autoplay');v.pause()}});
document.querySelectorAll('video').forEach(v=>v.addEventListener('play',()=>document.querySelectorAll('video').forEach(o=>{if(o!==v&&!o.muted)o.pause()})));
const fd=document.getElementById('feed');if(fd){document.querySelectorAll('[data-feed]').forEach(b=>b.addEventListener('click',()=>{fd.showModal();fd.querySelector('.fwrap').scrollTop=0}));
 document.getElementById('fclose').onclick=()=>fd.close();
 fd.querySelectorAll('.ftabs button').forEach(b=>b.addEventListener('click',()=>{fd.querySelectorAll('.ftabs button').forEach(x=>x.setAttribute('aria-pressed',x===b));fd.querySelectorAll('.flist .lic').forEach(c=>c.hidden=b.dataset.f!=='all'&&c.dataset.k!==b.dataset.f)}));}
document.querySelectorAll('.mthumbs button').forEach(b=>b.addEventListener('click',()=>{const box=document.querySelector('.mail .scrollbox');box.querySelector('img').src=b.dataset.src;box.querySelector('img').alt=b.dataset.alt;box.scrollTop=0;document.querySelectorAll('.mthumbs button').forEach(x=>x.setAttribute('aria-pressed',x===b))}));
'''
DLG='<dialog id="lb" aria-label="Ansicht"><div class="vw"><div class="vwtop"><b id="vwT"></b><span id="vwC"></span><button id="close" aria-label="Schliessen">✕</button></div><div class="vwstage"><button id="prev" aria-label="Zurück">‹</button><div class="sp" id="sp"></div><button id="next" aria-label="Weiter">›</button></div><div id="thumbs"></div></div></dialog>'
def page(fn,title,crumb,body,extra=''):
    top=f'<div class="wrap topbar"><a class="crumb" href="{crumb[0]}">{crumb[1]}</a><div class="lang"><button data-lang="de" aria-pressed="true">DE</button><button data-lang="en" aria-pressed="false">EN</button></div></div>'
    gjs='const G='+json.dumps({k:[["img/"+s,a] for s,a in v] for k,v in G.items()},ensure_ascii=False)+';'
    out=f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap"><style>{BASE}{CSS}</style></head>
<body>{top}<main class="wrap">{body}</main>{DLG}{extra}<script>{gjs}{JS}</script></body></html>'''
    open(P+fn,'w',encoding='utf-8').write(out)
    G.clear()

# ================= SOCIAL MEDIA =================
ig=[f'ig{n:02d}.jpg' for n in range(14)]
hero=f'''<div class="hero"><div><span class="kick">{T("Digital · Social Media","Digital · Social Media")}</span>
<h1>{T("Inhalte, die man im Feed anhält.","Content that stops the scroll.")}</h1>
<p class="lead">{T("Für zwei sehr unterschiedliche Marken habe ich Social Media geplant, gestaltet und produziert: für ein Immobilienunternehmen, das Vertrauen bei Privatpersonen aufbaut, und für einen Schweizer Pumpenhersteller, der Fachleute in der Industrie erreicht.","I have planned, designed and produced social media for two very different brands: a real estate company building trust with private clients, and a Swiss pump manufacturer reaching industry professionals.")}</p>
<div class="chips"><span>Instagram</span><span>Facebook</span><span>LinkedIn</span><span>YouTube</span><span>{T("Storys","Stories")}</span><span>Reels</span><span>{T("Redaktionsplanung","Editorial planning")}</span></div></div>
<div class="stage" aria-hidden="true"><div class="ph a"><div class="feed">{"".join(f'<img src="img/{f}" alt="">' for f in ig[:12])}</div></div>
<div class="ph b"><video src="vid/maerstetten.mp4" poster="vid/maerstetten.jpg" muted loop playsinline autoplay data-auto></video></div>
<div class="ph c"><img src="img/st00.jpg" alt=""></div></div></div>'''

s1=sec(1,'marken',('Zwei Marken, zwei Tonalitäten','Two brands, two tones of voice'),('Dasselbe Handwerk, ganz andere Zielgruppen. Deshalb beginnt jeder Kanal mit der Frage, wen er erreichen soll.','The same craft, very different audiences. That is why every channel starts with the question of who it should reach.'),
f'''<div class="duo"><div class="brand"><span class="client">GOLDINGER Immobilien</span><h3>{T("Nahbar und vertrauensvoll","Approachable and trustworthy")}</h3>
<p>{T("Instagram, Facebook, LinkedIn und YouTube. Ziel: Vertrauen in die Fachleute aufbauen und Objekte, Infoabende und das Hausmagazin bekannt machen.","Instagram, Facebook, LinkedIn and YouTube. Goal: build trust in the experts and promote properties, information evenings and the customer magazine.")}</p>
<ul><li>{T("Redaktionsplan und Gestaltung aller Feed-Beiträge","Editorial plan and design of all feed posts")}</li><li>{T("Storys mit Umfragen, Fragerunden und Countdowns","Stories with polls, Q&As and countdowns")}</li><li>{T("Fotografie, Video und Schnitt, auch Luftaufnahmen mit Drohne","Photography, video and editing, including drone footage")}</li></ul></div>
<div class="brand"><span class="client">CP Pump Systems</span><h3>{T("Fachlich und international","Technical and international")}</h3>
<p>{T("LinkedIn und Facebook, in Deutsch, Englisch und Französisch. Ziel: Messeauftritte ankündigen, Produkte zeigen und die Marke als Schweizer Hersteller sichtbar machen.","LinkedIn and Facebook, in German, English and French. Goal: announce trade fairs, show products and make the brand visible as a Swiss manufacturer.")}</p>
<ul><li>{T("Beiträge vor, während und nach jeder Messe","Posts before, during and after every trade fair")}</li><li>{T("Grafiken zu Feiertagen und Anlässen","Graphics for holidays and occasions")}</li><li>{T("Planung und Versand über Zoho One","Planning and publishing via Zoho One")}</li></ul></div></div>''')

s2=sec(2,'raster',('Feed-Design GOLDINGER','Feed design GOLDINGER'),('Ein klares Raster in Königsblau und Weiss: Serien, die man sofort wiedererkennt, und Inhalte, die Käuferinnen und Verkäufern wirklich weiterhelfen.','A clear grid in royal blue and white: series you recognise at once, and content that genuinely helps buyers and sellers.'),
f'''<div class="split"><div class="phone"><div class="scr"><div class="bar"><span>goldinger_immobilien</span><span>···</span></div><div class="igrid">{"".join(zb("ig",f,f"GOLDINGER Beitrag {k+1}") for k,f in enumerate(ig[:12]))}</div></div></div>
<div class="txt"><h3>{T("Ratgeber statt Werbung","Advice, not advertising")}</h3><p>{T("Alle Feed-Beiträge habe ich gestaltet. Statt reiner Objektwerbung standen nützliche Inhalte im Vordergrund, die das Fachwissen des Teams zeigen.","I designed all feed posts. Instead of pure property ads, the focus was on useful content that shows the team's expertise.")}</p>
<div class="pts"><div><b>{T("Serien mit Nummern","Numbered series")}</b><span>{T("#1 Vorsorgeauftrag, #2 Steuern beim Verkauf, #3 Tipps für den privaten Verkauf","#1 Advance directive, #2 Taxes when selling, #3 Tips for private sales")}</span></div>
<div><b>{T("Infografiken","Infographics")}</b><span>{T("Prozess zum Hauseigentum, Mieten oder Kaufen, Grundstückgewinnsteuer","The path to home ownership, rent or buy, property gains tax")}</span></div>
<div><b>{T("Events und Print im Feed","Events and print in the feed")}</b><span>{T("Infoabende, neue Ausgabe des Hausmagazins, Online-Bewertung","Information evenings, new issue of the customer magazine, online valuation")}</span></div>
<div><b>{T("Themen mit Haltung","Topics with a stance")}</b><span>{T("Stille Vermarktung, Immobilie im Alter, Empfehlungsprogramm","Silent marketing, property in old age, referral programme")}</span></div></div></div></div>''')

stl=[('st00','Countdown Infoabend','Countdown information evening'),('st01','Fragerunde','Q&A'),('st02','Vor dem Infoabend','Before the information evening'),('st03','Umfrage','Poll'),('st04','Umfrage','Poll'),('st05','Umfrage','Poll'),('st06','Fragerunde','Q&A'),('st07','Umfrage','Poll'),('st08','Umfrage','Poll'),('st09','Umfrage','Poll'),('st10','Presse-Repost','Press repost'),('st11','Live vom Infoabend','Live from the event')]
s3=sec(3,'storys',('Storys','Stories'),('Storys machen aus einem Kanal ein Gespräch: Umfragen zu Wohnträumen, Fragerunden mit den Fachleuten und Countdowns, die zu den Infoabenden einladen. Seitlich scrollen.','Stories turn a channel into a conversation: polls on dream homes, Q&As with the experts and countdowns inviting people to the information evenings. Scroll sideways.'),
'<div class="rail">'+''.join(f'<div class="sto">{zb("st",s+".jpg",de)}<small>{T(de,en)}</small></div>' for s,de,en in stl)+'</div>')

rl=[('maerstetten','Märstetten','Exklusive Attikawohnung','Exclusive penthouse'),('thundorf','Thundorf','Modernisiertes Riegelhaus','Modernised half-timbered house'),('amlikon','Amlikon-Bissegg','Ökologisches Einfamilienhaus','Ecological family home'),('interview','Im Spotlight','Interview aus der Bewirtschaftung','Interview from property management'),('jahresvorsaetze','Jahresvorsätze 2023','Mitarbeitende über ihre Vorsätze','Team members on their resolutions')]
s4=sec(4,'reels',('Reels und Immobilienvideos','Reels and property videos'),('Gefilmt, mit Drohne aus der Luft aufgenommen und geschnitten: Rundgänge, die ein Objekt in Sekunden erlebbar machen, und Reels, die die Menschen hinter der Marke zeigen.','Filmed, shot from the air by drone and edited: tours that let you experience a property in seconds, and reels that show the people behind the brand.'),
'<div class="reels">'+''.join(f'<div class="reel"><div class="frame"><video src="vid/{v}.mp4" poster="vid/{v}.jpg" controls playsinline preload="none"></video></div><b>{t}</b><small>{T(de,en)}</small></div>' for v,t,de,en in rl)+
f'</div><p><a class="lnk" href="{A}AWzk8y7iyFhZyJJQF4gszF" target="_blank" rel="noopener">{T("Mehr zum Aufbau der Immobilien-Reels","More on how the property reels are built")} ↗</a></p>')

oc=[('an_7445757007560720384_0.jpg','Frohe Ostern','Happy Easter','CP Pump Systems'),('an_7449750379623301120_0.jpg','Songkran','Songkran','CP Pump Systems · Thailand'),('an_7452662755553312768_0.jpg','Earth Day','Earth Day','CP Pump Systems'),('an_7489198237002715136_0.jpg','1. August','Swiss National Day','CP Pump Systems'),('an_auffahrt.jpg','Auffahrt','Ascension Day','GOLDINGER Immobilien'),('an_weihnacht.jpg','Weihnachten','Christmas','GOLDINGER Immobilien')]
s5=sec(5,'anlaesse',('Anlässe und Feiertage','Occasions and holidays'),('Feiertage sind eine Gelegenheit, Danke zu sagen und die Marke von ihrer persönlichen Seite zu zeigen. Jede Grafik ist eigens gestaltet, im Stil der jeweiligen Marke.','Holidays are a chance to say thank you and show the brand\'s personal side. Each graphic is designed from scratch, in the style of the brand.'),
'<div class="occ">'+''.join(f'<figure>{zb("oc",f,de)}<figcaption><b>{T(de,en)}</b>{c}</figcaption></figure>' for f,de,en,c in oc)+'</div>')

# LinkedIn feed
posts={x['id']:x for x in json.load(open('/home/user/yanasenn/docs/archiv/linkedin/posts.json'))}
LI=[('7489198237002715136','0','anlass'),('7470111895358971905','0','messe'),('7467192207263997952','0','messe'),('7462878873559531520','0','messe'),('7462801353191575554','1','messe'),('7460259790200627200','0','messe'),('7459905847805259776','0','messe'),('7457361699642277888','3','messe'),('7455156430019653632','0','messe'),('7452662755553312768','0','anlass'),('7449750379623301120','0','anlass'),('7447654124722139136','0','messe'),('7445757007560720384','0','anlass'),('7442164052803592193','0','messe'),('7432384793536802816','1','messe'),('7429848836312952832','0','messe'),('7419677481609154560','0','messe'),('7418947336564797442','0','messe'),('7396564126686343168','0','messe')]
MON=['Jan.','Feb.','März','Apr.','Mai','Juni','Juli','Aug.','Sept.','Okt.','Nov.','Dez.']
def lic(pid,im,k,cut=False):
    p=posts[pid]; y,m=p['date'][:4],int(p['date'][5:7])
    t=html.escape(p['text'].strip()).replace(' ',' ')
    return f'<article class="lic" data-k="{k}"><div class="lih"><span class="av">cp</span><div><b>CP Pump Systems</b><small>{MON[m-1]} {y} · LinkedIn</small></div></div><p class="{"cut" if cut else ""}">{t}</p><img src="img/li_{pid}_{im}.jpg" alt="" loading="lazy"><div class="act"><span>👍 {T("Gefällt mir","Like")}</span><span>💬 {T("Kommentieren","Comment")}</span><span>↗ {T("Teilen","Share")}</span></div></article>'
s6=sec(6,'linkedin',('LinkedIn CP Pump Systems','LinkedIn CP Pump Systems'),('Jede Messe erzählt auf LinkedIn eine kleine Geschichte: Ankündigung mit Stand und Gratis-Ticket, erster Messetag, Rückblick. Dazu Anlässe und Themen wie Nachhaltigkeit, oft in zwei oder drei Sprachen.','On LinkedIn, every trade fair tells a short story: announcement with stand and free ticket, first day, recap. Plus occasions and topics like sustainability, often in two or three languages.'),
f'''<div class="lipre"><div class="listack" aria-hidden="true">{lic(*LI[17],cut=True)}{lic(*LI[6],cut=True)}{lic(*LI[0],cut=True)}</div>
<div class="txt"><h3>{T("Text und Bild aus einer Hand","Copy and visuals from one source")}</h3><p>{T("Ich schreibe die Beiträge, gestalte die Grafiken im Stil der Marke und plane die Veröffentlichung. Bei Messen greifen LinkedIn, E-Mail-Banner, Website und Newsletter ineinander.","I write the posts, design the graphics in the brand style and schedule publication. For trade fairs, LinkedIn, email banners, website and newsletter work hand in hand.")}</p>
<p><button class="btn" data-feed>{T(f"Feed öffnen · {len(LI)} Beiträge",f"Open feed · {len(LI)} posts")}</button></p>
<p><a class="lnk" href="{A}NcW3BUdbXA5pKkgtA91Zvi" target="_blank" rel="noopener">{T("Beiträge pro Messe unter «Messen»","Posts per trade fair under «Trade Fairs»")} ↗</a></p></div></div>''')
feed=f'''<dialog id="feed" aria-label="LinkedIn Feed"><div class="fwrap"><div class="fhead"><span class="av">cp</span><div><b>CP Pump Systems</b><br><small>{T("Auswahl LinkedIn-Beiträge 2025–2026","Selected LinkedIn posts 2025–2026")}</small></div><button id="fclose" aria-label="Schliessen">✕</button></div>
<div class="ftabs"><button data-f="all" aria-pressed="true">{T("Alle","All")}</button><button data-f="messe" aria-pressed="false">{T("Messen","Trade fairs")}</button><button data-f="anlass" aria-pressed="false">{T("Anlässe","Occasions")}</button></div>
<div class="flist">{"".join(lic(*x) for x in LI)}</div></div></dialog>'''

s7=sec(7,'arbeitsweise',('Arbeitsweise','How I work'),('Vom Plan bis zum fertigen Beitrag liegt alles in einer Hand.','From plan to published post, everything stays in one pair of hands.'),
f'''<div class="tools"><div><h4>{T("Planen","Plan")}</h4><p>{T("Redaktionsplan mit Themen, Anlässen und Messen.","Editorial plan with topics, occasions and trade fairs.")}</p></div>
<div><h4>{T("Gestalten","Design")}</h4><p>{T("Grafiken, Serien und Vorlagen im Stil der Marke, mit Photoshop, Illustrator und Canva.","Graphics, series and templates in the brand style, with Photoshop, Illustrator and Canva.")}</p></div>
<div><h4>{T("Produzieren","Produce")}</h4><p>{T("Fotografie, Video, Drohnenaufnahmen und Schnitt in Premiere Pro.","Photography, video, drone footage and editing in Premiere Pro.")}</p></div>
<div><h4>{T("Veröffentlichen","Publish")}</h4><p>{T("Planung und Versand über Zoho One und Meta, Storys teils als Anzeigen beworben.","Scheduling and publishing via Zoho One and Meta, some stories promoted as ads.")}</p></div></div>''')

nxt=f'<a class="next" href="{WEBURL}" target="_blank" rel="noopener"><div><span class="kick" style="color:inherit;opacity:.6">{T("Weiter","Next")}</span><h3>{T("Website, Newsletter und E-Mail-Banner","Website, newsletter and email banners")}</h3><p>{T("Wie eine Messe vom Kalender auf der Website bis in die E-Mail-Signatur kommt.","How a trade fair travels from the website calendar into every email signature.")}</p></div><span class="arr">→</span></a>'
page('social-media.html','Social Media',('#',f'{T("Arbeiten","Work")} / <b>Social Media</b>'),hero+s1+s2+s3+s4+s5+s6+s7+'<div style="height:60px"></div>',feed)

# ================= WEBSITE =================
web=[('w_home.jpg','Startseite','Home page'),('w_messen.jpg','Messekalender mit Standnummern','Trade fair calendar with stand numbers'),('w_news.jpg','News und Blog','News and blog'),('w_post_dk.jpg','Messebeitrag DK HUB GLOBAL','Trade fair post DK HUB GLOBAL'),('w_post_prod.jpg','Produktbeitrag','Product post'),('w_downloads.jpg','Download-Bibliothek','Download library')]
brw=lambda f,a: f'<figure class="brw"><div class="bb"><i></i><i></i><i></i><span>cp-pumps.com</span></div>{zb("web",f,a)}</figure>'
whero=f'''<div class="hero" style="grid-template-columns:minmax(0,1fr)"><div><span class="kick">{T("Digital","Digital")}</span><h1>{T("Website, Newsletter und E-Mail-Banner","Website, newsletter and email banners")}</h1>
<p class="lead">{T("Eine Messe taucht bei mir an mehreren Orten auf: im Messekalender, als Blogbeitrag, im Newsletter, auf LinkedIn und im E-Mail-Banner. So erzählen alle Kanäle dieselbe Geschichte.","With me, a trade fair appears in several places: in the calendar, as a blog post, in the newsletter, on LinkedIn and in the email banner. That way every channel tells the same story.")}</p></div></div>'''
w1=sec(1,'website',('Website','Website'),('Inhaltliche Pflege der Website von CP Pump Systems in Craft CMS, in Deutsch, Englisch, Französisch und Chinesisch.','Content management for the CP Pump Systems website in Craft CMS, in German, English, French and Chinese.'),
f'''<div class="wlead">{brw(*web[0][:2])}<div class="txt"><h3>{T("Die Website lebendig halten","Keeping the website alive")}</h3>
<p>{T("Technisch betreut eine Agentur die Website. Ich bin für die Inhalte verantwortlich: Ich schreibe Beiträge, halte Seiten und Downloads aktuell und sorge dafür, dass Website, Newsletter und Social Media dieselbe Geschichte erzählen.","An agency looks after the technical side. I am responsible for the content: I write posts, keep pages and downloads up to date and make sure website, newsletter and social media tell the same story.")}</p></div></div>
<div class="wgrid">{"".join(f'<div>{brw(f,de)}<small>{T(de,en)}</small></div>' for f,de,en in web[1:])}</div>
<div class="blocks"><div><h4>{T("News und Blog","News and blog")}</h4><p>{T("Beiträge zu Messen, Produkten und Unternehmensthemen, inklusive Messekalender mit Standnummern und Gratis-Tickets.","Posts on trade fairs, products and company topics, including a trade fair calendar with stand numbers and free tickets.")}</p></div>
<div><h4>Downloads</h4><p>{T("Broschüren, Factsheets und Explosionszeichnungen in allen Sprachen laufend erneuern.","Continuously updating brochures, factsheets and exploded drawings in all languages.")}</p></div>
<div><h4>{T("Unternehmen und Karriere","Company and careers")}</h4><p>{T("Weltkarte und Kontaktseiten pro Land aktualisieren, Stellenanzeigen aufschalten und wieder entfernen, neue Mitarbeitende vorstellen.","Updating the world map and country contact pages, publishing and removing job ads, introducing new team members.")}</p></div>
<div><h4>{T("Service und Formulare","Service and forms")}</h4><p>{T("Zusammen mit der Agentur überarbeitet, auf Basis von Feedback.","Revised together with the agency, based on feedback.")}</p></div></div>
<p style="color:var(--muted)">{T("Bei GOLDINGER Immobilien pflegte ich die Website in TYPO3: Inhalte austauschen, Bilder wählen, Texte anpassen.","At GOLDINGER Immobilien I maintained the website in TYPO3: updating content, choosing images, adjusting copy.")}</p>''')
mails=[('mail1_de','Einladung','Invitation'),('mail2_de','Mailing 2','Mailing 2'),('mail3_de','Mailing 3','Mailing 3'),('dank_de','Dank nach der Messe','Thank-you after the fair')]
w2=sec(2,'newsletter',('Newsletter und Mailings','Newsletter and mailings'),('Ich gestalte und versende Newsletter und Mailings über Zoho, für jede grössere Messe und für Produktthemen. Als Beispiel die Serie zur ACHEMA 2024.','I design and send newsletters and mailings via Zoho, for every major trade fair and for product topics. Shown here as an example: the series for ACHEMA 2024.'),
f'''<div class="mail"><div class="scrollbox" tabindex="0" aria-label="Mailing, scrollbar"><img src="img/{mails[0][0]}.jpg" alt="{mails[0][1]}"></div>
<div class="txt"><h3>{T("Beispiel: ACHEMA 2024","Example: ACHEMA 2024")}</h3><p>{T("Von der Einladung mit persönlichem Code für ein Geschenk am Stand bis zum Dank nach der Messe. Im Fenster links lässt sich jedes Mailing ganz durchscrollen.","From the invitation with a personal code for a gift at the stand to the thank-you after the fair. Scroll through each mailing in the window on the left.")}</p>
<div class="mthumbs">{"".join(f'<button data-src="img/{f}.jpg" data-alt="{de}" aria-pressed="{str(k==0).lower()}" aria-label="{de}"><img src="img/c_{f}.jpg" alt=""></button>' for k,(f,de,en) in enumerate(mails))}</div></div></div>''')
EB=[('achema','ACHEMA 2024'),('pv25','Pumps & Valves 2025'),('tfs25','The Fertilizer Show 2025'),('cru25','Sulphur + Sulphuric Acid 2025'),('pv26','Pumps & Valves 2026'),('fla26','Fertilizer Latino Americano 2026'),('dahej26','Dahej 2026'),('petro26','Petrochymia 2026'),('uk26','CHEMUK 2026'),('dk26','DK HUB GLOBAL 2026'),('tfs26','The Fertilizer Show 2026'),('cru26','Sulphur + Sulphuric Acid 2026')]
w3=sec(3,'banner',('E-Mail-Banner','Email banners'),('Zu jeder Messe ein Banner für die E-Mails des ganzen Teams, meist mit Link zum Gratis-Ticket. Dieselben Banner setze ich auch auf Messeportalen ein.','For every trade fair a banner for the whole team\'s emails, usually linking to a free ticket. I also use the same banners on trade fair portals.'),
 '<div class="bgrid">'+''.join(f'<figure>{zb("eb",f"e_{k}_vor0.jpg",n)}<figcaption>{n}</figcaption></figure>' for k,n in EB)+'</div>')
wnext=f'<a class="next" href="{A}9pLQefB7tUVEDh7QPpWNy6" target="_blank" rel="noopener"><div><span class="kick" style="color:inherit;opacity:.6">{T("Siehe auch","See also")}</span><h3>Social Media</h3><p>{T("Feed, Storys, Reels und LinkedIn.","Feed, stories, reels and LinkedIn.")}</p></div><span class="arr">→</span></a>'
page('website.html','Website und E-Mail',('#',f'{T("Arbeiten","Work")} / <b>{T("Website und E-Mail","Website and email")}</b>'),whero+w1+w2+w3+'<div style="height:60px"></div>')

# ================= OVERVIEW =================
ov=f'''<div class="hero" style="grid-template-columns:minmax(0,1fr);padding-bottom:36px"><div><span class="kick">{T("Arbeiten","Work")}</span><h1>{T("Digital und Social Media","Digital and Social Media")}</h1>
<p class="lead">{T("Von der Story bis zum Newsletter: Ich plane, gestalte und produziere Inhalte für digitale Kanäle und sorge dafür, dass sie zusammenspielen.","From stories to newsletters: I plan, design and produce content for digital channels and make sure they work together.")}</p></div></div>
<div class="ov"><a class="ovc" href="social-media.html"><div class="pic"><img src="img/ig03.jpg" alt="" style="width:46%;left:6%;top:30px;transform:rotate(-4deg)"><img src="img/st00.jpg" alt="" style="width:30%;left:40%;top:16px;z-index:2"><img src="img/an_7489198237002715136_0.jpg" alt="" style="width:38%;right:4%;top:60px;transform:rotate(4deg)"></div>
<div class="body"><span class="kick">GOLDINGER · CP Pump Systems</span><h2>Social Media</h2><p>{T("Feed-Design, Storys, Reels und Immobilienvideos, Feiertagsgrafiken und LinkedIn.","Feed design, stories, reels and property videos, holiday graphics and LinkedIn.")}</p><span class="go">{T("Mehr erfahren →","Learn more →")}</span></div></a>
<a class="ovc" href="website.html"><div class="pic"><img src="img/w_home.jpg" alt="" style="width:72%;left:6%;top:34px"><img src="img/c_mail1_de.jpg" alt="" style="width:30%;right:5%;top:70px;z-index:2"></div>
<div class="body"><span class="kick">CP Pump Systems</span><h2>{T("Website und E-Mail","Website and email")}</h2><p>{T("Website-Pflege in Craft CMS, Newsletter und Mailings, E-Mail-Banner zu jeder Messe.","Website content in Craft CMS, newsletters and mailings, email banners for every trade fair.")}</p><span class="go">{T("Mehr erfahren →","Learn more →")}</span></div></a></div>'''
page('digital.html','Digital und Social Media',('#',f'yanasenn.ch / <b>{T("Arbeiten","Work")}</b>'),ov)
print('ok')
