from django.shortcuts import render
from django.contrib import messages
from decimal import Decimal
import math
from . forms import MortgageForm

def mortgage_calculator(request):
    result = None
    chart_data = None
    
    if request.method == 'POST':
        form = MortgageForm(request.POST)
        
        if form.is_valid():
            # Get form data
            property_price = form.cleaned_data['property_price']
            down_payment_percent = form.cleaned_data['down_payment_percent']
            principal = form.cleaned_data['principal']
            annual_interest_rate = form.cleaned_data['annual_interest_rate']
            years = form.cleaned_data['years']
            
            # Calculate down payment amount
            down_payment_amount = property_price * (down_payment_percent / Decimal('100'))
            
            # Monthly interest rate
            monthly_rate = (annual_interest_rate / Decimal('100')) / Decimal('12')
            
            # Total number of payments
            total_payments = years * 12
            
            # Calculate monthly payment using the formula
            # M = P [ i(1 + i)^n ] / [ (1 + i)^n - 1]
            if monthly_rate > 0:
                one_plus_i_pow_n = (Decimal('1') + monthly_rate) ** total_payments
                monthly_payment = principal * (monthly_rate * one_plus_i_pow_n) / (one_plus_i_pow_n - Decimal('1'))
            else:
                # If interest rate is 0%
                monthly_payment = principal / total_payments
            
            # Round to 2 decimal places
            monthly_payment = round(monthly_payment, 2)
            
            # Calculate total payment and interest
            total_payment = monthly_payment * total_payments
            total_interest = total_payment - principal
            
            # Prepare result dictionary
            result = {
                'property_price': float(property_price),
                'down_payment_percent': float(down_payment_percent),
                'down_payment_amount': float(down_payment_amount),
                'loan_amount': float(principal),
                'monthly_payment': float(monthly_payment),
                'total_payment': float(total_payment),
                'total_interest': float(total_interest),
                'interest_rate': float(annual_interest_rate),
                'loan_term': years,
                'total_months': total_payments,
            }
            
            # Prepare chart data
            chart_data = {
                'property_price': float(property_price),
                'down_payment': float(down_payment_amount),
                'principal': float(principal),
                'interest': float(total_interest),
            }
            
            # Add chart data to result for template access
            result.update(chart_data)
            
    else:
        form = MortgageForm()
    
    context = {
        'form': form,
        'result': result,
        'chart_data': chart_data,
    }
    
    return render(request, 'mortgages/mortgage.html', context)