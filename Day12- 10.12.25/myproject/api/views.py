from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Django API is working"})

def welcome(request):
    return JsonResponse({"message": "Welcome to Django API"})

def status(request):
    return JsonResponse({"status" : "running" , "framework": "Django"})