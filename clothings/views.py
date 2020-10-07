from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Clothing
# Create your views here.
def index(request):
    clothings = Clothing.objects
    return render(request, 'clothings/index.html', {'clothings': clothings})


def detail(request, clothing_id):
    clothing_detail = get_object_or_404(Clothing, pk=clothing_id)

    return render(request, 'clothings/detail.html', {'clothing': clothing_detail})

    
