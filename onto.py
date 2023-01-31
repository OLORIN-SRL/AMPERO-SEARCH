from rdflib import Graph, term
g = Graph()
g.parse("testAMPERO.owl", format="xml")

from rdflib.namespace import RDF, OWL
from rdflib import URIRef

#get classes and properties from given ontology file
classes = []
for s,p,o in g.triples((None, RDF.type, OWL.Class)):
    classes.append(s)
properties = []
for s,p,o in g.triples((None, RDF.type, OWL.ObjectProperty)):
    properties.append(s)

#if you have stored all the retrieved entities from the web scraping/api search:
# Connect to database and retrieve entities
# import sqlite3
# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM entities")
# entities = cursor.fetchall()

#otherwise, as a test example:
entities=['LASER_SCANNER','PLC_SAFE','FUNGO']

#match scraped entities with ontology classes and return results.
for entity in entities:
    match = any(entity in url for url in classes)
    if match:
        for url in classes:
            if entity in url:
                print(f"{entity} maps to {url}")
                break
    else:
        print(f"{entity} not mapped to any class")
