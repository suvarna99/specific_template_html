from django.shortcuts import render

# Create your views here.
def f2(request):
    return render(request,'app2/second.html')