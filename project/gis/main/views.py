from django.shortcuts import render, redirect, get_object_or_404
from .models import Place, Client, Status
from django.http import JsonResponse


def index(request):
    places = Place.objects.all()
    return render(request, 'main.html', {'places' : places})

def create_client(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')

        if email and name:
            new_client = Client(email=email, name=name, status=Status.objects.get(id=1))
            new_client.save()
            return redirect('main')
        else:
            return JsonResponse({"error": "Необходимо указать почту и имя."}, status=400)

    return JsonResponse({"error": "Метод не поддерживается."}, status=405)


def test(request):
    return render(request, 'index.html')