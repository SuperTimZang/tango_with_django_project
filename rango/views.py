from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    res = HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>.")
    context_dict = {'boldmessage':  'Crunchy, creamy, cookie, candy, cupcake!'}
    # res.write("<a href='/rango/about/'>About</a>.")
    # return res
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    # res = HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>.")
    # res.write("<a href='/rango/'>Index</a>.")
    return render(request,'rango/about.html')
