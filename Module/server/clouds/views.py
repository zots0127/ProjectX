from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
#注：每个响应对应一个函数，函数必须返回一个响应
from clouds import models

def index(request):
    info = models.Clog.objects.all()
    #返回至前端渲染
    return render_to_response("index.html",{"userinfo":info}) #必须用这个return