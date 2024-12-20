from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'mallu','age':20}
    
    return render(request,'conditions.html',context=d)