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
- E-Mail ✅ und LinkedIn ✅ (siehe Kapitel 8)
- Kein Formular ✅ (Yana 06.10.2026): nur E-Mail-Adresse mit Button «E-Mail kopieren»

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

**✅ Portfolio-Aufbau v11 mit Kategorien und Ordnern (Yana 06.10.2026: «weiter gehts», als Arbeitsstand freigegeben)** · Entwurf: `docs/portfolio-struktur.html` (Artifact https://claude.ai/artifact/49ZGEQbYrgPgZhXQiNeCmw)
- ✅ Regeln: oben nur die wichtigsten Projekte · darunter «Alle Arbeiten» in Kategorien, darin **Ordner nach Art** (zusammenfassen, nicht verstreuen) · keine Jahreszahlen auf der Übersicht · Molten Sulphur keine Kampagne · Reels und Halloween-Videoflyer = Social Media · Weltkarte = Grafik (bei Messen/Broschüren nur auf der Projektseite erwähnen) · Werbeartikel und Giveaways sind dasselbe · Titel kurz und professionell · ✅ kein «inklusive»/«u. a.» bei Offensichtlichem · ✅ Beschriftungen simpel halten, keine Erklärsätze in Listen (Yana 06.10.2026).
- **Ausgewählte Projekte (6):** ACHEMA 2024 in Frankfurt · Weihnachten 2026 · Mobiler Messestand für die USA · Produktbroschüren in neun Sprachen · Immobilien-Reels · Die Marke im eigenen Gebäude.
- **Kategorien → Ordner:**
  1. **Messen:** International (Messen 2024–2026, Messestand USA, Partnerstände) · Schweiz (WEGA, Immozionale)
  2. **Grafik & Print:** Broschüren und Magazin · Flyer · Inserate · Infoblätter · Grusskarten · Messegrafik · Infografiken
  3. **Corporate Design & Raum:** Raumgestaltung · Redesigns · Markenidentität (Trailer Park)
  4. **Digital & Social Media:** Website · Newsletter · E-Mail-Banner · Web-Banner · LinkedIn · Instagram
  5. **Foto & Video:** Firmenshooting · Reportage · Immobilienvideos · Erklärvideos
  6. **Werbeartikel:** Giveaways (alle Werbeartikel mit Logo, Fruchtgummis nicht separat) · Kunden- und Mitarbeitergeschenke (Weihnachten und weitere Kundengeschenke; weitere Kundengeschenke erscheinen zusätzlich bei Giveaways, Yana 06.10.2026) · Arbeits- und Messekleidung
- Infoabende und Tage der offenen Tür: kein eigener Ordner; ihre Flyer, Inserate und Instagram-Beiträge liegen in den passenden Ordnern, die Geschichte steht auf der Projektseite.
- Ersetzt v4–v10 (Verlauf in Git).

**Aktuell: CP Pump Systems (2024 bis heute)**
1. Internationale Messen 2024–2026 (mit ACHEMA 2024)
2. Weihnachtskampagnen
3. Giveaways und Werbeartikel (inkl. Arbeits- und Messekleidung)
4. Broschüren und Factsheets
5. Website und Newsletter
6. Songkran-Grusskarte
7. Werbung: Print & Digital (ehemals «Anzeigen und Fachartikel», z. B. World Fertilizer)
8. Fotografie (Gebäude, Details, Reportagen und ✅ vorerst auch Mitarbeitende bei der Arbeit, nur mit Einverständnis; kann später wieder entfernt werden, Yana 05.10.2026)
9. Infografiken und Karten
10. ✅ Raumgestaltung: die Marke im Gebäude (eigener Case, Yana 05.10.2026)

**Frühere Projekte: GOLDINGER und Freelance (2021–2023)**
1. Hausmagazin
2. Social Media, Reels und Immobilienvideos
3. Animierte Erklärvideos (IPA)
4. Infoabende und Tage der offenen Tür
5. Messen WEGA und Immozionale (mit Gummibärchen)
6. BAILA BASILEA (Freelance)
7. ✅ **Redesigns Print (Vorher/Nachher)** – Faltmappe, Flyer, Inserate, Messewände

Company Tip Game 🔒 nur erwähnen (z. B. auf Über mich), keine eigene Kachel ✏️.
Die Abschnitte 6.1–6.3 unten sind die Faktensammlung pro Thema; sie werden beim Schreiben den Kacheln oben zugeordnet.


### 6.1 Hauptcases (Selected Work)

#### TEXT-ENTWURF Case «Internationale Messen 2024–2026» ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
- **Titel:** Internationale Messen 2024–2026
- **Stichworte:** Organisation · Standdesign · Mailings · Logistik
- **Kurz ✅ (Yana 06.10.2026: keine Länder und keine Zahl; Ort und Details nur auf den einzelnen Messen):** Messeauftritte von CP Pump Systems und an Partnerständen, von der Idee bis zur Nachbereitung. («eigene» vermeiden, klingt nach «selbst gemacht», Yana 06.10.2026)
- **Ausgangslage:** CP Pump Systems ist an internationalen Fachmessen für Chemie, Petrochemie, Düngemittel und Pumpentechnik präsent. Dazu kommen Messen von Partnern, für die CP Marketingmaterial und Giveaways liefert.
- **Meine Rolle:** 2024 und 2025 habe ich die Messen über weite Strecken allein betreut, von der Anmeldung bis zum Follow-up. Seit 2026 liegt mein Schwerpunkt auf der Gestaltung: Standdesign, Messewände und Mailings. Messebriefing, Lead-Formular und E-Mail-Banner gehören weiterhin zu meinen Aufgaben.
- **Vorgehen ✅ (v2, Yana 06.10.2026):** Jeder Messeauftritt beginnt mit einer Idee, sei es von mir, von der Geschäftsleitung oder aus dem Verkauf. Bevor etwas entschieden wird, schaffe ich eine solide Grundlage: Ich hole Offerten ein und kläre, was die Messe bietet und was ein Auftritt kostet. Im Kick-off fällt dann, abgestimmt auf das Budget, der Entscheid. Erst danach beginnt die eigentliche Planung: Standfläche und Standdesign, Exponate und Material, Logistik, Werbung im Vorfeld und ein Briefing, damit das Team vor Ort bestens vorbereitet ist. Mit der Nachbereitung schliesse ich jeden Auftritt ab.
- **Umsetzung:** Anmeldung und Planung · Standkonzept und Standdesign · Möbel, Banner und Messewände · Giveaways · Einladungen und Mailings · Personalplanung und Badges · E-Mail-Signaturen und -Banner · Logistik, Versand und Aufbau · Koordination vor Ort · Lead-Formular und Nachbereitung
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
  - Text ✏️ (Version 7, neutraler Ton; Version 6 war freigegeben, Inhalt unverändert):
    - *Kurz:* 20.–22. August 2024 · Houston, Texas · Stand 2725 · über 350 Aussteller, Besucher aus über 45 Ländern
    - *Ausgangslage:* Die TPS in Houston zählt zu den etablierten Fachmessen der Pumpen- und Turbomaschinenbranche. Ein Markt mit eigenem Publikum, eigenen Erwartungen und eigenen Abläufen. Der Anspruch: ein Auftritt, der Schweizer Qualität sichtbar macht, in den Exponaten, im Standbild und in der Organisation.
    - *Meine Aufgaben:* Gesamtverantwortung · erster eigener Messeauftritt in den USA · Gesamtplanung · Standdesign · Exponate · Versand mit der Exportabteilung · Messesystem USA · Mailings und Werbung · Messebriefing · Lead-Formular · Standteam vor Ort · Verteilung der Leads
    - *Vorbereitung:* Am Anfang standen ein eigenes Standdesign und die Auswahl der Exponate; der Versand lief in Abstimmung mit der Exportabteilung. Die Einladungskampagne der ACHEMA wurde für den US-Markt übertragen: drei Mailings, abgestimmt mit den Kollegen in den USA, ergänzt durch E-Mail-Banner und geschaltete Werbung. Registrierte Kunden erhielten am Stand ein Geschenk. Ein Messebriefing bereitete das Team auf Ablauf, Dresscode und Standorganisation vor.
    - *Ein Messesystem für die USA ✅:* Statt für jede Messe Mobiliar zu mieten, entstand ein eigenes, wiederverwendbares System: eine aufklappbare Standbox, die als Bühne mitten auf dem Stand steht, und eine separate Box für die Möbel. Beide werden zu jeder Messe verschickt und enthalten alles, was es für einen Auftritt braucht, vom Mobiliar bis zum Werbematerial. Zwischen den Messen lagern sie in einem gemieteten Lager in den USA. Nach jedem Einsatz wird die Box wieder aufgefüllt: Das Verkaufsteam in den USA hat Zugang, meldet seinen Bedarf, und Broschüren kommen per Post nach oder reisen bei Besuchen in der Schweiz mit.
    - *Herausforderung ✅:* Die Standbox hätte am Wochenende vor der Messe eintreffen sollen, kam aber nicht an. Laut Transportunternehmen befand sie sich in einer anderen Stadt, genauere Informationen gab es zunächst nicht. Erst ein enger, beharrlicher Austausch mit dem Transportunternehmen brachte die Sendung nach Houston. Am Tag vor Messebeginn stand der Stand vollständig.
    - *Vor Ort:* Live-Demos zeigten die Sicherheitsfunktionen der Pumpen. Neben den technischen Gesprächen der Verkäufer gehörten Firmenpräsentationen, Kundengespräche und Kundenessen zum Programm. Schweizer Spezialitäten wie Kägi und Biberli unterstrichen die Herkunft von CP.
    - *Nachbereitung ✅:* Nach der Messe gingen die Leads an die zuständigen Verkäufer und wurden zentral abgelegt.
    - *Ausblick ✅ (Yana 04.10.2026):* «Im Jahr darauf war CP an der TPS in Houston am Stand eines Partners vertreten.» → TPS Houston 2025 bekommt keinen eigenen Eintrag (Partnermesse, kein eigener Stand); nur in Liste/Karte als Partnermesse.
- **Arbeitsregel Claude ✅:** Drive-Ordner immer vollständig lesen (alle Seiten der Dateiliste, nextPageToken!).
- **Ton-Regel ✅:** professionell und gepflegt formulieren; keine saloppen Wendungen (z. B. nicht «aufgeräumter Stand», «Hauch Swissness», «am Ende stand der Stand»).
- **Regel ✅:** Bei jedem Messe-Highlight die ganze Kette zeigen: Vorbereitung (Design, Material, Logistik, Lager, Briefing, Mailing/Werbung) → Herausforderung → vor Ort → Nachbereitung. Nichts davon weglassen.

- **Messe: Petrochymia 2024 ✏️** (Quelle: Drive «Messen/Petrochymia 24» + Yana; nicht verwendet: Preise, Rechnungen, Bankdaten)
  - *Kurz:* 27.–28. November 2024 · Martigues, Frankreich · Stand E8-F7 · 12 m² Standfläche, drei Seiten offen
  - *Meine Aufgaben:* Gesamtverantwortung · Anmeldung und Standbuchung · Standdesign und Druck der Standwände · Möbel · Exponate (MKP, MKPL, MKTP) · Material in französischer Sprache (Broschüren, Explosionszeichnungen) · Giveaways · Versandauftrag · Logistik vor Ort
  - *Logistik (Erklärung von Yana, sauber formuliert):* Bei den französischen Messen dieses Veranstalters läuft die Logistik über einen Partner des Veranstalters. Unser Material gelangte deshalb nicht direkt an die Messe: Gemeinsam mit unserer Exportabteilung liessen wir es zunächst ins Lager des Partners in Frankreich bringen. Von dort wurde es zur Messe geliefert, am Stand per Stapler abgeladen und während der Messe zwischengelagert. Nach Messeschluss ging alles denselben Weg zurück: ins Lager und anschliessend zurück zu uns in die Schweiz.
  - *Text ✏️ (neutraler Ton; Inhalt wie freigegebene Version):* «Eine kompakte Fachmesse für die Chemie- und Petrochemie-Industrie in Südfrankreich. Der 12 m² grosse Stand erhielt eigens gestaltete Standwände, dazu Möbel, drei Exponate und Material in französischer Sprache, von den Broschüren bis zu den Explosionszeichnungen. Anspruchsvoll war die Logistik: Sie lief über einen Partner des Veranstalters. In Abstimmung mit der Exportabteilung ging das Material zuerst in dessen Lager in Frankreich, von dort an die Messe und nach Messeschluss auf demselben Weg zurück in die Schweiz.»
  - *Bilder ✅:* 2 Stand-Fotos (26.11.2024, Aufbautag), «Standlayout Petrochymia 2024» (Design von Yana). Hinweis: Im Ordner liegt auch «EMail Banner_Fertilizer Show 2025 EN» → gehört zu TFS Orlando 2025.
- **Messe: Pumps & Valves Dortmund 2025 ✏️** (Quelle: Drive «Messen/Pumps & Valves Dortmund 2025», alle Seiten gelesen; nicht verwendet: Preise, Rechnungen, Kontaktdaten, Namen)
  - *Kurz:* 19.–20. Februar 2025 · Dortmund, Deutschland · Halle 5, Stand 5-I06 · 20 m² Eckstand, zwei Seiten offen · parallel zur «maintenance Dortmund»
  - *Funde:* Angebot/Buchung an Yana (Juni 2024); Standdesign (PSD, Aug. 2024) mit zwei Wänden: links Pumpen-Wasser-Motiv «cleaner pumps, cleaner planet™» + Swiss Made, rechts Logo, «Safety first: Magnetic driven pumps, hermetically sealed» und Weltkarte; Druckfreigabe beim Veranstalter (Nov. 2024); Standplanung von oben; Shipment-Liste (3 Exponate MKP, MKPL, ET; Broschüren und Explosionszeichnungen auf Deutsch; Giveaways; Kägi; Kaffeemaschine; Büromaterialkiste); Spedition über den Messespediteur des Veranstalters, Einfuhr nach Deutschland (Einfuhrsteuer); E-Mail-Banner mit Link zum kostenlosen Ticket (3 Formate + Version ohne Rahmen); LinkedIn-Posttexte (3 Varianten); Messebriefing DE (Ausweise, Parkieren, Lesegeräte mit Broschüren, Lead-App, Sideboard, Standauf-/abbau, Dresscode Tag 1/2, Catering, Kundengeschenke mit Voranmeldung); Lead-Formular (Branche, Einsatzbereich, Produktinteresse, To-do); 4 Fotos vom Stand (18.02.2025, Aufbautag; Exponate noch abgedeckt).
  - *Text ✏️:*
    - (Version 3: neutraler Ton)
    - «Die Pumps & Valves in Dortmund ist eine Fachmesse für industrielle Pumpen, Armaturen und Prozesstechnik, mit Besucherinnen und Besuchern aus Chemie, Pharma, Energie und Wasserwirtschaft. CP Pump Systems war mit einem 20 m² grossen Eckstand vertreten. Die beiden Standwände zeigten auf der einen Seite das Motiv ‹cleaner pumps, cleaner planet™›, auf der anderen die Kernbotschaft ‹Safety first: Magnetic driven pumps, hermetically sealed› mit einer Weltkarte der Standorte.»
    - «Zur Vorbereitung gehörten die Standplanung, drei Exponate, Broschüren und Explosionszeichnungen auf Deutsch, Giveaways sowie der Versand über den Messespediteur, inklusive Einfuhr nach Deutschland. Im Vorfeld luden E-Mail-Banner zum kostenlosen Messeticket ein, LinkedIn-Beiträge kündigten den Auftritt an. Kundinnen und Kunden konnten sich vorab für ein Geschenk anmelden und es am Stand abholen. Ein Messebriefing und das Lead-Formular bereiteten das Standteam vor.»
    - *Meine Aufgaben:* Standbuchung · Standdesign · Standplanung · Exponate und Material · Versand · E-Mail-Banner · LinkedIn-Posts · Messebriefing · Lead-Formular
  - **Ton-Regel ✅ (Yana 04.10.2026, ersetzt die «wir»-Regel und die «ich»-Ausnahme):** Alle Messetexte (eigene und Partnermessen) durchgehend **neutral, aber lebendig**: kein «ich», kein «wir»; Messe, Stand, Auftritt oder CP Pump Systems als Subjekt; Passiv-Ketten vermeiden. Ausnahme: die Rubriken «Meine Rolle» und «Meine Aufgaben» sowie Über-mich-Texte sprechen bewusst in der Ich-Form, weil sie Yanas persönliche Leistung benennen. Yanas Rolle ist ohne Label erkennbar (Yana 04.10.2026: «muss man nicht labeln»): über die feste Zeile **«Meine Aufgaben»**; bei Messen, die sie allein umgesetzt hat, beginnt die Zeile mit **«Gesamtverantwortung»**, bei Team-Messen stehen nur ihre konkreten Beiträge.
  - **Gesamtverantwortung ✏️ (in «Meine Aufgaben», Vorschlag):** ACHEMA 2024, TPS Houston 2024, Petrochymia 2024, CRU 2025, Pétro+Chimie Le Havre 2025.
  - *Bilder ✅:* 4 Fotos vom Aufbautag (18.02.2025), Standdesign-Freigabe, E-Mail-Banner.
  - ✅ LinkedIn-Posts: schreibt Yana grundsätzlich selbst (gilt für alle Messen, Yana 04.10.2026).
- **Messe: The Fertilizer Show (TFS) Orlando 2025 ✏️** (Quelle: Drive «Messen/TFS Orlando 2025», alle Seiten und Unterordner gelesen; nicht verwendet: Budget, Preise, Rechnungen, Namen, Kontaktdaten, Passwörter)
  - *Kurz:* 8.–10. April 2025 · Orange County Convention Center, Orlando, Florida · Halle WA2, Stand 3014 · 600 sq ft (20 × 30 ft) Freifläche, nach allen vier Seiten offen · erste Teilnahme von CP
  - *Funde:* Briefing EN (über 2'500 Besucher, über 120 Aussteller, dreitägige Konferenz mit über 100 Referierenden; Vortrag eines CP-Verkäufers am 10. April über Pumpentechnik für eine nachhaltige, dekarbonisierte Düngemittelproduktion); Messe-Motto «Safety first: Magnetic driven pumps, hermetically sealed»; Selbstaufbau: Genehmigung als Self-Booth-Builder, Method Statement, Risk Assessment, Nachweis Brandschutz des Materials; Aufbau: Teppichfliesen (in den USA bestellt), Restore-Box (Standbox mit Birkenwald-Motiv «cleaner pumps, cleaner planet™»), Regale mit Material, Exponate MKP, MKPL, MKP-Bio, MKTP (Sumpfpumpe) mit Podesten, Prospektständer, Birken als Pflanzen; Logistik: Boxen aus dem Zwischenlager in Florida (nach TPS 2024) per US-Spediteur zur Messe, zusätzlich Sendung aus der Schweiz (MKTP, Prospektständer, Broschüren, Giveaways) über den Messespediteur, nach der Messe Boxen in ein neues Zwischenlager bei Houston (für die nächsten US-Messen), Exponate zurück in die Schweiz; Marketing: 3 Mailings (MKP-Sicherheitsfunktionen, MKTP inkl. Heizmantel, MKTP), Geschenk-Registrierung (SIGG-Flasche, Badetuch, Fussball), Anzeige im Messekatalog A5 («Swiss Pump Technology for Sustainable and Decarbonized Fertilizer Production»), E-Mail-Banner mit Gratis-Ticket, Anzeige in der E-Mail-Signatur, Katalogeintrag (auf Düngemittelbranche angepasst), Lead-Formular, Namensschilder, CP-Kleidung; Fotos vom Stand (April 2025, auf einem Foto Personen → unscharf machen oder nicht verwenden); Fotos der Restore-Box/Transportkiste.
  - ✅ Zeitraum Jan.–März 2025 = Phase mit Leiterin: Gestaltung von Yana, Organisation gemeinsam (Yana unterstützte bei allem).
  - *Text ✏️ (neutraler Ton):*
    - «The Fertilizer Show in Orlando bringt die gesamte Lieferkette der Düngemittelproduktion zusammen: über 120 Aussteller, mehr als 2'500 Fachbesucherinnen und -besucher und eine dreitägige Konferenz. 2025 war CP Pump Systems zum ersten Mal dabei, mit einer 600 sq ft grossen Freifläche, nach allen vier Seiten offen. Der Verkauf in den USA hielt zudem einen Vortrag über Pumpentechnik für eine nachhaltige, dekarbonisierte Düngemittelproduktion.»
    - «Der Stand entstand im Selbstaufbau. Dafür brauchte es eine Genehmigung des Veranstalters, ein Method Statement, eine Risikobeurteilung und den Brandschutznachweis für das Standmaterial. Das Herzstück war das Messesystem für die USA: Die Standbox mit dem Birkenwald-Motiv und die Möbelbox kamen aus dem Zwischenlager in Florida, ergänzt durch eine Sendung aus der Schweiz mit Exponaten, Broschüren und Giveaways. Nach der Messe blieb das System in den USA eingelagert, bereit für die nächsten Messen.»
    - «Der Auftritt war auf die Branche zugeschnitten: eine Anzeige im Messekatalog unter dem Titel ‹Swiss Pump Technology for Sustainable and Decarbonized Fertilizer Production›, ein angepasster Katalogeintrag, E-Mail-Banner mit Gratis-Ticket und drei Mailings. Registrierte Kundinnen und Kunden konnten ihr Geschenk am Stand abholen. Ein Messebriefing und das Lead-Formular bereiteten das Team auf Aufbau und Ablauf vor.»
    - *Meine Aufgaben ✅ (Yana 04.10.2026: «Design war immer ich, und sie habe ich bei allem unterstützt»):* Gestaltung: Anzeige im Messekatalog · E-Mail-Banner · Mailings · Design der Standbox (Rundum-Design) · Messebriefing (selbst erstellt, Yana 04.10.2026) · Mitarbeit bei Planung, Logistik und Anmeldung
  - *Bilder ✅ (Vorschlag):* Stand mit Standbox (IMG_2152, IMG_2130), Prospektständer mit Birke (IMG_2137), Anzeige A5, E-Mail-Banner.
- **Messe: Leuna-Dialog 2025 ✏️** (Quelle: Drive «Messen/Leuna Dialog, April 2025.», alle Seiten gelesen; nicht verwendet: Preise, Namen, Kundennamen, Kontaktdaten)
  - *Kurz:* 24. April 2025 · cCe Kulturhaus Leuna (Sachsen-Anhalt), Standortmesse am Chemiestandort Leuna · Stand D13, Komplettstand 9 m² · Auftritt der CP Pumpen GmbH (deutsche Tochter)
  - *Funde:* Anmeldung Sept. 2024 (durch Leiterin), Auftragsbestätigung Dez. 2024 inkl. ganzseitiger Farbanzeige A5 im Messekatalog; Shipment-Liste März 2025 (Kürzel SAB): 2 Exponate MKP (u. a. Schnittmodell mit Heizmantel) auf Podest, 3 Roll-ups (Corporate DE, MKP EN, MKP-Schnittzeichnung DE), Prospektständer, Sortimentsbroschüre DE, Giveaways (SIGG-Flasche, Lunchbox, Kägi, Massstab, Golfbälle); Abstimmung mit dem Verkauf Deutschland per E-Mail; Feedback-Mail des Verkaufs nach der Messe: 21 Gespräche, davon 3 Interessenten, 5 bestehende Kunden, 2 Partner; Vormittag sehr gut besucht; 1 Foto (leerer Stand vor dem Aufbau, 23.04.2025).
  - ✅ Yanas Anteil geklärt: Vorbereitung und Versand wie bei den anderen Messen.
  - *Darstellung ✅ (Yana 04.10.2026):* nur kurz als Info erwähnen, nicht im Detail; professionell, nicht abwertend («regional», «klein» vermeiden); keine Zahlen (keine Gesprächszahl).
  - *Text ✏️ (Version 4, neutraler Ton, ohne Zahlen):*
    - «Der Leuna-Dialog ist die Standortmesse des Chemiestandorts Leuna in Mitteldeutschland. Hier treffen sich Unternehmen, die am Standort produzieren, mit ihren Lieferanten und Dienstleistern. Die Messe bietet die Gelegenheit, bestehende Kunden in der Region persönlich zu treffen und neue Kontakte in der Chemieindustrie zu knüpfen.»
    - «Die deutsche Gesellschaft, die CP Pumpen GmbH, präsentierte sich mit einem Komplettstand. Im Mittelpunkt standen zwei Magnetkupplungspumpen, darunter ein Schnittmodell mit Heizmantel, das den Aufbau der Pumpe sichtbar macht. Drei Roll-ups zum Unternehmen, zur Pumpenbaureihe MKP und zu ihrer Schnittzeichnung bildeten die Rückwand des Stands. Ergänzt wurde der Auftritt durch einen Prospektständer mit der Sortimentsbroschüre und Giveaways wie Kägi-Schokolade.»
    - «Bereits im Vorfeld war CP mit einer ganzseitigen Anzeige im Messekatalog präsent, der am Standort und darüber hinaus verteilt wird. Material, Exponate und Standausstattung entstanden in Abstimmung mit dem Verkauf in Deutschland und reisten aus der Schweiz an die Messe.»
  - *Meine Aufgaben ✅ (Yana 04.10.2026: «wie immer»):* Vorbereitung · Exponate und Material · Versand · Anzeige im Messekatalog · Abstimmung mit dem Verkauf
  - *Bilder:* ❓ nur 1 Foto vom leeren Stand → eher nicht verwenden; Alternative: Anzeige (falls vorhanden) oder nur Eintrag in der Liste/Karte ohne Bild.
- **Messe: CRU Sulphur + Sulphuric Acid Expoconference 2025 ✏️** (Quelle: Drive «Messen/CRU Sulphur + Sulphuric Acid in The Woodlands», alle Seiten und Unterordner gelesen; nicht verwendet: Preise, Budget, Rechnungen, Namen, Kontaktdaten; Tabellenblatt «Verzehrmaterial ACHEMA 2022» in der Shipment-Datei gehört nicht dazu)
  - *Kurz:* 3.–5. November 2025 · The Woodlands, Texas (bei Houston) · 41. Ausgabe der Konferenz mit Fachausstellung für die Schwefel- und Schwefelsäureindustrie · über 500 internationale Teilnehmende (laut Veranstalter) · Stand 37, 3 × 2 m
  - *Funde:* Buchung Dez. 2024 (Leiterin); Übergabe der Planung an Yana per Mail 15.04.2025 (Abstract-Möglichkeit, Rückwand/Banner klären, Daten für das «Sulphur Magazine», Exponate, Print und Gadgets im US-Format, Anmeldung auf CP Pumps Inc. prüfen); Checkliste 2025 mit Kürzel YAS bei: Rückwand/Roll-up-Layout und Produktion («Sulphuric Design», MKP mit Heizmantel), Briefing, Lead-Formular, Import Leads, Mailing-Vorlagen, Geschenk-Formulare, Marketingplan (3 Mailings), E-Mail-Signatur-Anzeige, Exponate MKP und Heizmantel, Kägi/Biberli/CP-Gummibärchen, Namensschilder, Budget vs. effektive Kosten; Shipment: Exponat, Möbel (Bartische, Barhocker, Hocker, Tische, Kabine) aus dem US-Lager, englische Broschüren in der Schweiz gedruckt, Giveaways, Roll-up «Sulphur», Tischtuch; Fotos: Roll-up «Keep Your Molten Sulphur Flowing – Leak-Free and at the Perfect Temperature» (gelbe Schwefel-Grafik), MKP mit Heizmantel auf CP-Podest mit Infotafel, Tisch mit CP-Tischtuch; auf mehreren Fotos Personen.
  - *Text ✏️ (neutraler Ton):*
    - «Die CRU Sulphur + Sulphuric Acid Expoconference ist der internationale Treffpunkt der Schwefel- und Schwefelsäureindustrie: eine Fachkonferenz mit begleitender Ausstellung, 2025 bereits zum 41. Mal und mit über 500 Teilnehmenden aus aller Welt. CP Pump Systems nutzte die Gelegenheit, eine spezifische Anwendung in den Mittelpunkt zu stellen: das sichere Fördern von flüssigem Schwefel.»
    - «Darauf war der ganze Auftritt ausgerichtet. Die Ausstellung war als Tischmesse mit kompakten Ständen angelegt, deshalb entstand eigens für diesen Anlass ein Roll-up: Unter dem Titel ‹Keep Your Molten Sulphur Flowing – Leak-Free and at the Perfect Temperature› stellte es die beheizten Magnetkupplungspumpen vor, die den Schwefel auf der richtigen Temperatur halten. Als Exponat diente eine Magnetkupplungspumpe mit Heizmantel. Das Mobiliar kam aus dem Lager in den USA; die englischen Broschüren wurden in der Schweiz gedruckt und reisten zusammen mit Giveaways und Schweizer Spezialitäten an die Messe.»
    - «Im Vorfeld luden drei Mailings zum Besuch ein, verbunden mit einem Geschenk zum Abholen am Stand; zusätzlich warb die E-Mail-Signatur für die Messe. Ein Messebriefing und das Lead-Formular bereiteten das Team vor Ort vor.»
    - *Meine Aufgaben ✏️ (laut Checkliste YAS, Planung ab April 2025 übernommen):* Gesamtverantwortung · Planung und Organisation · Design und Produktion des Roll-ups (eigens für diese Tischmesse) · Exponate · Mailings und Geschenk-Ablauf · E-Mail-Signatur-Anzeige · Messebriefing · Lead-Formular und Import der Leads · Namensschilder · Budgetkontrolle
  - ✅ **Regel (Yana 04.10.2026, gilt für alle Messen):** Messebriefing und Lead-Formular erstellt immer Yana; das Formular gibt sie dem Team mit oder das Team druckt es aus. Im Text aktiv nennen (z. B. «Ein Messebriefing und das Lead-Formular bereiteten das Team vor»); Yanas Urheberschaft steht in «Meine Aufgaben» (neutraler Ton, siehe Ton-Regel).
  - *Bilder (Vorschlag):* MKP mit Heizmantel auf Podest (IMG_0079), Exponat mit Halle (IMG_0082); Fotos mit Roll-up zeigen Personen → nur unscharf oder zugeschnitten.
- **Messe: LH Pétro+Chimie Le Havre 2025 ✏️** (Quelle: Drive «Messen/Petro-Chimie Le Havre 2025», alle Seiten und Unterordner gelesen; nicht verwendet: Preise, Budget, Rechnungen, Namen, Kontaktdaten)
  - *Kurz:* 19.–20. November 2025 · Carré des Docks, Le Havre (Normandie) · Stand D17-E20 · 18 m², drei Seiten offen
  - *Funde:* Buchung Feb. 2025 (Leiterin); Checkliste mit Kürzel YAS bei fast allen Vorbereitungspunkten (Standfläche und Pakete, Möbel, Rückwand-Layout und Produktion, Strom, Teppich, Badges, Parkkarten, Namensschilder, Lead-Formular, Briefing, Werbemittel, Online-Werbung, E-Mail-Signatur für das Team Frankreich, Exponate, Broschüren, Giveaways, Versand, Budget vs. effektive Kosten); Motto laut Checkliste «même design comme Martigues» (Design von Petrochymia 2024 weiterentwickelt); Kommunikationspaket (Farbanzeige im Katalog, Standschild mit Logo, 2 Web-Banner, Firmenporträt auf der Messe-Website); Design Messewände (Okt. 2025): «La sécurité avant tout : Pompes étanches à entraînements magnétiques», Weltkarte über mehrere Paneele, Pumpen-Wasser-Motiv, Swiss Made; Blenden («Bandeau de façade») mit «cleaner pumps, cleaner planet™»; Exponate MKP, MKPL, MKTP und zwei MKP-Bio auf einem Podest, Kabine; Broschüren, Explosionszeichnungen und Factsheets auf Französisch; Logistik über den Logistikpartner des Veranstalters (Lager in Louvres bei Paris, Zwischenlagerung, Transport und Entladen vor Ort, Lagerung des Leerguts, Rücktransport), wie bei Petrochymia 2024; Messebriefing auf Französisch (Ziel: «un stand bien rangé qui mette en valeur la qualité suisse»); Lead-Formular FR; 5 Fotos vom Stand mit Besuchern (20.11.2025).
  - *Text ✏️ (neutraler Ton):*
    - «Die LH Pétro+Chimie in Le Havre ist eine Fachmesse für Chemie, Petrochemie und die Energien der Zukunft, im Herzen des französischen Industrie- und Hafengebiets an der Seine-Mündung. Zwei Tage lang treffen sich hier Industrieunternehmen, Dienstleister und Zulieferer aus Chemie, Raffinerie, Energie und Logistik zu Konferenzen, B2B-Gesprächen und Produktpräsentationen.» *(Quelle: Messebriefing)*
    - «CP Pump Systems war mit einem 18 m² grossen Stand vertreten, nach drei Seiten offen. Das Standdesign führte den Auftritt der Petrochymia 2024 weiter: Die Rückwände tragen die französische Kernbotschaft ‹La sécurité avant tout : Pompes étanches à entraînements magnétiques›, eine Weltkarte der Standorte und das Motiv ‹cleaner pumps, cleaner planet™›, das sich auch auf den Blenden über dem Stand wiederfindet. Zu sehen waren fünf Exponate, darunter zwei Pumpen der Baureihe MKP-Bio auf einem gemeinsamen Podest.»
    - «Broschüren, Explosionszeichnungen und Factsheets lagen auf Französisch bereit. Die Logistik lief, wie schon in Martigues, über den Logistikpartner des Veranstalters: zuerst in sein Lager bei Paris, von dort an die Messe und nach Messeschluss auf demselben Weg zurück. Über das Kommunikationspaket des Veranstalters war CP zudem im Messekatalog und auf der Messe-Website präsent, mit eigens gestalteter Anzeige und eigenen Web-Bannern. Ein französisches Messebriefing und das Lead-Formular bereiteten das Team vor Ort vor.»
  - *Meine Aufgaben ✏️ (laut Checkliste YAS):* Gesamtverantwortung · Standplanung und Buchungen · Standdesign (Rückwände und Blenden) · Exponate, Broschüren und Giveaways · Versand und Logistik · Gestaltung von Katalog-Anzeige und Web-Bannern · E-Mail-Signatur · Messebriefing (FR) · Lead-Formular · Budgetkontrolle
  - ✅ Anzeige im Katalog und Web-Banner von Yana gestaltet (Yana 04.10.2026).
  - *Bilder (Vorschlag):* Standdesign-Entwurf (PDF), Stand-Foto 3.jpg oder 1.jpg (Personen unscharf machen).
- **Messe: FLA – Fertilizer Latino Americano 2026 ✏️** (Quelle: Drive «Messen/FLA – Fertilizer Latino Americano», alle Seiten und Unterordner gelesen; nicht verwendet: Preise, Verträge, Teilnehmerliste, Namen, Zugangscodes, Ausblick 2027)
  - *Kurz:* 26.–28. Januar 2026 · Miami, Florida · Doppelstand 22/23 · gemeinsam veranstaltet von Argus Media und CRU · über 900 Teilnehmende, über 400 Unternehmen, 56 Länder (laut Recap des US-Verkaufs)
  - *Funde:* Phase 2 (mit Leitung, Kürzel NIM): Buchung, Briefing-Versand und Lead-Formular-Versand laut Checkliste über die Leiterin; YAS bei E-Mail-Signatur-Anzeige und Social Media (Bilder vom US-Team an YAS). Druckdaten Booth A und B (Dez. 2025, InDesign): Rückwand mit Birkenwald-Motiv über den Doppelstand; Roll-up «Keep Your Molten Sulphur Flowing» von der CRU 2025 wiederverwendet; Standmaterial aus der US-Messebox (Teppich, Strom, Namensschilder, Broschüren, Giveaways, Kaffeemaschine); Exponate 2× MKP + MKPL; TV-Bildschirm mit CP-Videos; Briefing EN (Fokus: Markttrends, Stickstoff, Phosphat, Kali, Biostimulanzien, Dekarbonisierung; Bildanfrage fürs Team für Social Media); E-Mail-Banner (CRU/Argus, Gelb-Akzent wie Sulphur); Social-Media-Grafik «Meet us at Fertilizer Latino Americano» + Posttexte vor, während und nach der Messe; Recap des US-Verkaufs: Leads aus u. a. USA, Brasilien, Kolumbien, Spanien, Peru, Indien, Kanada, Türkei, Mexiko; Fotos vom Stand (teilweise mit Personen).
  - *Text ✏️ (neutraler Ton):*
    - «Die Fertilizer Latino Americano ist der jährliche Branchentreff der Düngemittelindustrie mit Fokus auf Lateinamerika. 2026 fand sie in Miami statt, gemeinsam veranstaltet von Argus Media und CRU, mit über 900 Teilnehmenden aus 400 Unternehmen und 56 Ländern: Produzenten, Händler, Distributoren und Dienstleister aus der gesamten Lieferkette.»
    - «CP Pump Systems war mit einem Doppelstand vertreten, aufgebaut auf dem Messesystem für die USA: Teppich, Technik, Broschüren und Giveaways kamen aus der Messebox. Eine eigens gestaltete Rückwand mit Birkenwald-Motiv zog sich über beide Standflächen, ergänzt durch das Roll-up zu den beheizten Pumpen für flüssigen Schwefel. Auf einem Bildschirm liefen Videos zu den Pumpenbaureihen, als Exponate standen Magnetkupplungspumpen der Baureihen MKP und MKPL bereit.»
    - «Die Kommunikation lief über mehrere Kanäle: E-Mail-Banner und eine Anzeige in der E-Mail-Signatur im Vorfeld, Social-Media-Beiträge vor, während und nach der Messe, mit Bildern, die das Team vor Ort lieferte.»
  - *Meine Aufgaben ✅ (Yana 04.10.2026):* Design der Rückwand für den Doppelstand · E-Mail-Banner · E-Mail-Signatur-Anzeige · Social-Media-Grafik und Beiträge (vorher, währenddessen, Rückblick) · Messebriefing (von Yana erstellt; verschickt hat es die Leiterin)
  - ✅ **Regel (Yana 04.10.2026, gilt für alle Messen):** Wie Leads erfasst werden, nicht ausführen. Ablauf: Verkäufer füllen das Lead-Formular auf Papier aus, es wird gescannt und im CRM abgelegt; an manchen Messen zusätzlich über das Scan-System des Veranstalters. Im Text nur «Lead-Formular» als Yanas Arbeit nennen; Erfassungsweg nur erwähnen, wenn etwas ungewöhnlich war.
  - ✅ **Regel (Yana 04.10.2026, gilt für alle Messen):** Gespräche, Kontakte und Leads nicht beiläufig erwähnen; die Gespräche führt der Verkauf, nicht Yana. Nur erwähnen, wenn daraus nachweislich feste Kunden entstanden sind.
  - *Bilder (Vorschlag):* Stand mit Birkenwand und Exponat (Image 7/8, Personen unscharf), Social-Media-Grafik, E-Mail-Banner.
- **Messe: Pumps & Valves Dortmund 2026 ✏️** (Quelle: Drive «Messen/Pumps & Valves Dortmund 2026», alle Seiten und Unterordner gelesen; nicht verwendet: Rechnungen, Namen, Ticket-Links, Kontaktdaten)
  - *Kurz:* 25.–26. Februar 2026 · Dortmund · Halle 7, Stand 7238 · 6 × 3 m · parallel zur «maintenance Dortmund»
  - *Funde:* Phase 2 (Leiterin NIM: Buchung, Möbel, Versand mit Lager/Export); Standdesign von Yana (PSD/PNG Dez. 2025): Rückwand mit grossformatigem Anlagenfoto (Referenzprojekt eines Kunden: Tanklager für Lösemittel mit MKPL-Pumpen), Weltkarte (neu gestaltet, Dez. 2025), Swiss Made; Druckfreigabe beim Veranstalter (Dez. 2025); Standplanung (Grundriss mit Podesten, Exponaten, Tischen, Lesegeräten); Exponate MKP, MKPL, ET, MKTP; Podeste neu mit Türen und Schloss; Briefing DE (Fakten, Personalplanung, Ausstellerabend, Referenzprojekt mit Erklärung für das Team, Pflege der Podeste, Lead-Erfassung per Badge-Scan mit App, Fragen aus dem Lead-Formular in die App übernommen, SMS-Benachrichtigung bei Check-in von Kunden mit Gratisticket, Dresscode, Catering, 20 vorbereitete Kundensäckli); E-Mail-Banner mit Gratis-Ticket; E-Mail-Signatur (ab 09.12.2025, YAS+NIM); Social-Media-Grafik + Posttexte (YAS+FRJ); Namensschilder (YAS); Fotos vom Stand (25./26.02.2026, teilweise mit Personen).
  - *Text ✏️ (neutraler Ton):*
    - «Nach 2025 war CP Pump Systems auch im Februar 2026 an der Pumps & Valves in Dortmund, der Fachmesse für industrielle Pumpen, Armaturen und Prozesstechnik, diesmal mit einem neu gestalteten Stand: Die Rückwand zeigt ein grossformatiges Foto einer Industrieanlage, daneben die neu gestaltete Weltkarte der Standorte und das Swiss-Made-Zeichen.»
    - «Im Vorfeld luden E-Mail-Banner, eine Anzeige in der E-Mail-Signatur und Social-Media-Beiträge zum kostenlosen Messeticket ein. Vor Ort standen vier Exponate auf den CP-Podesten, die neu mit abschliessbaren Türen ausgestattet sind.»
    - «Das Messebriefing enthielt diesmal auch ein Referenzprojekt für die Gespräche am Stand: ein Tanklager für Lösemittel, in dem CP-Pumpen im Einsatz sind. Dazu kam wie immer das Lead-Formular.»
  - *Meine Aufgaben ✏️:* Standdesign (Rückwand, Weltkarte) · Standplanung · E-Mail-Banner · E-Mail-Signatur · Social-Media-Grafik und Beiträge · Messebriefing · Lead-Formular · Namensschilder
  - ✅ Anlagenfoto: Yana weiss nicht, ob es das Referenzprojekt zeigt → neutral als «Foto einer Industrieanlage» beschreiben. Kundenname nicht nennen.
  - *Bilder (Vorschlag):* Stand mit Rückwand und Weltkarte (IMG_6076_kopie), E-Mail-Banner.
- **Messe: DK Hub Global Dunkerque 2026 ✏️** (Quelle: Drive «Messen/DK Hub Global in Dunkerque», alle Seiten und Unterordner gelesen; nicht verwendet: Preise, Budget, Kontaktlisten, Leads, Namen)
  - *Kurz:* 20.–21. Mai 2026 · Kursaal, Dunkerque (Nordfrankreich, Grenze zu Benelux) · Stand C12 · drei Fachmessen unter einem Dach: Industrissime, Genead, Pharma+Agro
  - *Funde:* Phase 2 (YAS/NIM gemeinsam bei Buchung, Möbel, Rückwand, Versand; ELS = Kollegin Marketing für Material); Motto laut Checkliste: gleiches Design wie Pétro+Chimie + aktualisierte Weltkarte; Design Messewände (InDesign, April 2026) mit Weltkarte, Swiss Made, Blenden «cleaner pumps, cleaner planet™», Tür der Standkabine mit grossformatigem Anlagenfoto; Kommunikationspaket: ganzseitige Anzeige A5 im Katalog (FR: MKP, MKPL, MKTP mit Kurzbeschrieb, QR-Code), Web-Banner 1000×90 und 1000×400; E-Mail-Banner; Mailing mit Gratis-Tickets an Kontakte des französischen Verkaufs; Exponate MKP OH2 HT, MKPL, MKTP; Broschüren und Explosionszeichnungen auf Französisch; Logistik über den Logistikpartner des Veranstalters (wie Martigues/Le Havre); Briefing FR; Goodie-Bags am Eingang (2 × 60 Säckli mit Bleistift und Memory-Spiel, pro Messetag eine Kiste, damit Besucher beider Tage CP-Taschen durch die Messe tragen); Checklisten für die Rücknahme der Exponate; Fotos vom Stand (Mai 2026).
  - *Text ✏️ (neutraler Ton):*
    - «Der DK Hub Global vereint in Dunkerque drei Fachmessen unter einem Dach: Industrissime, Genead und Pharma+Agro. Er richtet sich an die Industrie in Nordfrankreich und den Benelux-Ländern, von Chemie und Energie bis zur Pharma- und Lebensmittelindustrie.»
    - «Das Standdesign führte den Auftritt der Pétro+Chimie weiter, mit aktualisierter Weltkarte der Standorte. Neu trug die Tür der Standkabine ein grossformatiges Anlagenfoto. Über das Kommunikationspaket des Veranstalters war CP mit einer ganzseitigen Anzeige im Katalog und mit Web-Bannern präsent; die französische Anzeige stellte die drei ausgestellten Pumpenbaureihen vor.»
    - «Eine besondere Aktion entstand im Marketingteam: Goodie-Bags direkt am Eingang. Pro Messetag stand eine Kiste mit 60 Säckli bereit, damit Besucherinnen und Besucher an beiden Tagen eine CP-Tasche durch die Messe trugen. Ein französisches Messebriefing bereitete das Standteam vor.»
  - *Meine Aufgaben ✏️:* Standdesign (Rückwände, Blenden, Kabinentür, Weltkarte) · Katalog-Anzeige und Web-Banner · E-Mail-Banner · E-Mail-Signatur · Messebriefing (FR) · Idee der Goodie-Bag-Aktion (gemeinsam im Team) · Mitarbeit bei Buchung, Möbeln und Versand
  - ✅ Goodie-Bags: gemeinsame Idee im Team (Yana 04.10.2026).
  - *Bilder (Vorschlag):* Stand mit Kabinentür und Weltkarte (IMG_20260519_135159), Katalog-Anzeige, E-Mail-Banner.
- **Messe: ChemUK Birmingham 2026 ✏️** (Quelle: Drive «Messen/ChemUK in Birmingham», alle Seiten und Unterordner gelesen; nicht verwendet: Preise, Rechnungen, Namen, private Hinweise aus der Personalplanung, Konkurrenzanalyse-Details)
  - *Kurz:* 20.–21. Mai 2026 · NEC Birmingham, Halle 5 · Stand G60 · Process & Chemical Engineering Zone
  - *Funde:* Phase 2 (Leiterin NIM: Buchung, Aufbau, Versand; Verkauf UK: Mailing mit Gratisticket); Ziel laut Checkliste: Präsenz im britischen Markt erhöhen; Motto-Input: «Different solutions, one partner» (Chemie, Pharma, Bio); Konkurrenzanalyse UK (Dez. 2025: Hersteller, Distributoren, Dosiersysteme; Fazit zu Mag-Drive-Wettbewerb und Materialkompetenz); Design Rückwand 6 m und Blenden 5 m/6 m (April 2026) mit Weltkarte, Swiss Made, Claim zur sichersten und effizientesten Chemiepumpe; Anzeige 189 × 132 mm (EN: «Swiss made», «Low maintenance», «cleaner pumps, cleaner planet™»); Eintrag für die Show News (Titel «World's most secure and most efficient chemical pumps», Firmenbeschrieb EN); E-Mail-Banner; E-Mail-Signatur und organischer Social-Media-Post (YAS); Exponate: 2 × MKP, 2 × MKP-Bio, MKPL, EB, ET; Logistik über den Messespediteur direkt an den Stand; Briefing DE mit Lead-Erfassung per App (Fragen aus dem Lead-Formular); Fotos vom Stand (20.05.2026).
  - *Text ✏️ (neutraler Ton):*
    - «Die ChemUK im NEC Birmingham ist die Fachmesse der britischen Chemie- und Prozessindustrie, mit Schwerpunkten von Prozessinnovation und Green Chemistry bis zu Sicherheit, Compliance und Digitalisierung. 2026 stellte CP Pump Systems dort aus, mit dem Ziel, die Präsenz im britischen Markt zu stärken.»
    - «Zur Vorbereitung gehörte eine Analyse der Aussteller: Welche Hersteller und Distributoren sind vor Ort, und wo stehen sie im Vergleich zu CP? Der Stand in der Process & Chemical Engineering Zone erhielt Rückwand und Blenden mit Weltkarte und Swiss-Made-Zeichen, dazu kam eine Anzeige mit den Kernargumenten Schweizer Qualität und geringer Wartungsaufwand. Zu sehen waren sieben Exponate aus fünf Baureihen, von der Magnetkupplungspumpe bis zur Pumpe für Bio- und Pharmaanwendungen.»
    - «Im Vorfeld machten E-Mail-Banner, E-Mail-Signatur, ein Eintrag in den Show News und ein Social-Media-Beitrag die Teilnahme bekannt. Messebriefing und Lead-Formular bereiteten das Team vor.»
  - *Meine Aufgaben ✏️:* Standdesign (Rückwand, Blenden) · Anzeige · E-Mail-Banner · E-Mail-Signatur · Social-Media-Beitrag · Messebriefing · Lead-Formular
  - ✅ Konkurrenzanalyse nicht von Yana (bleibt neutral im Text, nicht in «Meine Aufgaben»).
  - *Bilder (Vorschlag):* Stand mit Rückwand und Exponaten (IMG_8299), Anzeige, E-Mail-Banner.
- **Messe: ChemE Show by ACHEMA Houston 2026 ✏️** (Quelle: Drive «Messen/ChemE by ACHEMA», alle Seiten und Unterordner gelesen, Fotos über Vorschaubilder geprüft; nicht verwendet: Lead-Liste, Rechnung/Bestellung, Hotelreservation, Preise, Namen, Badges)
  - *Kurz:* 9.–10. Juni 2026 · George R. Brown Convention Center, Houston, Exhibit Hall A3 · Booth 507 · Standardstand 10' × 10'
  - *Funde:* Phase 2 (Leiterin NIM: Anmeldung, Firmeneintrag im Messeprogramm, 50 Wörter EN); neue jährliche Veranstaltung, Partnerschaft von Gulf Energy Information und DECHEMA (Veranstalter der ACHEMA), Teil des ACHEMA-Ökosystems (eigenständige US-Ausgaben 2026 und 2028, Networking-Track an der ACHEMA 2027); Zielgruppe: Chemie-, Pharma- und biobasierte Wertschöpfungskette in Nordamerika; Schwerpunkte Verfahrenstechnik und Biotech, Downstream, Nachhaltigkeit und Wasserstoff, Prozessoptimierung und digitale Transformation; Briefing EN (1.6.2026, 17 Seiten): Fakten zur Messe, Hallenplan mit Standort, Ausstellerliste, Auf- und Abbauzeiten, Programm beider Tage, Standausstattung, Lieferadresse des Messespediteurs, Anleitung zur Lead-App (Cvent LeadCapture) mit eigenen Qualifizierungsfragen (Branche, Medium, Produkte, To-dos), überarbeitetes Lead-Formular mit sechs Anwendungsbereichen, Dresscode, Verpflegung, Giveaways aus dem Lager in Houston; Promotionspaket des Veranstalters (Grafik, Social-Media-Text, Rabattcode) → nicht von CP gestaltet; Fotos: Roll-up «Keep Your Molten Sulphur Flowing» (Design Yana, von der CRU 2025), drei weisse CP-Podeste mit Logo (bestehende Podeste, lange vor dieser Messe hergestellt; Yana 04.10.2026 → gehört in die Kategorie Messematerial, nicht in diesen Eintrag), «cleaner pumps, cleaner planet™» und Prospektfach, Exponate: Schnittmodell, Pumpe in Hygieneausführung auf Gestell, blaue Prozesspumpe, CP-Prospektständer.
  - *Text ✏️ (neutraler Ton):*
    - «Die ChemE Show in Houston ist eine neue, jährliche Fachmesse für die Chemie-, Pharma- und biobasierte Industrie Nordamerikas, entstanden aus einer Partnerschaft von Gulf Energy Information und DECHEMA, dem Veranstalter der ACHEMA. Im Juni 2026 war CP Pump Systems mit einem eigenen Stand im George R. Brown Convention Center vertreten und mit einem Firmeneintrag im Messeprogramm präsent.»
    - «Der kompakte Stand setzte auf Elemente, die sich bereits bewährt hatten: Das Roll-up für geschmolzenen Schwefel aus der CRU-Konferenz kam erneut zum Einsatz. Auf den CP-Podesten standen ein Schnittmodell, eine Pumpe in Hygieneausführung und eine Prozesspumpe, ergänzt durch den Prospektständer. Die Giveaways kamen aus dem Lager in den USA.»
    - «Ein englisches Messebriefing bereitete das Team vor Ort vor: von den Fakten zur Messe über Hallenplan, Ausstellerliste und Programm bis zu Standausstattung, Dresscode und Giveaways. Dazu gehörte das überarbeitete Lead-Formular, neu mit sechs Anwendungsbereichen.»
  - *Meine Aufgaben ✏️:* Messebriefing (EN) · Lead-Formular (überarbeitet) · Roll-up (Design, wiederverwendet)
  - ✅ **Regel (Yana 04.10.2026, gilt für alle Messen):** Jede Messe bekommt einen eigenen Eintrag, auch kommende, ausser Yana sagt ausdrücklich «auslassen». Ordner immer ganz auswerten und alles zeigen, was Yana beigetragen hat (z. B. wiederverwendete eigene Designs, Briefing-Inhalte, Lead-Formular), nicht nur das Offensichtliche.
  - ✅ Einladungsbanner «Join us at ChemE Show 26» stammt vom Veranstalter (Yana 04.10.2026) → nicht als eigene Arbeit, nicht als Bild.
  - *Bilder (Vorschlag):* Stand mit Roll-up, Podesten und Schnittmodell (Image (14) oder (16); Personen unkenntlich machen oder zuschneiden), Podest mit Prozesspumpe und Prospektständer (Image (27)_kopie, ebenso).
- **Messe: CRU Sulphur + Sulphuric Acid Berlin 2026 ✏️ (bevorstehend)** (Quelle: Drive «Messen/Sulphur + Sulphuric Acid Berlin», alle Seiten und Unterordner gelesen; nicht verwendet: Preise, Rechnung, Offerte und Frachtetikett des Spediteurs, Hotel, Namen, Kontaktdaten)
  - *Kurz:* 3.–5. November 2026 · Estrel Berlin · Stand 60 · Tischstand 3 × 2 m · 42. Ausgabe
  - *Funde:* Phase 2 (Leiterin NIM: Buchung, Möbel, Strom, Teppich, Bestellung der Rückwand beim Standbauer, Klärung Rückwand/Möbel mit dem Veranstalter; Versand NIM + ALD); Briefing DE (23.9.2026): internationale Fachkonferenz mit Ausstellung, über 450 Teilnehmende aus 42 Ländern, rund 120 Produzenten; Fokus Schwefel- und Schwefelsäureindustrie (Produktion, Prozessoptimierung, Technologie, Equipment); für CP interessant wegen Produzenten, Anlagenbetreibern und Lösungsanbietern; Standpaket: Tisch mit weisser Tischdecke, zwei Stühle, Strom, 2,5 m hohe Rückwand aus drei Paneelen; Briefing-Inhalte: Fakten, Organisatorisches, Personalplanung, Ablauf, Lageplan, Programm, Standpaket, Standlayout, Pflegehinweise für die Podeste (neu mit Türen und Schloss, weisse Handschuhe, nur Wasser, künftig U-Blech als Kantenschutz), offizieller Spediteur, Parking, Kontakte, Lead-Formular, Dresscode, Catering (keine Snacks, da Tischmesse im Hotel), Kundengeschenke (vorbereitete Säckli), Bitte um Fotos für Social Media; Checkliste: YAS bei Rückwand-Layout und Produktion, E-Mail-Signatur-Anzeige, Online-Werbung und Social Media (eine Woche vorher und während der Messe); Design Rückwand (Sept. 2026): «Keep Your Molten Sulphur Flowing», Schnittbilder CP-Design (voll beheizte Heizkammer) im Vergleich zur konventionellen Bauweise (teilbeheizt, ungeheizte Stellen), Swiss Made, «cleaner pumps, cleaner planet™», gelbes Schwefel-Dreiecksmuster (vom Roll-up der CRU 2025 weitergeführt); E-Mail-Banner (Juli 2026, DE) mit Gratis-Ticket; Lead-Formular DE für diese Messe; Exponate: zwei MKP, eine MKTP; Giveaways (Notizbuch, Stift, Fruchtgummi, Tasche, Golfball, Multitool), Broschüren DE/EN, Büromaterialbox; Logistik über den offiziellen Spediteur, Leergut-Lagerung während der Messe.
  - *Text ✏️ (neutraler Ton):*
    - «Die CRU Sulphur + Sulphuric Acid ist eine internationale Fachkonferenz mit begleitender Ausstellung für die Schwefel- und Schwefelsäureindustrie. Im November 2026 findet sie zum 42. Mal statt, im Estrel Berlin, mit über 450 Teilnehmenden aus 42 Ländern, darunter rund 120 Produzenten. Nach der Teilnahme in The Woodlands 2025 ist CP Pump Systems auch in Berlin mit einem eigenen Stand vertreten.»
    - «Die Rückwand entwickelt das Design der CRU 2025 weiter: Unter dem Titel ‹Keep Your Molten Sulphur Flowing› zeigt sie im direkten Vergleich, wie die voll beheizte Heizkammer von CP den geschmolzenen Schwefel gleichmässig auf Temperatur hält, während konventionelle Bauweisen ungeheizte Stellen aufweisen. Dazu kommen das Swiss-Made-Zeichen und das gelbe Schwefelmuster, das bereits das Roll-up prägte. Gezeigt werden zwei Magnetkupplungspumpen der Baureihe MKP und eine MKTP.»
    - «Im Vorfeld laden ein E-Mail-Banner mit Gratis-Ticket und die E-Mail-Signatur zur Messe ein. Messebriefing und Lead-Formular bereiten das Team vor.»
  - *Meine Aufgaben ✏️:* Rückwand-Design · E-Mail-Banner · E-Mail-Signatur · Social Media · Messebriefing · Lead-Formular
  - *Bilder (Vorschlag):* Rückwand-Design (drei Paneele), E-Mail-Banner. Nach der Messe: Standfoto ergänzen.
- **Messe: The Fertilizer Show (TFS) Tampa 2026 ✏️ (bevorstehend)** (Quelle: Drive «Messen/TFS Tampa», alle Seiten und Unterordner gelesen; Checkliste-Excel nicht lesbar; nicht verwendet: Budget, Rechnungen, Preise, Lagerofferte, Versicherungsnachweise, Namen, Kontaktdaten)
  - *Kurz:* 18.–19. November 2026 · Tampa Convention Center, West Hall · Booth 1114 · Freifläche 20 × 20 ft (400 sq ft)
  - *Funde:* Phase 2 (Leiterin NIM: Gold-Sponsoring unterzeichnet, Standlayout 16.9.2026, Stromanschlüsse); Messe vom Frühling in den November verschoben (Notiz im Ordner); da wir die Anmeldung behielten, Upgrade zum Gold Sponsor: Firmenprofil bis 250 Wörter und Logo auf der Startseite der Messe; Briefing EN (Entwurf, Sept. 2026, Folien teils «noch anpassen»): Besucher (Produzenten, Ingenieure, Betrieb, Einkauf, Management), Ausstellung, zweispurige Konferenz (Effizienz, Innovation, Nachhaltigkeit, Agronomie), Hallen- und Standplan, Auf-/Abbau, Move-out-Checkliste, Selbstaufbau (Genehmigung als Self-Booth-Builder), Zwischenlager der Messeboxen (aktuell Orlando, Option Houston offeriert), Lead-Formular, Dresscode, Catering, Kundengeschenke aus dem US-Lager in Houston, Gold-Sponsoring, Bitte um Fotos für Social Media; Formulare des Veranstalters: Risk Assessment, Compulsory Booth Form, Booth Plans Inspection, Versicherungsnachweis; Standlayout: Kabinenbox, Pflanzen, Stehtische, Kaffee, Exponate; Unterordner «Restore Box» (Masse Transportkiste und Kabine, Datenblätter Plattenmaterial, Sicherheitsdatenblatt, Fotos, Feb. 2025) und «Health & Safety» (Aufbauanleitung des Stands, Masse); Fact Sheets EN (MKP, MKPL, MKP-Bio, MKTP); E-Mail-Banner EN (Juli 2026) mit «Free admission»; Lead-Formular EN mit neuen Fragen zum Einsatz von Magnetkupplungspumpen (eigene, CP oder andere Hersteller); Firmentext 50–100 Wörter (Aug. 2026); Exhibitor Spotlight (Antworten vom Verkauf, SIB) und Grafiken «New Exhibitor», «Exhibitor Spotlight», «We are exhibiting» → Vorlagen des Veranstalters, nicht von CP gestaltet.
  - *Text ✏️ (neutraler Ton):*
    - «The Fertilizer Show bringt die Lieferkette der Düngemittelproduktion zusammen: Produzenten, Ingenieure, Betrieb, Einkauf und Management, dazu eine zweispurige Konferenz zu Effizienz, Innovation, Nachhaltigkeit und Agronomie. Nach Orlando 2025 ist CP Pump Systems im November 2026 in Tampa erneut mit einem eigenen Stand vertreten. Ursprünglich war die Messe für den Frühling geplant; weil CP die Anmeldung trotz Verschiebung beibehielt, folgte das Upgrade zum Gold Sponsor, mit erweitertem Firmenprofil und Logo auf der Startseite der Messe.»
    - «Der 400 sq ft grosse Stand entsteht wieder im Selbstaufbau, mit Genehmigung als Self-Booth-Builder, Risikobeurteilung und Abnahme der Standpläne. Dabei kommt erneut das Messesystem für die USA zum Einsatz, das zwischen den Messen in den USA lagert.»
    - «Im Vorfeld lädt ein E-Mail-Banner zum kostenlosen Messebesuch ein. Ein englisches Messebriefing und das Lead-Formular bereiten das Team vor.»
  - *Meine Aufgaben ✏️:* E-Mail-Banner · Messebriefing (EN) · Lead-Formular
  - ✅ (Yana 04.10.2026): Lagerort nicht erwähnen. Vorlagen des Veranstalters nicht verwenden. Firmentext (50–100 Wörter) bestand bereits, nicht von Yana.
  - *Bilder (Vorschlag):* E-Mail-Banner. Nach der Messe: Standfoto ergänzen.
- **Messe: Petrochymia Martigues 2026 ✏️ (bevorstehend)** (Quelle: Drive «Messen/Petrochymia 2026», alle Seiten und Unterordner gelesen; InDesign-Dateien nur als PDF geprüft; nicht verwendet: Preise, Rechnungen, Hotelreservation, AGB, Namen, Kontaktdaten)
  - *Kurz:* 25.–26. November 2026 · La Halle de Martigues · Stand B4-C3 · 18 m², nach drei Seiten offen · 5. Ausgabe
  - *Funde:* Phase 2 (Bestellung Dez. 2025 durch Leiterin; Checkliste FR: vieles «same as DK Hub», Verkauf FR mit Aufbau-Verantwortung; Büromaterial durch Team FR); Messe laut Veranstalter: Chemie, Petrochemie, Raffinerie, Oil & Gas, Offshore, Hafen; Schwerpunkte Dekarbonisierung, Umwelt, Sicherheit; im «Triangle d'Or de la Chimie» an der Étang de Berre, grösste Industriezone Frankreichs; Kommunikationspaket: ganzseitige Farbanzeige im Katalog, Standschild mit Logo, zwei Web-Banner (1000 × 90 und 1000 × 400), Firmenporträt auf der Messe-Website; Design (Juli–Sept. 2026): Messewände mit grossformatigem Anlagenfoto, Kernbotschaft «Les pompes chimiques les plus sûres et les plus efficaces au monde», Weltkarte mit allen Standorten und Partnern (u. a. Frankreich, Deutschland, Schweiz, Spanien, USA, Norwegen, Korea, Singapur, China, Indien, Thailand), Swiss Made; Varianten mit und ohne Kabinentür; Blenden 3 m und 6 m mit «cleaner pumps, cleaner planet™»; Anzeige A5 (FR): Firmenporträt und vier Baureihen (MKP, MKP-Bio, MKPL, MSKPP); Web-Banner mit Standnummer und Swiss Made; E-Mail-Banner (FR) mit Gratis-Eintritt; Sammelbanner «Nos prochains salons professionnels» (Sept. 2026, FR) für CRU, TFS, Petrochymia und Industrial Expo; Bestellung des Messematerials beim Verkauf FR (Broschüren und Explosionszeichnungen FR, Factsheet, Prospektständer, Giveaways); Mietmöbel; Marketplace pourlindustrie.com des Veranstalters (bis fünf Produktinfos mit Fotos; Ordner mit Produktbildern MKP, MKP-S, MKPL, MKP-Bio, ET).
  - *Text ✏️ (neutraler Ton):*
    - «Die Petrochymia in Martigues liegt mitten im ‹Triangle d'Or de la Chimie› an der Étang de Berre, der grössten Industriezone Frankreichs. Die Fachmesse richtet sich an Chemie, Petrochemie, Raffinerie, Oil & Gas und Offshore, mit den Schwerpunkten Dekarbonisierung, Umwelt und Sicherheit. Nach 2024 ist CP Pump Systems im November 2026 wieder dabei, mit einem 18 m² grossen Stand, nach drei Seiten offen.»
    - «Der Stand entwickelt den Auftritt von Le Havre 2025 und Dunkerque 2026 weiter: ein grossformatiges Anlagenfoto, die Kernbotschaft ‹Les pompes chimiques les plus sûres et les plus efficaces au monde›, eine Weltkarte mit allen Standorten und Partnern sowie das Swiss-Made-Zeichen. Die Blenden über dem Stand tragen ‹cleaner pumps, cleaner planet™›.»
    - «Über das Kommunikationspaket des Veranstalters ist CP im Messekatalog und auf der Messe-Website präsent, mit einer Anzeige, die vier Baureihen vorstellt, und zwei Web-Bannern. Im Vorfeld lädt ein E-Mail-Banner zum kostenlosen Messebesuch ein; ein französisches Messebriefing und das Lead-Formular bereiten das Team vor.»
  - *Meine Aufgaben ✏️:* Standdesign (Messewände, Blenden) · Anzeige im Katalog · Web-Banner · E-Mail-Banner · Messebriefing (FR) · Lead-Formular
  - *Bilder (Vorschlag):* Messewände (Gesamtansicht), Anzeige A5, E-Mail-Banner. Nach der Messe: Standfoto ergänzen.
  - ✅ (Yana 04.10.2026): Marketplace pourlindustrie.com = bestehende Produktbilder mit Link auf unsere Website und QR-Code → nicht als eigene Leistung. Sammelbanner «alle kommenden Messen» ist von Yana, gehört aber nicht in diesen Eintrag → siehe Merkliste.
- **Messe: Dahej Industrial Expo 2026 ✏️ (bevorstehend)** (Quelle: Drive «Messen/Dahej Industrial Expo», alle Seiten gelesen; nicht verwendet: Budget, Zahlungsbelege, Preise, Pässe, Namen, Kontaktdaten)
  - *Kurz:* 16.–18. Dezember 2026 · Atali Ground, Dahej GIDC, Gujarat, Indien · Halle B, Stand B35 · 45 m² (9 × 5 m), Shell Scheme, nach drei Seiten offen · 6. Ausgabe
  - *Funde:* Phase 2 (Leiterin NIM: Buchung Mai 2026, Abklärungen mit dem Veranstalter zu Rückwand, Blende, Strom und Möbeln, Zusatzmöbel mit abschliessbaren Tischen, Sofas und TV, Versand über Export; Standpersonal aus dem Verkauf); Messe laut Veranstalter: «Gujarat's biggest industrial show», über 500 Aussteller, parallel CPTX (Chemical Pharma Tech Expo) und PVTX (Pumps Valves Tech Expo); Dahej als Teil der Petroleum, Chemicals and Petrochemicals Investment Region (PCPIR), Industriezentrum mit Chemie, Petrochemie, Engineering; Checkliste: YAS bei E-Mail-Signatur-Anzeige; Rückwand-Grafik und Branding der abschliessbaren Tische im CP-Design geplant (Anfragen laufen); Exponate MKP, MKP-S, MKPL; Giveaways, Broschüren und Explosionszeichnungen EN, Kaffeemaschine, Prospektständer, Büromaterialbox; E-Mail-Banner EN (Juli/Sept. 2026, schwarze und weisse Version) mit «Register now for free entry»; Grafiken «Stall B35» und «Exhibitor Spotlight» → Vorlagen des Veranstalters.
  - *Text ✏️ (neutraler Ton):*
    - «Die Dahej Industrial Expo findet in einem der am schnellsten wachsenden Industriezentren Indiens statt: Dahej in Gujarat ist Teil der Investitionsregion für Erdöl, Chemie und Petrochemie. Zur 6. Ausgabe im Dezember 2026 werden über 500 Aussteller erwartet, parallel laufen Fachmessen für Chemie und Pharma sowie für Pumpen und Armaturen. CP Pump Systems ist mit einem 45 m² grossen Stand vertreten, nach drei Seiten offen.»
    - «Rückwand und abschliessbare Tische tragen eine eigene Grafik im CP-Design. Gezeigt werden drei Magnetkupplungspumpen aus den Baureihen MKP, MKP-S und MKPL. Material, Exponate und Büromaterial reisen aus der Schweiz nach Indien, vor Ort betreut das Verkaufsteam den Stand.»
    - «Im Vorfeld laden ein E-Mail-Banner und die E-Mail-Signatur zum kostenlosen Messebesuch ein. Messebriefing und Lead-Formular bereiten das Team vor.»
  - *Meine Aufgaben ✏️:* E-Mail-Banner · E-Mail-Signatur · Rückwand-Design · Tisch-Branding · Messebriefing · Lead-Formular
  - ✅ (Yana 04.10.2026): Rückwand und Tisch-Branding gestaltet Yana.
  - *Bilder (Vorschlag):* E-Mail-Banner, Rückwand-Design (sobald fertig). Nach der Messe: Standfoto ergänzen.
- **Messe: Yncoris Hausmesse Hürth 2026 ✅ kein eigener Eintrag** (Yana 04.10.2026: überspringen) → nur in Liste/Karte.
- **Messe: Leuna-Dialog 2026 ✅ kein eigener Eintrag** (Yana 04.10.2026: zu wenig aussagekräftig) → nur in Liste/Karte.
- **Höhepunkt ACHEMA 2024 ✏️ (ausführlich, auf Wunsch von Yana):**
  - *Ausgangslage:* Die ACHEMA in Frankfurt ist eine der wichtigsten Messen der Prozessindustrie, 2024 mit rund 2'800 Ausstellern aus über 50 Nationen. CP Pump Systems war vom 10. bis 14. Juni mit einem 108 m² grossen Stand in Halle 8 vertreten, unter dem Motto «Sichere Pumpentechnik – zum Schutz von Menschen, Umwelt und Investition.»
  - *Ziel:* Bestehende Kunden an den Stand holen und die Beziehung pflegen, neue Kontakte gewinnen und zeigen, dass CP für jede Anwendung die passende Pumpe hat.
  - *Meine Aufgaben:* Gesamtverantwortung nach Übernahme des laufenden Projekts im Frühling 2024 · Überarbeitung der Planung · Gesamtkoordination bis zur Messe · Einladungskampagne · Geschenk-Ablauf · Infopanels · Giveaways · Hotel und Anreise · Versand von Exponaten und Material · Verpflegung am Stand · Messebriefing · Lead-Formular · Standteam vor Ort
  - *Hinweis im Text (neutral):* Standdesign, Standbau und Montage lagen bei einer Agentur.
  - *Idee und Vorgehen:* Eine Einladungskampagne sollte Kunden gezielt an den Stand bringen: Drei Mailings, ein Reminder und eine Dankesmail luden dazu ein, vorab ein Geschenk zu wählen und es am Stand persönlich abzuholen. Zur Wahl standen eine SIGG-Flasche, ein Badetuch und ein Fussball im CP-Stil, passend zur Fussball-EM in Deutschland, die am letzten Messetag begann. Vor Ort sorgten ein Buzzer Game, ein Wettbewerb um die schnellste Pumpenmontage, und eine Live-Demo für Gespräche. Schweizer Schokolade als Giveaway sowie Schweizer Fleisch und Käseplätzchen im Catering unterstrichen die Herkunft von CP.
  - *Umsetzung:* Mailings und Einladungsmanagement · Geschenk-Ablauf am Stand · Infopanels zu den Exponaten · Folie für den Buzzer-Tisch · Giveaways · Namensschilder und Dresscode · Hotel und Anreise für Standteam und Besuchende · Messebriefing mit Schichtplänen · Lead-Formular und Erfassung der Leads
  - *Ergebnis:* 📌 später (Zahlen von Yana)
  - *Seitenentwurf ✏️ v6 (06.10.2026, Yana: mehr Text):* Texte pro Kapitel ausgebaut (Einstieg mit Messefakten und Motto, Ziel, Einladung mit Geschenk, Stand mit vier Produktinseln, Buzzer und Live-Demo, Swissness im Catering, Briefing, neues Kapitel «Rückblick: Was ich mitnehme» aus dem Rückblick-Dokument). Datei `docs/entwuerfe/achema.html`.
  - *Seitenentwurf ✏️ v7 (06.10.2026, Yana: Rückblick raus, positiver, gleich grosse Bilder, Briefing zum Aufklappen):* Kapitel «Rückblick» entfernt (Lessons Learned werden nicht gezeigt). Texte positiver formuliert. Alle Bilder einer Reihe gleich gross. Titelbild neu: bearbeitetes Standfoto. Neu: Montagetisch im Test (Jan. 2024), Fussball in drei Schritten (Muster → Vorlage → Design), vier Info-Stelen plus Stele im Einsatz. Briefing als Tablet zum Anklicken mit Galerie aus fünf Seiten (Standplan, Ablauf Geschenk-Abholung, Dresscode, Verpflegung mit Swissness, Lead-Erfassung). Die Seiten sind aus dem Original nachgebaut, ohne Namen, Hotel und Schichtpläne. Offen: PDF-Export des Briefings von Yana, dann echte Seiten zeigen.
  - *Seitenentwurf ✏️ v8 (06.10.2026, Yana: Fussballbilder kleiner, Badetuch hervorheben, Mailings zeigen):* Neues Kapitel «Neue Werbeartikel für die Messe»: Fussball und Badetuch wurden für die ACHEMA neu gestaltet (laut Yana). Ball-Entstehung als kleine Vorschaubilder zum Anklicken. Badetuch-Fakten aus der Auftragsbestätigung (Mai 2024): Zwirnfrottier, 100 % Baumwolle, 100 × 180 cm, Logo in Hoch-Tief-Webung, Blau nahe Pantone 2935 C (Preise und Lieferant werden nicht genannt). Einladung: drei Mailings in drei Sprachen (laut Yana). Mailings in der Galerie: Mailing 1 DE «Willkommen zur ACHEMA 2024 in Frankfurt!» (CP-Code, Live-Demo mit fünf Sicherheitsfeatures, Gratis-Ticket; Upload Yana 06.10.2026), Mailing 3 DE (Webansicht aus Zoho) und EN (25.04.2024), jeweils vollständig zum Scrollen. Kontaktblock Verkäufer (Mailing 1) ebenfalls verpixelt. Noch offen: Mailing 2 und weitere Sprachen. Persönliche Anrede entfernt, Foto und Kontaktdaten des Verkäufers (EN) verpixelt, Fusszeile mit Abmeldelink und Empfängeradresse (DE) abgeschnitten. Anmeldeformular und Zoho-Vorschau brauchen ein Login, noch nicht gezeigt. Offen: Mailings 1 und 2 sowie die anderen Sprachen sind noch nicht im Drive.
  - *Mailings ✅ Vorgabe Yana (06.10.2026):* So zeigen, wie die Kundschaft sie gesehen hat, nicht als Vorlage mit Platzhaltern. Anrede «Frau Senn» / «Mrs. Senn» / «Madame Senn», eine Ansprechperson pro Mail. Galerie: Mailing 1 DE (.msg), Mailing 2 DE/EN/FR (aus Zoho-PDF: Platzhalter durch Anrede ersetzt, von den vielen Verkäufer-Varianten nur eine behalten), Mailing 3 DE/EN (.msg), Dankesmail DE (.msg). Ansprechperson (Foto, Name, Kontakt) vorerst verpixelt, bis Einverständnis geklärt 📌. Fusszeilen mit Abmeldelink abgeschnitten. Offen: Dankesmail EN (PDF über 10 MB, Download nicht möglich), Mailing 1 EN/FR, Mailing 3 FR. Ausserdem im Drive: «CampaignPdfReport.pdf» (Kampagnenauswertung, noch nicht gelesen).
  - *Auswahl Mailings ✅ (Yana 06.10.2026):* Nur Mailing 1, Mailing 2 und Dankesmail, je DE und EN. Alle gleich breit (800 px), nicht verzerrt. Mailing 2 FR und Mailing 3 nicht zeigen. Vorhanden: Mailing 1 DE, Mailing 2 DE/EN, Dankesmail DE. Fehlt: Mailing 1 EN, Dankesmail EN (PDF zu gross, bitte als .msg).
  - *Update 06.10.2026:* Alle sechs Mails in der Galerie. Mailing 1 EN aus Zoho-PDF (Platzhalter → «Mrs. Senn», eine Ansprechperson). Dankesmail EN: PDF über 10 MB, deshalb Layout der deutschen Dankesmail mit dem offiziellen englischen Text aus dem PDF gefüllt (Text 1:1 übernommen).
  - *Schrift ✅ (Yana 06.10.2026):* Überall die gleiche Schrift, kein Wechsel. Entwurf: Lato für Seite, Mails (Schrift der CP-Vorlage) und Briefing-Seiten. Für die echte Website gilt die Regel weiter: eine Schriftfamilie, selbst gehostet.
  - *Kampagnenauswertung Zoho ✏️ (CampaignPdfReport, nicht veröffentlichen: enthält Empfängeradressen):*
    - Mailing 1, Versand 19.03.2024: DE 2271 versendet, 1457 zugestellt, 367 eindeutige Öffnungen (25,2 %), 77 eindeutige Klicks, davon 75 aufs Anmeldeformular; FR 139 versendet, 22 Öffnungen, 4 Klicks Anmeldung; EN 42 versendet, 9 Öffnungen, 1 Klick Anmeldung. Total 2452 versendet, 398 Öffnungen, 80 Klicks Anmeldung.
    - Mailing 2 DE, Versand 18.04.2024: 1644 versendet, 1454 zugestellt, 256 Öffnungen (17,6 %), 55 eindeutige Klicks, 42 aufs Anmeldeformular. Mailing 2 EN/FR: kein Report vorhanden.
    - Klickrate unter Öffnenden: rund 21 % (DE, beide Mailings).
    - Nachtrag 06.10.2026: Mailing 2 EN (18.04.2024): 19 versendet, 1 Öffnung, 0 Klicks. Mailing 2 FR: 89 versendet, 10 Öffnungen, 0 Klicks. Report (7) betrifft ACHEMA 2022 → nicht verwenden. Reports (5)/(6) = Duplikate. Für Dankesmail und Anzahl Formular-Einträge kein Report.
    - **Gesamt ✏️ (auf der Seite als «Die Einladung in Zahlen»):** 4204 Einladungen versendet · 665 Kontakte öffneten (Summe eindeutiger Öffnungen pro Mailing) · 122 gingen weiter zur Anmeldung (Klicks auf den Formular-Link) · 18 % der Öffnenden klickten weiter («fast jede fünfte Person»). Zeitleiste: 19.03. Mailing 1 (2452/398/80), 18.04. Mailing 2 (1752/267/42), 10.–14.06. ACHEMA, danach Dankesmail. Tabelle nach Mailing und Sprache aufklappbar. Bounces nicht gezeigt.
    - **Anmeldungen ✏️ (Quelle: Messebriefing, Folien 28–32, Stand 27.05.2024):** 78 Einträge im Anmeldeformular; ohne 3 interne Einträge (CP) und 1 Doppeleintrag = **74 Anmeldungen**. Geschenkwahl: SIGG-Flasche 32, Badetuch 27, Fussball 15. Endstand nach dem 27.05. unbekannt (Zoho Forms). Namenslisten nur verpixelt zeigen.
  - *Messebriefing ✏️ (06.10.2026, Yana: «einiges ausgelassen»):* Galerie jetzt 15 Seiten, aus den 37 Original-Folien nachgebaut: Titel, Lage Stand F28, Fakten + Messemotto, Kongressprogramm, Standplan, Standansicht, Ablauf Geschenk-Abholung, Anmeldungen (verpixelt), Auf- und Abbau (ohne Name/Telefon/Logistiknummer), Schichtplan (Namen verpixelt), Dresscode, Lead-Erfassung, Live-Demo und Display (ohne Referent), Verpflegung, Dank. Weggelassen: Hotel/Belegungsplan, Transfer und Restaurants, Parkieren, WLAN, Hallenplan mit Ausstellernamen.
  - *Anmeldeformular ✏️ (Screenshots Yana 06.10.2026):* Zoho Forms «ACHEMA2024AnmeldungYana», von Yana gebaut, DE/EN/FR (Report-Links mit zf_lang=en/fr). Inhalt: Kontakt, E-Mail, Sprache, Geschenkwahl (3 Geschenke), Teilnahmebedingungen; nach dem Absenden Bestätigung mit CP-Code fürs Gratis-Ticket; Einträge gehen ins CRM (Spalten «Zoho Forms zu CRM», «CP Sales»). Auf der Seite: Block «Ein Klick zum Geschenk» mit Galerie DE + EN. Wegen schlechter Screenshot-Qualität als scharfer Nachbau in doppelter Auflösung (Lato, Original-Header und -Geschenkbilder, Texte 1:1 aus den Screenshots).
  - *Formular interaktiv ✏️ (Yana 06.10.2026: «wie ein echtes Formular»):* Klickbarer Nachbau im Dialog, DE/EN umschaltbar, Pflichtfelder, Geschenkwahl, scrollbare Teilnahmebedingungen, Absenden zeigt Hinweis «Nachbau zur Ansicht, es werden keine Daten gesendet». Teilnahmebedingungen DE vollständig von Yana (Zofingen, 05.03.2024). EN: bis «…increase the number of gifts» aus dem Original-Screenshot; die letzten vier Absätze (18 Jahre, Mitarbeitende, Datenschutz, Datum) von Claude aus dem Deutschen übersetzt, Korrektur gelesen (06.10.2026).
  - *Ansprechperson in Mails ✅ (Yana 06.10.2026):* bleibt verpixelt.
  - *Korrekturlesen ✅ (06.10.2026):* Einladungstext korrigiert (zwei Mailings in drei Sprachen + Reminder, Dankesmail nach der Messe; vorher widersprüchlich «drei Mailings»), Satzfragment beim Fussball korrigiert, Hinweis oben aktualisiert, «Anmeldeformular» bei «Meine Aufgaben» ergänzt. «Im Frühling 2024 übernahm ich das laufende Projekt» ✅ bleibt so (Yana 06.10.2026).
  - Report (10): Dankesmail FR, 03.07.2024, 1 Empfänger → nicht in die Gesamtzahlen (betrifft nur Dank, keine Anmeldung).
  - *Bilder ✏️ v5 (06.10.2026, Feedback Yana: Rendering mit weissem Grund unschön → Skizze; alle 3 Mailing-Geschenke zeigen; mehr über den Tellerrand):* Kapitel 2 neu «Von der Skizze zum fertigen Stand» (isometrische Skizze aus dem Planungs-PDF neben Standfoto, nebeneinander statt Schieberegler, weil Perspektive abweicht). Kapitel 1 ergänzt um Entstehung des CP-Fussballs: Muster eines Fremdballs → Vorlage mit 32 Panels → eigenes Design (Drive «Achema/Gadgets», Feb.–März 2024). ✅ Geschenke im Mailing: SIGG-Flasche, Badetuch, Fussball (Bild «3 Produkte.jpg», Drive «Achema/Mailling», Yana 06.10.2026). Hinweis: Messewand «Safety first» war unverändert von 2022 (laut «Anpassungen Messestand», Jan. 2024) → nicht als Yanas Design zeigen. ✅ Info-Stelen (800 × 2200 mm, MKP / MKP Bio / MKPL / CP Service; Layout von 2022, **Texte 2024 von Yana angepasst**, Datei «CP_Pumpen_Grafik_zur Freigabe.pdf»): als Mockup + herangezoomter Ausschnitt aus dem Standfoto (Stele «MKP Reactor», web-6).
  - *Bilder ✏️ v4 (06.10.2026): Seitenentwurf mit echten Bildern* → Artifact https://claude.ai/artifact/XWP2ub9yg6MDibVE8ZQZ2c. Kapitel: Titelbild Stand · 1 Einladung (E-Mail-Banner, Fussball im CP-Design «DEF_3dBall» von Yana, März 2024, Schokolade) · 2 Plan → Stand (Schieberegler, Rendering auf weissem Grund statt schwarz) · 3 Am Stand (Buzzer, Exponat) · 4 Hinter den Kulissen (Standplan und Lead-Formular als Tablet-Mockup) · Meine Aufgaben. ✅ Yana: alles zeigen, was Hand und Fuss hat; schwarzer Hintergrund nicht schön; keine Platzhalter.
  - *Bilder ✏️ v3 (06.10.2026, Geschichte «Einladung → Idee → Realität → hinter den Kulissen»):*
    1. **Einladung:** Mailing mit Geschenkwahl, dazu der Fussball im CP-Stil (✅ Yana 06.10.2026: Geschenk zur Fussball-Zeit, im Mailing auswählbar; EM 2024 in Deutschland startete am 14. Juni 2024, dem letzten ACHEMA-Tag) und Schweizer Schokolade. ❓ Screenshot des Mailings vorhanden?
    2. **Idee → Realität** (Schieberegler): 3D-Rendering des Stands aus dem Briefing ↔ Foto des fertigen Stands (web-4).
    3. **Am Stand:** Buzzer Game, nur Hände (web-3).
    4. **Hinter den Kulissen:** Messebriefing als Tablet-Mockup (Ablauf Geschenk-Abholung, Standplan, Dresscode).
    - Quellen: Briefing «ACHEMA-Messebriefing 24_de.pptx» (Rendering image10, Standplan image11), Fotos eines Messefotografen (Bildrechte ✅ nicht weiter verfolgen, Yana 06.10.2026: Fotos werden nicht als eigene Arbeit ausgegeben). Nicht verwenden: Anmeldelisten, Schichtpläne, Hotel- und Parkdaten (Briefing-Folien mit Namen).
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
- Zusammenarbeit mit einer Standbau-Agentur ✅ (Name nicht nennen, Yana 06.10.2026): Standbau, Konstruktion, Logistikplan, Montage
- Yana: Infopanels zu den einzelnen Exponaten gestaltet
- Yana: Mailing
- Yana: Leads am Schluss über ein System erfasst
- ✅ Mietmaterial, Logistik und Einlagerung über die Agentur; Yana: Versand der Exponate und weiteren Materials an die Messe, Organisation von Artikeln und Verpflegung (Yana 06.10.2026)
- Yana war zu diesem Zeitpunkt relativ neu im Unternehmen

**Geklärt ✅ (06.10.2026)**
- Datum: ACHEMA 2024, 10.–14. Juni 2024, Frankfurt am Main (öffentlich bekannt)
- Materialien und Teamkoordination: siehe «Meine Aufgaben» (Einladungskampagne, Giveaways, Messebriefing, Standteam)
- Resultate 📌 keine Zahlen zeigen (Regel: keine schwachen Zahlen)

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

Abgeleitet aus dieser Liste (❓ bitte bestätigen, bevor es auf die Website kommt): **19 eigene Messen 2024–2026 in 5 Ländern** (DE, FR, US, UK, IN), davon 15 bereits durchgeführt (Stand 04.10.2026) und 8 in Phase 1. (TPS Houston 2025 am 04.10.2026 zu den Partnermessen verschoben.)

**Offen ❓**
- **Entscheide ✅:** Nur die Messen aus der Liste oben. Remstone Sulfur gestrichen. Die 2027-Messen kommen nicht auf die Website (Yana ist dort wahrscheinlich nicht mehr dabei) 📌 im Hinterkopf behalten.
- **Partner-Events ✅** (Yana lieferte Marketingmaterial und Giveaways für Partner/Vertretungen; Liste von Yana, ersetzt die Liste aus dem ersten Briefing):

| Datum | Land | Partner (nicht veröffentlichen) | Messe | Ort |
|---|---|---|---|---|
| 27.–29.11.2024 | TR | Metrans | Turkchem | ❓ (Stadt nicht in den Quellen) |
| 05.–07.03.2025 | KR | Dongil | InterBattery | Seoul, COEX |
| 22.–25.04.2025 | KR | Dongil | Korea Chem (mit Korea Pharm) | Seoul ❓ |
| 27.–30.05.2025 | IT | Exonder | Pharmintech | Mailand |
| 03.–05.06.2025 | ES | Atlas | Pumps & Valves | Bilbao |
| 09.–11.07.2025 | JP | Gadelius | Japan Pharm | Tokio |
| 17.–19.09.2025 | JP | Gadelius | Inchem | Tokio |
| 16.09.2025 | US | ❓ | TPS – Turbomachinery & Pump Symposium | Houston (kein Ordner) |
| 31.03.–03.04.2026 | KR | Dongil | Korea Chem | Seoul, KINTEX |
| 04.–07.05.2026 | DE | VDMA | IFAT (Stand des VDMA) | München |
| 02.–06.06.2026 | ES | Atlas | Expoquimia | Barcelona |
| Okt. 2026 | ES | Atlas | MMH (Bergbaumesse) | Sevilla · bevorstehend |

Quelle: Drive «Messen/Partnermessen», alle Unterordner gelesen (04.10.2026). Korrekturen gegenüber der alten Liste: «Korea Inter-Battery 22.04.2025» war Korea Chem 2025; InterBattery war im März 2025. Neu dazu: Pharmintech Mailand 2025 und Gielink/Lanxess. Zuständigkeit laut Quellen: Turkchem 2024 und Japan Pharm 2025 direkt an Yana adressiert; Gielink, InterBattery, Korea Chem 2025, Pharmintech, Bilbao mit Kürzel SAB (Leiterin bis April 2025); ab Nov. 2025 Koordination über Leiterin NIM. Deshalb pro Messe in der «wir»-Form schreiben.

**Absätze zum Aufklappen ✏️ (neutraler Ton, ohne Partnernamen:**
- **Turkchem 2024 (Türkei):** «An der Turkchem im November 2024 stellte der Partner von CP in der Türkei auf einem 90 m² grossen Stand aus, grösser als im Vorjahr. Wie schon im Jahr davor reisten Schnittmodelle der Magnetkupplungspumpen MKP und MKPL aus der Schweiz an, dazu englische Broschüren, Factsheets und Giveaways. Die Versanddokumente waren vorab mit der Logistik des Partners abgestimmt, damit die Einfuhr in die Türkei reibungslos lief.»
- **InterBattery 2025 (Seoul):** «Die InterBattery in Seoul ist die Fachmesse der Batterieindustrie. Der Partner von CP in Korea zeigte dort im März 2025 eine MKP und eine MKPL in Ex-Ausführung auf CP-Podesten, ergänzt durch englische Broschüren und Schweizer Schokolade als Giveaway. Die Exponate blieben im Anschluss in Korea, bereit für die nächste Messe.»
- **Korea Chem 2025 (Seoul):** «Nur sieben Wochen später folgte die Korea Chem, die Fachmesse der koreanischen Chemieindustrie, gemeinsam mit einer Pharmamesse. Die Exponate der InterBattery standen erneut am Stand, aus der Schweiz kamen Broschüren zu MKP, MKP-Bio und MKPL. Danach gingen die Pumpen per Luftfracht zurück in die Schweiz.»
- **Pharmintech 2025 (Mailand):** «Die Pharmintech in Mailand gehört zu den wichtigen Messen des italienischen Pharmamarkts. Für den Partner in Italien, der seine Präsenz in diesem Markt ausbauen wollte, ging ein MKP-Bio-Set auf Podest nach Mailand, dazu englische Broschüren mit Schwerpunkt MKP-Bio, Explosionszeichnungen und Giveaways.»
- **Pumps & Valves 2025 (Bilbao):** «An der Pumps & Valves in Bilbao war der Partner von CP in Spanien vertreten. Aus der Schweiz kamen ein Schnittmodell der PFA-ausgekleideten MKPL auf fahrbarem Podest, englische Broschüren, Explosionszeichnungen und Giveaways.»
- **Japan Pharm 2025 (Tokio):** «Die Japan Pharm in Tokio richtet sich an die Pharmaindustrie. Ein neuer Partner in Japan stellte dort im Juli 2025 aus, noch bevor die Partnerschaft vertraglich besiegelt war. Für den Auftritt reisten zwei MKP-Bio-Pumpen nach Japan, dazu englische Broschüren, Explosionszeichnungen und Schweizer Schokolade, die als Zeichen für Swiss Made schon an den Messen in Korea gut ankam.»
- **Inchem 2025 (Tokio):** «Zwei Monate später folgte mit der Inchem in Tokio eine Chemiemesse ❓. Zwei Schnittmodelle der MKP, englische Broschüren, Giveaways und Schokolade gingen nach Japan; die Exponate kamen danach per Luftfracht zurück in die Schweiz.»
- **Korea Chem 2026 (Seoul):** «2026 war der Partner in Korea erneut an der Korea Chem, diesmal im KINTEX in Seoul. Die Vorbereitung lag beim Marketing in der Schweiz: E-Mail-Banner, Exponate, Broschüren und Versand per Luftfracht. Weil Demopumpen in diesem Jahr an vielen Messen gefragt waren, entstand eine passende Kombination aus MKPL und vertikal montierter MKP. Am Stand warben koreanische Poster für die Magnetkupplungspumpen von CP.»
- **Expoquimia 2026 (Barcelona):** «An der Expoquimia in Barcelona zeigte der Partner in Spanien eine grosse MKPL 150-125-315 und daneben die zerlegten Bauteile, von der PFA-Auskleidung bis zur Magnetkupplung. Pumpe, Firmenbroschüren und Giveaways kamen aus der Schweiz bis ins Lager des Partners.»
- **MMH 2026 (Sevilla):** «Für die Bergbaumesse MMH in Sevilla stehen eine MKPL auf fahrbarem Podest und Giveaways bereit. Es ist das erste Mal, dass CP über einen Partner an einer Bergbaumesse vertreten ist ❓.»
- **IFAT 2026 (München):** ✅ Partnermesse (Yana 04.10.2026: Stand des VDMA, CP nicht selbst Aussteller; ein CP-Kollege besuchte und unterstützte den Stand). «An der IFAT in München war CP am Stand des VDMA vertreten, der sich dem Thema Textilrecycling widmete. Zwei Schnittmodelle der MKP auf einem Podest, deutsche Broschüren und Giveaways kamen aus der Schweiz; ein Kollege aus dem CP-Team unterstützte den Stand vor Ort. Im Vorfeld lud ein E-Mail-Banner zum kostenlosen Messebesuch ein.»
- **Gielink/Lanxess 2025:** ✅ weglassen (Yana 04.10.2026: Anlass unbekannt).
- **TPS Houston 2025:** kein Ordner → nur in Liste/Karte.

**Bilder (Vorschlag):** InterBattery IMG_4223 und IMG_4224 (CP-Podeste, keine Personen); Expoquimia «Image 2026-06-03 at 10.49.32» (zerlegte Bauteile, keine Personen); Korea Chem 2026 IMG_0029 (Personen zuschneiden); Turkchem-Fotos nur zugeschnitten (überall Personen).

  - ✅ **Darstellung (Yana 04.10.2026):** Partnermessen nur in Messeliste und Karte, ohne eigenen Eintrag, gekennzeichnet mit «am Stand eines Partners» (EN: «at a partner's booth»); auf der Karte optisch von den eigenen Messen unterschieden.
  - «InnoTrans» aus dem ersten Briefing war ein Versehen ✅ gestrichen.
  - ✅ **Partnernamen nicht nennen** (Yana 04.10.2026): nur Messe, Ort, Land und Datum.
  - ✅ **Zwei Ebenen pro Partnermesse** (Yana 04.10.2026: Kurzzeile allein zu knapp): sichtbar eine Zeile; beim Aufklappen bzw. Antippen ein kurzer Absatz (3–4 Sätze): Was ist das für eine Messe, wer stellt aus (Partner nur umschreiben, z. B. «unser Partner in Spanien»), was wir dafür vorbereitet und hingeschickt haben, Besonderheiten. Kurzzeile: Art der Messe (Branche) und was wir hingeschickt haben. Format ✏️: «Expoquimia · Barcelona, Spanien · Juni 2026 · Fachmesse für Chemie · Exponate, Broschüren, Giveaways». Quelle: Drive-Ordner der Partnermessen (noch offen).
  - ✅ **Einleitung zur Partnerliste** (Fakten von Yana 04.10.2026: Exponate, Marketingmaterial usw. an die Partner geschickt). Textentwurf ✏️:
    - DE (neutraler Ton): «Auch an Messen von Partnern und Vertretungen weltweit war CP präsent. Exponate, Broschüren, Giveaways und weiteres Marketingmaterial kamen dafür aus der Schweiz, zusammengestellt und verschickt an den jeweiligen Stand.»
    - EN: «CP was also present at trade fairs of its partners and representatives worldwide, with exhibits, brochures, giveaways and other marketing material put together and shipped from Switzerland to each booth.»
    - Rolle über «Meine Aufgaben»: Exponate und Material zusammenstellen · Versand organisieren · E-Mail-Banner (je nach Messe)
- Schreibweisen: Petrochymia / Petro-Chimie
- Golf Event Thailand: ✅ weglassen

#### Case 3 · Christmas Campaigns & Corporate Gifting (CP Pump Systems)
**Kernaussage ✏️:** Jährliche Kampagne für A-Kunden, B-Kunden und Mitarbeitende, von der Idee bis zum Versand. Die Fallstudie zeigt die Entwicklung von «mit Agentur» (2024) zu eigenständig (2025).

- **2024 ✅:** B-Geschenk Bienenwachstuch-Set, Nachhaltigkeitsbezug. Zusammenarbeit mit einer Agentur (Yana war neu im Unternehmen) und mit einer Werkstatt, in der die Produkte von Hand gefaltet bzw. verpackt wurden. Dazu Karte, Verpackung, Produktbeschreibung und Versand.
- **2025 ✅:** Richartz K Tool Plus Neck and Bike (BB Trading). Yana: Auswahl/Bestellung, Branding, Verpackung, Karte, Organisation. Mitarbeitergeschenk: grossformatiges gebrandetes Badetuch.
- **2026 ✅ (erledigt, siehe Text-Entwurf Weihnachten 2026):** Ideen: Cardholder (B-Kunden), Picnic Blanket (A-Kunden), eventuell Karandashi Pen. Zeigen wir das schon, als «in progress», oder erst nach dem Versand?
- 🔒 Lieferanten bzw. Partner nur nennen, wenn freigegeben 📌 (A12)

#### TEXT-ENTWURF Case «Weihnachtskampagne 2026» ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
**Entscheid ✅:** Auf der Website nur **2026** zeigen. ✅ **Yana 05.10.2026:** im Team mitgeholfen, Karten **komplett gestaltet**, Austausch mit den Druckereien. (Frühere Notiz «Konzept, Design, Text eigenständig» dadurch präzisiert.) 2025: Yana leitete die Kampagne mit einer Agentur (nur evtl. ein Satz). 2024 (mit Agentur) weglassen.
- **Stichworte:** Konzept · Kartendesign · Text · Geschenkauswahl
- **Ausgangslage:** Jedes Jahr bedankt sich CP Pump Systems zu Weihnachten mit einem Geschenk, abgestimmt auf drei Zielgruppen: A-Kunden, B-Kunden und Mitarbeitende.
- **Meine Rolle ✅:** 2026 arbeitete ich im Team an der Kampagne mit. Gestaltung und Texte der Karten lagen komplett bei mir, ebenso die Abstimmung mit den Druckereien. Zudem holte ich die Offerten ein und koordinierte Bestellung und Lieferanten.
- **Vorgehen ✅ (Yana 05.10.2026: Vergleich im Team, Offerten und Koordination bei Yana):** Statt die Geschenke einfach festzulegen, fragte das Team zuerst den Verkauf und die Vertretungen: Welche Ideen kommen bei den Kunden an, und wie viele Geschenke braucht es? Die Favoriten wurden bei drei Anbietern nach Preis, Druckfläche, Lieferzeit und Herkunft verglichen. Ich holte die Offerten ein und koordinierte die Anbieter bis zur Lieferung.
- **Idee ✏️:** Jedes Geschenk erzählt etwas über CP. Die Picknickdecke für A-Kunden ist «leakproof»: Sie hält dicht, von unten und von oben, so wie die dichtungslosen Pumpen von CP. Der Kartenhalter für B-Kunden schützt Bank- und Visitenkarten mit einem RFID-Blocker, «Sicherheit, die man nicht sieht, aber spürt», ebenfalls eine Brücke zu den Pumpen. Die Mitarbeitenden erhalten ebenfalls die Picknickdecke, mit einer eigenen Karte unter dem Titel «Gemeinsam stark».
- **Kartenmotiv ✅ (Konzept-Variante 2):** Rentiere ziehen einen Schlitten mit einer CP-Pumpe durch den Nachthimmel über verschneite Berge, dazu «Merry Christmas» und der CP-Claim «cleaner pumps, cleaner planet™». Auf der Innenseite ein Zahlen-verbinden-Rätsel: «Strich für Strich zur Lösung. / Every line reveals more. / Chaque ligne en révèle davantage.» Die Karten sind mit Anrede und Namen personalisiert (Seriendruck).
- **Umsetzung ✅:** Ich habe die Karten gestaltet und alle Texte geschrieben: für A-Kunden («Zeit für Dankbarkeit»), B-Kunden («Die schönste Zeit des Jahres») und Mitarbeitende («Gemeinsam stark»). Die Kundenkarten gibt es auf Deutsch, Englisch und Französisch, jeweils in der Sie- und der Du-Form; die Mitarbeiterkarte auf Deutsch und Englisch. Dazu kamen Druckvorbereitung mit der Druckerei (Karten, Adressetiketten, Couverts), Bestellung der Geschenke und die Organisation des Versands.
- **Ergebnis:** 📌 später (Versand Ende 2026)
- Quellen ✅ gelesen: Texte Kunde A, Kunde B, Mitarbeitende (Version 1.2, Sept. 2026); Übersicht/Umfrage 2026.
- ✅ Mitarbeitende erhalten die Picknickdecke. Schneekugel war eine andere Konzept-Variante (nicht umgesetzt).
- *Bilder* 📌 später: Kartenvorderseite (Schlitten mit Pumpe), Rätsel-Seite, Picknickdecke, Kartenhalter, Konzept-Skizzen
- *Seitenentwurf ✏️ v1 (06.10.2026):* `docs/entwuerfe/weihnachten-2026.html`, Artifact https://claude.ai/artifact/1ub6RRXMbhZQRUq33avRvH. Aufbau: Titelbild (Vorder- und Innenseite) · 1 Umfrage als Balkendiagramm · 2 Geschenke mit Botschaft (Picknickdecke Produktfoto Lieferant, Kartenhalter-Mockup mit CP-Logo) · 3 Karte: Moodboard → Illustration → fertige Vorderseite, Galerie mit 13 Kartenseiten · 4 Rätsel zum Selberlösen (35 Punkte, Lösung XMAS, aus der Druckdatei übernommen) · 5 Umsetzung · Meine Aufgaben.
  - *Umfrage-Auswertung ✏️ (Quelle: «20260513_Auswertung_Christmas Gifts 2026», 16 Antworten, 15.04.–06.05.2026, Skala 1–5):* Anteil Bewertungen 4 oder 5 – A-Ideen: Picknickdecke 9/16 (56 %), Tagungsmappe 8, Notizbuch 7, Schneidebrett 7, Kühltasche 7, Kuscheldecke 4, Untersetzer 3. B-Ideen: Kartenhalter 8/16 (50 %), Tischkalender 7, Mütze 6, Multitool 6, Handschuhe 4, Brillenputztuch 4, Handwärmer 2, Mausmatte 2. Gewählt wurden jeweils die Ideen mit den meisten Top-Bewertungen.
  - Unterschrift auf der Mitarbeiterkarte entfernt.
- *Seitenentwurf ✏️ v2 (06.10.2026, Feedback Yana):*
  - ✅ Umfrage-Auswertung NICHT im Detail zeigen (Privatsphäre/intern). Ersetzt durch Ablauf «18 Ideen → Umfrage → 10 Ideen × 3 Anbieter, 8 Kriterien → 2 Geschenke» und Ausschnitt aus der Ideensammlung (12 Produktbilder, ohne fremde Logos). Keine Preise, keine Mengen.
  - ✅ Platzhalternamen statt Seriendruck-Feldern: «Sehr geehrte Frau Muster», «Dear Ms Muster», «Chère Madame Muster», «Liebe Anna», «Dear Anna» (Schrift ähnlich nachgesetzt).
  - ✅ Karten einzeln anklickbar, öffnen gross in der Galerie (13 Seiten), nichts mehr abgeschnitten.
  - ✅ Konzept-Präsentation als Galerie (8 Seiten, nachgebaut, Jahr im Titel weggelassen): Moodboards, Rätsel-Idee, drei Textvarianten, Favorit Schneekugel, Zeitplan. Text: Favorit war Schneekugel, umgesetzt wurde der Schlitten.
  - Druckdetails aus Offerte (ohne Preise/Mengen): A5 6-seitig Wickelfalz, Mitarbeiterkarte 4-seitig, 300 g/m² FSC, 4-farbig personalisiert, Adressetiketten und Couverts C5.

- **Funde aus Drive «Weihnachtskampagnen» (03.10.2026)** (nicht verwendet: Adresslisten, Preise, Rechnungen, Offerten):
  - 2025: Projektplan Juni–Dez mit einer Agentur (laut Plan: Konzept, Text, Layout, Verpackung bei der Agentur; Lektorat extern; Druck in Druckerei; Übersetzung EN/FR bei CP; Versand DE/FR direkt, Mitarbeitende persönlich; A-Gadget wird von Verkäufern persönlich übergeben; digitales Mailing an übrige Kunden/Agenten weltweit). Karten in vielen Varianten: A-Kunden Sie/Du, männlich/weiblich/neutral, EN personalisiert; Mitarbeiterkarten DE/EN. Badetücher (zweite Lieferung). Skizzen zum Weihnachtsmailing vorhanden (Prozessbilder!). → ✅ nicht relevant: Website zeigt nur 2026.
  - Konzept-Präsentation «Weihnachtsmailing» (Ideen & Konzept): Kartendesigns, Favorit «Schneekugel mit CP-Pumpe», Zahlen-verbinden-Rätsel (ergibt Pumpe oder XMAS), drei Wording-Varianten, Zeitplan. → ✅ nicht relevant (Schneekugel nicht umgesetzt; Website zeigt nur 2026).
  - 2026: interne Umfrage (April 2026) bei Verkauf/Ländern zu Geschenk-Ideen und Mengen; Vergleich von drei Lieferanten (Preis, Druckfläche, Lieferzeit, Herkunft). Entscheid: A-Kunden Picknickdecke, B-Kunden RFID-Kartenhalter; Karten in allen Sprachen, Sie/Du-Form; Mitarbeiterkarte DE/EN. Starkes «Vorgehen»-Beispiel (datenbasiert). ❓ 2026 zeigen?
- ✅ Nicht relevant (nur 2026 wird gezeigt): A-Kunden-Geschenke 2024/2025? Was für eine Werkstatt (z. B. soziale Einrichtung)? 2025 Multitool für welche Zielgruppe?

#### TEXT-ENTWURF Case «Giveaways und Werbeartikel» ✅ (Inhalt freigegeben, Bilder offen)
Quelle: Drive «Giveaways» (CP und GOLDINGER getrennt), gelesen 03.10.2026: Give-Aways_2025 (Anbietervergleiche), Zeitplan Versand USA-Box, Katalog «CP Brochures & Gadgets» (Artikelnummern, zum Bestellen für Events). Nicht verwendet: Preise, Rechnungen, Offerten, Namen.
- **Stichworte:** Auswahl · Branding · Produktion · Versand
- **Ausgangslage:** An Messen, bei Kundenbesuchen und als Dankeschön braucht CP Werbeartikel, die zur Marke passen und gerne benutzt werden, für eigene Messen ebenso wie für Partner weltweit.
- **Meine Rolle ✅ (Yana 06.10.2026):** Ich wähle die Artikel aus, kümmere mich um Branding und Druckdaten, bestelle, organisiere Lagerung und Versand. Für Kundenbesuche und Messen stelle ich den Verkäuferinnen und Verkäufern passende Sets zusammen, die sie mitnehmen.
- **Vorgehen:** Für neue Artikel vergleiche ich mehrere Anbieter, zum Beispiel bei Fruchtgummis nach Menge, Druckfläche, Lieferzeit und Zutaten. Einen Teil der Bestellungen habe ich klimaneutral über myClimate abgewickelt. ✅
- **Sortiment (Auswahl):** SIGG-Flaschen und -Lunchboxen, Rucksäcke, Badetücher, Fussbälle, Golfbälle, Teleskoplampen, Notizbücher, Multitools, Swiss Tool, Victorinox-Taschenmesser, Kugelschreiber, Kägi-Schokolade, Biberli, Zuckersticks, Kaffee- und Mehrwegbecher, Massstäbe, Universal-Ladestecker, Arbeits- und Messekleidung ✅ (Biberli, Kaffeebecher, Kugelschreiber, Swiss Tool von Yana ergänzt)
- **Kunden- und Mitarbeitergeschenke ✅ (Yana 06.10.2026):** Weihnachtsgeschenke sowie Kundengeschenke über das Jahr, z. B. Golfbälle, Caran-d'Ache-Stifte, Lunchboxen und Rucksäcke (erscheinen auch bei den Giveaways).
- **Logistik:** Material für Messen und Partner im Ausland, z. B. eine Box mit Broschüren und Giveaways für eine Messe in den USA, geplant mit Luft- oder Seefracht-Vorlauf.
- **Eigene Gestaltung ✅:** Verpackung für die Kägi-Schokolade; neues Design für die Dokumentenmappe und den 3D-Ball bei der Neubestellung (Yana: «nimm rein»)
- **Katalog ✅:** Den internen Katalog «Brochures & Gadgets» (Broschüren, Factsheets und Giveaways mit Artikelnummern, zum Bestellen für Events) habe ich erneuert und aktualisiert.
- **GOLDINGER:** Mini-Fruchtgummis im eigenen Design, Autoaufkleber
- **Bilder:** vorhandene Fotos im Ordner (Badetuch, Fussball, Lampen, Taschen, Stifte, Notizbuch, Golf, Box, Mappe); 📌 Yana macht neue Fotos im Büro; bis dahin Mockups als Platzhalter.


#### Case 4 · Branded Objects & Giveaways (CP + GOLDINGER)
**Kernaussage ✏️:** «Branding extends beyond the screen.» Ein bildstarker Case mit wenig Text.

- CP-Giveaways ✅ (Liste aus dem Briefing): Backpacks, Bath Towels, Biberli, Cups, Fruit Gummies, Footballs, Golf Balls, Helmets, Coffee Cups, Kegi, Tape, Travel Items, Pens, Memos, Meter, Swiss Tool, Notepads, Notebooks, Folders, Post-its, Umbrellas, SIGG Lunchboxes & Bottles, Sports Backpacks, Metal Straws, Telescopic Lamps, Tote Bags, Universal Travel Chargers, USB Sticks, Victorinox, Sugar Sticks
- Arbeitskleidung und Messekleidung ✅ 📌
- GOLDINGER-Fruchtgummis ✅ (Formen und Grafik gestaltet, 2022 gelb/schwarz, 2023 blau, für WEGA & Immozionale) → ✅ **auch separat zeigen** (Yana 06.10.2026): eigenes Beispiel in diesem Case, zusätzlich zur Messe-Kachel.

#### TEXT-ENTWURF Case «Broschüren und Factsheets» ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
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
- **GOLDINGER im Ordner «Broschüren» ✅ gefunden** (Claude hatte zuerst nur Seite 1 der Dateiliste gelesen): Hausmagazin «Die IMMO-EXPERTEN», Ausgabe Februar 2023, 12 Seiten, erscheint 2× im Jahr ✅. Inhalt: Marktausblick 2023, Infoabende an 7 Standorten mit Anmeldetalon und QR-Code, aktuelle Immobilien und Neubauprojekte (S. 4–11), Gutschein für Gratis-Bewertung. Dazu Word-Texte «Editorial», «Ausblick 2023», «Infoabende» und ein älteres Hausmagazin (2022). ✅ geklärt: Layout von Yana, Texte gemeinsam mit dem Verkaufsteam (siehe Text-Entwurf). Zuordnung: «Frühere Projekte» → Hausmagazin.

#### TEXT «Website und Newsletter» (CP) ✅ – Version 2 (freigegeben)
Fakten ✅ (Yana): Website nicht erstellt, sondern gepflegt; News-Beiträge geschrieben; neue Mitarbeitende (Fototermine organisiert, vorgestellt); Formulare/Service-Seiten mit der Agentur nach Feedback überarbeitet; Downloads laufend erneuert; Weltkarte bei neuen Standorten angepasst; Stellenanzeigen vom HR aufgeschaltet/entfernt; Newsletter und Social Media via Zoho One (LinkedIn, Facebook).
Auf cp-pumps.com gesehen (03.10.2026), ✅ Inhalte von Yana gepflegt (siehe Text «Website und Newsletter»): Messekalender mit Standnummern und «Gratis-Ticket sichern»; Blogbeiträge pro Messe; Produktbeiträge (z. B. «Sofort verfügbare Pumpensysteme», «saures Prozesswasser»); Download-Bibliothek (Broschüren, Explosionszeichnungen, Zertifikate, AGB); Videoseite; 360°-Showroom; Kontaktseiten pro Land; Karriereseiten inkl. Lernende; Sprachen DE/EN/FR/CN.
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

#### Funde CP-Website News/Blog (05.10.2026, cp-pumps.com/de/blog, alle Kategorien gelesen) ✏️
Beiträge ab Yanas Start (2024–2026). ✅ Yana (05.10.2026): 2024 und 2025 nicht jeden Beitrag selbst, aber einige; ab 2025 ein paar → im Case als «News-Beiträge verfasst» erwähnen, ohne einzelne Zuordnung:
- 30.04.2024 Neuer Meilenstein: Südkoreanische Tochterfirma erweitert internationales Netzwerk (kurz)
- 16.05.2024 Magnetgekuppelte Pumpe zur Reaktorumwälzung in der chemischen Industrie (~425 Wörter)
- 16.05.2024 Ist Ihre Pumpe bakteriendicht? Hygienepumpen in Food und Pharma (~300 Wörter)
- 16.05.2024 Keramisch ausgekleidete Pumpe gegen Abrasion (~370 Wörter)
- 25.03.2025 Angehende Chemie- und Pharmatechnologen besuchten die CP Pumpen AG (~230 Wörter)
- 01.04.2025 Grossauftrag für die CP Pumpen GmbH (~170 Wörter)
- 13.01.2026 Erfolgreiche Projektumsetzung 2024/2025: keramisch ausgekleidete ET-Pumpen gegen Abrasion (~350 Wörter)
- 23.01.2026 Messe-Ankündigungen FLA Miami, Korea Chem, Pumps & Valves Dortmund (je ~110–130 Wörter)
- 16./17.03.2026 Messe-Ankündigungen IFAT München, ChemUK, DK Hub Global
- 21.04.2026 Sofort verfügbare Pumpensysteme (kurz, zum Lieferzeiten-Flyer)
- 22.04.2026 Dichtungslose Magnetkupplungspumpen für saures Prozesswasser (Referenz Düngemittelproduktion, ~280 Wörter; = Blogbeitrag aus Ordner «Werbung»)
- 25.06.2026 Messe-Ankündigung CRU Sulphur + Sulphuric Acid Berlin
Vor 2024 (nicht Yana): Beiträge 2019–2023.

#### Funde Nachtrag «Werbung/Print» (05.10.2026) ✏️
- **GOLDINGER Prozess Inserate:** «Wegführung Inserate» (Jan. 2023): Ablauf Offerten einholen → prüfen → Inserate, PR-Texte und Fotos senden → Gut zum Druck prüfen → Rechnungen gegen Offerten prüfen → ablegen; «Daten Inserate»: Streuplan nach Kalenderwoche und Zeitung (Inserate 112 × 70, halbseitig 285 × 183, PR-Texte 1500–2000 Zeichen). Starker Beleg für Kampagnenplanung.
- **GOLDINGER Inserate:** Infoabende 2023 (sieben Orte, 14.–29. März, Varianten mit TKB bzw. SGKB, mehrere Formate und Regionalausgaben); HEV 2022 («Die 3 grössten Irrtümer zur Grundstückgewinnsteuer», «Geballtes Wissen online abrufbar» – enthält Zahlen, nicht übernehmen); HEV 2023 (v6-final); SCK-Clubmagazin; WEGA 2022.
- **GOLDINGER weitere Print:** Jahresessen-Einladungen Okt. 2021 (Farb-/Designvarianten, Entwürfe); Visitenkarte; Anmeldetalon Infoabende 2023; Hausmagazin Frühling 2023 (Editorial, Infoabende-Text 2022 vs. 2023, Ausblick 2023; Editorial mit Vermerk «Wortwahl Winkler» ❓ externe Texterin?); Lieferspezifikationen für Zeitungsbeilagen (Hausmagazin als Beilage).
- **GOLDINGER WEGA:** Stand 2022 (dunkelblaue Paneele, Objektfotos, Theke) = **«vorher»**; neu 2023 = «wände neu.jpg» = **«nachher»**; Anmeldung und Messeplan WEGA 2023 (28.9.–2.10.2023); Messewand Kradolf (Neubauprojekt, Feb. 2023). Sunneberg-Flyer 2019 = vor Yanas Zeit (evtl. Referenz für den alten Stil).
- **CP Weihnachten 2026 (Ergänzung):** finale Karten 1.10.2026: A- und B-Kunden je Du/Sie, 6-seitig A5, DE/EN/FR; Mitarbeitende 4-seitig DE/EN; blaues Cover, verschneite Berge, Rentierschlitten mit Pumpe, Rätsel «Strich für Strich zur Lösung», Rückseite mit sechs Standorten; Geschenke: Picknickdecke (A-Kunden, Mitarbeitende), RFID-Kartenhalter (B-Kunden); Umfrage im Verkauf (April/Mai 2026, 22 Ideen bewertet), Lieferantenvergleich, Druckerei selbst organisiert (2025 noch über Agentur). Koordination Druck/Umfrage laut E-Mails Leiterin NIM. ✅ Yana: Karten komplett gestaltet und getextet, Austausch mit Druckereien, im Team mitgeholfen. ✅ Französisch bewusst «vous» auch in der Du-Form (Yana 05.10.2026: in Frankreich siezt man Kundschaft auch per Du-Ansprache, ausser enge Beziehung).
- **CP Songkran 2026:** Skizzen Nr. 1–6, Agentur-Offerte zur Umsetzung «einer der drei Kundenskizzen», Druck über Flyeralarm. ✅ **Yana 05.10.2026: Songkran komplett von Yana.**

#### TEXT-ENTWURF «Songkran-Grusskarte 2026» ✅ (Inhalt freigegeben, Bilder offen)
- **Stichworte:** Konzept · Illustration · Print
- **Kurz:** Grusskarte zum thailändischen Neujahr für die Niederlassung in Thailand
- **Ausgangslage:** Songkran ist das thailändische Neujahrsfest im April und ein Fest des Wassers. CP Pump Systems hat in Thailand eine Niederlassung (Branch); die Karte ging an das Team dort (✅ Yana 05.10.2026: Branch stimmt).
- **Meine Rolle ✅:** Die Karte lag komplett bei mir: Ideen und Skizzen, Gestaltung, Druckvorbereitung und Bestellung.
- **Umsetzung:** Sechs Skizzen als Ausgangspunkt (Jan. 2026), daraus zwei Entwürfe. Motiv: zwei Pagoden mit der thailändischen und der Schweizer Flagge, die Thailand und die Schweiz verbinden; dazu Wasserspritzer, Blüten und Sonne auf einem Verlauf von Gelb zu Blau, mit CP-Logo und «Happy Songkran Festival». Druck über eine Online-Druckerei (Feb. 2026).
- **Wellness-Set:** ✅ weglassen (Yana 05.10.2026: nicht ihre Arbeit).
- **Bilder:** Skizzen und finale Karte (Vorderseite) 📌; aus Thumbs bekannt, Originale noch suchen.
- Nicht verwenden: Preise, Bestellnummern, Adressen, Namen und Telefonnummern aus den E-Mails.
- **CP weitere:** Lieferzeiten-Flyer DE/EN; Molten-Sulphur-Anwendungsblatt; Sammelbanner Messen DE/EN/FR; Panels zur Firmengeschichte (Aug. 2026, vermutlich Wandpaneele); Weltkarte mit Farbvarianten (schwarz, hellgrün, grün, grau, blau) → Auswahl → Sprachversionen (guter Prozess); Fotoshooting Betrieb Aug. 2026 und Mai 2026 (Dateien zu gross, nicht angesehen); Firmenprofil-Präsentation 2026 (77 MB, nicht angesehen).

#### TEXT-ENTWURF «GOLDINGER Hausmagazin» (Frühere Projekte) ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
- **Stichworte:** Layout · Editorial · Print
- **Kurz:** «Die IMMO-EXPERTEN», 12 Seiten, zweimal im Jahr
- **Ausgangslage:** GOLDINGER Immobilien gab zweimal im Jahr ein eigenes Hausmagazin heraus. Es zeigte die aktuellen Immobilien und Neubauprojekte, lud zu den Infoabenden ein und lag teilweise Zeitungen in der Ostschweiz bei.
- **Meine Rolle ✅:** Ich gestaltete das Magazin und schrieb die Texte gemeinsam mit dem Verkaufsteam. Die Inhalte legten wir zusammen mit meinem Vorgesetzten fest; Bilder und Objektangaben kamen von den Standorten. Zudem organisierte ich die Verteilung als Zeitungsbeilage: In welchen Zeitungen erreichen wir unsere Zielgruppe, und wo wird das Magazin gestreut? So warb das Magazin auch für die Infoabende.
- **Umsetzung (Ausgabe Februar 2023):** Marktausblick als Titelgeschichte · Infoabende an sieben Standorten mit Anmeldetalon und QR-Code · aktuelle Immobilien und Neubauprojekte auf acht Seiten · Gutschein für eine kostenlose Immobilienbewertung · Planung der Zeitungsbeilagen
- ✅ **Yana 05.10.2026:** Hausmagazin von Yana gemacht; eine Ausgabe zeigen, das PDF darf verwendet werden.
- **Gezeigte Ausgabe: Februar 2023** (A4, 12 Seiten; gelesen aus «Hausmagazin-2023-komp.pdf», 1,5 MB; Druck-PDF «Hausmagazin Februar 2023 final» 20 MB nicht geöffnet). Aufbau mit festem Seitenkopf (blaue Linie, Rubrik in Versalien, goldinger.ch in der Fusszeile):
  - S. 1 · Titel «Ausblick auf das Jahr 2023» mit Editorial der Verwaltungsräte und Inhaltsübersicht
  - S. 2–3 · NEWS «Alles rund um unsere Infoabende», Termine, QR-Code, Partnerbank, Leistungsübersicht
  - S. 4 · PREMIUM-Objekte · S. 5–8 · KAUFEN (Objektraster) · S. 9–11 · PROJEKTE (Neubauprojekte)
  - S. 12 · GUTSCHEIN für die kostenlose Wertermittlung und Anmeldetalon Infoabend
- ✅ **Yana 05.10.2026: alle 12 Seiten zeigen, als Online-Magazin zum Durchblättern** (Blätteransicht mit Doppelseiten, Pfeile/Wischen, Vollbild; auf dem Handy Einzelseiten). Umsetzung erst in der Code-Phase 📌: Seiten als optimierte Bilder (WebP, zwei Grössen), ohne externen Dienst, mit Tastatur bedienbar, `prefers-reduced-motion` ohne Umblätter-Animation, Alternativtext pro Seite.
- ✅ **Yana 05.10.2026: Seiten unverändert zeigen, wie gedruckt** (keine Retusche von Preisen, Namen, Nummern oder Fotos), da das Magazin so öffentlich verteilt wurde. Ausnahme gilt nur für das Hausmagazin.
- **Hinweis:** Text des Editorials nicht als Yanas Text ausgeben (gezeichnet von den Verwaltungsräten).

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
- ✅ Editorial: World Fertilizer (Sulfur), Fachartikel, Messeartikel → ✅ geklärt im Case «Werbung: Print & Digital» (EUREKA ausgelassen, Anwendungsbericht von Yana)
- ✅ Koordination mit Druckereien, Agenturen, Lieferanten
- Tools: InDesign, Illustrator, Photoshop

#### Funde Drive «Goldinger» + altes Portfolio (04.10.2026) ✏️
Quelle: Ordner «Goldinger» (Screenshots der alten Portfolio-Website, Ordner «Inhalt 2024», «Storys goldinger insta») und älterer Ordner «Goldinger» (Giveaways). Listing evtl. nicht ganz vollständig (Drive-Index). Nicht verwendet: Preise, Rechnungen, Namen von Mitarbeitenden.
- **Altes Portfolio (ca. 2023):** «Marketing / Social Media / Grafik Design». Über mich: Mediamatikerin-Ausbildung bei der SBW Neue Medien mit BMS, nach zwei Theoriejahren zwei Praxisjahre bei GOLDINGER (Marketing, Grafikdesign) → abgleichen siehe Kapitel Werdegang. Projektseiten mit eigenen Texten: Hausmagazin, Social-Media-Kampagne Infoabende (Meta-Anzeigen, Fokus Ostschweiz, 4 Wochen; Zielgruppe wenig auf Social Media → Schwerpunkt Print), Printwerbung (Inserate in Ostschweizer Zeitungen, von der Offertanfrage über Gestaltung bis Übermittlung), Immobilien-Videos (Rundgänge, Luftaufnahmen), zwei animierte Erklärvideos («Immobilienverkauf bei GOLDINGER», «Stiller Verkauf»), Messestand neu (Mockup, Foto WEGA/Immozionale), Printwerbung für Messen (wöchentliche Inserate, Flyer in den Büros, Ziel ältere Zielgruppe), Instagram (Reels mit Interviews von Fachleuten, Storys mit Umfragen, Fragerunden, Infoabend-Countdowns, beworbene Storys), Halloween-Videoflyer Basel, Grünblick-Flyer.
- **Print GOLDINGER:** Hausmagazin (halbjährlich; Inhalte mit dem Vorgesetzten festgelegt, Texte und Bilder von den Standorten, Layout von Yana, gedruckt, teils als Zeitungsbeilage; Ausgaben 2021–2023); Inserate WEGA 2022 (Wertschätzung der Immobilie in 5 Minuten am Stand; Hallen-/Standnummer in zwei Versionen widersprüchlich), Inserat Infoabende (Frauenfelder Woche, sieben Termine, mit St. Galler Kantonalbank), Inserat SCK-Clubmagazin 2023; Flyer «Tag der offenen Tür» Neubauprojekt Grünblick (Juli 2023); Mockup Bewertungsbroschüre (2022); Fahrzeugaufkleber (2022, Bestellung von Yana koordiniert); Fruchtgummi-Säckli als Giveaway (2022 gelb/schwarz, 2023 blau).
- **Digital GOLDINGER:** Social-Media-Posts 2021–2023 (u. a. «Stille Vermarktung», Kundenstimmen, Weihnachten, Infoabende, Hausmagazin, Tipps für Käufer, Immobilie im Alter); Instagram-Storys (Umfragen, Fragerunden, Infoabend-Countdowns, Presse-Reposts); Videos (nur als Screenshots, MP4 zu gross). ✅ Alle Feed-Posts von Yana gestaltet (Yana 06.10.2026).
- **Events:** Infoabende 2022/2023 (u. a. Romanshorn, Wil, Weinfelden, Arbon, Sargans, Frauenfeld), WEGA, Immozionale, Tag der offenen Tür Grünblick 2023.
- **Vorher/Nachher (für Redesign-Darstellung):** 1. **Messewände** (stärkstes Paar): alt «alt mässewnede.jpg» (waagrechtes Band, «Wir lieben Immobilien», Siegel «30 Jahre», Projektkacheln) → neu «wände neu.jpg» (Mai 2023, hochformatige, bildstarke Paneele in Blau/Weiss, CTA «Jetzt Immobilie direkt am Stand bewerten!», Projektpaneele, graue Felder für wechselnde Aushänge) + Mockup + Foto vom Stand. 2. Fruchtgummi-Säckli gelb/schwarz → blau. 3. Social-Posts: Entwicklung Gold-Blau → Blau-Weiss (siehe Social Media). Ältere Magazin- oder Inseratversionen zum Vergleich nicht gefunden → Yana fragen, ob es «vorher»-Versionen gibt.
- **Andere Auftraggeber/Projekte:** «Trailer Park – Street Food» komplette Markenidentität (Manual mit Farb-, Bild-, Schriftkonzept, Logo, Claim; Plakat, Becher, Food-Box, Mockups, Newsletter; 2021–2023) ✅ Projekt aus dem überbetrieblichen Kurs (Yana 04.10.2026; = Food-Truck-Konzept im Archiv), Yana findet es stark → aufnehmen, klar als Kursprojekt kennzeichnen; Details beim Schreiben im Material nachlesen; Halloween-Videoflyer Basel (Sa 28. Oktober 2023) = BAILA BASILEA ✅; eigenes Logo «Yana Senn» (2023, nicht angesehen).
- **Personen:** viele Storys/Posts mit Mitarbeitenden und Kundschaft → nicht ohne Einverständnis verwenden.

- ✅ **Yana 05.10.2026:** Bei GOLDINGER viele Videos gemacht (nicht nur WEGA); **Faltmappen neu gestaltet**; **Inserate neu gestaltet**; alles mit Redesign aufnehmen (Vorher/Nachher). GOLDINGER-Teil ausführlicher darstellen.
  - Videos in Drive «Goldinger/Inhalt 2024» (2023): «Immobilienverkauf» (Erklärvideo), «Stiller Verkauf» (Erklärvideo), «jahresvorsätze» (Reel), «Interview Samira» (Reel-Interview), mehrere Objekt-/Rundgangvideos (MP4/MOV, 18–53 MB; für die Website später komprimieren). Faltmappen: ✅ später gefunden (siehe Nachtrag Upload 05.10.2026). Inserate: ✅ alle aus Yanas Zeit, als Entwicklung gezeigt.
  - **Suche nach Design (05.10.2026, beide Goldinger-Ordner + Werbung-Baum + Thumbs.db + Volltextsuche):**
    - *Faltmappen:* bei der ersten Suche nicht gefunden; ✅ nach Upload von Yana gefunden (siehe Nachtrag unten).
    - *Vorher/Nachher Messewände (stärkstes Paar):* vorher 2019 = alte CI «GOLDINGER Immobilien Treuhand AG», weiss mit Goldlinie und Bordeaux (Wandpaneel «Arbon», Standfotos 2019 mit kleinen Objektplakaten); nachher 2022/2023 = durchgehend königsblaue Paneele («Jetzt Immobilie direkt am Stand bewerten», Neubauprojekte, Geschäftsbereiche), «wände neu.jpg», «Stand 2023.jpg» (Mockup).
    - *Vorher/Nachher Flyer:* vorher 2019 «Schnellbewertung A5» (blauer Balken, Goldlinie, Bordeaux-Titel) und Sunneberg-Flyer; nachher Infoabend-Flyer 2022 und Grünblick-Flyer 2023 (klares Blau-Weiss).
    - *Inserate:* alle aus Yanas Zeit (2022–2023), kein älteres GOLDINGER-Inserat in Drive. Entwicklung sichtbar: HEV 2022 textlastig → HEV 2023 und Infoabende 2023 mit klarem Blau-Weiss-System (Datums-Pills, Siegel «Eintritt frei», blaue Fusszeile mit Logo und Partnerbank). ✅ Keine älteren gefunden → als Entwicklung zeigen.
    - *Social Media:* Entwicklung innerhalb Yanas Zeit: Ende 2021 Gold/Senf + Blau (Canva) → 2022/2023 klares Königsblau-Weiss.
  - **Nachtrag Upload 05.10.2026 (Ordner Werbung/Print):**
    - *Faltmappe ✅ gefunden:* «Goldinger_Mappe_2022.pdf» (vorher) und «Goldinger_Mappe_2023.pdf» (nachher, Feb. 2023), je Aussen- und Innenseite, A4-Mappe mit Einstecklasche. **Vorher:** einzelne Felder mit unterschiedlichen Bildern (Altbau-Fassade mit Herbstlaub, Wohnraum), Text in schmaler blauer Spalte, Adressen als Block. **Nachher:** ein durchgehendes Panoramabild (moderner Neubau im Abendlicht) über Rücken, Vorder- und Rückseite, halbtransparente Textflächen, Standorte als Leiste oben, Innenseite «Unser Leistungsspektrum» neu gesetzt. Auch der Einleitungstext ist neu (u. a. «Mitarbeitende», «Kundinnen und Kunden»).
    - *Vergleich (Yana 05.10.2026: «vergleiche es einfach»):* **Gleich geblieben:** Format und Stanzform, Logo, Schriften (Frutiger, Helvetica Neue, Minion), Blau als Hauptfarbe, Mitgliedschaften. **Neu 2023:** ein durchgehendes Panoramabild statt zwei getrennter Bilder; Textflächen halbtransparent über dem Bild statt weisser Felder; Standorte als Leiste oben statt Block in der Mitte; Porträts und Text der Geschäftsleitung neu angeordnet; Innenseite neu gesetzt. **Texte:** alle Abschnitte neu formuliert (kundennäher, geschlechtergerecht: «Interessentinnen und Interessenten», «Mitarbeiterinnen und Mitarbeiter»; «Was dürfen wir für Sie tun?» bleibt).
    - *Darstellung im Portfolio:* als **Redesign der Faltmappe** (Vorher/Nachher, Aussen- und Innenseite). Formulierung: «neu gestaltet, Texte aktualisiert», ohne Textautorschaft zu behaupten.
    - *Flyer Wertermittlung:* vorher «Online Schnellbewertung KL V2» (2019, vor Yanas Zeit: Bordeaux-Titel, Diagramm) → nachher «Flyer Gutschein Wertermittlung FF 2023» (Jan. 2023, Klappkarte mit Antwortkarte, Teamfoto, goldener Gutschein).
    - *Flyer Infoveranstaltungen:* 2022 (weiss, Siegel, Teamfoto) → 2023 (Gebäudefoto als Hintergrund, blaue Diagonale, Banner «Eintritt frei», QR-Anmeldung). Beide aus Yanas Zeit → Entwicklung, kein Vorher/Nachher im engeren Sinn.
    - *Neubauprojekt Sonnenhof:* Flyer 2023 (Juni), Blau-Weiss-System mit Visualisierungen und QR-Code.
    - *Nicht geöffnet (≥ 6 MB):* «Maklerbroschüre Janette 2023» (persönliche Maklerbroschüre, Name nicht veröffentlichen), «Hausmagazin Februar 2023 final» (bekannt).
    - *Nicht verwenden:* «Hausmagazin.pdf» ist ein internes Kostenblatt (nicht das Magazin); Offerten, Rechnungen, Messewand Kradolf (Preise); Visitenkarte und HEV 2023 (direkte Telefonnummern von Personen, nur unkenntlich); Fotos mit erkennbaren Personen.

#### Case 6 · GOLDINGER Immobilien: Content, Campaigns & Print (2021–2023)
**Kernaussage ✏️:** Zwei Praxisjahre im Immobilienmarketing: Social Media, Fotografie, Video und Print für Verkauf, Events und Marke.

**Fakten ✅** (CV und altes Portfolio)
- Social-Media-Management (Instagram, Facebook, LinkedIn, YouTube), Redaktionspläne
- Posts, Reels, Stories (Erlebnisberichte, Fragerunden, Umfragen, Bewerbung der Infoabende), Mitarbeitervorstellungen, Infografiken
- **Immobilienvideos:** Aufnahmen, Rundgänge, Schnitt, Reels, Luftaufnahmen mit Drohne ✅
- **Interview-Reels** mit Fachleuten (Makler, Bewirtschafter)
- **Animierte Erklärvideos** ✅ = Yanas **IPA (Abschlussarbeit der Lehre)**
- **Hausmagazin** ✅ halbjährlich (gemäss altem Portfolio-Text): Inhalte mit Vorgesetztem festgelegt, Texte und Bilder von den Standorten, Layout von Yana, Druck, teilweise Zeitungsbeilage
- **Infoabende 2023:** Meta-Ads (Fokus Ostschweiz, 4 Wochen Laufzeit, Ziel Anmeldungen) und Printinserate in Ostschweizer Zeitungen (Offerte bis Übermittlung)
- **Tag der offenen Tür (TDOT) 2023:** Vermarktungsstrategie für schwer verkäufliche bzw. Spezialobjekte; Printinserate, Flyer in Büros, Instagram-Kampagnen über Meta; Organisation in Absprache mit Verkäufern
- **WEGA & Immozionale 2022:** Messewände neu gestaltet, Gummibärchen, Printstrategie (wöchentliche Inserate, Flyer)
- Print: Inserate, Broschüren, Bautafeln/Aussenplakate, Flyer, Texte
- Website-Pflege mit TYPO3
- Entwicklung und Analyse von Kampagnen, Evaluation von Partnern und Lieferanten

#### TEXT-ENTWURF «GOLDINGER Social Media, Reels und Immobilienvideos» (Frühere Projekte, Kachel 2) ✅ (Inhalt freigegeben, Bilder offen)
- **Stichworte:** Social Media · Reels · Immobilienvideo · Redaktionsplanung
- **Kurz:** Zwei Jahre Kanalbetreuung, von der Story bis zum Objektrundgang
- **Ausgangslage:** GOLDINGER war auf Instagram, Facebook, LinkedIn und YouTube präsent. Die Kanäle sollten regelmässig bespielt werden, Vertrauen in die Fachleute aufbauen und Objekte, Infoabende und das Hausmagazin bekannt machen.
- **Meine Rolle ✏️:** Ich betreute die Kanäle während zwei Jahren: Redaktionsplan, Gestaltung der Beiträge, Fotografie und Video bis zum Schnitt.
- **Umsetzung:** Beiträge zu Themen wie stille Vermarktung, Kundenstimmen, Tipps für Käufer oder Immobilie im Alter · Storys mit Umfragen, Fragerunden und Countdowns zu den Infoabenden, teils beworben · Reels mit Interviews von Fachleuten aus Verkauf und Bewirtschaftung, dazu Reels wie «Jahresvorsätze» · Objektvideos und Rundgänge, auch mit Luftaufnahmen per Drohne, gefilmt und geschnitten · Vorstellung neuer Mitarbeitender · Pflege der Website in TYPO3.
- **Entwicklung:** Ende 2021 noch Gold und Blau, ab 2022 ein klares Blau-Weiss im Stil des übrigen Auftritts (siehe «Redesigns Print»).
- **Bilder/Video 📌:** Auswahl Feed (Raster), Story-Beispiele, ein Objektvideo (komprimiert), ein Reel. Personen nur mit Einverständnis.
- ✅ Alle Feed-Beiträge von Yana gestaltet (Yana 06.10.2026). ✅ Luftaufnahmen mit Drohne von Yana (Yana 06.10.2026).

#### TEXT-ENTWURF «Halloween-Videoflyer» (Freelance, BAILA BASILEA) ✅ (Inhalt freigegeben, Video offen)
- **Stichworte:** Motion Design · Instagram Story · Event
- **Kurz:** Ein animierter Flyer für eine Halloween-Party in Basel
- **Ausgangslage:** Die Veranstalter einer Halloween-Party in Basel (28. Oktober 2023) suchten einen auffälligen Flyer für Instagram-Storys, der in wenigen Sekunden Datum, Ort und Stimmung vermittelt.
- **Meine Rolle ✅ (Yana 06.10.2026):** Als erster Freelance-Auftrag entwickelte, gestaltete und animierte ich den Videoflyer. Die Musik kam direkt über die Story-Funktion von Instagram dazu.
- **Bilder/Video 📌:** Videoflyer (Story-Format), ein Standbild. Logos von Partnerlokalen nicht hervorheben.

#### TEXT-ENTWURF «Trailer Park – Street Food» (Kursprojekt) ✅ (Inhalt freigegeben, Bilder offen)
- **Stichworte:** Markenidentität · Corporate Design · Kursprojekt
- **Kurz:** Eine komplette Marke für einen Food-Truck
- **Ausgangslage:** Im überbetrieblichen Kurs der Ausbildung entstand für einen fiktiven Food-Truck eine eigene Marke, vom Logo bis zur Verpackung.
- **Umsetzung ✏️ (neutral formuliert; Teamarbeit, Team nicht erwähnen, Yana 06.10.2026):** Logo, Claim, Farb-, Bild- und Schriftkonzept, zusammengefasst in einem Manual, dazu Plakat, Becher, Food-Box und Newsletter.
- **Kennzeichnung:** klar als Kursprojekt ✅.
- ✅ Fiktiver Auftrag; im Team erarbeitet, Team im Text nicht erwähnen (Yana 06.10.2026). Daher keine «ich»-Rolle, sondern neutrale Beschreibung.
- **Bilder 📌:** Logo, Manual-Seiten, Mockups (Becher, Food-Box, Plakat).

#### TEXT-ENTWURF «Animierte Erklärvideos» (GOLDINGER, Abschlussarbeit) ✅ (Inhalt freigegeben, Video offen)
- **Stichworte:** Animation · Storytelling · Abschlussarbeit
- **Kurz:** Zwei animierte Videos, die komplexe Abläufe einfach erklären
- **Ausgangslage:** Wer eine Immobilie verkaufen will, hat viele Fragen: Wie läuft ein Verkauf ab, und was bedeutet ein «stiller Verkauf»? GOLDINGER wollte das kurz und verständlich erklären, für die Website und Social Media.
- **Meine Rolle ✅ (Yana 06.10.2026: alles komplett selbst):** Als Abschlussarbeit meiner Lehre (IPA) entwickelte ich zwei animierte Erklärvideos, komplett selbst: vom Drehbuch über Storyboard und Illustrationen bis zu Animation und Ton.
- **Videos:** «Immobilienverkauf bei GOLDINGER» · «Stiller Verkauf»
- **Bilder/Video 📌:** beide Videos komprimiert einbinden, dazu Storyboard oder Standbilder.

#### TEXT-ENTWURF «GOLDINGER Infoabende und Tage der offenen Tür» (Frühere Projekte, Kachel 4) ✅ (Inhalt freigegeben, Bilder offen)
- **Stichworte:** Kampagnenplanung · Print · Meta Ads · Event
- **Kurz:** Kampagnen, die Menschen an Infoabende und in Neubauprojekte bringen
- **Ausgangslage:** GOLDINGER lud jedes Frühjahr zu kostenlosen Infoabenden rund um Immobilien im Alter, Steuern und Verkauf ein, an sieben Standorten in der Ostschweiz und gemeinsam mit den Kantonalbanken. Die Zielgruppe ist eher älter und liest vor allem Zeitung. Für Neubauprojekte und schwer verkäufliche Objekte kamen Tage der offenen Tür dazu.
- **Meine Rolle ✅:** Ich plante die Kampagnen und setzte sie um: von der Offertanfrage bei den Zeitungen über Gestaltung und Streuplan bis zu Anzeigen auf Meta und Storys auf Instagram.
- **Infoabende 2023:** Inserate als Serie in drei Formaten für mehrere Regionalausgaben, je mit der passenden Partnerbank · Flyer · Einladung mit Anmeldetalon und QR-Code im Hausmagazin · Meta-Anzeigen mit Fokus Ostschweiz während vier Wochen · Instagram-Storys mit Countdown. Schwerpunkt auf Print, weil die Zielgruppe wenig auf Social Media unterwegs ist.
- **Tag der offenen Tür 2023:** Vermarktung eines Neubauprojekts (Grünblick): Flyer (✅ Logo nicht von Yana, Yana 06.10.2026), Inserate, Flyer in den Büros, Instagram-Kampagne über Meta; Organisation in Absprache mit dem Verkauf.
- **Hinter den Kulissen:** Ablauf für Inserate (Offerte → Prüfung → Gestaltung → Gut zum Druck → Rechnungskontrolle) und Streuplan nach Kalenderwoche und Zeitung.
- **Bilder 📌:** Inserate-Serie Infoabende (drei Formate), Infoabend-Flyer 2023, Grünblick-Flyer (ohne Logo als eigene Leistung), Story-Beispiel ohne erkennbare Personen.
- Nicht verwenden: Preise, Namen und Telefonnummern von Mitarbeitenden, Fotos mit erkennbaren Gästen.

#### TEXT-ENTWURF «GOLDINGER Messen WEGA und Immozionale» (Frühere Projekte, Kachel 5) ✅ (Inhalt freigegeben, Bilder offen)
- **Stichworte:** Messestand · Print · Giveaway · Video
- **Kurz:** Ein neuer Messeauftritt für die regionalen Publikumsmessen
- **Ausgangslage:** GOLDINGER war jedes Jahr an der WEGA und an der Immozionale vertreten. Der bisherige Stand stammte aus früheren Jahren und zeigte vor allem viele kleine Objektplakate. Gleichzeitig sollte die eher ältere Zielgruppe schon vor der Messe erfahren, dass sie am Stand ihre Immobilie bewerten lassen kann.
- **Meine Rolle ✅:** Ich gestaltete die Messewände neu, entwarf ein Mockup des Stands, plante die Werbung vor der Messe und gestaltete die Fruchtgummis als Giveaway.
- **Umsetzung:** Königsblaue Paneele mit klaren Botschaften wie «Jetzt Immobilie direkt am Stand bewerten», Neubauprojekte und Geschäftsbereiche (2022/2023) · Inserate in den Wochen vor der Messe mit dem Angebot einer Immobilien-Bewertung in fünf Minuten am Stand, dazu Flyer in den Büros · Fruchtgummis in eigener Form und Grafik (2022 gelb/schwarz, 2023 blau; zusätzlich separat im Case Giveaways) · (✅ keine Videos an den Messen, Yana 06.10.2026).
- **Vorher/Nachher:** siehe Kachel «Redesigns Print» (Messewände 2019 → 2022/2023).
- **Bilder 📌:** Standfoto bzw. Mockup 2023 (ohne Personen), Wände neu, Inserat WEGA 2022, Fruchtgummi-Säckli.
- Nicht verwenden: Preise (Wand «Kradolf»), Rechnungen, Anmeldungen, Fotos mit erkennbaren Gästen.

#### TEXT-ENTWURF «GOLDINGER Redesigns Print» (Frühere Projekte, Kachel 7) ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
- **Stichworte:** Redesign · Print · Corporate Design
- **Kurz:** Faltmappe, Flyer, Inserate und Messewände in einer klaren Linie
- **Ausgangslage:** Viele Printmittel von GOLDINGER stammten aus früheren Jahren und wirkten uneinheitlich: weisse Felder mit kleinen Bildern, Bordeaux-Titel, Goldlinien und teils noch der alte Firmenname «Immobilien Treuhand AG».
- **Meine Rolle ✅:** Ich gestaltete die bestehenden Printmittel neu und brachte sie in eine gemeinsame Linie: grosse Bilder, kräftiges Blau, klare Typografie und gut sichtbare Handlungsaufforderungen wie QR-Code, Anmeldung oder Gutschein.
- **Vorher/Nachher:**
  - *Faltmappe:* 2022 → 2023, ein durchgehendes Panoramabild statt getrennter Felder, Textflächen über dem Bild, Innenseite neu gesetzt, Texte aktualisiert.
  - *Flyer Wertermittlung:* 2019 → 2023, aus dem Flyer mit Diagramm wurde eine Klappkarte mit Antwortkarte und Gutschein.
  - *Messewände WEGA:* 2019 → 2022/2023, königsblaue Paneele mit klaren Botschaften statt kleiner Objektplakate.
  - *Inserate:* Entwicklung 2022 → 2023, von textlastigen Anzeigen zu einem System mit Datumsfeldern, Siegel und blauer Fusszeile; die Infoabende-Serie in drei Formaten für mehrere Regionalausgaben.
- **Hinter den Kulissen:** Ablauf für Inserate von der Offerte bis zum Gut zum Druck und ein Streuplan nach Kalenderwoche und Zeitung.
- **Bilder:** Vorher/Nachher-Schieberegler pro Paar (Code-Phase 📌).

**Videos (Ergänzung Kachel 2/3, Funde Drive 05.10.2026):** zwei animierte Erklärvideos («Immobilienverkauf bei GOLDINGER», «Stiller Verkauf»), Reels (u. a. «Jahresvorsätze», Interview-Reel mit einer Fachperson), mehrere Objekt- und Rundgangvideos. Für die Website komprimieren; Person im Interview-Reel nur mit Einverständnis zeigen.

**Offen ❓**
- Altes Portfolio und Videos vom anderen PC 📌
- Alte Texte sind teils sehr blumig («faszinierend», «renommiert») und werden im neuen Ton neu geschrieben.

#### TEXT-ENTWURF Case «Fotografie» (CP Pump Systems) ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
- **Stichworte:** Reportage · Menschen bei der Arbeit · Bildbearbeitung
- **Kurz:** Bilder für Broschüren, Website, Messen und Wände, von der Aufnahme bis zur Druckdatei
- **Meine Rolle ✏️:** Ich fotografiere Produkte, Gebäude, Events, Messeauftritte und Mitarbeitende und bearbeite die Bilder bis zum fertigen Einsatz auf der Website, in Print und auf Social Media (Service-Text ✅).
- **Beispiele (Drive):**
  - *Mitarbeitende bei der Arbeit (Aug. 2026) ✅ von Yana:* PFA-Auskleidung am Ofen, CAD und Simulation, CAM-Programmierung; in Farbe und Schwarzweiss bearbeitet und als Wandbilder gedruckt. Kantinenplakate mit neuen Fotos ✅.
  - *Reportage Maschinenlieferung (Mai 2026):* neue Bearbeitungszentren werden per Kran und Tieflader angeliefert und eingebracht; rund 30 ausgewählte Bilder (Ordner «FAV») plus Videoclips. ✅ von Yana fotografiert und gefilmt (Yana 05.10.2026). ❓ Verwendung (News-Beitrag, Social Media)?
  - *Produktfotos:* ✅ teils von Yana, die meisten gab es schon vorher (Yana 05.10.2026) → **gemeinsam durchgehen**, welche von ihr sind; nur diese zeigen.
- **Weiterbildung:** 2026 Fotografie-Workshop mit Bildbearbeitung (2 Tage, vor Ort bei CP) ✅.
- **Bilder 📌:** Auswahl später; erkennbare Personen nur mit Einverständnis.

#### TEXT-ENTWURF Case «Raumgestaltung: die Marke im Gebäude» (CP Pump Systems) ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
- **Stichworte:** Raumkonzept · Wandgestaltung · Fotografie · Produktion
- **Kurz:** Sitzungszimmer, Lounge und Abteilungen im Erscheinungsbild von CP
- **Ausgangslage:** Die Marke CP sollte nicht nur an Messen und in Broschüren sichtbar sein, sondern auch im eigenen Gebäude: dort, wo Kundschaft empfangen wird, und dort, wo die Mitarbeitenden täglich arbeiten.
- **Meine Rolle ✅:** Ich gestaltete die Wände der Räume, wählte zusammen mit der Möbelfirma die Einrichtung nach Farbpaletten aus und organisierte die Lieferung. Für die Abteilungen fotografierte ich die Mitarbeitenden bei der Arbeit und gestaltete daraus Wandbilder und Paneele. Die Plakate in der Kantine aktualisierte ich mit neuen Fotos und liess sie als Stoffbilder produzieren.
- **Sitzungszimmer und Lounge (2024):** Wandbild mit Birkenwald und dem Claim «cleaner pumps, cleaner planet™» als Digitaldruck-Tapete, Logo- und Claim-Paneele im Fensterband; mehrere Layout-Varianten bis zur finalen Version. Möbel in Grün- und Blautönen passend zum Wandbild, ausgewählt nach Showroom-Besuch und Renderings der Möbelfirma.
- **Abteilungen (2026):** Wandbilder und Paneele für die Abteilungen, unter anderem PFA-Auskleidung, CAM sowie Technik und Entwicklung: eigene Fotos, bearbeitet in Farbe und Schwarzweiss, kombiniert mit Produkt- und Betriebsbildern und Grafiken wie der Weltkarte.
- **Kantine (2026) ✅ (Yana 05.10.2026):** bestehende Plakate mit Mitarbeitenden von Yana aktualisiert, mit neuen, von ihr geschossenen Fotos, und als Stoffbilder produziert.
- **Bilder 📌:** Raum vorher (Foto vorhanden), Layout-Varianten, Rendering, fertiger Raum (❓ Fotos folgen, Yana 06.10.2026), Paneele der Abteilungen. Erkennbare Mitarbeitende nur mit Einverständnis.
- Nicht verwenden: Preise, Offerten, Namen von Lieferanten und Mitarbeitenden.

#### TEXT-ENTWURF Case «Infografiken & Karten» (CP Pump Systems) ✅ (Arbeitsstand freigegeben, Yana 06.10.2026; Bilder offen)
- **Stichworte:** Informationsdesign · Illustration · Mehrsprachigkeit
- **Kurz:** Weltkarte und Firmengeschichte als wiederverwendbare Grafiken für Broschüren, Messen und Website
- **Ausgangslage:** CP Pump Systems ist mit Standorten, Tochterfirmen und Partnern weltweit tätig und blickt auf eine lange Firmengeschichte zurück. Beides sollte auf einen Blick verständlich sein, in mehreren Sprachen und für ganz unterschiedliche Formate.
- **Meine Rolle ✅ (Regel: Design ab 2024 von Yana; Fakten Yana 03.10.2026: neue Grafiken wie Weltkarte und Zeitstrahl):** Ich entwickelte die Weltkarte und den Zeitstrahl, von den ersten Entwürfen bis zu den fertigen Sprachversionen.
- **Weltkarte:** Standorte, Tochterfirmen und Niederlassungen (Schweiz, Deutschland, Frankreich, USA, Republik Korea, Thailand) sowie Mitarbeitende in weiteren Ländern, mit Legende «CP Pump Systems» und «Partner». Erste Fassung Dez. 2025, laufend aktualisiert (Stand 2026). Mehrere Farbvarianten getestet (Blau, Grün, Hellgrün, Grau, Schwarz) und je nach Einsatz gewählt: flächig in CP-Blau für Messewände, als feines Punktraster in Grün oder Grau für Broschüren. Eigene Fassung mit allen Messen. Sprachversionen DE, EN, FR, PL u. a. Eingesetzt auf Messewänden (u. a. Dortmund 2026, Le Havre, ChemUK, Martigues), in Broschüren und auf der Website.
- **Zeitstrahl «Firmengeschichte»:** zwei A4-Seiten, «passioniert – swiss made – innovativ», Meilensteine von der Gründung bis heute als Schlangenlinie mit grünen Jahreszahlen und Bildern (Produkte, Maschinen, Gebäude, Flaggen für neue Märkte). Im Company Profile eingesetzt. Sprachversionen DE, EN, FR, IT, PL, CN sowie US-Version; Stand bis 2026, Ausblick bis 2027.
- **Weitere ✏️:** Icons und Infografiken für das Broschürenkonzept (wiederkehrende Elemente), Explosionszeichnung (Molten Sulphur).
- ✅ **Wandbilder der Abteilungen (Yana 05.10.2026):** «PFA», «CAM», «Technik Entwicklung» hängen als grosse Bilder an den Wänden der jeweiligen Abteilungen; **Fotos von Yana geschossen**, bearbeitet (Farb- und Schwarzweiss-Versionen) und für den Druck aufbereitet (Aug. 2026). Motive: Mitarbeitende an der Arbeit (PFA-Auskleidung am Ofen, CAD/Simulation in Technik und Entwicklung, CAM-Programmierung). → passt besser zu **Fotografie** bzw. **Raumgestaltung bei CP** als zu Infografiken. Erkennbare Mitarbeitende → nur mit Einverständnis zeigen.
- ✅ «20260825_Finale Version_CP_Pumpen_Panels» (InDesign, Aug. 2026) = die Wandpaneele der verschiedenen Abteilungen (Yana 05.10.2026); kombiniert eigene Fotos, Produktbilder, Betriebsfotos und Grafiken wie die Weltkarte. Gehört zusammen mit den Wandbildern zu «Raumgestaltung bei CP».
- **Bilder 📌:** Weltkarte in zwei Varianten (Messewand blau, Broschüre Punktraster), Farbvarianten als Prozessbild, Zeitstrahl Seite 1, Stand mit Weltkarte.
- ✅ Thailand = Niederlassung (Branch), nicht Tochterfirma (Yana 05.10.2026); Songkran-Text angepasst.

#### Case «Werbung: Print & Digital» ✏️ (Name-Vorschlag, ersetzt «Anzeigen & Fachartikel»; Yana 04.10.2026: zu eng)
- EN: «Advertising: Print & Digital»
- Unterteilung innerhalb des Cases: **Print** (Anzeigen in Messekatalogen und Fachzeitschriften) · **Fachartikel** (redaktionelle Beiträge) · **Digital** (E-Mail-Banner, Web-Banner, Signatur-Anzeigen, Sammelbanner, Social Ads)
- Abgrenzung: Broschüren und Factsheets bleiben eigener Case; Messe-Banner werden hier nur gebündelt gezeigt, Details stehen bei den Messen.
- Quelle ✅ (Yana 04.10.2026): Drive-Ordner «Werbung» mit «Print» und «Digital», Rest lose im Hauptordner; dazu Material aus den Messe-Ordnern (Anzeigen, Banner) und aus Yanas altem Portfolio (GOLDINGER, Print). Claude ordnet zu.
- Broschüren gehören thematisch zu Print (Yana) → beim Sortieren entscheiden, ob «Broschüren und Factsheets» eigener Case bleibt oder Teil von Print wird.
- **Funde Drive «Werbung» (04.10.2026) ✏️** (alle Unterordner gelesen; nicht verwendet: Preise, Rechnungen, Kontaktdaten, Passwörter im Deck «Konzept News» → nie veröffentlichen)
  - *Zuordnung:* CP-Material 2020–2023 (Redaktionspläne, Agentur-Briefing, Treppenhaus-Layouts) ist von SAB bzw. Agentur, vor Yanas Zeit → nicht verwenden. GOLDINGER «Team KL» und «Arbon KV» (2019) vor Yanas Zeit → nicht verwenden. Presse-Korrespondenz 2025/26 lief über die Leiterin (NIM), Antworten teils vom Verkauf → ✅ nicht zeigen (EUREKA ausgelassen). Design ab 2024 grundsätzlich von Yana (Regel).
  - *Print-Anzeigen CP:* World Fertilizer (Palladian Publications), ½ Seite quer, EN, Sept. 2025, «Sulphur at the perfect temperature» (Schwefel-Foto, MKP, Swiss Made, QR-Code, «cleaner pumps, cleaner planet»); drei Entwurfsvarianten mit anderen Headlines («Keeping molten sulphur warm», «Always warm. Always liquid. Always safe.»); Buchung zweier Ausgaben 2025, eine mit Artikel.
  - *Print-Anzeigen GOLDINGER:* HEV-Magazin A4 2022 («Mit wenigen Klicks am Ziel»: neue Website, Online-Bewertung, Ratgeber, 35 Jahre) und 2023 («Die drei wichtigsten Ratgeber für Immobilieneigentümer»); WEGA 2022; Infoabende 2023 als Serie in drei Formaten für mehrere Regionalausgaben (mit St. Galler und Thurgauer Kantonalbank).
  - *Fachartikel/PR CP:* EUREKA Flash Info n°118 (März 2026, FR) «CP pompes optimise la fiabilité de ses pompes verticales» ✅ auslassen (Yana 05.10.2026); Chemical Engineering (April 2026, EN), Q&A-Antworten zu Pumpentrends (Entwurf vom Verkauf → ✅ nicht zeigen); Blogbeitrag «Sealless Magnetic Drive Pumps for Acidic Pond Water» (Mai 2026, EN/FR/DE, Referenz Düngemittelwerk, 3 Pumpen).
  - *Digital CP:* LinkedIn-Texte zu FLA Miami, P&V Dortmund, ChemE Houston, Expoquimia (2026); Grafik «Happy Birthday Schwiiz!» (1. August 2026); Fotoserie einer 13 Jahre alten Pumpe (zerlegte Teile) für LinkedIn; Konzept «News» (Feb. 2026: Kanalrollen, Content-Säulen, Workflow; enthält Passwörter → nie zeigen); Redaktionsplan 2026.
  - *Digital GOLDINGER:* Posts Infoabende 2021, Hausmagazin-Titelbild Sept. 2021.
  - *Broschüren/Print CP:* **Molten-Sulphur-Broschüre** (EN, 8 Seiten A4, Sept. 2026, gelbes Dreiecksmuster, Explosionszeichnung; stark) + 2-seitiger Flyer + US-Letter-Version (vermutlich für Tampa); Flyer «Sofort verfügbare Pumpensysteme» (DE/EN, April 2026, 16 Einheiten ab Lager, 1–2 Wochen Lieferzeit); **Weltkarte der Standorte** (A3, DE/EN/FR u. a., Dez. 2025–Sept. 2026); **Firmengeschichte als Zeitstrahl** (2 Seiten, sieben Sprachen, Aug.–Okt. 2026, evtl. noch in Arbeit); Songkran-Grusskarte CP Thailand (Jan./Feb. 2026: Skizzen, Referenzen, 75 Karten bestellt; finale Datei fehlt); Pumpen-Icons (2024/2025), Explosionszeichnungen.
  - *Print GOLDINGER:* Infoabende-Flyer 2022 (A5, mit TKB); Grünblick-Flyer (2023; ✅ Logo nicht von Yana); Fruchtgummi-Säckli; Visitenkarte (2022); Messewand-Material 2023 (Seitenpaneel, Wandtext Kradolf, Standfoto «Stand 2023.jpg» ohne Personen); Hausmagazin als Zeitungsbeilage (Feb. und Sept. 2022).
  - *Stärkste Stücke:* Molten-Sulphur-Serie (Broschüre, Anzeige, Flyer) · Lieferzeiten-Flyer · Weltkarte und Zeitstrahl · HEV-Anzeige 2023 · Infoabende-Serie · Grünblick-Flyer · 1.-August-Grafik.
  - *Vorschlag Gliederung Case «Werbung: Print & Digital»:* Print-Anzeigen (CP + GOLDINGER) · Fachartikel & PR (CP) · Digitale Werbung (Banner, Social, Signaturen). Molten-Sulphur-Serie (✅ keine Kampagne, sondern zusammengehörende Werbemittel) (Anzeige → Roll-up → Rückwand → Broschüre) prominent zeigen. Weltkarte, Zeitstrahl, Icons → Case «Infografiken & Karten». Songkran → kleine Card.
#### TEXT-ENTWURF Case «Werbung: Print & Digital» (CP Pump Systems) ✅ (Inhalt freigegeben, Bilder offen)
- **Stichworte:** Anzeigen · Kampagne · Banner · Anwendungsbericht
- **Kurz:** Eine Botschaft, viele Formate: von der Fachzeitschrift bis zur E-Mail-Signatur
- **Ausgangslage:** CP Pump Systems wirbt dort, wo Fachleute aus Chemie, Düngemittel- und Prozessindustrie lesen und sich informieren: in Fachzeitschriften, Messekatalogen, auf Fachportalen und per E-Mail. Jede Anzeige muss in Sekunden zeigen, welches Problem die Pumpen lösen.
- **Meine Rolle ✏️ (Regel: Design ab 2024 von Yana):** Ich gestalte die Anzeigen und digitalen Werbemittel von der ersten Headline-Variante bis zur Druckdatei und passe sie für jedes Format und jede Sprache an.
- **Serie «Molten Sulphur» (2025–2026; ✅ keine Kampagne, Yana 06.10.2026):** Anzeige in World Fertilizer «Sulphur at the perfect temperature» (Sept. 2025, drei Headline-Varianten im Entwurf) → Roll-up → Messe-Rückwand «Keep Your Molten Sulphur Flowing» (CRU Berlin 2026) → Broschüre, Flyer und US-Letter-Version (Sept. 2026) Eine Botschaft über mehrere Werbemittel.
- **Weitere Print-Anzeigen:** Katalog-Anzeigen der Messen (u. a. Petrochymia, ChemUK); Flyer «Sofort verfügbare Pumpensysteme» (DE/EN, April 2026).
- **Digital:** E-Mail-Banner und -Signaturen zu jeder Messe, Web-Banner für Messeportale, Sammelbanner «Nos prochains salons professionnels» (DE/EN/FR, Sept. 2026), LinkedIn-Grafiken und -Texte (u. a. «Happy Birthday Schwiiz!» zum 1. August).
- **Anwendungsbericht ✅ (Yana 05.10.2026: von Yana, fachliche Unterstützung beim Text durch das Verkaufsteam):** «Dichtungslose Magnetkupplungspumpen für die Förderung von saurem Prozesswasser» (Website-Blog, April/Mai 2026, DE/EN/FR): Referenzprojekt aus der Düngemittelproduktion, drei MKP-Pumpen für ein Pondwasser-Rückführungssystem; Aufbau Ausgangslage → Lösung → Gründe → technische Kennwerte. Formulierung im Case: «Den Anwendungsbericht verfasste ich mit fachlicher Unterstützung des Verkaufsteams und veröffentlichte ihn in drei Sprachen.» ✅ (Yana 05.10.2026: selbst in DE/EN/FR auf der Website veröffentlicht) EUREKA auslassen ✅.
- **GOLDINGER-Inserate** stehen im Case «Redesigns Print» (Frühere Projekte), nicht hier.
- **Bilder 📌:** Anzeige World Fertilizer mit Headline-Varianten, Kampagnenstrecke Molten Sulphur (Anzeige, Rückwand, Broschüre nebeneinander), Banner-Set einer Messe, Sammelbanner.
- 📌 GOLDINGER: viele Redesigns von Yana → als **Vorher/Nachher** zeigen (Idee Yana 04.10.2026).
- ✅ Yanas altes Portfolio liegt im GOLDINGER-Ordner in Drive → als Quelle nutzen, Inhalte je nach Eignung übernehmen. Ablage ist nicht sauber sortiert → Claude sucht passende Sachen selbst zusammen.

#### Neu ✅ (Yana 05.10.2026): Raumgestaltung bei CP
- Sitzungszimmer neu eingerichtet (2024): Möbel ausgesucht, Lieferung organisiert, Wandgestaltung gestaltet (Layouts von Yana ✅); Auswahl nach Farbpaletten, zusammen mit der Möbelfirma. Ein weiteres Zimmer ebenso (laut Ideenskizze Lounge). ❓ Fotos vom fertigen Raum.
- Einordnung ✅ (Yana 05.10.2026): **eigener Case** «Raumgestaltung: die Marke im Gebäude», siehe Text-Entwurf unten.
- Hinweis: Im Ordner «Werbung» lag «Bild_Sitzungszimmer_DEF.png» (0 Byte, leer) und Treppenhaus-Layouts von 2023 (SAB/Agentur, nicht Yana).

#### Funde Raumgestaltung Sitzungszimmer (Drive «Werbung», 05.10.2026) ✏️
- 2024: Wandgestaltung über Fella (Offerte Mai 2024, Projekt «Sitzungszimmer», adressiert an Yana): Digitaldruck-Tapete 4,33 × 2,53 m, Montage vor Ort, optional magnetisches Whiteboard unter der Tapete.
- Layouts (Juni/Juli 2024): Foto des bestehenden Raums + Layout 1–3; Birkenwald-Wandbild mit «cleaner pumps, cleaner planet™», Logo- und Claim-Paneele im Fensterband (V2).
- Möbel über Haworth: Ideenskizze für zwei Räume (Jan. 2024), Showroom-Besuch Zürich (Feb. 2024), Stuhlübersicht, Renderings (Mai 2024: Lounge vor dem Birkenwald-Wandbild mit hellgrünen Stühlen, Sitzungszimmer mit grünen Stühlen und blau-grünen Wandpaneelen), Auftrag Juli 2024, Lieferung Juli/Aug. 2024 (Lieferkoordination durch Yana). Möbelauswahl laut E-Mails mit CEO und SAB.
- ✅ Layouts der Wandgestaltung von Yana (Yana 05.10.2026). ❓ Fotos vom fertigen Raum (für Vorher/Nachher)?
- **Kantinen-Plakate (Update 2026):** Agentur-Original (2021–2024) → interne Aktualisierungen Jan.–Mai 2026 mit neuen Mitarbeitenden → Produktion als 5 Stoffbilder 895 × 1280 mm (Offerte Fella Juni 2026 an Yana). Viele erkennbare Mitarbeitende → nur mit Einverständnis zeigen.

### 6.2 Kleinere Cards
- **Digital & Web, CP:** Craft CMS (Updates, Content, Bilder, Formulare), Newsletter und Social via Zoho One, LinkedIn/Facebook, Blogposts
- **Songkran Greeting Card:** ✅ 2026, Grusskarte für die Niederlassung in Thailand, komplett von Yana (siehe Text-Entwurf)
- **Company Tip Game** 🔒: nur erwähnen
- **Animated Explainer Videos** (GOLDINGER, IPA ✅) eigene Card
- **BAILA BASILEA 2023:** Videoflyer für die Instagram Story einer Halloween-Party in Basel ✅ **Freelance-Auftrag** (erster Freelance-Beleg)
- **Flyer:** TDOT GOLDINGER, Skatepark-Eröffnung ❓ (für wen?)
- **Visual Content:** Infografiken, World Maps, Timelines, Zahlenstrahlen, Icons, Fotografie (Mitarbeitende, Gebäude, Outdoor, Event, Messe, Exponate)

### 6.3 Archiv / eventuell weglassen ❓
- Food-Truck-Marketingkonzept Romanshorn (überbetrieblicher Kurs) → ✅ wird aufgenommen als «Trailer Park – Street Food» (Kursprojekt), siehe Funde GOLDINGER-Ordner
- Logo ÜK (Gruppenarbeit)
- «Webdesign» (unklar, was gemeint ist)

---

## 7. Werdegang & Fakten

| Zeitraum | Station | Status |
|---|---|---|
| 01/2018 – 08/2019 | IT-Support (Teilzeit), V-ZUG AG | ✅ (Yana 06.10.2026: Teilzeitstelle) |
| 08/2019 – 07/2023 | Lehre Mediamatikerin EFZ, SBW Neue Medien (2 Jahre Schule, 2 Jahre Praxis) | ✅ (Endmonat bestätigt, Yana 06.10.2026) |
| 2019 – 2022 | Berufsmaturität BM1, Richtung TALS (Technik, Architektur, Life Sciences), parallel zur Lehre | ✅ |
| 08/2021 – 08/2023 | GOLDINGER Immobilien AG, Praktikum Marketing / Mediamatikerin | ✅ |
| 01/2024 – heute | CP Pump Systems, Mitarbeiterin Marketing & Kommunikation | ✅ |
| 01/2026 | **Praxisbildnerin**, zB. Zentrum Bildung, Baden (Seminar mit Kursbestätigung) | ✅ |

**Sprachen ✅:** Deutsch und Schweizerdeutsch (fliessend), Englisch C1, Französisch B1 (DELF B1 ✅, Yana 06.10.2026), 
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
- LinkedIn: `https://www.linkedin.com/in/yana-senn-331436173` ✅ (Yana 06.10.2026; Zusatz «?originalSubdomain=ch» weggelassen)
- Telefon: ✅ nicht auf der Website; Kontakt per E-Mail (yana.senn1@gmail.com), Telefon nur auf Anfrage (Yana 06.10.2026)
- CV-Download: ✅ ja, vorerst einbauen (Yana 06.10.2026; kann später wieder entfernt werden). 📌 Aktuellen Lebenslauf als PDF von Yana nötig; vor dem Hochladen private Angaben prüfen (Adresse, Geburtsdatum, Telefon).

---

## 9. Merkliste für später 📌
- ✅ **Bild-Regeln (Yana 06.10.2026):** pro Projekt **wenige, starke Bilder (max. 3–4)**; Erzählung **«Idee → Umsetzung → Detail»** (Skizze, Plan, Mockup oder Entwurf neben dem fertigen Ergebnis, gerne als Schieberegler); **keine erkennbaren Gesichter** (Personen von hinten sind okay, sonst unscharf/zuschneiden); Druckdateien von Wänden, Panels, Folien, Roll-ups als **Mockup**, ergänzt durch einen Ausschnitt, wo sie im Einsatz sind.
- ✅ **Texte bleiben änderbar (Yana 05.10.2026):** Freigegebene Texte (✅) gelten als Arbeitsstand. Wenn die Website im Gesamtbild steht, gehen wir alle Texte nochmals durch und passen an, was nicht gefällt.

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

- 📌 Arbeitsvertrag (Nebenbeschäftigung, Zeigen von Firmenarbeiten) prüfen: ✅ vorerst ausgelassen (Yana 06.10.2026).
- ✅ ~~Bildrechte prüfen~~ – entfällt (Yana 06.10.2026): Fotos von SBW/CP werden nur gezeigt, nicht als eigene Fotos ausgegeben und nicht beworben.
  - YouTube-Video (Design-Inspiration): https://www.youtube.com/watch?v=hTwbCmZhFNA
    Screenshot erhalten (Hero «I'm a Coder.»): sehr grosse fette Grotesk-Headline, ein Wort kursiv in Akzentfarbe (Terracotta), freigestelltes Portrait vor Himmel-Collage, Name und Rolle rechts mit Akzentlinie, runder Button «Hire Me», abgerundeter Rahmen, Akzentfarben-Varianten Terracotta / Salbei / Blau / Rost. ❓ Welche Elemente gefallen Yana?
  - https://www.louisplant.ch/ (Design)
  - https://www.oliviahug.ch/ (Design)
  - https://www.pascalfrey.ch/ (nur Inhalt interessant, nicht Design)
- [ ] **Lebenslauf als PDF** für den Download (Yana liefert; Claude prüft private Angaben).
- [ ] **Produktfotos durchgehen:** gemeinsam mit Yana bestimmen, welche Produktfotos von ihr sind (die meisten gab es schon vorher). Service-Text «Ich fotografiere Produkte …» bleibt ✅.
- [ ] **Fotos Sitzungszimmer und Lounge (fertig eingerichtet)** in Drive hochladen – Yana macht das am 06.10.2026; Claude erinnert, falls nichts kommt.
- [ ] **Altes GOLDINGER-Portfolio** und Videos vom anderen PC übertragen
- [ ] **Hero-Portrait** für die Freistellung (Stil wie im YouTube-Screenshot): ruhiger Hintergrund, gute Auflösung, Kopf und Schultern
- [ ] **Praxisbildnerin:** betreut Yana selbst Lernende bei CP? (nur erwähnen, wenn ja)
- [ ] **Fotografie** ✅ als Kompetenz: in der Ausbildung gelernt, zusätzlich 2026 ein Fotografie-Workshop bei CP (2 Tage, vor Ort bei CP): Auffrischung und Post-Production bzw. Bildbearbeitung ✅. ~~Keine Fotos von Menschen zeigen~~ → ✅ geändert (Yana 05.10.2026): Mitarbeitende bei der Arbeit vorerst aufnehmen, nur mit Einverständnis; Porträts weiterhin nicht. Zeigbar: Produktfotos nur die von Yana (✅ die meisten gab es schon vorher; gemeinsam durchgehen), Reportage Maschinenlieferung, Mitarbeitende bei der Arbeit, eventuell Gebäude, Details. ✅ Eigener Service «Fotografie» (allgemein) und eigene Kachel im Portfolio.
- [ ] **Persönliches später einbauen:** künstlerische Begabung, AI
- [ ] **Messematerial als eigenes Thema (Kategorie oder Abschnitt) ✅ Fakten von Yana 04.10.2026:** Neben Print hat Yana auch Messemöbel und -material entwickelt: Konzept für die Möbel, Messebox(en), Transportboxen, Roll-ups, Messeaufsteller. CP-Podeste: lange vor den Phase-2-Messen hergestellt, Yana war mit dem Hersteller in Kontakt (Hersteller noch bestätigen; im Transkript unklar), später punktuell Anpassungen und Nachbestellungen, z. B. ein Podest mit Ersatzteilen (evtl. folgt mehr). Gilt für alle Messen; bei der Erfassung der Messen nicht einzeln aufführen, erst nach dem Messe-Durchgang ausarbeiten.
  - Vorschlag ✏️ (04.10.2026): kein eigenes Projekt, sondern ein Abschnitt «Messesystem & Messematerial» innerhalb von Messen & Events. Bestehende Punkte «Messeboxen USA» und «Ein Messesystem für die USA» dort zusammenführen. In den einzelnen Messe-Einträgen das Material nur kurz nennen (z. B. «unsere CP-Podeste»), die Details stehen einmal im Abschnitt → nichts doppelt.
  - *Textentwurf ✏️ (04.10.2026, neutraler Ton, aus den Fakten der Sammelliste):*
    - «Hinter den einzelnen Auftritten steht ein Messesystem, das über Jahre gewachsen ist. Für die USA entstand eine aufklappbare Standbox mit Birkenwald-Motiv, die als Bühne mitten auf dem Stand steht, dazu eine Box für die Möbel. Beide lagern zwischen den Messen in den USA: Für kleinere Auftritte holen die Verkäufer Broschüren und Geschenke direkt im Lager ab, für grössere reist die ganze Box an die Messe.»
    - «In Europa bilden weisse CP-Podeste das Rückgrat der Stände. Sie tragen die Exponate, bieten Platz für Broschüren und wurden laufend weiterentwickelt, zuletzt mit abschliessbaren Türen. Pflegeregeln im Messebriefing sorgen dafür, dass sie lange halten. Dazu kommen Roll-ups für Unternehmen, Produkte und einzelne Anwendungen, Prospektständer, eine Standkabine, Tischtücher, Namensschilder und eine Büromaterialbox, die jedes Standteam mit allem Nötigen ausstattet.»
    - «Für den Transport entstanden massgeschneiderte Kisten, für den Aufbau eine Anleitung, mit der das Team den Stand selbst stellen kann.»
  - *Meine Aufgaben ✅ (Yana 05.10.2026: «soweit so gut», plus Möbel):* Konzept des Messesystems USA · Gestaltung der Standbox · Anfrage und Abstimmung der Standbox mit einem Schweizer Kistenbauer · Auswahl und Kauf der Möbel · Organisation des Lagers · Kontakt mit dem Hersteller der Podeste und Weiterentwicklung · Roll-ups · Transportkisten · Aufbauanleitung · Pflegeregeln im Briefing
  - *Funde Drive «TPS Houston 24/Stand» (05.10.2026):* **Standbox = Messekabine nach Mass** (Angebot Juni 2024 an Yana nach Telefonat, von ihr intern weitergeleitet): leichte weisse Tischlerplatten, Tür mit Riegelschloss, verstellbare Tablare, aufklappbarer Tisch; dazu eine passende **Transportkiste** aus Dreischichtplatten. **Möbel gekauft, nicht gemietet** (Juni 2024, Bestellung u. a. auf Yanas Namen): weisse Barhocker, weisse Tische, weisse Stühle und zwei runde weisse Stehtische; alles in Weiss passend zur Standbox. Nicht verwenden: Preise, Lieferanten- und Kontaktnamen.
  - *Seitenentwurf Highlight «Mobiler Messestand für die USA» ✏️ v1 (06.10.2026):* `docs/entwuerfe/messestand-usa.html`, Artifact https://claude.ai/artifact/5CenZNzAZtaKJN37GonvR1. Aufbau: Titelbild (Stand Houston) · Kennzahlen (2 Boxen, 2 × 2 × 3 m laut Plan, 1 Lager, seit 2024) · 1 Idee als Kreislauf (Lager → Versand → Auftritt → Nachfüllen) · 2 Standbox mit Plan der Kabine und der Transportkiste (ca. 3 × 1,9 m), Innenfotos, Inhalt Box 1 / Box 2 · 3 Rundum-Design Birkenwald «cleaner pumps, cleaner planet™» · 4 Aufbauanleitung (Drive «TPS Houston 24/Stand», Canva, EN, 2 Seiten) mit vier Schritten · 5 Herausforderung Houston als Ablauf · 6 Zeitleiste der Einsätze (Houston 2024, Orlando 2025, Miami 2026, Tampa 2026 bevorstehend) · Meine Aufgaben. Gesichter automatisch verpixelt (auch Monteure in der Anleitung). Nicht verwendet: Lagerort, Lieferanten, Preise, 3D-Standkonzept «CP Pumps Concept 4.15.24» (Urheber unklar). ❓ Fotos TFS Orlando 2025 (IMG_2152/2130/2137) im Drive nicht gefunden.
    - v2 ✏️ (06.10.2026, Wünsche Yana): Titelbild ohne Personen → Visualisierung der Standbox aus Yanas finalem Layout (Drive «TPS Houston 24/Stand/Fella»: «Layout_Messebox» mit zwei Varianten, «Finale_Layout» als Abwicklung der vier Wände, Juli 2024; Name des Druck-/Lieferbetriebs nicht nennen). Rundum-Design zeigt jetzt Entwurf → finales Layout → gebaut → an der Messe. Gesichter weichgezeichnet statt verpixelt. Transportkiste mit Foto der offenen Kiste. ✅ **FLA Miami 2026 entfernt: Die Box wurde dort nicht verwendet (Yana 06.10.2026)** → Text im FLA-Eintrag («aufgebaut auf dem Messesystem … aus der Messebox») prüfen. Alle 30 Houston-Fotos gesichtet: kein Bild ohne Besucher.
    - v3 ✏️ (06.10.2026): «Fertig aufgebaut» jetzt IMG_2105 (Stand von vorne, Gesichter und Badge weichgezeichnet). 📌 Fotos der Holzbox für Möbel und Material (aufklappbar) von Yana hochgeladen in Drive «Giveaways/CP»: DSC02077, DSC02102, DSC02106, DSC02117 (je 9–14 MB) → zu gross für den Download, Yana lädt kleinere Versionen hoch.
    - ✅ Korrektur (Yana 07.10.2026): **Messebox = Aufbewahrungskiste** (Box 2, Holz, aufklappbar, Möbel und Unterlagen). Die vier DSC-Fotos gehören nicht dazu. Plan «Aufbewarungskiste für Werbeartikel.pdf» (Drive «Giveaways/CP», Nov. 2025): ca. 1333 × 1057 × 1539 mm, Fach 1 und Fach 2 mit Tablaren und Kisten, Türen mit Kistenverschluss → auf der Seite als Box 2. 📌 Fotos dazu vermutlich «Box vorne.jpg» / «Box hinten.jpg» (je ~9,7 MB, zu gross) → Yana lädt verkleinert hoch. Hinweis: «Zeitplan Versand USA Box» nennt als Zieldatum 26.01.2026 (= Beginn FLA Miami); mit Yana klären, ob die Kiste dort im Einsatz war.
    - ✅ Yana 07.10.2026: «Box vorne» / «Box hinten» = die zwei Fotos der Aufbewahrungskiste (Messebox). Dazu Yanas Handskizze «CP Pumpen_überarbeitete Skizze.pdf» (Sept. 2025: Fach 1 und Fach 2, offene Fächer, geschlossene Schubladen) → auf der Seite Skizze → Plan. 📌 Fotos noch verkleinert hochladen.
    - ✅ Yana 07.10.2026: IMG_0526 (Restore-Box-Ordner, Stand in Houston mit Standbox, Möbeln, Podesten) zeigen → im Rundum-Design statt IMG_2087, Gesichter weichgezeichnet.
    - ✅ Yana 07.10.2026: Innenraum-Fotos der Standbox (IMG_0518/0519) entfernt, «sieht nicht schön aus». Fotos der Aufbewahrungskiste verkleinert hochgeladen (Drive «TPS Houston 24»: «Box vorne» = Fach 1, «Box hinten» = Fach 2) → eingebaut. Neu hochgeladen, noch offen: zwei 3D-Standkonzepte als Screenshots (13.08.2024 und 16.07.2024; das zweite mit Wasserzeichen eines Anbieters).
    - ✅ Yana 07.10.2026: Standbox und Aufbewahrungskiste klar trennen; die Standbox hat ihre eigene Transportkiste. → Seite neu gegliedert: 2 Standbox (+ Transportkiste) · 3 Aufbewahrungskiste (Skizze → Plan → gebaut) · 4 Vorher – nachher. Die zwei Screenshots sind **Yanas eigene 3D-Skizzen** (Juli und August 2024) → Vorher-Nachher mit dem fertigen Stand in Houston (IMG_0526). Wasserzeichen und Logo-Schild des Anbieters aus der Juli-Skizze entfernt, Name nicht nennen.
    - ✅ Yana 07.10.2026: «zweimal fast der gleiche Text … sowas geht nicht» → **Regel: Jeder Gedanke und jedes Bild nur einmal pro Seite** (vor dem Veröffentlichen Textabgleich machen). Texte gestrafft: Mieten statt eigene Ausstattung nur im Lead; kleinere Auftritte/Lager nur im Kreislauf; Schrauben/Schachtel nur in der Anleitung; Herausforderung: kurzer Einstieg, Details in den vier Kästchen. Titelbild jetzt IMG_0526; Nachher-Bild IMG_2105; Visualisierung im Rundum-Design.
    - ✅ **Korrektur Kisten (Yana 07.10.2026):** Es gibt neben der Standbox (mit eigener Transportkiste) **zwei weitere Kisten**: (1) **Möbelkiste**: Möbel und alles weitere Standmaterial, reist an die jeweiligen Messen; kein Bild, keine Skizze, nur im Text erwähnen. (2) **Aufbewahrungskiste** (die mit Skizze, Plan und Fotos «Box vorne/hinten»): wird **nicht verschickt**, bleibt im Lager, wird aufgefüllt, Verkäufer nehmen Material heraus. Raus: 3D-Skizze August, Layout 1/2, Einzelschritte der Anleitung (Anleitung selbst genügt). Vorher-Nachher nur 3D-Skizze Juli → Foto Houston. Eckdaten-Kästchen oben entfernt (wiederholten «Die Idee»).
    - ✅ **Korrektur (Yana 07.10.2026, gilt):** Drei Teile: (1) **Standbox** mit eigener Transportkiste → wird verschickt. (2) **Messebox** = Möbel **und alle Werbeartikel** für die Messe → wird verschickt (kein Bild). (3) **Aufbewahrungskiste** (Skizze, Plan, Fotos) = Lagerbox für Werbematerial → wird nicht verschickt, Verkäufer nehmen heraus, wird aufgefüllt. Begriff «Möbelkiste» nicht mehr verwenden.
    - ✅ Auffüllen der Aufbewahrungskiste (Yana 07.10.2026): Verkäufer in den USA nehmen Material heraus und melden, wenn etwas fehlt oder mehr gebraucht wird. Aufgefüllt wird auf zwei Wegen: Die amerikanischen Verkäufer nehmen bei Besuchen in der Schweiz Material mit, oder es wird ihnen zugeschickt; sie bringen es ins Lager und füllen selbst auf.
    - ✅ Gestaltungsregel (Yana 07.10.2026): Nebenbilder (Skizze, Plan, Detailfotos) klein als anklickbare Vorschaubilder, nicht gross im Vordergrund («nicht bam in your face»). Gross nur, was Hauptthema ist.
    - ✅ Yana 07.10.2026: kompakter, zusammengehörig → Abschnitte 1–3 zu «1 · Das Messesystem» zusammengefasst: «Reist an die Messe» (Standbox mit Transportkiste · Messebox) und darunter «Bleibt im Lager» (Aufbewahrungskiste als Zusatzinfo); Kreislauf entfernt. Danach 2 Vorher – nachher · 3 Rundum-Design · 4 Aufbauanleitung · 5 Herausforderung · 6 Im Einsatz.
    - ✅ v-final-Struktur (Yana 07.10.2026: «was dazugehört zusammen», nicht verstreut) → nach Gegenständen gegliedert: **1 Die Standbox** (Text: Konstruktion, Rundum-Design, Transportkiste, Aufbauanleitung; Visualisierung; darunter kleine Bildgruppen Konstruktion · Design · Transportkiste · Aufbauanleitung) · **2 Messebox und Aufbewahrungskiste** (zwei Karten) · 3 Vorher – nachher · 4 Herausforderung · 5 Im Einsatz · Meine Aufgaben. Überblick über die drei Teile im Lead.
    - ✅ Yana 07.10.2026: **Herausforderung raus, nichts Negatives auf den Projektseiten** (gilt allgemein). Texte professionell überarbeitet. Vorher-Nachher: Nachher = IMG_0526 (ganzer Stand); Titelbild = IMG_2105.
  - *Ergänzung Text ✅ (v3, Yana 05.10.2026: «ja» zu v2, plus zweite Box):* «Statt Mobiliar für jede Messe neu zu mieten, setzt CP auf eine eigene Standausstattung. Möbel und Standbox sind aufeinander abgestimmt und bilden ein wiederkehrendes Standkonzept: Jeder Auftritt hat das gleiche Erscheinungsbild, ist schnell aufgebaut und gut planbar. Die Standbox ist eine Massanfertigung und dient zugleich als Stauraum, Arbeitsfläche und Blickfang. Eine eigene Transportkiste schützt sie unterwegs. Eine zweite, ebenfalls angefertigte Box ist in den USA eingelagert und enthält die Möbel und das Marketingmaterial. Das Verkaufsteam bedient sich bei Bedarf direkt daraus, und für grössere Messen wird die ganze Box an den Stand geschickt.»
  - Sammelliste (Claude ergänzt beim Durchgehen der Ordner, Yana entscheidet am Schluss, was rein soll): CP-Podeste (u. a. neu mit abschliessbaren Türen, P&V 2026) · Standbox USA mit Birkenwald-Motiv und Möbelbox · Roll-ups (Corporate DE, MKP EN, MKP-Schnittzeichnung DE, «Sulphur») · Prospektständer · Kabine · CP-Tischtuch · Namensschilder · Messe-Rückwände und Blenden (je Messe) · Pflegeregeln für die Podeste im Briefing (weisse Handschuhe, nur Wasser, geplant: U-Blech als Kantenschutz; Berlin 2026) · Büromaterialbox und Messebox mit Büromaterial (Klemmbretter, Notizblöcke, Post-its, Stifte, Taschen, Namensschilder, Lead-Formulare; Berlin 2026). · Restore Box / Kabine USA: technische Unterlagen (Masse Transportkiste und Kabine, Datenblätter Plattenmaterial, Sicherheitsdatenblatt, Fotos, Feb. 2025) und Aufbauanleitung des Stands für das Team (2024), aus Ordner TFS Tampa. · ✅ Prinzip US-Lager (Yana 04.10.2026): Alles Messematerial kommt aus dem Lager in den USA. Bei kleineren Messen holen die Verkäufer Broschüren und Geschenke selbst im Lager ab; braucht es Möbel und grösseres Material, wird die ganze Box an die Messe verschickt.
- [ ] **Sammelbanner «Nos prochains salons professionnels» (Sept. 2026, von Yana):** ein Banner für alle kommenden Messen (CRU, TFS, Petrochymia, Industrial Expo). Vorschlag: einmal zeigen, in der Messe-Übersicht oder unter digitaler Werbung, nicht bei einer einzelnen Messe.
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
