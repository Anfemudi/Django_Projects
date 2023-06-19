from multiprocessing import context
from pipes import Template
from pydoc import doc
from django.http import HttpResponse
import datetime as dt
import pandas as pd
from django.template import Context, Template,loader
from django.shortcuts import render

class persona(object):
    
    def __init__(self,nombre,apellido) :
        self.nombre=nombre
        self.apellido=apellido


def Herencia(request) :


    actual_time=dt.datetime.now()
    ctx={"fehca_hoy":actual_time}


    return render(request,"plantillaHerencia.html",ctx)



def templat_render(request):

    p1=persona("Mr Felipe","Muñoz")
    actual_time=dt.datetime.now()
    temas=['Plantillas','Modelo','Formulario','Vista','Despliegue']
    ctx={"nombre_persona":p1.nombre,"apellidos":p1.apellido,"hora":actual_time,"lista":temas,"lista2":temas}

    return render(request,"miplantilla.html", ctx)


def templat_loader(request):

    p1=persona("Mr Felipe","Muñoz")
    temas=['Plantillas','Modelo','Formulario','Vista','Despliegue']
    temas2=[]

    #nombre='Andrés Felipe'
    #apellido="Muñoz Díaz"
    actual_time=dt.datetime.now()

    doc_externo=loader.get_template('miplantilla.html')

    ctx={"nombre_persona":p1.nombre,"apellidos":p1.apellido,"hora":actual_time,"lista":temas,"lista2":temas2}

    documento=doc_externo.render(ctx)


    return HttpResponse(documento)


def plantilla_lista(request): 


    p1=persona("Mr Felipe","Muñoz")
    temas=['Plantillas','Modelo','Formulario','Vista','Despliegue']
    temas2=[]

    #nombre='Andrés Felipe'
    #apellido="Muñoz Díaz"
    actual_time=dt.datetime.now()

    doc_externo=open('/Users/AFMD/Documents/Django_Projects/Proyecto1/Proyecto1/Plantillas/miplantilla.html')
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre,"apellidos":p1.apellido,"hora":actual_time,"lista":temas,"lista2":temas2})

    documento=plt.render(ctx)


    return HttpResponse(documento)

def variable(request): 


    p1=persona("Mr Felipe","Muñoz")

    #nombre='Andrés Felipe'
    #apellido="Muñoz Díaz"
    actual_time=dt.datetime.now()

    doc_externo=open('/Users/AFMD/Documents/Django_Projects/Proyecto1/Proyecto1/Plantillas/miplantilla.html')
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre,"apellidos":p1.apellido,"hora":actual_time})

    documento=plt.render(ctx)


    return HttpResponse(documento)


def saludo(request): #primera vista

    doc_externo=open('/Users/AFMD/Documents/Django_Projects/Proyecto1/Proyecto1/Plantillas/miplantilla.html')
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)


    return HttpResponse(documento)

  

def despedida(request): #primera vista

    return HttpResponse("see you later")

def fecha(request):
    cur_date=dt.datetime.now()

    documento= """
    <html>
    <body>
    <h1>
    fecha y hora actuales %s
    </s>
    </body>
    </html>
    
    
    """% cur_date
    return HttpResponse(documento)


def Calc_age(request,edad,anho):


    periodo=anho-pd.to_numeric(dt.datetime.now().year)

    future_age=edad+periodo

    documento= """
    <html>
    <body>
    <h2>
    en el año %s tendras %s años
    </s>
    </body>
    </html>
    
    
    """% (anho,future_age)
    return HttpResponse(documento)