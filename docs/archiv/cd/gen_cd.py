import re,subprocess,glob,os
S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
I=S+'/cd/page/img/'
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
exec(open(S+'/cd/content_cd.py',encoding='utf-8').read())
toc=''.join(f'<a href="#{k}"><span>{i:02d}</span>{T(*t)}</a>' for i,(k,t,_,_) in enumerate(SEC,1))
secs=''.join(f'<section class="cat" id="{k}"><div class="chead"><span class="num">{i:02d}</span><div><h2>{T(*t)}</h2><p>{T(*intro)}</p></div></div><div class="list">{html}</div></section>' for i,(k,t,intro,html) in enumerate(SEC,1))
body=f'<div class="wrap"><div class="topbar"><p class="note">{T("Entwurf «Corporate Design &amp; Raum»","Draft “Corporate Design &amp; Space”")}</p><div class="lang" role="group" aria-label="Sprache"><button data-lang="de" aria-pressed="true">DE</button><button data-lang="en" aria-pressed="false">EN</button></div></div><header class="hero"><p class="crumb">{T("Arbeiten","Work")}</p><h1>{T("Corporate Design &amp; Raum","Corporate Design &amp; Space")}</h1><p class="lead">{T("Marken sichtbar machen: im eigenen Gebäude, in einem durchgängigen Erscheinungsbild und in neu gestalteten Printmitteln.","Making brands visible: in our own building, in a consistent identity and in redesigned print materials.")}</p><nav class="toc">{toc}</nav></header>{secs}</div>'
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
.note2{display:inline-block;background:var(--tint);border-radius:99px;padding:6px 14px;font-size:.85rem;color:var(--muted);margin:0}
.agrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px}.ag{all:unset;cursor:pointer;aspect-ratio:1/1;border-radius:12px;overflow:hidden;background:var(--tint);display:block}.ag img{width:100%;height:100%;object-fit:contain;padding:10px;box-sizing:border-box;transition:transform .4s}.ag.fill img{object-fit:cover;padding:0}.ag:hover img{transform:scale(1.04)}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:26px 22px}
.mt{all:unset;cursor:pointer;display:grid;gap:6px;align-content:start}.mt .mi{position:relative;display:grid;place-items:center;aspect-ratio:16/10;background:var(--tint);border-radius:12px;padding:16px;overflow:hidden}
.mt .mi img{position:absolute;inset:16px;width:calc(100% - 32px);height:calc(100% - 32px);object-fit:contain;transition:transform .3s}.mt:hover .mi img{transform:scale(1.03)}
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
out='<title>Corporate Design und Raum</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap">\n'+style+'\n'+body+'\n'+d+'\n\n'+scr+'\n'
open(S+'/cd/page/corporate-design.html','w',encoding='utf-8').write(out)
print('ok',sum(len(v) for v in G.values()))
