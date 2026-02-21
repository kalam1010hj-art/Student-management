from django import forms
COURSE_CHOICES = [
        ('CSE', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics'),
        ('ME', 'Mechanical'),
    ]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':"Enter your name",'class':'mb-3'}))
    roll_number=forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            'placeholder':'Enter your roll_number',
            'class':'mb-3'
            }
            )
            ,label='Roll Number')
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'example@gmail.com','class':'mb-3'}),required=False)
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    phone=forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class':"mb-3"}),required=False)
    address=forms.CharField(
        widget=forms.Textarea(  
            attrs={
                'rows': 5,
                'cols': 40,
                'class': 'form-control mb-3',
                'placeholder': 'Enter your address',
                'style': 'resize:none;'
            }
        ),required=False
    )
    created_at=forms.DateField(required=False,label='Created Date',widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form-control mb-3'
        }
    )
)
    updated_at=forms.DateField(required=False,label='Last Updated',widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form-control mb-3'
        }
    )
)
    image=forms.ImageField(required=False)
    video=forms.FileField(required=False)