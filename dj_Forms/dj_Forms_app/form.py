from django import forms

class SampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

    def clean_email(self):
        print(f"sending email: {self.cleaned_data.get('email')} with message: {self.cleaned_data.get('message')}")
        