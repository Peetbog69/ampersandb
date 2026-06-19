#!/usr/bin/env python3
"""
Convert a simple code list (CSV) to Leica Captivate XML codelist (.xcl).

Input CSV format — one code per line:
    code,description,type,color
    code,description,type,color,linestyle

type: line | point | area
color (optional): red, blue, green, yellow, cyan, magenta, white, orange, black
                  or hex RRGGBB
linestyle (optional): solid, dashed, dotted, dashdot

Examples:
    100,Back of Curb,line,red
    102,Gutter line,line,blue
    107,Sidewalk,line,green
    1001,Back of Curb #1,line,red
    1002,Back of Curb #2,line,red
    MH,Manhole,point
    TR,Tree,point

Usage:
    python3 leica_codelist_gen.py codes.csv > codelist.xcl
"""

import csv
import sys
from xml.etree import ElementTree as ET
from xml.dom import minidom

COLORS = {
    "red": "FF0000", "blue": "0000FF", "green": "00FF00",
    "yellow": "FFFF00", "cyan": "00FFFF", "magenta": "FF00FF",
    "white": "FFFFFF", "orange": "FF8800", "black": "000000",
}

LINESTYLES = {
    "solid": "Solid", "dashed": "Dashed", "dotted": "Dotted",
    "dashdot": "DashDot",
}

NS = "http://www.leica-geosystems.com"
ET.register_namespace("", NS)


def parse_color(raw):
    raw = raw.strip().lower()
    if raw in COLORS:
        return COLORS[raw]
    # assume hex
    if len(raw) == 6 and all(c in "0123456789ABCDEF" for c in raw):
        return raw
    return "000000"  # fallback


def parse_style(raw):
    raw = raw.strip().lower()
    return LINESTYLES.get(raw, "Solid")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 leica_codelist_gen.py codes.csv > codelist.xcl")
        print()
        print("CSV columns: code,description,type[,color][,linestyle]")
        sys.exit(1)

    csv_path = sys.argv[1]

    root = ET.Element(f"{{{NS}}}Codelist")

    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            row = [c.strip() for c in row if c.strip()]
            if not row or row[0].startswith("#"):
                continue

            code = row[0]
            desc = row[1] if len(row) > 1 else ""
            ctype = (row[2] if len(row) > 2 else "line").lower()

            code_el = ET.SubElement(root, f"{{{NS}}}Code")
            code_el.set("name", code)
            code_el.set("type", ctype.title())  # "Line", "Point", "Area"
            code_el.set("desc", desc)

            if ctype in ("line", "area"):
                style_el = ET.SubElement(code_el, f"{{{NS}}}LineStyle")

                if ctype == "area":
                    # area gets fill color too
                    style_el.set("fill", "true")

                if len(row) > 3:
                    style_el.set("color", parse_color(row[3]))
                else:
                    style_el.set("color", "000000")

                if len(row) > 4:
                    style_el.set("style", parse_style(row[4]))
                else:
                    style_el.set("style", "Solid")

                style_el.set("width", "1")

    # pretty-print
    rough = ET.tostring(root, encoding="unicode")
    dom = minidom.parseString(rough)
    pretty = dom.toprettyxml(indent="  ", encoding="UTF-8").decode("utf-8")

    # inject xsl for Captivate
    pretty = pretty.replace("?>", "?>\n<?xml-stylesheet type=\"text/xsl\" href=\"Codelist.xsl\"?>", 1)

    sys.stdout.write(pretty)


if __name__ == "__main__":
    main()
