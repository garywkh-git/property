

# Create your views here.

from django.contrib import messages
from . forms import MortgageForm

from django.shortcuts import render, redirect, get_object_or_404

def mortgage_calculator(request):
    result = None
    if request.method == "POST":
        form = MortgageForm(request.POST)
        if form.is_valid():
            P = form.cleaned_data['principal']
            annual_rate = form.cleaned_data['annual_interest_rate'] / 100
            years = form.cleaned_data['years']

            r = annual_rate / 12
            n = years * 12

            M = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
            total_payment = M * n
            total_interest = total_payment - P

            result = {
                "monthly_payment": round(M, 2),
                "total_payment": round(total_payment, 2),
                "total_interest": round(total_interest, 2),
            }
    else:
        form = MortgageForm()

    return render(request, 'mortgages/mortgage.html', {"form": form, "result": result})