from django.shortcuts import render

# Create your views here.
def index(request):
  name = "user"
  return render(request, "base.html", {"name": name})