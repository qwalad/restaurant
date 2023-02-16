from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import FeedBackForm


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")



def index(request):
    return render(request, "restaurant/index.html")

