from django.shortcuts import render

def engineers_view(request):
    return render(request, 'engineers.html')

def team_leaders_view(request):
    return render(request, 'team_leaders.html')

def department_leaders_view(request):
    return render(request, 'department_leaders.html')

def senior_managers_view(request):
    return render(request, 'senior_managers.html')
