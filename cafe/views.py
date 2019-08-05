from django.views import generic
from .models import Cafe

class IndexView(generic.ListView):
    model=Cafe
# Create your views here.
