from django import forms


class CreateNewTodo(forms.Form):
    name = forms.CharField(label="Item name ", max_length=250)
    checked = forms.BooleanField(required=False)
