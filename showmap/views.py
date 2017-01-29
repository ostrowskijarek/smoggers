from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    test = 1
    context = {'test': test}
    return render(request, 'showmap/index.html', context)