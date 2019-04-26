import json

import shapely
import shapely.geometry

# Soubor ruian-staty.geojson je JSON dokument, odpovídající standardu GeoJSON, viz
# https://en.wikipedia.org/wiki/GeoJSON. Dostal jsem ho konverzí z https://www.cuzk.cz/ruian/.
# GeoJSON může obsahovat různé typy dat (prvky, kolekce prvků, různé typy
# geometrií - body, linie, polygony), viz https://en.wikipedia.org/wiki/GeoJSON.
# Tip: zkus si soubor otevřít a prohlédnout na webu http://geojson.io.

# My soubor otevřeme a uložíme si ho jako Python datovou strukturu do proměnné:
with open("ruian-staty.geojson", encoding="utf-8") as f:
    staty = json.load(f)

# Proměnná staty teď odpovídá původnímu JSON dokumentu. Ten obsahuje kolekci prvků
# (FeatureCollection) o jednom prvku - stát ČR. Každý prvek (Feature) může mít
# atributy a geometrii - ta geometrie nás bude jako jediná zajímat:

cr_geometry = staty["features"][0]["geometry"]

# Teď použijeme knihovnu shapely (https://shapely.readthedocs.io/en/stable/manual.html), která
# umí s geometriemi pracovat.

# shapely pracuje s konceptem tzv. shapes, proto provedeme konverzi
cr_shape = shapely.geometry.shape(cr_geometry)

# Teď můžeme s tím shape dělat ruzné věci:

# ... jako třeba zjistit, jakého je typu:
print(cr_shape.type)  # MultiPolygon (což berme prostě jako polygon)

# ... nebo zjistit rozsah souřadnic:
minx, miny, maxx, maxy = cr_shape.bounds
print("Rozsah souřadnic ČR je", minx, miny, maxx, maxy)

# ... nebo zjišťovat, zda nějaký bod v našem polygonu leží:
bod_a = shapely.geometry.Point(15, 50)  # někde u Prahy
print("Leží bod A v ČR?: ", cr_shape.contains(bod_a))

bod_b = shapely.geometry.Point(-49, -12)  # tohle bude spíš v Brazílii
print("Leží bod A v ČR?: ", cr_shape.contains(bod_b))
