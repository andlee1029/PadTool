from django import forms
from .models import Monster_Attribute, Monster_Type

class MonsterSearchForm(forms.Form):
    monster_name = forms.CharField(required=False, label="Monster Name", max_length=100)
    monster_num = forms.IntegerField(required=False, label="Monster Number")
    monster_attribute = forms.MultipleChoiceField(required=False, label="Monster Attribute" ,choices=Monster_Attribute.Attribute, widget=forms.CheckboxSelectMultiple)
    monster_type = forms.MultipleChoiceField(required=False, label="Monster Type", choices=Monster_Type.Type, widget=forms.CheckboxSelectMultiple)