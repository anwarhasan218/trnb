from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'name', 'national_id', 'record_number', 'subject', 'stage',
            'region', 'administration', 'institute', 'job_grade'
        ]
        labels = {
            'name': 'اسم المعلم',
            'national_id': 'الرقم القومي',
            'record_number': 'رقم السجل',
            'subject': 'المادة',
            'stage': 'المرحلة التعليمية',
            'region': 'المنطقة',
            'administration': 'الإدارة',
            'institute': 'المعهد',
            'job_grade': 'الدرجة الوظيفية',
        } 