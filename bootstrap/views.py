from django.shortcuts import render
from .models import Carousel,About,Feature
# Create your views here.
def index(request):
    carousel_data= Carousel.objects.all()
    about_data= About.objects.all()
    feature_data= Feature.objects.all()

    context ={
        'carousel_data':carousel_data,
        'about_data':about_data,
        'feature_data':feature_data
    }

    return render(request,'index.html',context)