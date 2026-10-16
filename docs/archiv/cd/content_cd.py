# Kategorie «Corporate Design & Raum» (Quelle: content-plan.md, Texte ✅)
SEC=[]
CPN='CP Pump Systems'
# 01 Raumgestaltung
raum=row(CPN,('Die Marke im eigenen Gebäude','The brand in our own building'),
 ('Sitzungszimmer, Lounge und Abteilungen im Erscheinungsbild von CP: Wandbilder, Paneele und Einrichtung, abgestimmt auf die Marke.','Meeting room, lounge and departments in the CP look: murals, panels and furnishings in line with the brand.'),
 'v2_2.jpg',(('Raumkonzept','Space concept'),('Wandgestaltung','Wall design'),('Fotografie','Photography')),
 more=blocks(('Ausgangslage','Starting point','Die Marke CP sollte nicht nur an Messen und in Broschüren sichtbar sein, sondern auch im eigenen Gebäude: dort, wo Kundschaft empfangen wird, und dort, wo die Mitarbeitenden täglich arbeiten.','The CP brand was to be visible not only at trade fairs and in brochures, but also in its own building: where customers are welcomed and where employees work every day.'),
  ('Meine Rolle','My role','Ich gestaltete die Wände der Räume, wählte zusammen mit der Möbelfirma die Einrichtung nach Farbpaletten aus und organisierte die Lieferung. Für die Abteilungen fotografierte ich die Mitarbeitenden bei der Arbeit und gestaltete daraus Wandbilder und Paneele.','I designed the walls, selected the furnishings with the furniture company based on colour palettes and organised the delivery. For the departments, I photographed employees at work and turned the photos into murals and panels.'),
  ('Sitzungszimmer und Lounge','Meeting room and lounge','Wandbild mit Birkenwald und dem Claim «cleaner pumps, cleaner planet™» als Digitaldruck-Tapete, Logo- und Claim-Paneele im Fensterband, Möbel in Grün- und Blautönen passend zum Wandbild.','A birch forest mural with the claim “cleaner pumps, cleaner planet™” as digitally printed wallpaper, logo and claim panels along the windows, furniture in green and blue to match the mural.'),
  ('Abteilungen','Departments','Wandbilder und Paneele für die Abteilungen: eigene Fotos, bearbeitet in Farbe und Schwarzweiss, kombiniert mit Produkt- und Betriebsbildern und Grafiken wie der Weltkarte.','Murals and panels for the departments: my own photos, edited in colour and black and white, combined with product and plant images and graphics such as the world map.'))
 +gallery('rg','Raumgestaltung',['v2_2.jpg','v2_0.jpg','v2_1.jpg','rend_sitzung.jpg','rend_lounge.jpg','pan_14.jpg','pan_2.jpg','pan_21.jpg','pan_24.jpg','pan_25.jpg']),
 link=('Ganze Projektseite','Full project page','3YqAhMFfdAX84mYeGeTHFW'))
raum=raum.replace('>Seiten<','>Bilder<').replace('>pages<','>images<').replace('blättern','ansehen').replace('flip through','view')
def ag(g,lab,fs): 
    G[g]=[(x,lab[0]) for x in fs]
    return '<div class="sub"><h4>'+T(*lab)+'</h4></div><div class="agrid">'+''.join(f'<button class="ag fill" data-gallery="{g}" data-n="{i}"><img src="img/{x}" alt="{lab[0]}"></button>' for i,x in enumerate(fs))+'</div>'
raum+=ag('rg1',('Entwurf: Renderings der Einrichtung','Design: furnishing renderings'),['rend_sitzung.jpg','rend_lounge.jpg'])+ag('rg2',('Wandbild und Visualisierung des Sitzungszimmers','Mural and visualisation of the meeting room'),['v2_2.jpg','v2_0.jpg','v2_1.jpg'])+ag('rg3',('Paneele der Abteilungen','Department panels'),['pan_14.jpg','pan_2.jpg','pan_21.jpg','pan_24.jpg','pan_25.jpg'])
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
