from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

techs = [
    'Cloud Services',
    'Artificial Intelligence/Machine Learning',
    'Internet of Things',
    'Augmented Reality/Virtual Reality',
    'Cybersecurity',
    'Big Data/Analytics',
    'Blockchain',
    'Robotics/Industrial Automation',
    'Digital Marketing/Advertising',
    'FinTech',
    'HealthTech/MedTech',
    'Telecommunications',
    'Renewable Energy',
    '3D Printing',
    'Quantum Computing',
    'Biotechnology',
    'Nanotechnology',
    'Aerospace and Defense'
]

def index(request, techs=techs):
    context = {
        'techs': techs
    }
    return render(request, 'search/index.html', context)

def results(request):
    return render(request, 'search/results.html')