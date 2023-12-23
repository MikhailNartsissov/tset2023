from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def ha_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'homeanimals/index.html')
