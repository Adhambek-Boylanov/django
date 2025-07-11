from django.shortcuts import render
from django.http import JsonResponse
def json_qaytar1(request):
    return JsonResponse({"baland":"past","uzun":"kalta","ariq":"semiz"})
