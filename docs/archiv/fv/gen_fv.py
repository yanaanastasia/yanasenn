S='/tmp/claude-0/-home-user-yanasenn/7ecc29b7-822b-53aa-b4f8-02a11a401b6c/scratchpad'
src=open(S+'/sm/gen_sm.py',encoding='utf-8').read()
exec(src[:src.index('# ================= SOCIAL MEDIA')])
P=S+'/fv/page/'
CSS+=r'''
.photo{margin:0}.photo .zoom img{border-radius:4px;box-shadow:0 14px 34px rgba(0,0,0,.16)}
.shoot{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:18px}
.shoot>*{grid-column:span 3}.shoot>*:nth-child(1){grid-column:span 6}
.ba{position:relative;border-radius:4px;overflow:hidden;aspect-ratio:3/2;box-shadow:0 14px 34px rgba(0,0,0,.16)}
.ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ba .after{clip-path:inset(0 0 0 var(--p,50%))}
.ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.ba .bar{position:absolute;top:0;bottom:0;left:var(--p,50%);width:3px;background:#fff;transform:translateX(-50%);pointer-events:none}
.ba .bar::after{content:"⇆";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:#fff;color:#111;border-radius:99px;padding:6px 9px;font-size:.9rem}
.ba .lbl{position:absolute;top:10px;font:700 .68rem var(--font);letter-spacing:.08em;text-transform:uppercase;background:rgba(0,0,0,.6);color:#fff;padding:4px 9px;border-radius:99px;pointer-events:none}.ba .l1{left:10px}.ba .l2{right:10px}
.mas{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}.mas .zoom img{border-radius:4px;aspect-ratio:3/2;object-fit:cover}
.vids{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px}
.vid{display:grid;gap:10px}.vid video{width:100%;aspect-ratio:16/9;border-radius:6px;background:#000;box-shadow:0 14px 34px rgba(0,0,0,.18)}
.vid b{font-size:1.05rem}.vid small{color:var(--muted)}
.facts{display:flex;flex-wrap:wrap;gap:8px}.facts span{font-size:.8rem;border:1px solid var(--line);border-radius:99px;padding:4px 11px;color:var(--muted)}
.linkcard{display:grid;grid-template-columns:200px minmax(0,1fr);gap:24px;align-items:center;background:var(--tint);border-radius:16px;padding:20px;text-decoration:none;color:var(--ink)}
.linkcard img{width:100%;height:150px;object-fit:cover;border-radius:12px}.linkcard h3{font-size:1.25rem}.linkcard p{color:var(--muted);margin-top:6px}.linkcard span.go{font-weight:700;color:var(--accent);display:inline-block;margin-top:10px}
@media (max-width:860px){.shoot>*,.shoot>*:nth-child(1){grid-column:span 6}.vids{grid-template-columns:minmax(0,1fr)}.linkcard{grid-template-columns:minmax(0,1fr)}}
'''
JS+="document.querySelectorAll('.ba input').forEach(r=>r.addEventListener('input',()=>r.parentElement.style.setProperty('--p',r.value+'%')));"

hero=f'''<div class="hero"><div><span class="kick">{T("Foto und Video","Photo and video")}</span>
<h1>{T("Bilder, die zeigen, wie gearbeitet wird.","Images that show how the work gets done.")}</h1>
<p class="lead">{T("Ich fotografiere Produkte, Gebäude, Events, Messeauftritte und Mitarbeitende und bearbeite die Bilder bis zum fertigen Einsatz auf der Website, in Print und auf Social Media. Dazu kommen Videos, vom Drehbuch bis zum Schnitt.","I photograph products, buildings, events, trade fairs and employees and edit the images through to their final use on the website, in print and on social media. Plus videos, from script to edit.")}</p>
<div class="chips"><span>{T("Fotografie","Photography")}</span><span>{T("Bildbearbeitung","Image editing")}</span><span>{T("Reportage","Reportage")}</span><span>{T("Animation","Animation")}</span><span>{T("Schnitt","Editing")}</span></div></div>
<div><img src="img/sh_pfa2.jpg" alt="" style="width:100%;border-radius:4px;box-shadow:0 24px 50px rgba(0,0,0,.22)"></div></div>'''

s1=sec(1,'shooting',('Mitarbeitende bei der Arbeit','Employees at work'),('Fotoshooting im eigenen Betrieb, August 2026: Fertigung, Konstruktion und Programmierung. Die Bilder habe ich in Farbe und Schwarzweiss bearbeitet; einige hängen heute als grosse Wandbilder in den Abteilungen.','Photo shoot in our own plant, August 2026: production, design and programming. I edited the images in colour and black and white; some now hang as large wall pictures in the departments.'),
f'''<div class="shoot"><figure class="photo">{zb("sh","sh_pfa.jpg","PFA-Auskleidung am Ofen")}</figure>
<figure class="photo">{zb("sh","sh_cam.jpg","CAM-Programmierung")}</figure><figure class="photo">{zb("sh","sh_technik.jpg","Konstruktion und Simulation")}</figure></div>
<div class="split" style="grid-template-columns:minmax(0,1.4fr) minmax(0,1fr)"><div class="ba"><img src="img/sh_pfa2.jpg" alt="Farbe"><img class="after" src="img/sh_pfa2sw.jpg" alt="Schwarzweiss"><span class="bar"></span><span class="lbl l1">{T("Farbe","Colour")}</span><span class="lbl l2">{T("Schwarzweiss","Black and white")}</span><input type="range" min="0" max="100" value="50" aria-label="Farbe und Schwarzweiss vergleichen"></div>
<div class="txt"><h3>{T("Eine Aufnahme, zwei Wirkungen","One shot, two moods")}</h3><p>{T("Für die Wandbilder entstanden von ausgewählten Aufnahmen Fassungen in Farbe und in Schwarzweiss. Mit dem Regler lassen sich beide vergleichen.","For the wall pictures, selected shots were produced in colour and in black and white. Use the slider to compare them.")}</p>
<div class="facts"><span>{T("Aufnahme","Shooting")}</span><span>{T("Bildauswahl","Selection")}</span><span>{T("Bildbearbeitung","Retouching")}</span><span>{T("Druckdaten","Print files")}</span></div></div></div>''')

ml=[f'ml_{i:02d}.jpg' for i in range(18)]
s2=sec(2,'reportage',('Reportage: Maschinenlieferung','Reportage: machine delivery'),('Mai 2026: Neue Bearbeitungszentren werden per Tieflader angeliefert, mit dem Kran abgeladen und in die Halle eingebracht. Ich habe den ganzen Ablauf fotografiert und gefilmt.','May 2026: new machining centres arrive on a low-loader, are lifted off by crane and moved into the hall. I photographed and filmed the whole process.'),
 '<div class="mas">'+''.join(zb("ml",f,f"Maschinenlieferung {i+1}") for i,f in enumerate(ml))+'</div>')

s3=sec(3,'erklaervideos',('Animierte Erklärvideos','Animated explainer videos'),('Wie läuft ein Immobilienverkauf ab, und was bedeutet ein «stiller Verkauf»? Als Abschlussarbeit meiner Lehre habe ich für GOLDINGER Immobilien zwei Erklärvideos entwickelt, komplett selbst: Drehbuch, Storyboard, Illustrationen, Animation und Ton.','How does a property sale work, and what is a «silent sale»? As the final project of my apprenticeship, I created two explainer videos for GOLDINGER Immobilien entirely on my own: script, storyboard, illustrations, animation and sound.'),
f'''<div class="vids"><div class="vid"><video src="vid/verkauf.mp4" poster="vid/verkauf.jpg" controls playsinline preload="none"></video><b>{T("Immobilienverkauf bei GOLDINGER","Selling a property with GOLDINGER")}</b><small>{T("Erklärvideo, rund 3 Minuten","Explainer, about 3 minutes")}</small></div>
<div class="vid"><video src="vid/stiller.mp4" poster="vid/stiller.jpg" controls playsinline preload="none"></video><b>{T("Stiller Verkauf","Silent sale")}</b><small>{T("Erklärvideo, rund 2 Minuten","Explainer, about 2 minutes")}</small></div></div>
<div class="facts"><span>{T("Abschlussarbeit (IPA)","Final apprenticeship project")}</span><span>{T("Drehbuch","Script")}</span><span>Storyboard</span><span>{T("Illustration","Illustration")}</span><span>{T("Animation","Animation")}</span><span>{T("Ton","Sound")}</span></div>''')

s4=sec(4,'immobilienvideos',('Immobilienvideos und Reels','Property videos and reels'),('Objektvideos mit Rundgang und Luftaufnahmen per Drohne sowie Interview-Reels zeige ich auf der Seite Social Media.','Property videos with tours and drone footage, plus interview reels, are shown on the social media page.'),
f'<a class="linkcard" href="{A}9pLQefB7tUVEDh7QPpWNy6#reels" target="_blank" rel="noopener"><img src="img/reel.jpg" alt=""><div><h3>{T("Reels und Immobilienvideos","Reels and property videos")}</h3><p>{T("Märstetten, Thundorf, Amlikon-Bissegg und mehr: gefilmt, aus der Luft aufgenommen und geschnitten.","Märstetten, Thundorf, Amlikon-Bissegg and more: filmed, shot from the air and edited.")}</p><span class="go">{T("Zu Social Media","Go to social media")} ↗</span></div></a>')

note=f'<p style="color:var(--muted);padding:0 0 70px">{T("2026 habe ich zudem einen zweitägigen Fotografie-Workshop mit Schwerpunkt Bildbearbeitung besucht.","In 2026 I also attended a two-day photography workshop focused on image editing.")}</p>'
page('foto-video.html','Foto und Video',('#',f'{T("Arbeiten","Work")} / <b>{T("Foto und Video","Photo and video")}</b>'),hero+s1+s2+s3+s4+note)
print('ok')
