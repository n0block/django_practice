from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard_view(request):
    context = {'crew_members': [{'id': 1,
                                 'first_name': 'Fat',
                                 'last_name': 'Tony',
                                 'crew_name': 'Bad MF'},
                                {'id': 2,
                                 'first_name': 'Johnny',
                                 'last_name': 'Tightlips',
                                 'crew_name': 'Bad MF'},
                                {'id': 3,
                                 'first_name': 'Christopher',
                                 'last_name': 'Moltasanti',
                                 'crew_name': 'Loyle Capo'},
                                ]}

    return render(request, 'dashboard/dashboard.html', context=context)
