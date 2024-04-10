from django.shortcuts import render
from django.http import JsonResponse
from .models import Company, Vacancy
from django.db.models import F

# Create your views here.



def get_all_companies(request):
    companies = Company.objects.all()
    data = [
        {
            'id': company.id,
            'name': company.name,
            'description': company.description,
            'city': company.city,
            'address': company.address
        } 
        for company in companies
    ]

    return JsonResponse(data, safe=False)



def get_company_by_id(request, id):
    try:
        company = Company.objects.get(id=id)
        
        data = {
            'id': company.id,
            'name': company.name,
            'description': company.description,
            'city': company.city,
            'address': company.address
        } 
        return JsonResponse(data)
    
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    




def get_all_vacancies(request):
    vacancies = Vacancy.objects.all()
    data = [
        {
            'id': vacancy.id,
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company': vacancy.company.name
        } for vacancy in vacancies
    ]

    return JsonResponse(data, safe=False)




def get_vacancy_by_id(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        
        data = {
            'id': vacancy.id,
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company': vacancy.company.name
        } 
        return JsonResponse(data)
    
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)
    



def get_vacancies_by_company(request, id):
    
    try:
        company = Company.objects.get(id=id)
        vacancies = company.vacancy_set.all()
        
        data = [
            {
                'id': vacancy.id,
                'name': vacancy.name,
                'description': vacancy.description,
                'salary': vacancy.salary,
                'company': vacancy.company.name
            } for vacancy in vacancies
        ]

        return JsonResponse(data, safe=False)
    
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    



def get_top_10_vacancies (request):
    top_10_vacancies = Vacancy.objects.order_by('-salary')[:10]

    data = [
        {
            'id': vacancy.id,
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company': vacancy.company.name
        } for vacancy in top_10_vacancies
    ]

    return JsonResponse(data, safe=False)