# employees/forms.py

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Wyświetlamy wszystkie pola z modelu Employee

    # Nadpisujemy __init__, aby tylko imię, nazwisko i email były obowiązkowe
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        
        # Wszystkie inne pola są opcjonalne
        for field_name, field in self.fields.items():
            if field_name not in ['first_name', 'last_name', 'email']:
                field.required = False
