from lxml import etree
import argparse
import sys

################################# AULA 2 #######################################

def leitura(curso):
    tree = etree.parse("Aula2-XML/" + curso + ".xml")
    return tree.getroot()

def validar(curso):
    tree = etree.parse("Aula2-XML/" + curso + ".xsd")
    xsd = etree.XMLSchema(tree)

    # Validate XML file
    print(xsd.validate(tree))

def mostrar(elem, text=""):
    elem_contents = text + str(elem) + " " + str(elem.attrib) + " " + str(elem.text)
    elem_contents = elem_contents.replace("{}", "").replace("\n", "")
    print(elem_contents)  # print element
    if len(elem.getchildren()) != 0:  # if they exist, print children
        for e in elem:
            mostrar(e, text + "\t")


print("start")
def menu():
    key = 1
    root = ""
    curso = input("\nCurso: ")

    while key > 0:
        key = int(input("\n*** MENU ***\n"
                        "1. Leitura Doc XML\n"
                        "2. Validar Doc XML\n"
                        "3. Mostrar Info Curso\n"
                        "0. Sair\n"))
        if key == 1:
            root = leitura(curso)
        if key == 2:
            validar(curso)
        if key == 3:
            mostrar(root)
        if key == 0:
            return print("End!")

menu()
