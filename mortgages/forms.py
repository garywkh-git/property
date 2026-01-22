from django import forms



from django import forms

class MortgageForm(forms.Form):
    principal = forms.FloatField(
        label="Loan Amount",
        min_value=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Enter loan amount"
        })
    )
    annual_interest_rate = forms.FloatField(
        label="Interest Rate (%)",
        min_value=0.01,
        max_value=100,
        initial=3,  # Default value
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 3"
        })
    )
    years = forms.IntegerField(
        label="Loan Term (Years)",
        min_value=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 30"
        })
    )

# class MortgageForm(forms.Form):
#     principal = forms.FloatField(label="Loan Amount")
#     annual_interest_rate = forms.FloatField(label="Interest Rate (%)")
#     years = forms.IntegerField(label="Loan Term (Years)")