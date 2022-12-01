from .models import *
from django import forms

class applicant_bio(forms.ModelForm):
    class Meta:
        model = Bio_data
        fields = '__all__'

class applicant_bio_edit(forms.ModelForm):
    class Meta:
        model = Bio_data
        fields = '__all__'

class applicant_NEXT_OF_KIN(forms.ModelForm):
    class Meta:
        model = NEXT_OF_KIN
        fields = '__all__'

class applicant_CURRENT_ACADEMIC_LEVEL(forms.ModelForm):
    class Meta:
        model = CURRENT_ACADEMIC_LEVEL
        fields = '__all__'

class applicant_upload_certificates(forms.ModelForm):
    class Meta:
        model = upload_certificates
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']