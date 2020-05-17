from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from rest_framework import generics
from rest_framework import permissions
from .models import Crops
from .serializers import CropSerializer

class cropList(generics.ListCreateAPIView):
    queryset = Crops.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        youralt  = int(self.request.query_params.get('altitude', None))
        yourtemp = int(self.request.query_params.get('temperature', None))
        yourhum  = int(self.request.query_params.get('humidity', None))
        queryset = Crops.objects.all()
        queryset = sorted( queryset, key= lambda t:t.distance(youralt, yourtemp, yourhum))
        return queryset

class cropDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Crops.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# Create your views here.
# def indexView(request):
#     return render(request, "index.html", {})


