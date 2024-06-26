from django import forms
from django.forms.widgets import DateInput, TimeInput
from datetime import date, timedelta, time
from django.utils import timezone
from commondb.models.review import Review
from commondb.models.user import User
from commondb.models.booking import Booking
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import ( UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['visit_date', 'rating', 'comment', 'image1', 'image2', 'image3']
        labels = {
            'visit_date': '訪問日',
            'rating': '評価',
            'comment': 'コメント',
            'image1': '画像',
            'image2': '画像',
            'image3': '画像',
        }
        widgets = {
            'visit_date': DateInput(attrs={'class': 'form-control',"type": "date",'max': date.today().strftime('%Y-%m-%d')}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'class': 'form-control'}),
        }
        input_formats = ['%Y-%m-%d']  # 日付の入力フォーマットを指定


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='必須。有効なメールアドレスを入力してください。')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='8文字以上必須。')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='パスワードを再度入力してください。')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'ユーザーID'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'パスワード'
        self.fields['password2'].label = 'パスワード(確認用)'

# 予約フォーム
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['restaurant','booking_date', 'booking_time', 'numbers_of_ppl']
        tomorrow = date.today() + timedelta(days=1)
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'style': 'font-size: 0.9em;','min':tomorrow.strftime('%Y-%m-%d')}),
            'booking_time': forms.Select(choices=[(time(hour, minute), f"{hour:02d}:{minute:02d}") for hour in range(17, 22) for minute in [0, 30]], attrs={'type': 'time', 'style': 'font-size: 0.9em;'}),
        }

        
    def clean_booking_date(self):
        booking_date = self.cleaned_data['booking_date']
        if booking_date <= timezone.now().date():
            raise forms.ValidationError('予約日は翌日以降を選択してください。')
        return booking_date
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numbers_of_ppl'].widget = forms.NumberInput(attrs={'min': 1, 'max': 8,  'style': 'font-size: 0.9em;' })
        

class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
             