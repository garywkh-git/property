from django import forms
from decimal import Decimal

class MortgageForm(forms.Form):
    property_price = forms.DecimalField(
        max_digits=12, 
        decimal_places=2,
        min_value=10000,
        label="Property Price (HKD)",
        initial=5000000
    )
    
    down_payment_percent = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        min_value=10,
        max_value=90,
        label="Down Payment (%)",
        initial=30
    )
    
    principal = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=10000,
        label="Loan Amount (HKD)",
        initial=3500000
    )
    
    annual_interest_rate = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        min_value=0.1,
        max_value=15,
        label="Annual Interest Rate (%)",
        initial=3.5
    )
    
    years = forms.IntegerField(
        min_value=5,
        max_value=40,
        label="Loan Term (Years)",
        initial=25
    )
    
    def clean(self):
        cleaned_data = super().clean()
        
        property_price = cleaned_data.get('property_price')
        down_payment_percent = cleaned_data.get('down_payment_percent')
        
        if property_price and down_payment_percent:
            # Calculate down payment amount
            down_payment_amount = property_price * (down_payment_percent / Decimal('100'))
            
            # Calculate loan amount
            loan_amount = property_price - down_payment_amount
            
            # Update the principal field with calculated loan amount
            cleaned_data['principal'] = loan_amount
            
            # Add calculated fields to cleaned_data
            cleaned_data['down_payment_amount'] = down_payment_amount
            cleaned_data['loan_amount'] = loan_amount
        
        return cleaned_data