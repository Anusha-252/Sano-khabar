from django import forms


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class DatePickerInput(forms.DateInput):
    input_type = 'date'
