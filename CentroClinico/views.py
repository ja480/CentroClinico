from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    
    def get(self, request):
        return render(request, 'indexusuario.html')
    
def services(request):
        return render(request, 'services.html')

def meetus(request):
        return render(request, 'meetus.html')