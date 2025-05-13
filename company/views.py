from django.shortcuts import render, redirect
from .forms import CompanyForm

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CompanyForm()
    return render(request, 'company/create_company.html', {'form': form})

def success_page(request):
    return render(request, 'company/success.html')
