import rdflib
import sys
import json
import pandas as pd


def main():
    graph = rdflib.Graph()
    graph.parse("simpsons.ttl",  format="ttl")
    sparql_command_path = sys.argv[1]
    query_kind = sys.argv[2]

    assert(query_kind in ['select', 'construct', 'ask'])
    
    with open(sparql_command_path, 'r') as file:
        query = file.read()  
        query_result = graph.query(query)

    if query_kind == 'select':
        df = pd.DataFrame(query_result.bindings)
        print(df.to_markdown(index = False))

    if query_kind == 'ask':
        for row in query_result:
            print(row)
    
    if query_kind == 'construct':
        for row in query_result:
            print(row[0], row[1], row[2])


if __name__ == "__main__":
    main()
