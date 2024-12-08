# I have made this file on 19/01/23
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    upper_case = request.POST.get('upper_case', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if (removepunc == "on"):
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(upper_case == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase','analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext [index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover','analyzed_text':analyzed}
        djtext = analyzed

    if(removepunc != "on" and upper_case != "on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("<h1>Please enable any one option and try again !</h1>")

    return render(request,'analyze.html',params)
