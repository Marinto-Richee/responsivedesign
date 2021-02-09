from django.shortcuts import render
from .models import colours
# Create your views here.
def responsiveweb(request):
    context={}
    context["colour"]= colours.objects.all()  
    return render(request,'responsive/responsivewebpage.html',context)

