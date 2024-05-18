from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        response = requests.post("http://127.0.0.1:8000/explain/", json={"topic": topic})
        if response.status_code == 200:
            explanation = response.json().get("explanation")
            return render(request, "result.html", {"topic": topic, "explanation": explanation})
        else:
            return HttpResponse("Error: Unable to fetch explanation.")
    return render(request, "home.html")