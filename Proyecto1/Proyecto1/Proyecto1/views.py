from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context





def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>/a entendimos esto, es muy simple :)")


def DiaDeHoy(request):
    dia = datetime.now()

    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)


def probandoTemple(self):
    miHtml = open("C:/Users/Leon Estrada/Desktop/coderhause/Pythonproyecto1/plantillas/template1.html")
    
    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)






