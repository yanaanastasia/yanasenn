# Kategorie «Corporate Design & Raum» (Quelle: content-plan.md, Texte ✅)
SEC=[]
CPN='CP Pump Systems'
# 01 Raumgestaltung
def ag(g,lab,fs,fill=True):
    G[g]=[(x,lab[0]) for x in fs]
    return '<div class="sub"><h4>'+T(*lab)+'</h4></div><div class="agrid">'+''.join(f'<button class="ag{" fill" if fill else ""}" data-gallery="{g}" data-n="{i}"><img src="img/{x}" alt="{lab[0]}"></button>' for i,x in enumerate(fs))+'</div>'
def fix(h): return h.replace('>Seiten<','>Bilder<').replace('>pages<','>images<').replace('blättern','ansehen').replace('flip through','view')
intro=('<p class="note2">'+T('Fotos der fertigen Räume folgen.','Photos of the finished rooms will follow.')+'</p>')
r1=fix(row(CPN,('Zwei Besprechungsräume','Two meeting rooms'),
 ('Ein Wandbild mit Birkenwald und dem Claim «cleaner pumps, cleaner planet™» prägt die beiden Besprechungsräume. Dazu Logo- und Claim-Paneele im Fensterband und Möbel in Grün- und Blautönen.','A birch forest mural with the claim “cleaner pumps, cleaner planet™” defines the two meeting rooms, with logo and claim panels along the windows and furniture in shades of green and blue.'),
 'v2_2.jpg',(('2 Besprechungsräume','2 meeting rooms'),('Digitaldruck-Tapete','digitally printed wallpaper'),('Einrichtung','furnishing')),
 more=blocks(('Vorgehen','Approach','Vom ersten Entwurf der Seitenwand über mehrere Layout-Varianten bis zur finalen Version. Die Möbel wählte ich nach einem Showroom-Besuch und anhand von Renderings der Möbelfirma nach Farbpaletten aus und organisierte die Lieferung.','From the first draft of the side wall through several layout variants to the final version. I selected the furniture by colour palette after a showroom visit and based on renderings by the furniture company, and organised the delivery.'),
  ('Elemente','Elements','Wandbild als Digitaldruck-Tapete, Logo- und Claim-Paneele im Fensterband, Whiteboard-Flächen und eine Möblierung, die die Farben des Wandbilds aufnimmt.','Mural as digitally printed wallpaper, logo and claim panels along the windows, whiteboard surfaces and furniture that picks up the colours of the mural.'))
 +gallery('rs','Sitzungszimmer',['v2_2.jpg'])))
def room(g,lab,vis,txt):
    G[g]=[(x,lab[0]) for x in vis]
    tiles=''.join(f'<button class="ag fill" data-gallery="{g}" data-n="{j}"><img src="img/{x}" alt="{lab[0]}"></button>' for j,x in enumerate(vis))
    ph=f'<div class="ag ph"><span>{T("Fotos folgen","Photos to follow")}</span></div>'
    return f'<div class="sub"><h4>{T(*lab)}</h4><p class="subp">{T(*txt)}</p></div><div class="rgrid"><div><h5 class="lbl2">{T("Visualisierung","Visualisation")}</h5><div class="agrid">{tiles}</div></div><div><h5 class="lbl2">{T("So sieht es aus","As built")}</h5><div class="agrid one">{ph}</div></div></div>'
r1+=room('rl',('Raum 1: Lounge','Room 1: Lounge'),['v2_1.jpg','v2_0.jpg','rend_lounge.jpg'],('Wandbild mit Birkenwald und Claim, Logo- und Claim-Paneele im Fensterband, Lounge-Möbel in Grün und Blau.','Birch forest mural with claim, logo and claim panels along the windows, lounge furniture in green and blue.'))
r1+=room('rz',('Raum 2: Sitzungszimmer','Room 2: Meeting room'),['rend_sitzung.jpg'],('Sitzungszimmer mit Wandflächen in Blau und Grün und passender Möblierung.','Meeting room with wall areas in blue and green and matching furniture.'))
SCH=['sch_01.jpg', 'sch_02.jpg', 'sch_03.jpg', 'sch_04.jpg', 'sch_05.jpg', 'sch_06.jpg', 'sch_08.jpg', 'sch_09.jpg', 'sch_10.jpg', 'sch_11.jpg', 'sch_12.jpg', 'sch_13.jpg', 'sch_14.jpg', 'sch_15.jpg', 'sch_16.jpg', 'sch_17.jpg', 'sch_18.jpg', 'sch_19.jpg', 'sch_20.jpg', 'sch_21.jpg', 'sch_22.jpg', 'sch_23.jpg', 'sch_24.jpg', 'sch_25.jpg', 'sch_26.jpg']
TOP10=['sch_02.jpg','sch_14.jpg','sch_21.jpg','sch_13.jpg','sch_12.jpg','sch_08.jpg','sch_20.jpg','sch_25.jpg','sch_24.jpg','sch_22.jpg']
r2=fix(row(CPN,('Schilder für die Abteilungen','Department signs'),
 ('Neben jeder Tür hängt ein Schild, das die Abteilung vorstellt: ein grosses Bild, eine Kurzbeschreibung auf Deutsch und Englisch und die wichtigsten Kennzahlen. Die Fotos habe ich selbst gemacht und bearbeitet, ebenso die Grafiken wie die Weltkarte. Insgesamt sind es {n} Schilder, hier eine Auswahl von zehn.'.format(n=len(SCH)),'Next to every door hangs a sign introducing the department: a large image, a short description in German and English and the key figures. I took and edited the photos myself, as well as graphics such as the world map. There are {n} signs in total; here is a selection of ten.'.format(n=len(SCH))),
 'sch_mock.jpg',((f'{len(SCH)} Schilder','25 signs'),('Fotografie','photography'),('DE/EN','DE/EN')),
 more=blocks(('Inhalt','Content','Von der Pumpenmontage über CNC-Bearbeitung, Lackiererei und Qualitätskontrolle bis zu Technik und Entwicklung, Verkauf, Export und Marketing: jede Abteilung mit eigenem Bild und eigenen Fakten.','From pump assembly, CNC machining, paint shop and quality control to engineering, sales, export and marketing: each department with its own image and facts.'),
  ('Meine Arbeit','My work','Fotos der Mitarbeitenden bei der Arbeit, Bildbearbeitung, Grafiken, Layout aller Schilder in einem einheitlichen System und Aufbereitung für den Druck.','Photos of employees at work, image editing, graphics, layout of all signs in one consistent system and preparation for print.'))
 +gallery('sm','Schilder',['sch_mock.jpg']+TOP10)))
raum=r1+f'<p><a class="lnk" href="{A}3YqAhMFfdAX84mYeGeTHFW" target="_blank" rel="noopener">{T("Ganze Projektseite «Die Marke im eigenen Gebäude»","Full project page “The brand in our own building”")} ↗</a></p>'
_raumsec=('raum',('Raumgestaltung','Interior design'),('Die Marke CP sollte nicht nur an Messen und in Broschüren sichtbar sein, sondern auch im eigenen Gebäude: dort, wo Kundschaft empfangen wird, und dort, wo die Mitarbeitenden täglich arbeiten.','The CP brand was to be visible not only at trade fairs and in brochures, but also in its own building: where customers are welcomed and where employees work every day.'),raum)
SEC.append(_raumsec)
SEC.append(('schilder',('Schilder für die Abteilungen','Department signs'),('Jede Abteilung stellt sich neben ihrer Tür vor: mit eigenem Bild und kurzen Fakten auf Deutsch und Englisch.','Each department introduces itself next to its door: with its own image and short facts in German and English.'),r2))
# 02 Markenidentität
tp=row(T('Kursprojekt','Course project'),('Trailer Park – Street Food','Trailer Park – Street Food'),
 ('Eine komplette Marke für einen Food-Truck: Logo, Claim, Farb-, Bild- und Schriftkonzept, zusammengefasst in einem Manual, dazu Plakat, Becher, Food-Box und Newsletter.','A complete brand for a food truck: logo, claim, colour, image and type concept, summarised in a manual, plus poster, cup, food box and newsletter.'),
 'tp_m1.jpg',(('Markenidentität','Brand identity'),('Corporate Design','Corporate design'),('Kursprojekt','Course project')),
 more=blocks(('Ausgangslage','Starting point','Im überbetrieblichen Kurs der Ausbildung entstand für einen fiktiven Food-Truck eine eigene Marke, vom Logo bis zur Verpackung.','In an inter-company course during my apprenticeship, a brand was created for a fictional food truck, from the logo to the packaging.'),
  ('Umsetzung','Implementation','Logo, Claim, Farb-, Bild- und Schriftkonzept, zusammengefasst in einem Manual, dazu Plakat, Becher, Food-Box und Newsletter.','Logo, claim, colour, image and type concept, summarised in a manual, plus poster, cup, food box and newsletter.'))
 +gallery('tpm','Manual',['tp_m1.jpg','tp_m2.jpg','tp_m3.jpg','tp_m4.jpg','tp_m5.jpg']))
G['tpa']=[(x,'Trailer Park') for x in ['tp_plakat.jpg','tp_becher.jpg','tp_box.jpg','tp_box2.jpg','tp_mock1.jpg','tp_mock2.jpg','tp_news.jpg']]
apps='<div class="sub"><h4>'+T('Anwendungen','Applications')+'</h4></div><div class="agrid">'+''.join(f'<button class="ag" data-gallery="tpa" data-n="{i}"><img src="img/{x}" alt="Trailer Park"></button>' for i,(x,_) in enumerate(G['tpa']))+'</div>'
SEC.append(('marke',('Markenidentität','Brand identity'),('Eine Marke von Grund auf: vom Logo und Manual bis zu Verpackung und Newsletter.','A brand from scratch: from logo and manual to packaging and newsletter.'),tp+apps))
# 03 Redesigns
SEC.append(('redesigns',('Redesigns','Redesigns'),('Bestehende Printmittel und Messewände neu gestaltet: Vorher und nachher im Vergleich finden sich unter Grafik & Print.','Existing print materials and booth walls redesigned: before-and-after comparisons are under Graphic & Print.'),
 f'<p><a class="lnk" href="{A}GZFTrhEhSPs7GJyEAEEvNi#redesigns" target="_blank" rel="noopener">{T("Zu den Redesigns","To the redesigns")} ↗</a></p>'))
