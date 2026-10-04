# Content-Plan yanasenn.ch

Stand: 03.10.2026 · Grundriss, wird laufend verfeinert.

**Legende**
- ✅ von Yana bestätigt
- ❓ offen / noch prüfen
- 📌 bewusst auf später verschoben (nicht vergessen)
- 🔒 nur erwähnen, keine Details zeigen
- ✏️ Entwurf von Claude, muss von Yana freigegeben werden

> Grundregel: Keine erfundenen Fakten, Zahlen, Resultate oder Verantwortlichkeiten. Alles, was auf der Website steht, muss aus diesem Dokument stammen und hier als ✅ markiert sein.

---

## 1. Grundsatzentscheide

| Thema | Entscheid | Status |
|---|---|---|
| Ziel | Freelance-Portfolio: Firmen sehen Projekte und fragen Yana für eigene Projekte an | ✅ |
| Positionierung | Marketing + Creative + Projektmanagement aus einer Hand, end-to-end | ✅ |
| Sprachen | **Deutsch ist die Hauptsprache** (Startseite öffnet auf Deutsch), oben ein Umschalter **DE / EN** für Englisch | ✅ |
| Standort | Zürich | ✅ |
| Bilder | Farbig, kein Schwarz-Weiss-Look | ✅ |
| Schriften | Kostenlose Schriften mit freier kommerzieller Lizenz, selbst gehostet | ✅ |
| Farben | Warmes Off-White, tiefes Fast-Schwarz, eine zurückhaltende Akzentfarbe | ✅ (Akzent ❓) |
| Branding | Typografische Wortmarke «Yana Senn» und Monogramm «YS» für Favicon/Social (Empfehlung) | ✏️ |
| Technik | Astro (statische Website), Upload als normale Dateien auf one.com | ✏️ (keine Einwände) |
| Hosting / Domain | one.com, Domain yanasenn.ch gekauft | ✅ |
| Reihenfolge | 1. Inhalt → 2. Bilder & Assets → 3. Struktur/Design → 4. Code → 5. Test → 6. Live | ✅ |

---

## 2. Positionierung & Hero

### Aufbau «Hi.» (Startseite) ✅
Die Startseite ist eine **Übersicht**; Details stehen auf den Unterseiten.
1. **Hero:** Name, Rolle, grosse Überschrift (ein Wort farbig), Foto Nr. 27 freigestellt, Button «Projekt anfragen»
2. **Kurz über mich:** 2–3 Sätze, Link «Mehr über mich» → Über mich
3. **Ausgewählte Projekte ✅** (6 Kacheln, nur aktuelle Arbeit bei CP; Klick → Case; Link «Ganzes Portfolio» → Portfolio).
   Regel: **Jede Kachel = ein Projekt**, darunter Stichworte, was Yana gemacht hat (Print usw. ist ein Stichwort, keine eigene Kachel).

   | Projekt | Stichworte |
   |---|---|
   | Internationale Messen 2024–2026 (**ACHEMA 2024 als Höhepunkt darin**, keine eigene Kachel) | Organisation · Standdesign · Mailings |
   | Weihnachtskampagnen | Konzept · Verpackung · Karten |
   | Giveaways und Werbeartikel | Auswahl · Branding · Produktion |
   | Broschüren und Factsheets | Layout · Grafik · Druck |
   | Website und Newsletter | Craft CMS · Zoho · LinkedIn |
   | Songkran-Grusskarte | Konzept · Gestaltung |

   **GOLDINGER** steht nicht auf «Hi.», sondern auf der Portfolio-Seite unter **«Frühere Projekte»** ✅ (Fokus auf neuere Arbeit). Die Auswahl kann später noch angepasst werden.
4. **Services kurz:** die 8 Services als Stichworte, Link → Services
5. **Kontakt-Aufruf ganz unten** ✅: «Haben Sie ein Projekt?» mit E-Mail-Adresse und Button **«E-Mail kopieren»** (wie bei Louis), dazu Link zum Kontakt

**Grundsatz ✅:** «Best of both worlds» aus Olivia und Louis, aber **nicht überladen**. Nur das Wichtigste, lieber weniger als mehr.

### Hero ✅ Aufbau
- **Gross:** Name «Yana Senn»
- **Kurze Einleitung:** 2–3 Sätze, wer Yana ist und was sie macht
- **Button:** «Projekt anfragen»
- Überschrift-Slogan: vorerst **Platzhalter**. Die Entwürfe A («Von der Idee bis zum Follow-up.») und B («Ich plane, gestalte und setze um.») haben Yana nicht überzeugt. 📌 Claude bringt später neue Vorschläge.
- **Einleitung ✅:** Version Y + Motto (Text siehe Kapitel 4) – **nur auf «Hi.»**
- **Rolle ✅:** Marketing & Creative Communication

### Prozess-Kette (wiederkehrendes Element)
Idee → Konzept → Gestaltung → Organisation → Produktion → Umsetzung → Kommunikation → Follow-up

---

## 3. Sitemap ✅

```
/                 Hi. (Startseite, DE)   /en/               Hi. (Home, EN)
/portfolio        Alle Projekte          /en/portfolio
/portfolio/<case> Case Study             /en/portfolio/<case>
/services         Services               /en/services
/ueber-mich       Über mich              /en/about
/kontakt          Kontakt                /en/contact
/impressum        Impressum              /en/imprint
/datenschutz      Datenschutz            /en/privacy
/404
```

**Menü ✅:** **Hi. · Portfolio · Services · Über mich · Kontakt**, oben rechts **DE / EN**
(EN: Hi. · Portfolio · Services · About · Contact)

**Aufteilung ✅ (Mischung aus Olivia und Louis):**
- **Hi.** = Startseite mit *kurzer* Vorstellung (Foto, 2–3 Sätze), dann beste Projekte und eine kurze Services-Übersicht
- **Über mich** = das *Ausführliche*: Arbeitsweise, Werdegang als Zeitstrahl (ersetzt einen eigenen «CV»-Menüpunkt), Ausbildung, Sprachen, Tools
- **Services** = eigene Seite mit allen 8 Services

---

## 4. Seiteninhalte

### Home
1. **Hero:** Name, Titelzeile, Hero-Text, starkes Bild (ACHEMA-Stand oder Portrait), CTA «Start a project»
2. **Selected Work:** 4–6 grosse Cases (siehe Kapitel 6)
3. **Services:** was man bei Yana buchen kann (siehe Kapitel 5)
4. **How I work:** Prozess-Kette in 8 Schritten
5. **About-Teaser:** 2–3 Sätze und ein Portrait, Link zu About
6. **Facts-Band:** nur bestätigte Zahlen 📌 (siehe Kapitel 9)
7. **Contact-CTA:** «Have a project in mind?» mit E-Mail und LinkedIn

### Work
- Grosse Cases oben, kleinere Cards darunter
- Optionaler Filter: Trade Fairs & Events · Campaigns & Gifting · Print & Design · Content & Video · Digital & Web

### Case-Seite (Vorlage)
- Kopf: Titel, Kontext (Firma), Jahr(e), Disziplinen, Hero-Bild
- **Context:** Was war das Projekt?
- **My Role:** Was war meine Verantwortung? (Abgrenzung zu Agentur und Team)
- **Approach:** Wie bin ich vorgegangen?
- **Execution:** Was habe ich konkret umgesetzt? (Deliverables)
- **Outcome:** Was wurde umgesetzt bzw. erreicht? (nur Belegbares)
- Bildstrecke
- Nächstes Projekt

### About
- Kurztext 📌 (wird gemeinsam geschrieben, siehe Kapitel 9)
- Arbeitsweise und Prozess
- Werdegang als Timeline (Kapitel 7)
- Ausbildung, Sprachen
- Tools (dezent, sekundär)
- Persönliches (optional): Reisen, Malteser ❓ ob gewünscht (Herkunft wird nicht erwähnt ✅)

### Über mich, Entwurf 2 (DE) ✏️
**Wichtig ✅:** Nicht «Mediamatikerin» als Titel (Ausbildung ist 3 Jahre her, Blick nach vorne). Stattdessen ein moderner Berufstitel, gern mehrere Begriffe (wie «Creative Director» bei Olivia, «Designer» bei Louis).

**Titel ✅:** Marketing & Creative Communication

**Einleitung für «Hi.» ✅ (Version Y, vorerst final; nicht auf Über mich wiederholen):** «Hey, ich bin Yana – eine kreative Denkerin mit viel Enthusiasmus für gute Ideen. Ich gebe Marken ein Gesicht, dort wo Menschen ihnen begegnen: am Messestand, in Kampagnen, in Print und online. Mir ist wichtig, dass Idee, Strategie und Gestaltung zusammenpassen, bis ins letzte Detail.» + Motto: «Mein Motto: Schöne Dinge entstehen, wenn man mit offenen Augen durch die Welt geht.»

Reserve: frühere Varianten 2a, 2c (siehe Git-Verlauf). Nicht verwenden: «Sinn für Struktur», «Hand in Hand», «anpacken», «dranbleiben, bis alles sitzt», lange Reisen.

**Über mich: Referenzen angeschaut ✅**
- Louis: Einleitung (wer, wo, was) → Geschichte «Mein Weg in die Medienwelt» (von den Anfängen bis heute) → Lebenslauf → Story zum Logo → Aktuelles → Kontakt mit «E-Mail kopieren»
- Olivia: sehr kurzer, knackiger Einstieg («Ich habe Ideen, liebe Design und gute Werbung … Zu meinen Skills zähle ich das Konzepten, Gestalten, Planen, Denken und Abliefern.») → Stationen → Education → Awards → Kunden

**Aufbau Über mich ✏️:** 1. kurzer Einstieg (Olivia-Stil) → 2. «Mein Weg» (Louis-Stil, kurz) → 3. Stationen → 4. Weiterbildung, Sprachen, Tools → 5. Kontakt

**Über mich: Text ✅ (von Yana freigegeben)**

*Einstieg:* Ich mag es, wenn Ideen nicht nur gut aussehen, sondern auch ankommen. Darum verbinde ich Kreativität mit Marketing-Verständnis und einer sorgfältigen Organisation, von der ersten Idee bis zum fertigen Ergebnis.

*Mein Weg:*
Angefangen hat alles mit einer kleinen Digitalkamera. Ich habe fotografiert, gefilmt und meine Bilder am Computer bearbeitet, lange bevor ich wusste, dass man daraus einen Beruf machen kann. Mit der Ausbildung zur Mediamatikerin wurde aus dieser Neugier mein Handwerk, und mit jedem Projekt kam mehr Marketing dazu.

Die Ausbildung bei SBW Neue Medien habe ich mit der technischen Berufsmaturität verbunden. Dort habe ich gelernt, wie Gestaltung, Technik und Kommunikation zusammenspielen.

Mein Praktikum führte mich zu GOLDINGER Immobilien. Zwei Jahre lang betreute ich Social Media, fotografierte und filmte Immobilien, gestaltete das halbjährliche Hausmagazin und plante Kampagnen für Infoabende und Tage der offenen Tür. Als Abschlussarbeit entstanden animierte Erklärvideos.

Seit 2024 arbeite ich bei CP Pump Systems im Marketing. Über weite Strecken von 2024 und 2025 war ich dort allein für das Marketing verantwortlich, von internationalen Messen über Broschüren bis zu Website und Weihnachtskampagnen.

Erste Freelance-Aufträge habe ich schon 2023 umgesetzt. Heute unterstütze ich Unternehmen, die Marketing und Gestaltung aus einer Hand suchen.

*(Verworfene Varianten: siehe Git-Verlauf. Anfänge-Fakten: Digitalkamera als Kind, Bildbearbeitung, Schulzeitung, «immer die Kreative»; Paint/Gimp und Schulzeitung nicht betonen.)*

**So arbeite ich:** Idee → Konzept → Gestaltung → Organisation → Produktion → Umsetzung → Kommunikation → Follow-up

**Werdegang ✅:**
- 2024 – heute · CP Pump Systems · Marketing & Kommunikation
- 2021 – 2023 · GOLDINGER Immobilien AG · Praktikum Marketing (Teil der Ausbildung bei SBW Neue Medien)
- 2019 – 2023 · Ausbildung Mediamatikerin EFZ · SBW Neue Medien
- 2019 – 2022 · Technische Berufsmaturität (BM1)
- IT-Support 2018–2019 ✅ weggelassen

**Weiterbildung ✅:** 2026 Praxisbildnerin, zB. Zentrum Bildung · 2026 Fotografie-Workshop mit Bildbearbeitung

**Sprachen ✅:** Deutsch · Schweizerdeutsch · Englisch (fliessend) · Französisch (B1)

**Tools ✅ (nur sichere Kenntnisse zeigen):**
- Design & Bild: InDesign, Illustrator, Photoshop, Lightroom, Acrobat, Canva
- Video: Premiere Pro, CapCut
- Web: Craft CMS, TYPO3, Elementor, Shopify
- Marketing & Social: Meta Business Suite, Meta Ads, LinkedIn, Zoho One
- Office: Microsoft Office, Teams
- AI: ChatGPT, Claude, Midjourney, DeepL

Nur Grundkenntnisse ✅ (auf der Website weglassen): After Effects, Figma, WordPress, Wix, Google Analytics, Gemini. Nicht gebraucht: Adobe Express. Namecheap weggelassen (Domain-Anbieter, kein Arbeitstool).

**Persönliches:** ❓

### Contact
- E-Mail ❓ (siehe Kapitel 8), LinkedIn ❓ URL
- Optional ein kurzes Formular ❓

### Impressum / Datenschutz
- Name, Ort, E-Mail (siehe Kapitel 8)

---

## 5. Services (Freelance-Angebot) ✅

**8 Services** ✅ (inkl. Fotografie als eigener Service) (AI ist kein eigener Service, sondern ein Werkzeug, siehe Über mich). **SEO wird nicht erwähnt** (weder bei den Services noch in den Cases).

| Service | Belegt durch |
|---|---|
| Trade Fair & Event Management | CP-Messen 2024–2026, ACHEMA, GOLDINGER WEGA/Immozionale |
| Campaigns & Corporate Gifting | Weihnachtskampagnen, Songkran, Infoabende, TDOT |
| Print & Graphic Design | Broschüren, Factsheets, Poster, Anzeigen, Hausmagazin, Bautafeln |
| Content: Photo, Video & Social | GOLDINGER Videos/Reels/Erklärvideos, Fotografie, LinkedIn |
| Branded Merchandise | Giveaways, Gummibärchen, Arbeits- und Messekleidung |
| Web & Digital | Website-Pflege (Craft CMS, TYPO3), Newsletter (Zoho), Meta Ads |
| Marketing Support auf Zeit | z. B. wenn eine Firma gerade niemanden fürs Marketing hat (belegt durch die Phase, in der Yana das CP-Marketing allein geführt hat) |

### Services-Texte, Entwurf 1 (DE) ✏️
1. **Messe- und Eventmanagement:** Ich plane und organisiere Messeauftritte von der Anmeldung bis zum Follow-up: Standkonzept, Standdesign, Material, Logistik, Team- und Hotelplanung sowie die Erfassung der Leads. Erfahrung aus Messen in Deutschland, Frankreich, Grossbritannien und den USA.
2. **Kampagnen und Firmengeschenke:** Ich entwickle Kampagnen zu Anlässen wie Weihnachten oder Neujahr, von der Idee über Zielgruppen und Geschenkauswahl bis zu Branding, Verpackung, Karte und Versand.
3. **Print- und Grafikdesign:** Broschüren, Factsheets, Flyer, Anzeigen, Poster und Messegrafiken. Vom Layout bis zu den fertigen Druckdaten und der Abwicklung mit der Druckerei.
4. **Content: Video und Social Media:** Ich filme und schneide Inhalte für Social Media und Website, von Reels bis zu animierten Erklärvideos. Dazu Redaktionspläne und die Betreuung der Kanäle.
8. **Fotografie** ✅ eigener Service, allgemein (nicht nur Produkte), Text ✅: Ich fotografiere Produkte, Gebäude, Events, Messeauftritte und Mitarbeitende und bearbeite die Bilder bis zum fertigen Einsatz auf Website, in Print und auf Social Media.
5. **Werbeartikel und Giveaways:** Von der Auswahl über das Branding bis zur Bestellung: Giveaways, Firmengeschenke sowie Arbeits- und Messekleidung, die zur Marke passen.
6. **Web und Digital:** Pflege von Websites in Craft CMS und TYPO3, Newsletter mit Zoho sowie Kampagnen mit Meta Ads.
7. **Verstärkung fürs Marketing** ✅ vorerst Variante B (später noch verfeinern 📌): Ihr Marketing braucht für eine gewisse Zeit Verstärkung? Ich übernehme laufende Projekte und Aufgaben, von Messen über Print bis zu Web. Bei CP Pump Systems habe ich das Marketing 2024 und 2025 über weite Strecken allein geführt.

❓ Für welche Kundschaft (zum Beispiel KMU, B2B-Industrie, Immobilien)? 📌 später

---

## 6. Projekte

### 6.0 Aufbau Portfolio-Seite ✅
Filter oben: **Alle · Messen · Kampagnen · Print · Video & Content · Digital**. Jede Kachel = ein Projekt.

**Aktuell: CP Pump Systems (2024 bis heute)**
1. Internationale Messen 2024–2026 (mit ACHEMA 2024)
2. Weihnachtskampagnen
3. Giveaways und Werbeartikel (inkl. Arbeits- und Messekleidung)
4. Broschüren und Factsheets
5. Website und Newsletter
6. Songkran-Grusskarte
7. Anzeigen und Fachartikel (z. B. World Fertilizer)
8. Fotografie (nur Produkte, Gebäude, Details, keine Menschen)
9. Infografiken und Karten

**Frühere Projekte: GOLDINGER und Freelance (2021–2023)**
1. Hausmagazin
2. Social Media, Reels und Immobilienvideos
3. Animierte Erklärvideos (IPA)
4. Infoabende und Tage der offenen Tür
5. Messen WEGA und Immozionale (mit Gummibärchen)
6. BAILA BASILEA (Freelance)

Company Tip Game 🔒 nur erwähnen (z. B. auf Über mich), keine eigene Kachel ✏️.
Die Abschnitte 6.1–6.3 unten sind die Faktensammlung pro Thema; sie werden beim Schreiben den Kacheln oben zugeordnet.


### 6.1 Hauptcases (Selected Work)

#### TEXT-ENTWURF Case «Internationale Messen 2024–2026» ✏️
- **Titel:** Internationale Messen 2024–2026
- **Stichworte:** Organisation · Standdesign · Mailings · Logistik
- **Kurz:** 20 Messen in fünf Ländern, dazu Material für neun Partnerauftritte. ❓ (Zahl erst final, wenn alle 2026er-Messen durchgeführt sind)
- **Ausgangslage:** CP Pump Systems ist an Fachmessen für Chemie, Petrochemie, Düngemittel und Pumpentechnik präsent, in Deutschland, Frankreich, Grossbritannien, den USA und Indien. Dazu kommen Messen von Partnern in Spanien, Japan, Korea und der Türkei, für die CP Marketingmaterial und Giveaways liefert.
- **Meine Rolle:** 2024 und 2025 habe ich die Messen über weite Strecken allein betreut, von der Anmeldung bis zum Follow-up. Seit 2026 liegt mein Schwerpunkt auf der Gestaltung: Standdesign, Messewände und Mailings. Leads und E-Mail-Banner gehören weiterhin zu meinen Aufgaben.
- **Vorgehen:** ❓ (Yanas Input: Wie plant sie eine Messe?)
- **Umsetzung:** Anmeldung und Planung · Standkonzept und Standdesign · Möbel, Banner und Messewände · Giveaways · Einladungen und Mailings · Personalplanung und Badges · E-Mail-Signaturen und -Banner · Logistik, Versand und Aufbau · Koordination vor Ort · Erfassung der Leads und Follow-up
- **Logistik ✅ (Yana, 03.10.2026):** Transport und Versand von Messematerial organisiert, zusammen mit der Exportabteilung; Messekisten anfertigen lassen; Zwischenlagerung zwischen Messen.
- **Messeboxen USA ✅:** Zwei Boxen für die US-Messen konzipiert, organisiert und in die USA verschickt, inkl. Suche nach einem Lagerplatz:
  1. *Standbox:* aufklappbar, steht mitten auf dem Stand; Rundum-Design von Yana; darin Broschüren, Werbeartikel und Jacken des Teams; in den USA eingelagert und bei jeder Messe wiederverwendet.
  2. *Transport- und Lagerbox:* für alle Werbeartikel und Messematerialien; zwischen den Messen eingelagert, nicht auf dem Stand.
  Dateien im Drive «Giveaways/CP»: «Box vorne», «Box hinten», «Zeitplan Versand USA Box», «Aufbewahrungskiste für Werbeartikel».
- **Messe-Archiv ✅ (Wunsch Yana, 04.10.2026):** Auf der Projektseite «Internationale Messen» kommen **alle Messen** vor, nicht nur ACHEMA. Nicht auf der Startseite. Aufbau ✏️:
  1. Einleitung + Rolle (Phase 1 / Phase 2)
  2. Höhepunkt ACHEMA 2024 (ausführlich)
  3. **Messe-Archiv als Raster:** pro Messe eine Karte mit Stand-Foto bzw. Standdesign, Name, Ort, Datum, Land und einer Zeile «Meine Aufgaben». Standard-Zeile ✅ (korrigiert): **Standdesign/Messewände hat Yana bei allen Messen gemacht, ausser bei der ACHEMA.** 2024–2025 «Organisation von A bis Z, Standdesign und Messewände, Material, Mailing, Leads»; 2026 «Standdesign, Messewände, Mailing, Leads»; vor Ort: Zusatz «vor Ort im Standteam». Yana korrigiert Abweichungen.
  4. Partner-Messen als kleine Liste
  5. Logistik und Messeboxen USA
  - 📌 Yana lädt pro Messe ein Stand-Foto oder Standdesign hoch (Drive «Messen», Unterordner pro Messe).
- **Interaktive Weltkarte ✅ (Wunsch Yana, 04.10.2026):** Auf der Messe-Seite eine klickbare Weltkarte. Klick auf ein Land (z. B. USA, Frankreich) zeigt alle Messen in diesem Land; Klick auf eine Messe öffnet die Details: Datum, Ort, Stand-Bilder, was Yana gemacht hat, Transport/Logistik, Besonderheiten. Alle Messen zeigen, auch kleine. (Technisch: SVG-Karte in Astro, barrierefrei mit Liste als Alternative.)
- **Vorlage pro Messe ✏️:** Kurzinfo (Datum, Ort, Stand) · Meine Aufgaben · Transport/Logistik · Besonderheit · 2–4 Bilder
- ✅ **Vor Ort war Yana bei:** ACHEMA Frankfurt 2024 und TPS Houston 2024 (beides grosse Messen mit internationalem Publikum; spannend, um Partner und Kunden kennenzulernen und andere Firmen bzw. die Konkurrenz zu sehen).
- 📌 **Wunsch Yana:** Nicht nur ACHEMA zeigen, sondern **mehrere Messen**, besonders jene, bei denen sie vor Ort dabei war → Thema für die nächste Sitzung (Liste der Messen vor Ort, je 1–2 Sätze und Bilder).
- **Highlight TPS Houston 2024 ✏️ (vor Ort):**
  - Fakten ✅: Yanas erste Messe in den USA; sie flog nach Houston. Anderer Markt, anderes Publikum, andere Organisation als in Europa (lockerer, weniger strukturiert). Problem: Lieferung kam nicht wie vereinbart, am Telefon wusste niemand Bescheid → lange Abklärungen, am Ende konnte alles aufgebaut werden. Yanas Aufgaben: Aufbau, Organisation, an der Messe Kundengespräche, Firmenpräsentation, Kundenessen. Die Verkäufer sind Hauptansprechpersonen für die Produkte. Standdesign von Yana.
  - Zusätzliche Fakten ✅ (Yana, 04.10.2026): Vorbereitung umfasste Standdesign, Standbox und Transportkiste (USA), Miete eines Lagers in den USA (Material bleibt dort, kein Hin- und Herschicken), Messebriefing fürs Team (macht Yana vor jeder Messe), Mailing und Werbung im Vorfeld.
  - Funde Drive «Messen/TPS Houston 24» (04.10.2026): Briefing EN (20.–22. August 2024, George R. Brown Convention Center, Stand 2725; TPS seit über 50 Jahren, über 350 Aussteller, Besucher aus über 45 Ländern); Ziel laut Briefing: «a tidy booth that showcases Swiss quality»; Live-Demos der Sicherheitsfunktionen; Geschenk-Registrierung wie ACHEMA; Lead-Formular; Dresscode (CP-Polo/-Hemd); Snacks u. a. Kägi, Biberli; 3 Mailer, ACHEMA-Texte für US-Markt umgeschrieben (Überarbeitung mit US-Kollegen); Standkonzept, Möbel, Podeste, Aufbauanleitung; Shipment-Liste, Kisten; Fotos vom Stand. Nicht verwendet: Rechnungen, Passwörter, Namen.
  - Text ✅ (Version 6, freigegeben):
    - *Kurz:* 20.–22. August 2024 · Houston, Texas · Stand 2725 · über 350 Aussteller, Besucher aus über 45 Ländern
    - *Ausgangslage:* Die TPS in Houston zählt zu den etablierten Fachmessen der Pumpen- und Turbomaschinenbranche. Für mich war es der erste Messeauftritt in den USA, in einem Markt mit eigenem Publikum, eigenen Erwartungen und eigenen Abläufen. Der Anspruch: ein Auftritt, der Schweizer Qualität sichtbar macht, in den Exponaten, im Standbild und in der Organisation.
    - *Meine Rolle:* Gesamtplanung, Standdesign und Organisation sowie Mitarbeit im Standteam vor Ort.
    - *Vorbereitung:* Ich entwickelte das Standdesign und koordinierte die Exponate. Den Versand plante ich gemeinsam mit der Exportabteilung. Die Einladungskampagne der ACHEMA übertrug ich auf den US-Markt: drei Mailings, abgestimmt mit unseren Kollegen in den USA, ergänzt durch E-Mail-Banner und geschaltete Werbung. Registrierte Kunden erhielten am Stand ein Geschenk. Mit einem Messebriefing bereitete ich das Team auf Ablauf, Dresscode, Lead-Erfassung und Standorganisation vor.
    - *Ein Messesystem für die USA ✅:* Statt für jede Messe Mobiliar zu mieten, kauften wir eigene Möbel und entwickelten ein wiederverwendbares System: eine aufklappbare Standbox, die als Bühne mitten auf dem Stand steht, und eine separate Box für die Möbel. Beide werden zu jeder Messe verschickt und enthalten alles, was es für einen Auftritt braucht, vom Mobiliar bis zum Werbematerial. Zwischen den Messen lagern sie in einem gemieteten Lager in den USA. Nach jedem Einsatz wird die Box wieder aufgefüllt: Das Verkaufsteam in den USA hat Zugang, meldet seinen Bedarf, und Broschüren schicken wir nach oder die Kollegen nehmen sie bei Besuchen in der Schweiz mit.
    - *Herausforderung ✅:* Die Standbox hätte am Wochenende vor der Messe eintreffen sollen, kam aber nicht an. Laut Transportunternehmen befand sie sich in einer anderen Stadt, genauere Informationen gab es zunächst nicht. Ich blieb in engem Austausch mit dem Transportunternehmen, bis die Sendung gefunden und nach Houston gebracht wurde. Am Tag vor Messebeginn konnten wir den Stand vollständig aufbauen.
    - *Vor Ort:* In Live-Demos präsentierten wir die Sicherheitsfunktionen unserer Pumpen. Ich führte Kundengespräche, stellte das Unternehmen vor und begleitete Kundenessen, während unsere Verkäufer die technischen Fragen übernahmen. Schweizer Spezialitäten wie Kägi und Biberli unterstrichen die Herkunft von CP.
    - *Nachbereitung ✅:* Die Leads sammelte das Verkaufsteam am Stand. Nach der Messe verteilte ich sie per E-Mail an die Zuständigen und legte sie zentral ab.
- **Arbeitsregel Claude ✅:** Drive-Ordner immer vollständig lesen (alle Seiten der Dateiliste, nextPageToken!).
- **Ton-Regel ✅:** professionell und gepflegt formulieren; keine saloppen Wendungen (z. B. nicht «aufgeräumter Stand», «Hauch Swissness», «am Ende stand der Stand»).
- **Regel ✅:** Bei jedem Messe-Highlight die ganze Kette zeigen: Vorbereitung (Design, Material, Logistik, Lager, Briefing, Mailing/Werbung) → Herausforderung → vor Ort → Nachbereitung. Nichts davon weglassen.

- **Messe: Petrochymia 2024 ✏️** (Quelle: Drive «Messen/Petrochymia 24» + Yana; nicht verwendet: Preise, Rechnungen, Bankdaten)
  - *Kurz:* 27.–28. November 2024 · Martigues, Frankreich · Stand E8-F7 · 12 m² Standfläche, drei Seiten offen
  - *Meine Aufgaben:* Anmeldung und Standbuchung · Standdesign und Druck der Standwände · Möbel · Exponate (MKP, MKPL, MKTP) · Material in französischer Sprache (Broschüren, Explosionszeichnungen) · Giveaways · Versandauftrag · Logistik vor Ort
  - *Logistik (Erklärung von Yana, sauber formuliert):* Bei den französischen Messen dieses Veranstalters läuft die Logistik über einen Partner des Veranstalters. Unser Material gelangte deshalb nicht direkt an die Messe: Gemeinsam mit unserer Exportabteilung liessen wir es zunächst ins Lager des Partners in Frankreich bringen. Von dort wurde es zur Messe geliefert, am Stand per Stapler abgeladen und während der Messe zwischengelagert. Nach Messeschluss ging alles denselben Weg zurück: ins Lager und anschliessend zurück zu uns in die Schweiz.
  - *Text ✅ (freigegeben 04.10.2026):* «Eine kompakte Fachmesse für die Chemie- und Petrochemie-Industrie in Südfrankreich. Für den 12 m² grossen Stand gestaltete ich die Standwände, organisierte Möbel und Exponate und stellte das Material in französischer Sprache zusammen, von den Broschüren bis zu den Explosionszeichnungen. Anspruchsvoll war die Logistik: Sie lief über einen Partner des Veranstalters. Gemeinsam mit unserer Exportabteilung brachten wir das Material zuerst in dessen Lager in Frankreich; von dort ging es an die Messe und nach Messeschluss auf demselben Weg zurück in die Schweiz.»
  - *Bilder ✅:* 2 Stand-Fotos (26.11.2024, Aufbautag), «Standlayout Petrochymia 2024» (Design von Yana). Hinweis: Im Ordner liegt auch «EMail Banner_Fertilizer Show 2025 EN» → gehört zu TFS Orlando 2025.
- **Messe: Pumps & Valves Dortmund 2025 ✏️** (Quelle: Drive «Messen/Pumps & Valves Dortmund 2025», alle Seiten gelesen; nicht verwendet: Preise, Rechnungen, Kontaktdaten, Namen)
  - *Kurz:* 19.–20. Februar 2025 · Dortmund, Deutschland · Halle 5, Stand 5-I06 · 20 m² Eckstand, zwei Seiten offen · parallel zur «maintenance Dortmund»
  - *Funde:* Angebot/Buchung an Yana (Juni 2024); Standdesign (PSD, Aug. 2024) mit zwei Wänden: links Pumpen-Wasser-Motiv «cleaner pumps, cleaner planet™» + Swiss Made, rechts Logo, «Safety first: Magnetic driven pumps, hermetically sealed» und Weltkarte; Druckfreigabe beim Veranstalter (Nov. 2024); Standplanung von oben; Shipment-Liste (3 Exponate MKP, MKPL, ET; Broschüren und Explosionszeichnungen auf Deutsch; Giveaways; Kägi; Kaffeemaschine; Büromaterialkiste); Spedition über den Messespediteur des Veranstalters, Einfuhr nach Deutschland (Einfuhrsteuer); E-Mail-Banner mit Link zum kostenlosen Ticket (3 Formate + Version ohne Rahmen); LinkedIn-Posttexte (3 Varianten); Messebriefing DE (Ausweise, Parkieren, Lesegeräte mit Broschüren, Lead-App, Sideboard, Standauf-/abbau, Dresscode Tag 1/2, Catering, Kundengeschenke mit Voranmeldung); Lead-Formular (Branche, Einsatzbereich, Produktinteresse, To-do); 4 Fotos vom Stand (18.02.2025, Aufbautag; Exponate noch abgedeckt).
  - *Text ✏️:*
    - (Version 2: «wir»-Form auf Wunsch von Yana; ihre Rolle steht in «Meine Aufgaben»)
    - «Die Pumps & Valves in Dortmund ist eine Fachmesse für industrielle Pumpen, Armaturen und Prozesstechnik, mit Besucherinnen und Besuchern aus Chemie, Pharma, Energie und Wasserwirtschaft. Wir waren mit einem 20 m² grossen Eckstand vertreten. Die beiden Standwände zeigten auf der einen Seite das Motiv ‹cleaner pumps, cleaner planet™›, auf der anderen die Kernbotschaft ‹Safety first: Magnetic driven pumps, hermetically sealed› mit einer Weltkarte unserer Standorte.»
    - «Zur Vorbereitung gehörten die Standplanung, drei Exponate, Broschüren und Explosionszeichnungen auf Deutsch, Giveaways sowie der Versand über den Messespediteur, inklusive Einfuhr nach Deutschland. Im Vorfeld luden wir mit E-Mail-Bannern zum kostenlosen Messeticket ein und kündigten unseren Auftritt auf LinkedIn an. Kundinnen und Kunden konnten sich vorab für ein Geschenk anmelden und es am Stand abholen. Ein Messebriefing bereitete das Standteam auf Ablauf, Dresscode, Catering und Lead-Erfassung vor.»
    - *Meine Aufgaben:* Standbuchung · Standdesign · Standplanung · Exponate und Material · Versand · E-Mail-Banner · Messebriefing · Lead-Formular
  - **Ton-Regel ✅ (04.10.2026):** Messe-Texte in der «wir»-Form (als Firma), nicht «ich, ich». Yanas eigene Leistung steht kurz unter «Meine Aufgaben».
  - *Bilder ✅:* 4 Fotos vom Aufbautag (18.02.2025), Standdesign-Freigabe, E-Mail-Banner.
  - ❓ LinkedIn-Posts: von Yana geschrieben?
- **Höhepunkt ACHEMA 2024 ✏️ (ausführlich, auf Wunsch von Yana):**
  - *Ausgangslage:* Die ACHEMA in Frankfurt ist eine der wichtigsten Messen der Prozessindustrie, 2024 mit rund 2'800 Ausstellern aus über 50 Nationen. CP Pump Systems war vom 10. bis 14. Juni mit einem 108 m² grossen Stand in Halle 8 vertreten, unter dem Motto «Sichere Pumpentechnik – zum Schutz von Menschen, Umwelt und Investition.»
  - *Ziel:* Bestehende Kunden an den Stand holen und die Beziehung pflegen, neue Kontakte gewinnen und zeigen, dass CP für jede Anwendung die passende Pumpe hat.
  - *Meine Rolle:* Das Projekt war bereits angelaufen, als ich im Frühling 2024 übernahm. Ich überarbeitete die bestehende Planung und führte sie bis zur Messe zu Ende. Standdesign, Standbau und Montage lagen bei einer Agentur.
  - *Idee und Vorgehen:* Eine Einladungskampagne sollte Kunden gezielt an den Stand bringen: Mit drei Mailings, einem Reminder und einer Dankesmail luden wir sie ein, vorab ein Geschenk zu wählen und es am Stand persönlich abzuholen. Vor Ort sorgten ein Buzzer Game, ein Wettbewerb um die schnellste Pumpenmontage, und eine Live-Demo für Gespräche. Schweizer Schokolade als Giveaway sowie Schweizer Fleisch und Käseplätzchen im Catering unterstrichen die Herkunft von CP.
  - *Umsetzung:* Mailings und Einladungsmanagement · Geschenk-Ablauf am Stand · Infopanels zu den Exponaten · Folie für den Buzzer-Tisch · Giveaways · Namensschilder und Dresscode · Hotel und Anreise für Standteam und Besuchende · Messebriefing mit Schichtplänen · Lead-Formular und Erfassung der Leads
  - *Ergebnis:* 📌 später (Zahlen von Yana)
  - *Bilder* 📌 später: Stand, Giveaways (welche), Buzzer Game, Catering
- **Ergebnis:** 📌 später (Zahlen/Resultate)

#### ACHEMA 2024: Funde aus Yanas Drive-Ordner (03.10.2026)
**Rolle ✅:** Die Marketingleiterin hatte das Projekt begonnen (u. a. Messekonzept Jan 2024). Nach ihrem Ausfall übernahm Yana das laufende Projekt, überarbeitete, verbesserte und vollendete alles bis zur Messe. Ausnahme: Leistungen der Agentur (Standdesign, Standbau, Konstruktion, Logistikplan, Montage). Agentur wird **nicht namentlich** genannt ✅.
Gelesen: Messekonzept (Jan 2024, Ersteller-Kürzel nicht Yana), Ablaufplan Projekt, Ablaufplan Kommunikationsplan, Messebriefing DE (Mai 2024). **Nicht verwendet:** Budget, Rechnungen, Lead-Ziele/KPIs, Namen und Telefonnummern von Mitarbeitenden.
- Öffentliche Fakten: 10.–14.06.2024, Frankfurt, Halle 8, Stand F28
- Messemotto: «Sichere Pumpentechnik – zum Schutz von Menschen, Umwelt und Investition.»
- Einladungskampagne: 3 Mailings, Reminder, Dankesmail; Kunden konnten vorab ein Geschenk wählen und am Stand abholen (Ablauf über Infostand und Verkauf)
- Standerlebnis: «Buzzer Game» (Wettbewerb: schnellste Pumpenmontage, mit Foliendruck für den Buzzer-Tisch), Live-Demo am Demogerät, Display mit Einzelteilen, Catering und Bar
- Giveaways: Säckchen mit Schweizer Schokolade (Swissness), Gadgets (Memo, Schreiber, Mehrwegbecher)
- Team: Messebriefing mit Hallenplan, Schicht- bzw. Dienstplänen pro Tag, Dresscode (CP-Hemden blau/weiss nach Tag), Namensschilder, Hotel und Anreise mit ÖV, Auf- und Abbau
- Leads: überarbeitetes Lead-Formular
- Weitere Dateien: E-Mail-Banner, Namensschilder, Standlayout-Anpassungen, Konzept der Agentur, Bekleidung, Katalogeintrag/Medienpaket, Shipment

#### Case 1 · ACHEMA Frankfurt 2024 (CP Pump Systems)
**Kernaussage ✏️:** Grösste Messe des Programms. Yana koordinierte Organisation, Team, Hotel, Material und Kommunikation; Bau und Konstruktion lagen bei der Agentur.

**Fakten ✅**
- Standfläche **108 m²**
- **12 Personen am Stand** inkl. Yana (Sales und Marketing)
- Zusätzlich Besuchende aus der eigenen Firma (Technik, Produktion, Finanzen, Vorstand u. a.), teilweise mit Übernachtung
- Yana: Hotelplanung (Zimmer für Standteam und Besuchende)
- Zusammenarbeit mit der Agentur **Atelier Türke** ❓ (Schreibweise und Freigabe zur Namensnennung): Standbau, Konstruktion, Logistikplan, Montage
- Yana: Infopanels zu den einzelnen Exponaten gestaltet
- Yana: Mailing
- Yana: Leads am Schluss über ein System erfasst
- Themen Mietmaterial, Logistikkosten, Einlagerung ❓ (Was genau war Yanas Teil?)
- Yana war zu diesem Zeitpunkt relativ neu im Unternehmen

**Offen ❓**
- Datum (ACHEMA 2024 fand im Juni 2024 statt; bitte bestätigen)
- Welche weiteren Materialien: Einladungen, Badges, Signaturen, Giveaways?
- Teamkoordination: Einsatzplan, Briefing?
- Resultate 📌

#### Case 2 · International Trade Fairs 2024–2026 (CP Pump Systems)
**Kernaussage ✏️:** Ein internationales Messeprogramm in fünf Ländern. 2024–2025 hat Yana es weitgehend allein von der Anmeldung bis zum Follow-up betreut; ab 2026 lag ihr Schwerpunkt auf Gestaltung und Kommunikation.

**Phase 1: 2024–2025, weitgehend allein ✅**
Zeitachse ✅ (ungefähr, aus Yanas Erinnerung):
- 01/2024: Start bei CP, zusammen mit der Marketingleiterin
- ca. 03/2024 – ca. 11/2024: **Yana allein** verantwortlich für das Marketing
- ca. 11/2024 – ca. 02–03/2025: wieder zusammen
- ca. 03–04/2025 – ca. 11/2025: **Yana wieder allein**
- ab 2026: wieder mit Leitung

**Darstellung ✅:** nicht plakativ. Keine Gründe nennen (Krankheit, Kündigung der Kollegin sind privat und gehören nicht auf die Website). Nur sachlich formulieren. Formulierung ✅ freigegeben:
- EN: «For long stretches of 2024 and 2025, I was solely responsible for CP Pump Systems' marketing — from trade fairs to print, web and campaigns.»
- DE: «Über weite Strecken von 2024 und 2025 war ich allein für das Marketing von CP Pump Systems verantwortlich – von Messen über Print bis zu Web und Kampagnen.»

**Phase 2: ab 2026, wieder mit Leitung ✅**
Schwerpunkt Gestaltung: Standdesign, Messewände, Mailing. Wie schon zuvor: Mailing, Leads zusammentragen, E-Mail-Banner.

**Aufgabenspektrum** (aus dem Briefing ✅; pro Messe unterschiedlich): Registrierung, Planung, Standkonzept, Standdesign, Möbel, Banner, Giveaways, Einladungen, Mailings, Personalplanung, Badges, E-Mail-Signaturen, Logistik, Versand, Aufbau, Koordination vor Ort, Messeleads, Follow-up.

**Messe-Index ✅**

| Datum | Land | Messe | Ort | Phase |
|---|---|---|---|---|
| 2024 ❓ | DE | ACHEMA | Frankfurt | 1 |
| 2024 ❓ | US | TPS – Turbomachinery & Pump Symposium | Houston | 1 |
| 27.–28.11.2024 | FR | Petrochymia | Martigues | 1 |
| 19.02.2025 | DE | Pumps & Valves | Dortmund | 1 |
| 08.04.2025 | US | TFS – The Fertilizer Show | Orlando | 1 |
| 24.04.2025 | DE | Leuna Dialog | Leuna | 1 |
| 16.09.2025 | US | TPS – Turbomachinery & Pump Symposium | Houston | 1 |
| 03.11.2025 | US | CRU – Sulphur + Sulphuric Acid | The Woodlands | 1 |
| 19.11.2025 | FR | Petro-Chimie | Le Havre | 1 |
| 26.01.2026 | US | FLA – Fertilizer Latino Americano | Miami | 2 |
| 25.02.2026 | DE | Pumps & Valves | Dortmund | 2 |
| 23.04.2026 | DE | Leuna Dialog | Leuna | 2 |
| 20.05.2026 | FR | DK Hub Global | Dunkerque | 2 |
| 20.05.2026 | UK | ChemUK | Birmingham | 2 |
| 01.06.2026 | DE | Yncoris Hausmesse | Hürth | 2 |
| 09.06.2026 | US | ChemE by ACHEMA | Houston | 2 |
| 03.11.2026 | DE | Sulphur + Sulphuric Acid | Berlin | 2 · bevorstehend |
| 18.11.2026 | US | TFS – The Fertilizer Show | Tampa | 2 · bevorstehend |
| 25.11.2026 | FR | Petrochymia | Martigues | 2 · bevorstehend |
| 16.12.2026 | IN | Dahej Industrial Expo | Gujarat | 2 · bevorstehend |

Abgeleitet aus dieser Liste (❓ bitte bestätigen, bevor es auf die Website kommt): **20 Messen 2024–2026 in 5 Ländern** (DE, FR, US, UK, IN), davon 16 bereits durchgeführt (Stand 03.10.2026) und 9 in Phase 1.

**Offen ❓**
- **Entscheide ✅:** Nur die Messen aus der Liste oben. Remstone Sulfur gestrichen. Die 2027-Messen kommen nicht auf die Website (Yana ist dort wahrscheinlich nicht mehr dabei) 📌 im Hinterkopf behalten.
- **Partner-Events ✅** (Yana lieferte Marketingmaterial und Giveaways für Partner/Vertretungen; Liste von Yana, ersetzt die Liste aus dem ersten Briefing):

| Datum | Land | Partner | Messe | Ort |
|---|---|---|---|---|
| 2024 | TR | Metrans | Turkchem | ❓ |
| 22.04.2025 | KR | Dongil | Korea Inter-Battery Exhibition | Seoul |
| 03.06.2025 | ES | Atlas | Pumps and Valves | Bilbao |
| 09.07.2025 | JP | Gadelius | Japan Tokyo Pharm Expo | Tokyo |
| 17.09.2025 | JP | ❓ | Inchem Japan | Tokyo |
| 31.03.2026 | KR | Dongil | Korea Chem | Seoul |
| 04.05.2026 | DE | VDMA | IFAT | München |
| 02.06.2026 | ES | Atlas | Expoquimia | Barcelona |
| 20.10.2026 | ES | Atlas | MMH | Sevilla · bevorstehend |

  - «InnoTrans» aus dem ersten Briefing war ein Versehen ✅ gestrichen.
  - 📌 Partnernamen (Metrans, Dongil, Atlas, Gadelius, VDMA) nur nennen, wenn freigegeben (A12); sonst nur Messe und Ort.
- Schreibweisen: Petrochymia / Petro-Chimie
- Golf Event Thailand: ✅ weglassen

#### Case 3 · Christmas Campaigns & Corporate Gifting (CP Pump Systems)
**Kernaussage ✏️:** Jährliche Kampagne für A-Kunden, B-Kunden und Mitarbeitende, von der Idee bis zum Versand. Die Fallstudie zeigt die Entwicklung von «mit Agentur» (2024) zu eigenständig (2025).

- **2024 ✅:** B-Geschenk Bienenwachstuch-Set, Nachhaltigkeitsbezug. Zusammenarbeit mit einer Agentur (Yana war neu im Unternehmen) und mit einer Werkstatt, in der die Produkte von Hand gefaltet bzw. verpackt wurden. Dazu Karte, Verpackung, Produktbeschreibung und Versand.
- **2025 ✅:** Richartz K Tool Plus Neck and Bike (BB Trading). Yana: Auswahl/Bestellung, Branding, Verpackung, Karte, Organisation. Mitarbeitergeschenk: grossformatiges gebrandetes Badetuch.
- **2026 ❓:** Ideen: Cardholder (B-Kunden), Picnic Blanket (A-Kunden), eventuell Karandashi Pen. Zeigen wir das schon, als «in progress», oder erst nach dem Versand?
- 🔒 Lieferanten bzw. Partner nur nennen, wenn freigegeben 📌 (A12)

#### TEXT-ENTWURF Case «Weihnachtskampagne 2026» ✏️
**Entscheid ✅:** Auf der Website nur **2026** zeigen (Konzept, Design, Text eigenständig von Yana). 2025: Yana leitete die Kampagne mit einer Agentur (nur evtl. ein Satz). 2024 (mit Agentur) weglassen.
- **Stichworte:** Konzept · Kartendesign · Text · Geschenkauswahl
- **Ausgangslage:** Jedes Jahr bedankt sich CP Pump Systems zu Weihnachten mit einem Geschenk, abgestimmt auf drei Zielgruppen: A-Kunden, B-Kunden und Mitarbeitende.
- **Meine Rolle:** Nachdem ich die Kampagne 2025 zusammen mit einer Agentur geleitet hatte, setzte ich sie 2026 eigenständig um: vom Konzept über die Geschenkauswahl bis zu Kartendesign und Texten.
- **Vorgehen:** Statt Geschenke selbst festzulegen, fragte ich zuerst den Verkauf und die Vertretungen: Welche Ideen kommen bei den Kunden an, und wie viele Geschenke braucht es? Die Favoriten verglich ich bei drei Anbietern nach Preis, Druckfläche, Lieferzeit und Herkunft.
- **Idee ✏️:** Jedes Geschenk erzählt etwas über CP. Die Picknickdecke für A-Kunden ist «leakproof»: Sie hält dicht, von unten und von oben, so wie die dichtungslosen Pumpen von CP. Der Kartenhalter für B-Kunden schützt Bank- und Visitenkarten mit einem RFID-Blocker, «Sicherheit, die man nicht sieht, aber spürt», ebenfalls eine Brücke zu den Pumpen. Die Mitarbeitenden erhalten ebenfalls die Picknickdecke, mit einer eigenen Karte unter dem Titel «Gemeinsam stark».
- **Kartenmotiv ✅ (Konzept-Variante 2):** Rentiere ziehen einen Schlitten mit einer CP-Pumpe durch den Nachthimmel über verschneite Berge, dazu «Merry Christmas» und der CP-Claim «cleaner pumps, cleaner planet™». Auf der Innenseite ein Zahlen-verbinden-Rätsel: «Strich für Strich zur Lösung. / Every line reveals more. / Chaque ligne en révèle davantage.» Die Karten sind mit Anrede und Namen personalisiert (Seriendruck).
- **Umsetzung ✏️:** Ich habe die Karten gestaltet und alle Texte geschrieben: für A-Kunden («Zeit für Dankbarkeit»), B-Kunden («Die schönste Zeit des Jahres») und Mitarbeitende («Gemeinsam stark»). Die Kundenkarten gibt es auf Deutsch, Englisch und Französisch, jeweils in der Sie- und der Du-Form; die Mitarbeiterkarte auf Deutsch und Englisch. Dazu kamen Druckvorbereitung mit der Druckerei (Karten, Adressetiketten, Couverts), Bestellung der Geschenke und die Organisation des Versands.
- **Ergebnis:** 📌 später (Versand Ende 2026)
- Quellen ✅ gelesen: Texte Kunde A, Kunde B, Mitarbeitende (Version 1.2, Sept. 2026); Übersicht/Umfrage 2026.
- ✅ Mitarbeitende erhalten die Picknickdecke. Schneekugel war eine andere Konzept-Variante (nicht umgesetzt).
- *Bilder* 📌 später: Kartenvorderseite (Schlitten mit Pumpe), Rätsel-Seite, Picknickdecke, Kartenhalter, Konzept-Skizzen

- **Funde aus Drive «Weihnachtskampagnen» (03.10.2026)** (nicht verwendet: Adresslisten, Preise, Rechnungen, Offerten):
  - 2025: Projektplan Juni–Dez mit einer Agentur (laut Plan: Konzept, Text, Layout, Verpackung bei der Agentur; Lektorat extern; Druck in Druckerei; Übersetzung EN/FR bei CP; Versand DE/FR direkt, Mitarbeitende persönlich; A-Gadget wird von Verkäufern persönlich übergeben; digitales Mailing an übrige Kunden/Agenten weltweit). Karten in vielen Varianten: A-Kunden Sie/Du, männlich/weiblich/neutral, EN personalisiert; Mitarbeiterkarten DE/EN. Badetücher (zweite Lieferung). Skizzen zum Weihnachtsmailing vorhanden (Prozessbilder!). ❓ Was war Yanas Anteil 2025 (vorher hiess es «eigenständig»)?
  - Konzept-Präsentation «Weihnachtsmailing» (Ideen & Konzept): Kartendesigns, Favorit «Schneekugel mit CP-Pumpe», Zahlen-verbinden-Rätsel (ergibt Pumpe oder XMAS), drei Wording-Varianten, Zeitplan. ❓ Von Yana? Welches Jahr? Umgesetzt?
  - 2026: interne Umfrage (April 2026) bei Verkauf/Ländern zu Geschenk-Ideen und Mengen; Vergleich von drei Lieferanten (Preis, Druckfläche, Lieferzeit, Herkunft). Entscheid: A-Kunden Picknickdecke, B-Kunden RFID-Kartenhalter; Karten in allen Sprachen, Sie/Du-Form; Mitarbeiterkarte DE/EN. Starkes «Vorgehen»-Beispiel (datenbasiert). ❓ 2026 zeigen?
- ❓ Offen: A-Kunden-Geschenke 2024/2025? Was für eine Werkstatt (z. B. soziale Einrichtung)? 2025 Multitool für welche Zielgruppe?

#### TEXT-ENTWURF Case «Giveaways und Werbeartikel» ✏️
Quelle: Drive «Giveaways» (CP und GOLDINGER getrennt), gelesen 03.10.2026: Give-Aways_2025 (Anbietervergleiche), Zeitplan Versand USA-Box, Katalog «CP Brochures & Gadgets» (Artikelnummern, zum Bestellen für Events). Nicht verwendet: Preise, Rechnungen, Offerten, Namen.
- **Stichworte:** Auswahl · Branding · Produktion · Versand
- **Ausgangslage:** An Messen, bei Kundenbesuchen und als Dankeschön braucht CP Werbeartikel, die zur Marke passen und gerne benutzt werden, für eigene Messen ebenso wie für Partner weltweit.
- **Meine Rolle:** Ich wähle die Artikel aus, kümmere mich um Branding und Druckdaten, bestelle, organisiere Lagerung und Versand.
- **Vorgehen:** Für neue Artikel vergleiche ich mehrere Anbieter, zum Beispiel bei Fruchtgummis nach Menge, Druckfläche, Lieferzeit und Zutaten. Einen Teil der Bestellungen habe ich klimaneutral über myClimate abgewickelt. ✅
- **Sortiment (Auswahl):** SIGG-Flaschen und -Lunchboxen, Rucksäcke, Badetücher, Fussbälle, Golfbälle, Teleskoplampen, Notizbücher, Multitools, Swiss Tool, Victorinox-Taschenmesser, Kugelschreiber, Kägi-Schokolade, Biberli, Zuckersticks, Kaffee- und Mehrwegbecher, Massstäbe, Universal-Ladestecker, Arbeits- und Messekleidung ✅ (Biberli, Kaffeebecher, Kugelschreiber, Swiss Tool von Yana ergänzt)
- **Logistik:** Material für Messen und Partner im Ausland, z. B. eine Box mit Broschüren und Giveaways für eine Messe in den USA, geplant mit Luft- oder Seefracht-Vorlauf.
- **Eigene Gestaltung ✅:** Verpackung für die Kägi-Schokolade; neues Design für die Dokumentenmappe und den 3D-Ball bei der Neubestellung (Yana: «nimm rein»)
- **Katalog ✅:** Den internen Katalog «Brochures & Gadgets» (Broschüren, Factsheets und Giveaways mit Artikelnummern, zum Bestellen für Events) habe ich erneuert und aktualisiert.
- **GOLDINGER:** Mini-Fruchtgummis im eigenen Design, Autoaufkleber
- **Bilder:** vorhandene Fotos im Ordner (Badetuch, Fussball, Lampen, Taschen, Stifte, Notizbuch, Golf, Box, Mappe); 📌 Yana macht neue Fotos im Büro; bis dahin Mockups als Platzhalter.


#### Case 4 · Branded Objects & Giveaways (CP + GOLDINGER)
**Kernaussage ✏️:** «Branding extends beyond the screen.» Ein bildstarker Case mit wenig Text.

- CP-Giveaways ✅ (Liste aus dem Briefing): Backpacks, Bath Towels, Biberli, Cups, Fruit Gummies, Footballs, Golf Balls, Helmets, Coffee Cups, Kegi, Tape, Travel Items, Pens, Memos, Meter, Swiss Tool, Notepads, Notebooks, Folders, Post-its, Umbrellas, SIGG Lunchboxes & Bottles, Sports Backpacks, Metal Straws, Telescopic Lamps, Tote Bags, Universal Travel Chargers, USB Sticks, Victorinox, Sugar Sticks
- Arbeitskleidung und Messekleidung ✅ 📌
- GOLDINGER-Gummibärchen 2022 ✅ (Formen und Grafik gestaltet, für WEGA & Immozionale)

#### TEXT-ENTWURF Case «Broschüren und Factsheets» ✏️
- **Stichworte:** Konzept · Layout · Infografiken · Mehrsprachigkeit
- **Kurz:** 10 Broschüren in bis zu neun Sprachversionen
- **Ausgangslage:** Die Broschüren von CP Pump Systems waren über die Jahre gewachsen: unterschiedlich aufgebaut, teils mit Einklappfalte, mit verschiedenen InDesign-Strukturen und je nach Sprache mit anderen Inhalten. Das machte Pflege und Übersetzung aufwendig.
- **Ziel:** Ein einheitliches, modulares Broschürensystem: gleicher Aufbau für alle Produktbereiche, identische Inhalte in jeder Sprache, DIN- und ANSI-Normen nebeneinander und ein konsistenter Markenauftritt.
- **Meine Rolle ✏️ (korrigiert, «Grundkonzept bestand» NICHT erwähnen ✅):** Ich habe die bestehenden Broschüren selbst erneuert, verbessert und angepasst, die Inhalte laufend ausgebaut und Ende 2025 ein Konzept zur Vereinheitlichung erarbeitet.
- **Vorgehen:** Ein Standardformat ohne Einklappfalte, ein zentrales InDesign-Masterdokument mit festen Absatz-, Zeichen- und Tabellenformaten und eigenen Ebenen für Sprachen, eine einheitliche Terminologie und wiederkehrende Icons und Infografiken. Eine Pilotbroschüre dient als Referenz, danach folgen die übrigen Schritt für Schritt.
- **Umsetzung:** Intensive Überarbeitung, vor allem von Company-Profil und Sortimentsbroschüre · neue Grafiken wie Weltkarte und Zeitstrahl · Übersetzungen mit einem Übersetzungsbüro, unter anderem ins Chinesische, Polnische, Tschechische und Slowakische · eigene US-Versionen im Letter-Format · Druckvorbereitung und Nachdrucke · Übersicht über alle Druck- und Digitalversionen
- **Neu 2026:** Factsheet «Keeping Molten Sulphur Warm», komplett von mir gestaltet; die Texte basieren auf bestehendem Material und sind mit dem Verkauf abgestimmt.
- **Ergebnis ✅ (Yana):** Die Broschüren werden gedruckt und vom Verkauf weltweit genutzt, bei Kundenterminen, an Messen und überall dort, wo Produkte vorgestellt werden. Zusätzlich stehen sie online als Download zur Verfügung; diese Versionen halte ich laufend aktuell. Neu kamen 2026 Ausgaben auf Tschechisch und Slowakisch dazu. ✅
- 📌 Weitere Factsheets von Yana folgen später.
- **GOLDINGER im Ordner «Broschüren» ✅ gefunden** (Claude hatte zuerst nur Seite 1 der Dateiliste gelesen): Hausmagazin «Die IMMO-EXPERTEN», Ausgabe Februar 2023, 12 Seiten, erscheint 2× im Jahr ✅. Inhalt: Marktausblick 2023, Infoabende an 7 Standorten mit Anmeldetalon und QR-Code, aktuelle Immobilien und Neubauprojekte (S. 4–11), Gutschein für Gratis-Bewertung. Dazu Word-Texte «Editorial», «Ausblick 2023», «Infoabende» und ein älteres Hausmagazin (2022). ❓ Hat Yana auch Texte geschrieben oder nur Layout? Zuordnung: «Frühere Projekte» → Hausmagazin.

#### TEXT «Website und Newsletter» (CP) ✅ – Version 2 (freigegeben)
Fakten ✅ (Yana): Website nicht erstellt, sondern gepflegt; News-Beiträge geschrieben; neue Mitarbeitende (Fototermine organisiert, vorgestellt); Formulare/Service-Seiten mit der Agentur nach Feedback überarbeitet; Downloads laufend erneuert; Weltkarte bei neuen Standorten angepasst; Stellenanzeigen vom HR aufgeschaltet/entfernt; Newsletter und Social Media via Zoho One (LinkedIn, Facebook).
Auf cp-pumps.com gesehen (03.10.2026), ❓ ob Yana das pflegt: Messekalender mit Standnummern und «Gratis-Ticket sichern»; Blogbeiträge pro Messe; Produktbeiträge (z. B. «Sofort verfügbare Pumpensysteme», «saures Prozesswasser»); Download-Bibliothek (Broschüren, Explosionszeichnungen, Zertifikate, AGB); Videoseite; 360°-Showroom; Kontaktseiten pro Land; Karriereseiten inkl. Lernende; Sprachen DE/EN/FR/CN.
- **Stichworte:** Craft CMS · Content · Newsletter · LinkedIn
- **Ausgangslage:** Die Website von CP Pump Systems ist das digitale Schaufenster für Kunden, Partner und Bewerbende weltweit, in Deutsch, Englisch, Französisch und Chinesisch. Technisch betreut sie eine Agentur; damit sie lebendig und aktuell bleibt, braucht es jemanden, der sie inhaltlich pflegt.
- **Meine Rolle:** Ich bin für die Inhalte der Website verantwortlich: Ich schreibe Beiträge, halte Seiten und Downloads aktuell und sorge dafür, dass Website, Newsletter und Social Media dieselbe Geschichte erzählen.
- **Umsetzung:**
  - *News und Blog:* Beiträge zu Messen, Produkten und Unternehmensthemen, inklusive Messekalender mit Standnummern und Gratis-Tickets ✅
  - *Team:* neue Mitarbeitende vorstellen, Fototermine organisieren
  - *Downloads:* Broschüren, Factsheets und Explosionszeichnungen in allen Sprachen laufend erneuern
  - *Unternehmen:* Weltkarte bei neuen Standorten anpassen, Kontaktseiten pro Land aktualisieren ✅
  - *Karriere:* Stellenanzeigen vom HR aufschalten und wieder entfernen
  - *Service und Formulare:* zusammen mit der Agentur überarbeitet, auf Basis von Feedback
  - *Newsletter und Social Media:* Versand und Posts über Zoho One, vor allem LinkedIn und Facebook
- **Zusammenspiel ✏️:** Eine Messe zum Beispiel taucht bei mir an mehreren Orten auf: im Messekalender, als Blogbeitrag, im Newsletter, auf LinkedIn und in der E-Mail-Signatur. ✅
- **Ergebnis:** 📌 später (z. B. LinkedIn-Follower-Entwicklung)
- **GOLDINGER:** Website-Pflege in TYPO3 (Inhalte austauschen, Bilder wählen, Texte anpassen) → in Kachel «Social Media, Reels und Immobilienvideos». Yana kann animierte Erklärvideos und gute Reels liefern 📌.

#### TEXT-ENTWURF «GOLDINGER Hausmagazin» (Frühere Projekte) ✏️
- **Stichworte:** Layout · Editorial · Print
- **Kurz:** «Die IMMO-EXPERTEN», 12 Seiten, zweimal im Jahr
- **Ausgangslage:** GOLDINGER Immobilien gab zweimal im Jahr ein eigenes Hausmagazin heraus. Es zeigte die aktuellen Immobilien und Neubauprojekte, lud zu den Infoabenden ein und lag teilweise Zeitungen in der Ostschweiz bei.
- **Meine Rolle ✅:** Ich gestaltete das Magazin und schrieb die Texte gemeinsam mit dem Verkaufsteam. Die Inhalte legten wir zusammen mit meinem Vorgesetzten fest; Bilder und Objektangaben kamen von den Standorten. Zudem organisierte ich die Verteilung als Zeitungsbeilage: In welchen Zeitungen erreichen wir unsere Zielgruppe, und wo wird das Magazin gestreut? So warb das Magazin auch für die Infoabende.
- **Umsetzung (Ausgabe Februar 2023):** Marktausblick als Titelgeschichte · Infoabende an sieben Standorten mit Anmeldetalon und QR-Code · aktuelle Immobilien und Neubauprojekte auf acht Seiten · Gutschein für eine kostenlose Immobilienbewertung · Planung der Zeitungsbeilagen

#### Fakten «Broschüren und Factsheets» ✅ (Yana, 03.10.2026)
- Bestehende Broschüren (Layout stand), aber **intensiv überarbeitet**: viele Inhalte angepasst und ausgetauscht, vor allem **Company-Broschüre** und **Sortimentsbroschüre**.
- **Neue Grafiken von Yana** erstellt und eingesetzt, z. B. **Weltkarte** und **Zeitstrahl** (nicht nur diese).
- **Übersetzungen in viele Sprachen** koordiniert, zusammen mit einem Übersetzungsbüro, z. B. **Chinesisch, Polnisch** (wegen vieler Partner), u. a.
- **Funde Drive «Broschüren» (03.10.2026):**
  - «Konzept Broschüren» (Dez. 2025): Ausgangslage – Broschüren nicht vereinheitlicht (Aufbau, Layout teils mit Einklappfalte, InDesign-Struktur, Sprachen unterschiedlich). Ziel – einheitliches, modulares Konzept: konsistenter Markenauftritt, gleicher Aufbau für alle Produktbereiche, DIN- und ANSI-Normen, identischer Inhalt pro Sprache, einfachere Pflege und Übersetzung. Vorgehen – Standardformat ohne Einklappfalte, zentrales InDesign-Masterdokument mit Absatz-/Zeichen-/Tabellenformaten und Sprachebenen, einheitliche Terminologie, Sprachkonzept, wiederkehrende Icons und Infografiken, Pilotbroschüre, Rollout, Versionierung. ✅ Konzept von Yana erstellt, Broschüren von ihr überarbeitet.
  - «Übersicht aller Broschüren» (Stand 2026): 10 Broschüren (Company Profile, Sortiment, Produktreihen) in bis zu **9 Sprachversionen**: DE, EN, en-USA (Letter-Format), FR, IT, PL, CN, CZ, SK; Druck- und Digitalversionen, Lager CH und USA. 2026 neu gedruckt: Sortiment CZ und SK, MKP IT, MKPL IT; Nachdruck EN. Company Profile mit neuem Zeitstrahl.
  - Neuer Flyer «Keeping Molten Sulphur Warm» (Sept. 2026, EN) ✅ komplett von Yana gestaltet; Texte aus bestehendem Material übernommen bzw. mit dem Verkauf abgestimmt.
  - 📌 Weitere Flyer und Inserate folgen (später, Kachel «Anzeigen und Fachartikel»).
- 📌 Yana legt Beispiele in Drive-Ordner «Broschüren».

#### Case 5 · Print & Graphic Design (CP Pump Systems)
**Kernaussage ✏️:** Von der Produktbroschüre bis zum Messeplakat: Konzeption, Layout, Bild, Reinzeichnung und Druckabwicklung.

- ✅ Corporate-, Produkt- und Fachbroschüren, Factsheets, Poster/Plakate, Flyer, Banner, Anzeigen, Fachmagazin-Anzeigen, Mailings, Kundenkarten, Visitenkarten/Stationery, Messegrafiken, Verpackungen, Karten
- ✅ Editorial: World Fertilizer (Sulfur), Fachartikel, Messeartikel ❓ (Rolle: Text, Koordination oder Gestaltung?)
- ✅ Koordination mit Druckereien, Agenturen, Lieferanten
- Tools: InDesign, Illustrator, Photoshop

#### Case 6 · GOLDINGER Immobilien: Content, Campaigns & Print (2021–2023)
**Kernaussage ✏️:** Zwei Praxisjahre im Immobilienmarketing: Social Media, Fotografie, Video und Print für Verkauf, Events und Marke.

**Fakten ✅** (CV und altes Portfolio)
- Social-Media-Management (Instagram, Facebook, LinkedIn, YouTube), Redaktionspläne
- Posts, Reels, Stories (Erlebnisberichte, Fragerunden, Umfragen, Bewerbung der Infoabende), Mitarbeitervorstellungen, Infografiken
- **Immobilienvideos:** Aufnahmen, Rundgänge, Schnitt, Reels ❓ (Luftaufnahmen: eigene Drohne oder Fremdmaterial?)
- **Interview-Reels** mit Fachleuten (Makler, Bewirtschafter)
- **Animierte Erklärvideos** ✅ = Yanas **IPA (Abschlussarbeit der Lehre)**
- **Hausmagazin** ✅ halbjährlich (gemäss altem Portfolio-Text): Inhalte mit Vorgesetztem festgelegt, Texte und Bilder von den Standorten, Layout von Yana, Druck, teilweise Zeitungsbeilage
- **Infoabende 2023:** Meta-Ads (Fokus Ostschweiz, 4 Wochen Laufzeit, Ziel Anmeldungen) und Printinserate in Ostschweizer Zeitungen (Offerte bis Übermittlung)
- **Tag der offenen Tür (TDOT) 2023:** Vermarktungsstrategie für schwer verkäufliche bzw. Spezialobjekte; Printinserate, Flyer in Büros, Instagram-Kampagnen über Meta; Organisation in Absprache mit Verkäufern
- **WEGA & Immozionale 2022:** Messewände neu gestaltet, Gummibärchen, Printstrategie (wöchentliche Inserate, Flyer)
- Print: Inserate, Broschüren, Bautafeln/Aussenplakate, Flyer, Texte
- Website-Pflege mit TYPO3
- Entwicklung und Analyse von Kampagnen, Evaluation von Partnern und Lieferanten

**Offen ❓**
- Altes Portfolio und Videos vom anderen PC 📌
- Alte Texte sind teils sehr blumig («faszinierend», «renommiert») und werden im neuen Ton neu geschrieben.

### 6.2 Kleinere Cards
- **Digital & Web, CP:** Craft CMS (Updates, Content, Bilder, Formulare), Newsletter und Social via Zoho One, LinkedIn/Facebook, Blogposts
- **Songkran Greeting Card:** Grusskarte zum thailändischen Neujahr für die Partner- bzw. Tochterfirma in Thailand ❓ (Jahr, Format, Rolle)
- **Company Tip Game** 🔒: nur erwähnen
- **Animated Explainer Videos** (GOLDINGER, IPA ✅) eigene Card
- **BAILA BASILEA 2023:** Videoflyer für die Instagram Story einer Halloween-Party in Basel ✅ **Freelance-Auftrag** (erster Freelance-Beleg)
- **Flyer:** TDOT GOLDINGER, Skatepark-Eröffnung ❓ (für wen?)
- **Visual Content:** Infografiken, World Maps, Timelines, Zahlenstrahlen, Icons, Fotografie (Mitarbeitende, Gebäude, Outdoor, Event, Messe, Exponate)

### 6.3 Archiv / eventuell weglassen ❓
- Food-Truck-Marketingkonzept Romanshorn (überbetrieblicher Kurs)
- Logo ÜK (Gruppenarbeit)
- «Webdesign» (unklar, was gemeint ist)

---

## 7. Werdegang & Fakten

| Zeitraum | Station | Status |
|---|---|---|
| 01/2018 – 08/2019 | IT-Support bei «VQ» ❓ (Firmenname, Art der Anstellung) | ❓ |
| 08/2019 – 07/2023 ❓ | Lehre Mediamatikerin EFZ, SBW Neue Medien (2 Jahre Schule, 2 Jahre Praxis) | ✅ (Endmonat ❓) |
| 2019 – 2022 | Berufsmaturität BM1, Richtung TALS (Technik, Architektur, Life Sciences), parallel zur Lehre | ✅ |
| 08/2021 – 08/2023 | GOLDINGER Immobilien AG, Praktikum Marketing / Mediamatikerin | ✅ |
| 01/2024 – heute | CP Pump Systems, Mitarbeiterin Marketing & Kommunikation | ✅ |
| 01/2026 | **Praxisbildnerin**, zB. Zentrum Bildung, Baden (Seminar mit Kursbestätigung) | ✅ |

**Sprachen ✅:** Deutsch und Schweizerdeutsch (fliessend), Englisch C1, Französisch B1 (DELF ❓ Niveau prüfen), 
**Auf der Website ✅ (Variante A):** nur Deutsch, Schweizerdeutsch, Englisch, Französisch. **Russisch und Herkunft werden nicht erwähnt** (Yanas Entscheid).

**Tools ✅:** InDesign, Illustrator, Photoshop, Premiere Pro, Canva, TYPO3, Craft CMS, Elementor, Shopify, Meta Ads, Zoho One, Namecheap, ChatGPT, Claude

**AI ✅:** kein eigener Satz und kein Service. ChatGPT und Claude stehen einfach in der Tool-Liste wie Photoshop (eventuell gruppiert als «AI-Tools»).

**Aktuelle Anstellung:** Muss nicht prominent erwähnt werden ✅. Empfehlung: CP-Projekte ehrlich als «in-house» kennzeichnen. In der Timeline steht «2024 –» ohne Kommentar. ❓ Vor dem Livegang den Arbeitsvertrag auf Nebenerwerb und Vertraulichkeit prüfen.

---

## 8. Kontakt & Impressum

- Name: **Yana Senn** ✅
- E-Mail: `yana.senn1@gmail.com` ✅ (vorläufig; später eventuell eigene Domain-Adresse wie `hello@yanasenn.ch` 📌)
- Website-Text: «based in Zurich» ✅
- Impressum vorerst: **Yana Senn, Dielsdorf ZH**, E-Mail ✅ (so wenig Privates wie möglich)
- 📌 Vor dem Livegang nochmals entscheiden: volle Adresse oder Geschäfts- bzw. Postfachadresse (UWG Art. 3 verlangt eine Kontaktadresse; Datenschutzerklärung ebenso)
- LinkedIn-URL ❓
- Telefon: ❓ (Empfehlung: nein)
- CV-Download: ❓

---

## 9. Merkliste für später 📌

- [ ] **Resultate und messbare Werte** pro Case einholen (Leads, Teilnehmende, Anmeldungen, Reichweiten, Stückzahlen, Feedback)
- [ ] **LinkedIn-Follower-Entwicklung** (Yana ist sehr aktiv, Wachstum belegen: Zeitraum, Zahlen von–bis, persönliches Profil oder CP-Seite?)
- [ ] **Arbeitskleidung und Messekleidung** als Thema und Bilder
- [ ] **Moodboards, Skizzen, Entwürfe** als Prozessbilder
- [ ] **Punkt 4 «Projektdateien»** detailliert durchgehen (PDFs, Grafiken, Videos, Social Posts …)
- [ ] **A12 Partner- und Lieferantennamen**: was genannt werden darf
- [ ] **Personen auf Fotos** unkenntlich machen, wo keine Einwilligung vorliegt
- [ ] **About-Text** gemeinsam schreiben (der alte Text ist zu blumig; «About me kopiert» stammt von einer anderen Person und wird **nicht** verwendet)
- [ ] **Referenzen** ✅ erhalten und angeschaut (03.10.2026). Kurzanalyse:
  - **oliviahug.ch:** Name zentriert in eleganter Serif, Portrait im Bogenrahmen, persönlicher Intro-Satz («Hey. Ich bin Olivia …»), Cases als grosse Bilder bzw. Slider mit Kurztext und Liste der Leistungen, viel Weissraum, ruhig.
  - **louisplant.ch:** ähnlicher Werdegang (Marketing in-house → Freelance). Grosse Bildcollage oben, Kurzprofil mit Portrait, «Selected Projects» als 2er-Raster, Services mit je einem Absatz und «Learn more», Projekte mit Kategorie und Jahr, Testimonials, Sprachumschalter.
  - **pascalfrey.ch (Inhalt):** nummerierte Kapitel («01 — Profil»), Faktenliste neben dem Portrait (Erfahrung, Aktuell, Standort), Expertise als nummerierte Liste mit je einem Satz, Arbeiten als typografischer Index mit Jahr (passt sehr gut zum Messe-Index).
  - **Yanas Feedback ✅:**
    - **Olivia** gefällt optisch am besten: übersichtlich, einfach, klare Reihenfolge (Foto → kurze Vorstellung → Arbeiten), dazu die dezente Animation im Hintergrund.
    - **Louis:** Aufteilung gefällt (ähnlich wie Olivia), optisch aber weniger als Olivia.
    - **Pascal:** Inhaltlich wertvoll, weil er detailliert erklärt, was er kann (inklusive AI), mit Strategie, Positionierung und Erfolgen. Sein Stil ist Yana aber zu viel.
    - **YouTube-Screenshot:** gefällt optisch am meisten; Yana möchte so etwas mit ihrem eigenen Bild (freigestelltes Portrait im Hero).
  - **Design-Richtung ✅:** Hero im Stil des Screenshots mit eigenem Portrait, Rest der Seite ruhig und übersichtlich wie bei Olivia, Services aufgeteilt wie bei Louis.
  - **Texte ✅:** Aufbau und Ton wie bei Louis und Olivia (klar, persönlich, übersichtlich). Von Pascal nur die Tiefe: nicht nur zeigen, *was* gemacht wurde, sondern auch *wieso, weshalb, warum* (Ziel, Überlegung, Vorgehen). Pascal ist Inspiration, kein Vorbild zum Kopieren.

### Portraits (Drive: `yanasenn-website/Bilder Yana`)
| Datei | Beschreibung | Eignung |
|---|---|---|
| `SBWNM-LG19-Yana-Senn_web72dpi…jpg` (2942×1655) | Am Laptop, Büro/Lounge, natürlich, quer | ⭐ Yanas Favorit. ✅ **About-Bild**. Ideal für About bzw. «How I work». Für den Hero zum Freistellen weniger geeignet (unruhiger Hintergrund, Tisch und Laptop) |
| `CP-Pumpen-Yana-Senn-24.jpg` (5005×3337) | Studio, lächelnd, schwarzer Blazer, hellblau-grauer Hintergrund | Sehr gut zum Freistellen, hohe Auflösung |
| `CP-Pumpen-Yana-Senn-27.jpg` (5005×3337) | Studio, Arme verschränkt, selbstbewusst, gleicher Hintergrund | ✅ **Hero-Bild** (freistellen; Nr. 24 als Ersatz) |
| `CP-Pumpen-Yana-Senn-03.jpg`, `…-Webseite.jpg` | noch nicht angeschaut | – |

- 📌 **Bildrechte prüfen:** Die Fotos stammen aus Shootings von SBW bzw. CP Pump Systems. Klären, ob Yana sie für die eigene Website nutzen darf (Fotograf/Firma).
  - YouTube-Video (Design-Inspiration): https://www.youtube.com/watch?v=hTwbCmZhFNA
    Screenshot erhalten (Hero «I'm a Coder.»): sehr grosse fette Grotesk-Headline, ein Wort kursiv in Akzentfarbe (Terracotta), freigestelltes Portrait vor Himmel-Collage, Name und Rolle rechts mit Akzentlinie, runder Button «Hire Me», abgerundeter Rahmen, Akzentfarben-Varianten Terracotta / Salbei / Blau / Rost. ❓ Welche Elemente gefallen Yana?
  - https://www.louisplant.ch/ (Design)
  - https://www.oliviahug.ch/ (Design)
  - https://www.pascalfrey.ch/ (nur Inhalt interessant, nicht Design)
- [ ] **Altes GOLDINGER-Portfolio** und Videos vom anderen PC übertragen
- [ ] **Hero-Portrait** für die Freistellung (Stil wie im YouTube-Screenshot): ruhiger Hintergrund, gute Auflösung, Kopf und Schultern
- [ ] **Praxisbildnerin:** betreut Yana selbst Lernende bei CP? (nur erwähnen, wenn ja)
- [ ] **Fotografie** ✅ als Kompetenz: in der Ausbildung gelernt, zusätzlich 2026 ein Fotografie-Workshop bei CP (2 Tage, vor Ort bei CP): Auffrischung und Post-Production bzw. Bildbearbeitung ✅. **Keine Fotos von Menschen zeigen** ✅ (Porträts nicht verwendbar). Zeigbar: **Produktfotos** ✅ (viele vorhanden), eventuell Gebäude, Exponate, Details. ✅ Eigener Service «Fotografie» (allgemein) und eigene Kachel im Portfolio.
- [ ] **Persönliches später einbauen:** künstlerische Begabung, AI
- [ ] **Alle Messen einzeln erfassen** (Vorlage pro Messe, Weltkarte) – läuft
- [ ] **Image Checklist** im Format MUST / NICE / OPTIONAL erstellen
- [ ] **Logo** gemeinsam ausdenken (Vorschlag bisher: Wortmarke «Yana Senn» und Monogramm «YS»)
- [ ] **Akzentfarbe und Schriftpaar** festlegen (nach Referenzen)

---

## 10. Nächste offene Fragen (Priorität)

1. E-Mail für die Website und Wohnort fürs Impressum (Schreibweise)
2. Monate der Allein-Phasen bei CP (für die Story in Case 2)
3. Welche Services Yana anbieten will (Kapitel 5)
4. Weitere Messen und Partner-Events: aufnehmen oder nicht (Case 2)
