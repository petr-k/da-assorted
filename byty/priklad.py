import json

import shapely
import shapely.geometry

# nacteni GeoJSON souboru
with open("OVZ_Klima_Bonita_p.json", encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]

# pro každý prvek si jeho geometrii uložíme jako shape z knihovny
# shapely, protože s ním budeme potřebovat dále pracovat
for prvek in features:
    prvek["shape"] = shapely.geometry.shape(prvek["geometry"])

# nacteni datasetu s byty
with open("dataset_nabidky_pouzeSreality.json", encoding="utf-8") as f:
    byty = json.load(f)

print(len(byty), "bytů")

# TODO: otevření CSV souboru pro zápis
# viz https://docs.python.org/3/library/csv.html

for byt in byty:
    idcko = byt["_id"]  # mozna budete potřebovat jiný identifikátor...
    coords = byt["data"]["gpsCoord"]
    pt = shapely.geometry.Point(coords["lon"], coords["lat"])

    # projdeme pro daný by všechny prostorové prvky načtené na
    # začátku a zjišťujeme, ve kterém prvku byt leží
    vyhledany_prvek = None
    for prvek in features:
        je_v_polygonu = prvek["shape"].intersects(pt)
        if je_v_polygonu:
            vyhledany_prvek = prvek

    if vyhledany_prvek:
        #  TODO: zapis řádku do CSVčka
        # v jednom sloupci bude idčko bytu
        # ve druhém bude hodnota atributu z nalezeného prvku
        pass
    else:
        print("pro", idcko, "nenasli jsme", coords)

# TODO: uzavření CSV souboru
