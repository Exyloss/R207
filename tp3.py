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

def json2bdd(file: str) -> int:
    data = json.loads(open(file, "r").read())

if __name__ == "__main__":
    import sqlite3
    import json

    con = sqlite3.connect("sujet2.sqlite")
    cur = con.cursor()

    html_print("SELECT * FROM Machine;")
    bdd2json("SELECT * FROM Machine;", "file.json")
    json2bdd("file.json")

    con.close()
