from django.shortcuts import render

finches = [
    {'name': 'Vader', 'breed': 'too fat', 'description': 'fat with the force', 'age': 42},
    {'name': 'Luke', 'breed': 'too skinny', 'description': 'skinny with the force', 'age': 20},
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })