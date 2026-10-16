# Kategorie «Corporate Design & Raum» (Quelle: content-plan.md, Texte ✅)
SEC=[]
CPN='CP Pump Systems'
# 01 Raumgestaltung: nur Verweis auf die Projektseite
raum=row(CPN,('Die Marke im eigenen Gebäude','The brand in our own building'),
 ('Zwei Sitzungszimmer und Schilder für die Abteilungen im Erscheinungsbild von CP: Wandgestaltung, Einrichtung und eigene Fotos der Mitarbeitenden.','Two meeting rooms and department signs in the CP look: wall design, furnishing and my own photos of employees.'),
 'v2_2.jpg',(('Raumkonzept','Space concept'),('Wandgestaltung','Wall design'),('Fotografie','Photography')),
 link=('Zur Projektseite','To the project page','3YqAhMFfdAX84mYeGeTHFW'))
SEC.append(('raum',('Raumgestaltung','Interior design'),('Die Marke dort sichtbar machen, wo Kundschaft empfangen wird und das Team arbeitet.','Making the brand visible where customers are welcomed and the team works.'),raum))
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
