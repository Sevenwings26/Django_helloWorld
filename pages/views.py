# from django.shortcuts import render

from django.http import HttpResponse

# # statements 
# name = "Carboni"
# Statement = f"Hello world! {name} says you are welcome!"

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello World")