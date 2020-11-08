from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from lxml import etree
from webproj.settings import BASE_DIR
import requests
import os
from BaseXClient import BaseXClient
import xmltodict
from urllib.request import urlopen
#import argparse
#import urllib2


xml = etree.parse('app/cursos.xml')
url = "http://acesso.ua.pt/xml/curso.v5.asp?i="

session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')

# Create your views here.
def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)

################################# AULA 1 #######################################
def hello(request):
    return HttpResponse("Hello World!")

def numero(request,num):
    resp = "<http><body><h1>{}</h1></body></html>".format(num)
    return HttpResponse(resp)

def numerot(request, num):
    tparams = {
        'num_arg': num,
    }
    return render(request, 'numerot.html', tparams)

def info(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def sendinfo(request):
    """Renders sendinfo page."""
    assert isinstance(request, HttpRequest)
    if 'nome' in request.POST and 'idade' in request.POST:
        nome = request.POST['nome']
        idade = request.POST['idade']
        if nome and idade:
            return render(request, 'send_results.html',
                {'nome':nome, 'idade':idade,}
            )
        else:
            return render(request, 'send_info.html', {'error':True,})

    else:
        return render(request, 'send_info.html', {'error':False,})

################################# AULA 2 #######################################
def xml_view(request):

    url = 'http://acesso.ua.pt/xml/curso.v5.asp?i=23'
    resp = requests.get(url)

    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)

    tree = etree.parse("topnewsfeed.xml")

    html = mostrar(tree.getroot(), "\t")
    return HttpResponse(html)

def mostrar(xml, tabs):
    string = ""
    if len(xml) > 0:
        string += "<p>" + tabs + xml.tag + ":</p>"
        for e in xml:
            string += mostrar(e, tabs + "&emsp;")
    else:
        if xml.text:
            string += "<p>" + tabs + xml.tag + ": " + xml.text + "</p>"
    return string

################################# AULA 3 #######################################
def cursos(request):
    fname = 'cursos.xml'
    pname = os.path.join(BASE_DIR, 'Aula3-XML/' + fname)
    #xml = etree.parse("Aula3-XML/cursos.xml")
    xml = etree.parse(pname)
    info = dict()
    query = '//curso'
    curs = xml.xpath(query)
    for c in curs:
        info[c.find('guid').text] = c.find('nome').text
    tparams = {
        'cursos': info,
    }
    return render(request, 'cursos.html', tparams)

def curso(request):
    guid = request.GET.get('guid')
    xml = etree.parse("Aula3-XML/cursos.xml")
    c = xml.find("//curso[guid = '{}']".format(guid)) #vai buscar o curso
    info = dict()

    info['Nome'] = c.find('nome').text
    info['Codigo'] = c.find('codigo').text
    info['Grau'] = c.find('grau').text
    info['Departamentos'] = []
    for ellen in c.xpath(".//departamentos//departamento"): #vai buscar a lista dos departamentos
        info['Departamentos'].append(ellen.text)
    info['Areascientificas'] = []
    for ellen in c.xpath('.//areascientificas//areacientifica'): #vai buscar a lista das areacientificas
        info['Areascientificas'].append(ellen.text)
    info['Local'] = c.find('local').text

    tparams={
        'curso': info,
        'nome': info.get('nome'),
    }
    return render(request, 'curso.html', tparams)

def cursospordepart(request):
    depart = request.GET.get("depart")
    xml = etree.parse("Aula3-XML/cursos.xml")
    cursos = xml.xpath("//curso[departamentos//departamento = '{}']".format(depart))
    info = dict()
    for c in cursos:
        info[c.find("guid").text] = c.find("nome").text
    tparans = {
        "cursos": info,
        "frase": "Lista dos cursos para o "+depart+":",
    }
    return render(request,"cursos.html",tparans);

def departamento(request):
    xml = etree.parse("Aula3-XML/cursos.xml")
    info = dict()
    query = '//curso'
    curs = xml.xpath(query)

    info['Departamentos'] = []
    for c in curs:
        for ellen in c.xpath(".//departamentos//departamento"):  # vai buscar a lista dos departamentos
            info['Departamentos'].append(ellen.text)
    tparams = {
        'depart': info,
        'frase': "Lista de Departamentos:"
    }
    return render(request, 'departamentos.html', tparams)

################################# AULA 4 #######################################
def addExample(request):

    input = "xquery <root>{ for $a in collection('cursos')//curso return <elem> {$a/guid} {$a/nome} </elem>}</root>"
    query = session.execute(input)
    info = dict()
    res = xmltodict.parse(query)
    for c in res["root"]["elem"]:
        info[c["guid"]] = c["nome"]
    tparams = {
        'cursos': info,
        'frase': "Lista dos cursos da UA:",
    }

    return render(request, "cursos.html", tparams)

################################# AULA 5 #######################################
def pageRSS(request):
    url = 'http://feeds.jn.pt/JN-Ultimas'
    resp = requests.get(url)

    # saving the xml file
    #with open('topnewsfeed.xml', 'wb') as f:
        #f.write(resp.content)

    #tree = etree.parse("topnewsfeed.xml")
    tree = etree.parse(urlopen(url))
    html = mostrar(tree.getroot(), "\t")
    return HttpResponse(html)
    #return render(request, "pageRSS.html", tparams)