from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['no', 'name', 'salary', 'department']

    def clean_no(self):
        no = self.cleaned_data.get('no')
        if no < 1000:
            raise forms.ValidationError("社員番号は1000以上の数値で入力してください")
        return no

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("氏名の入力は必須です")
        return name

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is None:
            raise forms.ValidationError("給与額の入力は必須です")
        return salary
