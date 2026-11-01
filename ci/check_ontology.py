from pathlib import Path
from rdflib import Graph
root = Path(__file__).resolve().parents[1] / "docs"
graphs = [Graph().parse(root / name, format=fmt) for name, fmt in [("ontology.ttl", "turtle"), ("ontology.nt", "nt"), ("ontology.owl", "xml"), ("ontology.jsonld", "json-ld")]]
assert all(len(g) for g in graphs), "Empty ontology serialization"
from rdflib.compare import isomorphic
assert all(isomorphic(graphs[0], g) for g in graphs[1:]), "Ontology serializations differ"
print("Four RDF serializations parse and are isomorphic")

