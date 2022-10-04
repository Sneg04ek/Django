from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def helloworldview(request):

    template = "index.html"

    people = ["Неля", "Антон", "Алина", "Тимур"
              "Газиза", "Алан", и "Я"]

    context = {"people": people}    

    return render(request, template, context)