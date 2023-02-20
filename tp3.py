#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("sujet2.sqlite")
cur = con.cursor()

def html_print(table):
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
    res = cur.execute("SELECT * FROM "+table)
    for i in res:
        print("\t\t<tr>")
        for j in i:
            print("\t\t\t<td>"+j+"</td>")
        print("\t\t</tr>")
    print("\t</table>")
    print("</html>")

html_print("Machine")

con.close()
