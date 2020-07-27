from django.shortcuts import render

def home_view(response, *args, **kwargs):
    return render(response, "index.html", {})
