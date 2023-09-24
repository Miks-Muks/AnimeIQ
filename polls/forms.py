from django import forms


class PollForm(forms.Form):
    top_1 = forms.CharField(max_length=40, label='Первое место', required=True)
    top_2 = forms.CharField(max_length=40, label='Второе место', required=True)
    top_3 = forms.CharField(max_length=40, label='Третье место', required=True)
    top_4 = forms.CharField(max_length=40, label='Четвёртое место', required=True)
    top_5 = forms.CharField(max_length=40, label='Пятое место', required=True)
