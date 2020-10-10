from django.shortcuts import render

from .response import Response


def coba(request,id=None):
    
    if request.method  == "POST":
        return Response.ok(values="POSTT",message=id)

    
    if request.method  == "GET":
        return Response.ok(values="GETTT",message="VALID!")
