

Objektkatalog des Paketes UML\_DM\_LG\_GeolAssets\_V1
A {text-decoration: none }TD{border-bottom: solid black; border-bottom-width: 1px}



# 1 UML\_DM\_LG\_GeolAssets\_V1


## 1.1 Pakete


* [GeolAssetsCatalogues\_V1.ili](#2_GeolAssetsCatalogues_V1.ili)
* [GeolAssets\_V1.ili](#3_GeolAssets_V1.ili)
* [LG\_GeolAssetsCatalogues\_V1.ili](#4_LG_GeolAssetsCatalogues_V1.ili)
* [LG\_GeolAssets\_V1.ili](#5_LG_GeolAssets_V1.ili)


# 2 GeolAssetsCatalogues\_V1.ili


## 2.1 Pakete


* [GeolAssetsCatalogues\_V1](#6_GeolAssetsCatalogues_V1)


# 3 GeolAssets\_V1.ili


## 3.1 Pakete


* [GeolAssets\_V1](#7_GeolAssets_V1)


# 4 LG\_GeolAssetsCatalogues\_V1.ili


## 4.1 Pakete


* [LG\_GeolAssetsCatalogues\_V1](#8_LG_GeolAssetsCatalogues_V1)


# 5 LG\_GeolAssets\_V1.ili


## 5.1 Pakete


* [LG\_GeolAssets](#9_LG_GeolAssets)


# 6 GeolAssetsCatalogues\_V1


Datenmodell für die Beschreibung der Wertetabelle (Kataloge) des DMGeolAssets


## 6.1 Pakete


* [Catalogues](#10_Catalogues)


# 7 GeolAssets\_V1


Datenmodell Geologische Assets zur Beschreibung der Metadaten von geologischen Assets


## 7.1 Pakete


* [CoreGeolAssets](#11_CoreGeolAssets)


## 7.2 Klassen


* [Adress](#7.3_Adress)
* [ID](#7.4_ID)


## 7.3 Adress


Struktur für die Modellierung von Adressen







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Street | 0..1 | Zeichenkette |  |
| Housenumber | 0..1 | Zeichenkette |  |
| PLZ | 0..1 | Zeichenkette |  |
| Locality | 1 | Zeichenkette |  |
| Country | 1 | Zeichenkette |  |


## 7.4 ID


Struktur für die Definition einer ID, die in einem BAG {0..*} verwendet werden kann







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| ID | 0..1 | Zeichenkette | Identifikator |
| Descritption | 0..1 | Zeichenkette | Beschreibung woher die jeweilige ID stammt, bzw. wann/von wem sie vergeben wurde |


# 8 LG\_GeolAssetsCatalogues\_V1


Erweiterung des DMGeolAssetsCatalogies für die Beschreibung der Wertelisten (Kataloge) für die Langesgeologie


## 8.1 Pakete


* [Catalogues](#12_Catalogues)


# 9 LG\_GeolAssets


Erweiterung des DMGeolAssets für die Landesgeologie


## 9.1 Pakete


* [LGGeolAsset](#13_LGGeolAsset)


## 9.2 Klassen


* [AssetPartInfo](#9.3_AssetPartInfo)
* [LegalDoc](#9.4_LegalDoc)
* [OCRInfo](#9.5_OCRInfo)
* [TextDescr](#9.6_TextDescr)
* [UsedBy](#9.7_UsedBy)


## 9.3 AssetPartInfo


Structure für die Beschreiubung eines AssetParts







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| ObjectClass | 1 |  | Objektklasse, die von dem GAIA-Algorithmus automatisch zugewiesen wurde (z.B. Bohrprofil, Karte ...) |
| ObjectPage | 1 | PageNums | Seitennummer auf der das Objekt vom GAIA-Algorithmus gefunden wurde |
| ObjectBBox | 0..1 | ObjectCoord | Boundingbox des Objekts |
| ObjectScore | 0..1 | 0..1 | Score der Vorhersage des Algorithmus |


## 9.4 LegalDoc


Struktur zur Definition der rechtilich verbindlichen Dokumente, wie Einwilligiungsformulare oder Vertäge







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Titel | 0..1 | Zeichenkette | Titel des rechtlich verbindlichen Dokuments |
| Type | 1 |  | Typ des rechtlich verbindlichen Dokuments |
| RelativePathLegalDoc | 0..1 | Zeichenkette | Pfad zur Ablage des Administrativen Dokuments (z.B. Einwilligungsformular) |


## 9.5 OCRInfo







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| IsOCR | 1 | Boolean | Liegt im Asset Texterkennung vor? |
| OCRQuality | 0..1 |  | Qualität der Texterkennung |
| DateOCRProcessing | 0..1 |  | DateOCRProcessing |


## 9.6 TextDescr


Struktur zur Definition eines Textes, der in einem BAG {0..*} genutzt werden kann







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| TextDescrAtt | 0..1 | Zeichenkette |  |


## 9.7 UsedBy


Struktur für die Angabe in welchen Projekten das jeweilige Asset verwendet wurde.







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 0..1 | Zeichenkette | Name des Projekts |
| Description | 0..1 | Zeichenkette | Beschreibung des Projekts |
| DateDelivered | 0..1 |  | Datum der Abgabe des Assets an das jeweilige Projekt |


# 10 Catalogues


## 10.1 Klassen


* [AssetFormatItem](#10.2_AssetFormatItem)
* [AssetFormatRef](#10.3_AssetFormatRef)
* [AssetKindItem](#10.4_AssetKindItem)
* [AssetKindRef](#10.5_AssetKindRef)
* [ContactKindItem](#10.6_ContactKindItem)
* [ContactKindRef](#10.7_ContactKindRef)
* [GeomQualityItem](#10.8_GeomQualityItem)
* [GeomQualityRef](#10.9_GeomQualityRef)
* [LanguageItem](#10.10_LanguageItem)
* [LanguageRef](#10.11_LanguageRef)
* [ManCatLabelItem](#10.12_ManCatLabelItem)
* [ManCatLabelRef](#10.13_ManCatLabelRef)


## 10.2 AssetFormatItem


Codelist für das Attribut AssetItem.Format = Format des Assets (pdf, seg-y, ...)







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| MIME | 0..1 | Zeichenkette |  |
| AssetFormatRef |  | AssetFormatRef |  |


## 10.3 AssetFormatRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | AssetFormatItem |  |


## 10.4 AssetKindItem


Codelist für das Attribut Asset.Kind = Type des Assets (Bericht, Bohrprofil, ...)







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| AssetKindRef |  | AssetKindRef |  |


## 10.5 AssetKindRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | AssetKindItem |  |


## 10.6 ContactKindItem


Codelist für das Attribut Contact.Kind = Art des Kontakts (Bundesbehörde, Kantonale Bewilliungsbehörde, ...)







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| ContactKindRef |  | ContactKindRef |  |


## 10.7 ContactKindRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | ContactKindItem |  |


## 10.8 GeomQualityItem


Codelist für das Attribut GeometryOfInterest.GeomQuality = Qualität der Geometrie







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| GeomQualityRef |  | GeomQualityRef |  |


## 10.9 GeomQualityRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | GeomQualityItem |  |


## 10.10 LanguageItem


Codelist für das Attribut AssetItem.Language = Sprachversionen des Assets







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| LanguageRef |  | LanguageRef |  |


## 10.11 LanguageRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | LanguageItem |  |


## 10.12 ManCatLabelItem


Codelist für das Attribut Asset.ManCatLabel = Manuell vergebene Themen-Kategorie (Hydrogeologie, Geophysik, ...). Ersetzt die Attribute Topic und Purpose







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| ManCatLabelRef |  | ManCatLabelRef |  |


## 10.13 ManCatLabelRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | ManCatLabelItem |  |


# 11 CoreGeolAssets


Topic für das Kernmodell es ist zurzeit kein weiteres Topic definiert


## 11.1 Klassen


* [AssetBase](#11.2_AssetBase)
* [AssetItem](#11.3_AssetItem)
* [AssetPackage](#11.4_AssetPackage)
* [Contact](#11.5_Contact)
* [GeometryOfInterest](#11.6_GeometryOfInterest)
* [StudyArea](#11.7_StudyArea)
* [StudyLocation](#11.8_StudyLocation)
* [StudyTrace](#11.9_StudyTrace)


## 11.2 AssetBase


Basisklasse der Metadaten eines Assets oder Assetpackages







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| TitlePublic | 1 | Zeichenkette | Öffentlicher Titel des Assets. Dieser enthält keiner sensiblen Angaben |
| TitleOriginal | 0..1 | Zeichenkette | Titel des Assets. Wenn möglich soll der Originaltitel verwendet werden. |
| IDAlternate | 0..n |  | Identifikator(en) (ID) des Asset. Wenn möglich soll die Original-ID verwendet werden. |
| DateCreation | 1 |  | Datum des Erstellung des Assets. |
| Description | 0..1 | Zeichenkette | Beschreibung des Assets oder des Assetpackages |
| Author | 0..n | Contact |  |
| GeometryOfInterest | 0..n | GeometryOfInterest |  |
| Initiator | 0..n | Contact |  |
| Supplier | 0..n | Contact |  |


## 11.3 AssetItem


Klasse der Metadaten eines AssetItems







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Kind | 1 |  | Art des Dokuments |
| ManCatLabel | 1..n |  | Manuell vergebe Labels für das Thema oder den Zweck des Dokuments |
| Language | 1 |  | Sprachversionen in denen das Asset vorliegt. Bei identischem Inhalt können mehrere Sprachversionen des selben Assets vorliegen. Bei gemischtsprachlichen Assets gilt die Sprache des Titels. |
| Format | 1..n |  | Formate des Assets. Bei identischem Inhalt kann das selbe Asset in verschiedenen Formaten vorliegen. |
| AuthorBiblio | 0..1 | Zeichenkette | Autoren des Dokuments. Insbesondere für wissenschaftliche Publikationen. Wenn kein Autor über die Klasse Contact abgebildet werden kann/soll. Beispiel: Müller Maja, Meier Hans / Müller M. et.al/ |
| AssetComposition | 0..n |  | Zusammensetzung eines Assets, sofern es sich um AssetMain handelt. Die werte entsprechen denen des AssetKinds |
| TextBody | 0..1 | Zeichenkette | Textkörper aus OCR-Erkennung und GAIA-Algorithmen. Der Textkörper hat keine Längenbegrenzung, da er unterschiedlich lang sein kann. |
| IsPart | 1 | Boolean | Flag zur Anzeige, dass es sich bei diesem Asset um ein AssetPart handelt: default sollte "false" sein |
| AssetItemMain | 0..1 | AssetItem | Asset aus dem der AssetPart extrahiert wurde |
| AssetItemPart | 0..n | AssetItem | AssetPart |
| AssetItemX | 0..n | AssetItem |  |
| AssetItemY | 0..n | AssetItem |  |
| AssetPackage | 0..1 | AssetPackage |  |
| LGAssetItem | 1 | LGAssetItem |  |


## 11.4 AssetPackage


Klasse für die Metadaten eines AssetPackages







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| AssetItem | 0..n | AssetItem |  |
| LGAssetPackage | 1 | LGAssetPackage |  |


## 11.5 Contact


CLASS







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Kind | 1 |  | Information zur Art des Kontaktes (z.B. kantonale Bewilligungsbehörde, Bundesbehörde, Privatwirtschaft: begleitendes Fachbüro, etc.). Mindestkontakt ist nach Möglichkeit immer die Bewilligungsbehörde. |
| Name | 1 | Zeichenkette | Name des Kontakts |
| Adress | 0..1 |  | Adresse: die Struktur dieses Attributes ist in der Struktur "Adress" beschrieben |
| Telefon | 0..1 | Zeichenkette | Telefon-Nr., gemäss definierter Struktur von Tel. Nummern |
| Email | 0..1 | Zeichenkette | e-mail-Adresse, gemäss definierter Struktur von e-mail-Adressen |
| Website | 0..1 | Zeichenkette | URL von Websites, gemäss definierter Struktur von URLs |
| AuthoredAssetBase | 1..n | AssetBase |  |
| InitiatedAssetBase | 1..n | AssetBase |  |
| SuppliedAssetBase | 1..n | AssetBase |  |


## 11.6 GeometryOfInterest


Basisklasse für die Beschreibung der Geometrien







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| GeomQuality | 0..1 |  | Qualität der Geometrie (korrekte Geometrie oder Platzhaltergeometrie) |
| AssetBase | 1 | AssetBase |  |


## 11.7 StudyArea


CLASS Polygongeometrien







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Geometry | 0..1 | Surface |  |


## 11.8 StudyLocation


CLASS Punktgeometrien







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Geometry | 0..1 | Coord2 |  |


## 11.9 StudyTrace


CLASS Liniengeometrien







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Geometry | 0..1 | Line |  |


# 12 Catalogues


## 12.1 Klassen


* [AutoCatLabelItem](#12.2_AutoCatLabelItem)
* [AutoCatLabelRef](#12.3_AutoCatLabelRef)
* [AutoObjectCatItem](#12.4_AutoObjectCatItem)
* [AutoObjectCatRef](#12.5_AutoObjectCatRef)
* [LegalDocItem](#12.6_LegalDocItem)
* [LegalDocRef](#12.7_LegalDocRef)
* [NatRelItem](#12.8_NatRelItem)
* [NatRelRef](#12.9_NatRelRef)
* [OCRQualityItem](#12.10_OCRQualityItem)
* [OCRQualityRef](#12.11_OCRQualityRef)
* [PubChannelItem](#12.12_PubChannelItem)
* [PubChannelRef](#12.13_PubChannelRef)
* [StatusRestrictionItem](#12.14_StatusRestrictionItem)
* [StatusRestrictionRef](#12.15_StatusRestrictionRef)
* [StatusWorkItem](#12.16_StatusWorkItem)
* [StatusWorkRef](#12.17_StatusWorkRef)


## 12.2 AutoCatLabelItem


Codelist für das Attribut Asset.AutoCatLabel = vergebene Themen-Kategorie (Hydrogeologie, Geophysik, ...). Klasse durch GAIA zugewiesen







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| AutoCatLabelRef |  | AutoCatLabelRef |  |


## 12.3 AutoCatLabelRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | AutoCatLabelItem |  |


## 12.4 AutoObjectCatItem


Codelist für das Attribut Asset.AutoCatLabel = Typ eine AssetParts (Objekt-Extraks) (Bohrprofil, Karte ...). Klasse durch GAIA zugewiesen







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| AutoObjectCatRef |  | AutoObjectCatRef |  |


## 12.5 AutoObjectCatRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | AutoObjectCatItem |  |


## 12.6 LegalDocItem


Codelist für das Attribut LegalDoc.Type = Typ des rechtlichen Dokuments (Einwilligungsformular, Vertrag, ...)







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| LegalDocRef |  | LegalDocRef |  |


## 12.7 LegalDocRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | LegalDocItem |  |


## 12.8 NatRelItem


Codelist für das Attribut AdminAssetBase.TypeNationalRelevance = Begründung der Vergabe der nationalen Relevanz (Bohrung > 100m, Projekt bundesnaher Betriebe, ...).







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| NatRelRef |  | NatRelRef |  |


## 12.9 NatRelRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | NatRelItem |  |


## 12.10 OCRQualityItem


Codelist für das Attribut AdminAssetItem.OCRQuality = Qualität der Asset Texterkennung







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| OCRQualityRef |  | OCRQualityRef |  |


## 12.11 OCRQualityRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | OCRQualityItem |  |


## 12.12 PubChannelItem


Codelist für das Attribut Publication.Channel = Publikationskanal (internet, conference, ...)







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| PubChannelRef |  | PubChannelRef |  |


## 12.13 PubChannelRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | PubChannelItem |  |


## 12.14 StatusRestrictionItem


Codelist für das Attribut AdminAssetPackage.StatusRestriction = Berechtigungsstatus vom Asset







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| StatusRestrictionRef |  | StatusRestrictionRef |  |


## 12.15 StatusRestrictionRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | StatusRestrictionItem |  |


## 12.16 StatusWorkItem


Codelist für das AdminAssetBase.Statuswork = Bearbeitungsstatus (toBeControled, inProgress, ...)







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Name | 1 |  |  |
| Description | 0..1 |  |  |
| StatusWorkRef |  | StatusWorkRef |  |


## 12.17 StatusWorkRef







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| Reference | 0..1 | StatusWorkItem |  |


# 13 LGGeolAsset


Topic für die Erweitereung des DMGeolAssets


## 13.1 Klassen


* [LGAssetBase](#13.2_LGAssetBase)
* [LGAssetItem](#13.3_LGAssetItem)
* [LGAssetPackage](#13.4_LGAssetPackage)
* [LGContact](#13.5_LGContact)
* [Publication](#13.6_Publication)


## 13.2 LGAssetBase


Basisklasse für die administratischen Metadaten eines Assets oder Assetpackages







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| IsRestricted | 1 | Boolean | Angabe, ob das Asset frei verfügbar (no) oder der Zugang eingeschränkt (yes) ist |
| DateRestriction | 0..1 |  | Ablaufdatum der Zugriffsbeschränkung (Format: dd.mm.yyyy) Bemerkung: Wenn Restrict = yes, muss dieses Attribut ausgefüllt werden. Ist die Beschränkungsdauer unendlich bzw. unbestimmt, gilt: 31.12.9999. Für frei verfügbare Assets kann 01.01.1111 gesetzt werden. |
| RelativePath | 1 | Zeichenkette | Link und Name des zugehörigen Files, inkl. Dateiendung (zur Kennzeichnung des Formats). Beispiel: tiefbohrung\_abc.xlsx; http://www.meine- Domaene.ch/geothermie/tiefbohrungen.pdf; \\servername\meine-ablage\bohrprofil\_01.jpg |
| URL | 0..1 | Zeichenkette | Pfad zu einer Online-Ressource des Files vom RelativePfad |
| UsedBy | 0..n |  | UsedBy (Angabe der Projekte in den das Asset genutzt wurde)ERSETZT Attribut "Source" (In welchem Rahmen (z.B. in Projekt xy) wurde das Asset an die LG abgegeben?) |
| StatusWork | 1 |  | Bearbeitungsstatus |
| NationalRelevance | 1..n |  | Grund der Zuweisung der nationalen Bedeutung |
| LegalDoc | 0..1 |  | Rechtliche Dokumente |
| DateReceipt | 1 |  | Eingangsdatum des Assets |
| Processor | 0..1 | Zeichenkette | Bearbeiter: Mitarbeiter-Nr. Identifikator des User im System |
| DateLastProcessed | 1 |  | Letztes Bearbeitungsdatum |
| InfogeolData | 0..1 | Zeichenkette | Daten aus bestehender InfoGeol-DB, die nicht mit dem hier vorliegenden DM abgebildet werden können. |
| InfogeolContactData | 0..1 | Zeichenkette | Contaktinformationen aus Altdaten |
| InfogeolAuxData | 0..1 | Zeichenkette | BemerkungenDaten aus dem Feld "Auxiliary Information" der bestehenden InfoGeol-DB |
| Municipality | 0..1 | Zeichenkette | Gemeinde in dem das Asset liegt. Dieses Attribut dient dazu eine Gemeinde zu erfassen, falls keine Geometrie vorliegt |
| Remark | 0..1 | Zeichenkette | Bemerkungen zum Asset für besondere Informationen, die nicht mit den Attributen abgebildet werden können |
| Publication | 0..n | Publication |  |


## 13.3 LGAssetItem


Administrative Metadaten eines Assetitems







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| IDSGS | 0..1 | 0..1000000000 | ID, die von der LG vergeben wird (InfoGeol-Nr. oder Nachfolger) |
| OCRInfo | 1 |  | Information zur Texterkennung |
| AutoCatLabel | 0..1 |  | Automatisch für die im Rahmen von GAIA entwickelten Algortythmen zugewiesene Klasse |
| AssetPartInfo | 0..1 |  | Beschreibung eines AssetParts (s. STRUCTURE AssetPartInfo) |
| LocationAnalog | 0..1 | Zeichenkette | Physischer Standort des analogen Dokuments |
| AssetItem | 1 | AssetItem |  |


## 13.4 LGAssetPackage


Administrative Metadaten eines AssetPackages







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| StatusRestriction | 1 |  | Berechtigungsstatus. Ist der Berechtigungsstatus des Assets geklärt oder müssen Abklärungen getroffen werden. Muss das Asset evtl. aufgeteilt werden. |
| Project | 0..1 | Zeichenkette | Projekt im Rahmen dessen das Assetpackage erstellt wurde |
| AssetPackage | 1 | AssetPackage |  |


## 13.5 LGContact


Erweiterung der CLASS Contact aud dem DMGeolAssets







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| IDZAD | 0..1 | Zeichenkette | Referenz auf einen Eintrag in der zentralen Adress-Datenbank (ZAD) |


## 13.6 Publication


CLASS Publikation des jeweiligen Assets







| Name | Kardinalität | Typ | Beschreibung |
| ----- | ----- | ----- | ----- | 
| DatePublication | 1 |  | Datum der Publikation |
| Channel | 0..1 |  | Publikationskanal, z.B.: Publikation auf verschiedenen Kanälen: map.geo.admin.ch, Zeitschrift, Konferenz (Abstract, Präsentation), etc. |
| Description | 0..1 | Zeichenkette | Konkreter Name des Kanals. Z.B. Layer xyz auf map.geo.admin.ch, Bulletin der angewandten Geowissenschaften, SGM 2019 - Session Geoscience and Geoinformation , etc. |
| Link | 0..1 | Zeichenkette | URL oder DOI etc. zur jeweilgen Publikation |
| LGAssetBase | 1..n | LGAssetBase |  |






