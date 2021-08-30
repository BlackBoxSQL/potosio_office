from django.shortcuts import render

# Create your views here.

class ModelNameViewSet(viewsets.ModelViewSet):

    queryset = ModelName.objects.all()
    serializer_class = ModelNameSerializer