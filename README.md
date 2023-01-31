# AMPERO-SEARCH
Ampero Search aims at developing an ontology based search engine 

The project develops in successive phases. At first, web scraping (scraper.py) and API search (digikey_api.py) on known ecommerce will be used to retrieve a large dataset of entities. Parallelly, an ontology will be created to provide semantic values to the retrieved products (i.e. testAMPERO.owl). 

A mapping is necessary to categorize each retrieved product into the right ontology class (see onto.py).
