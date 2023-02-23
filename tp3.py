#!/usr/bin/env python3

def html_print(req: str) -> int:
    print("<!DOCTYPE html>")
    print("<html>")
    print("""\t<style>
    table {
        border-collapse: collapse;
        border: 1px solid black;
    }
    td {
        padding: 10px;
        border: 1px solid black;
    }
    </style>""")
    print("\t<table>")
    res = cur.execute(req)
    for i in res:
        print("\t\t<tr>")
        for j in i:
            print("\t\t\t<td>"+j+"</td>")
        print("\t\t</tr>")
    print("\t</table>")
    print("</html>")
    return 1

def bdd2json(req: str, file: str) -> int:
    res = cur.execute(req)
    tab = [[j for j in i] for i in res]
    string = json.dumps(tab, indent=2)
    f = open(file, "w")
    f.write(string)
    return 1

def json2bdd(file: str, table: str, bdd: str, types: str) -> int:
    """
    Format JSON d'entrée :
    [
        {clef: attribut, ...},
        ...
    ]
    """
    data    = json.loads(open(file, "r").read())
    con_fun = sqlite3.connect(bdd)
    cur_fun = con_fun.cursor()
    attributes = [i for i in (data[0]).keys()]
    for i in range(len(types)):
        attributes[i] += " "+types[i]+" NOT NULL"
    attr_str = ", ".join(attributes)

    cur_fun.execute("CREATE TABLE "+table+"("+attr_str+");")

    for i in data:
        insert_values = []
        for j in i.values():
            if isinstance(j, int):
                elt = str(j)
            else:
                elt = '"'+str(j)+'"'
            insert_values.append(elt)

        cur_fun.execute("INSERT INTO "+table+" VALUES ("+",".join(insert_values)+");")
    con_fun.commit()
    return 1


if __name__ == "__main__":
    import sqlite3
    import json

    con = sqlite3.connect("sujet2.sqlite")
    cur = con.cursor()

    html_print("SELECT * FROM Machine;")
    bdd2json("SELECT * FROM Machine;", "file.json")
    json2bdd("test.json", "table1", "test.sqlite", ["INTEGER", "TEXT"])

    con.close()
