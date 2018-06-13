from django.shortcuts import render

# Create your views here.
def add_list(request):
    return render(request, 'todo/recordadd.html', {})
