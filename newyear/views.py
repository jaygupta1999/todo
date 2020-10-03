from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, "newyear/index.html",{
        "now": now.month==1 and now.day==1,
    })


