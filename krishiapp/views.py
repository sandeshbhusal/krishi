from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request, "index.html", {})
  
def showCropsList(request):
	return render(request, "cropslist.html", {})

