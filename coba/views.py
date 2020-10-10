from django.shortcuts import render

from supenapi.response import Response
import json


def coba(request,id=None):
    
    if request.method  == "GET":
        if id == '123':
            data = json.dumps({
            "credential":"asdjksdfjkbjsdfbjasdfbjsdksdbn",
            "name":"SUPEN ASU",
            "email":"BAJINGAN@gmail.com",
            })
            data = json.loads(data)
            return Response.ok(values=data,message=id)
        else:
            return Response.badRequest(values="id tidak terdaftar",message="mohon coba lago")

    
    if request.method  == "POST" and 'document' in request.FILES:
        request_file = request.FILES['document'].name

        data = json.dumps({
            "credential":"asdjksdfjkbjsdfbjasdfbjsdksdbn",
            "name":"SUPEN ASU",
            "email":"BAJINGAN@gmail.com",
            })
        data = json.loads(data)

        return Response.ok(values=data,message="request_file")
    else:
        return Response.badRequest(values="need document param")
