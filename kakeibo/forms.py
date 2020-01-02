from django import forms
from .models import Balance

'''
ITEM_CATEGORY_CHOICES = [
  ('給与所得', '給与所得'),
  ('食費', '食費'),
  ('水道代', '水道代'),
  ('ガス代', 'ガス代'),
  ('電気代', '電気代'),
  ('携帯代', '携帯代'),
  ('ガチャ課金', 'ガチャ課金'),
  ('通信費', '通信費'),
  ('交際費', '交際費'),
  ('交通費', '交通費'),
  ('家賃', '家賃'),
  ('その他', 'その他')
]

BALANCE_CHOICES = [
  ('収入', '収入'),
  ('支出', '支出')
]


class BalanceForm(forms.Form):
  item_name = forms.CharField(
    label = "タイトル",
    max_length = 100,
    required=True
  )

  amount = forms.IntegerField(
    label = '金額',
    required = True
  )

  registered_date = forms.DateField(
    label="日時",
    widget=forms.DateInput(attrs={'type': 'date'}),
    input_formats=['%y-%m-%d'],
    required= False
  )

  category = forms.ChoiceField(
    label= 'カテゴリ',
    widget=forms.Select,
    choices = ITEM_CATEGORY_CHOICES,
    required=True
  )

  balance_type = forms.ChoiceField(
    label = '収支タイプ',
    widget=forms.Select,
    choices = BALANCE_CHOICES,
    required = True
  )
  '''


class BalanceForm(forms.ModelForm):
    
    class Meta:
      model = Balance
      fields = '__all__'