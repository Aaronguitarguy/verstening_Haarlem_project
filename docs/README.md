# Verstening van Haarlem – Data-analyseproject

## Rapportage
Voor een volledige toelichting op aanpak, methodologie en normkeuze, zie [`rapportage.md`](rapportage.md).

## Korte beschrijving
Dit project analyseert de mate van verstening in de gemeente Haarlem op basis van de norm "Groene stadslandschappen" uit het Sweco-rapport van 2024. Deze norm adviseert minimaal 75 m² groen per woning in stedelijk gebied. Aan de hand van luchtfoto’s, beeldclassificatie en geografische data wordt onderzocht hoe Haarlem hierop scoort, en welke wijken eventueel in aanmerking komen voor vergroening.

## Doel
Het doel is om beleidsrelevante inzichten te geven in de verdeling van groen en verharding binnen Haarlem. Daarbij wordt specifiek gekeken naar:
- het groenoppervlak per woning
- ruimtelijke verschillen tussen wijken
- visuele classificatie van bebouwde versus groene gebieden

## Onderzoeksvraag

> **Hoofdvraag**: Hoe versteend is Haarlem volgens de norm "Groene stadslandschappen"?

### Deelvragen:
1. Hoeveel groenoppervlak is er per woning in Haarlem gemiddeld?
2. Hoe is het groen verdeeld over de verschillende wijken van Haarlem?
3. Hoeveel procent van Haarlem is verhard, hoeveel groen, en hoeveel water of overig?
4. Welke wijken scoren het slechtst en welke het best?
5. Wat zijn mogelijke verklaringen voor verschillen in verstening per wijk?

## Projectstructuur

```bash
Verstening_Haarlem_Project/
├── data/              # Invoerdata: luchtfoto's, shapefiles
│   ├── raw/           # Originele bronnen
│   ├── processed/     # Bewerkt (bijgesneden, opgeschoond)
│   └── shapefiles/    # Gemeente- en wijkgrenzen
├── notebooks/         # Jupyter notebooks voor elke stap
├── src/               # Python scripts (preprocessing, classificatie, analyse)
├── output/            # Visualisaties, kaarten, resultaten
├── reports/           # Rapportage, o.a. rapportage.md
├── README.md          # Dit bestand
├── requirements.txt   # Lijst van benodigde Python packages
└── .gitignore         # Bestanden die GitHub moet negeren
```

## Installatie

1. Clone deze repository
2. Installeer de benodigde packages via pip:

```bash
pip install -r requirements.txt
```

## Status
Dit project bevindt zich in de analysefase. Eerste beeldverwerking en classificatie zijn in ontwikkeling.

## Auteur
Mijn naam is Aaron Janssens, afgestudeerd watermanager met interesse in data science en klimaatadaptatie. Dit project is onderdeel van een leerroute naar datagedreven werken in het ruimtelijk domein.
