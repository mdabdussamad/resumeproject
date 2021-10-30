from django.shortcuts import render

# Create your views here.
def myproject(request):
    context = {'myproject': 'active'}
    return render(request, 'proj/myproject.html', context)