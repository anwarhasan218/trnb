from django.contrib import admin
from .models import Teacher, TrainingProgram, Enrollment

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "national_id", "record_number", "subject", "stage")
    search_fields = ("name", "national_id", "record_number", "subject", "stage")
    list_filter = ("subject", "stage")

@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "target_group", "stage", "start_date", "end_date", "room_number")
    search_fields = ("name", "target_group", "stage", "room_number")
    list_filter = ("stage", "target_group")

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("teacher", "training_program", "date_joined")
    search_fields = ("teacher__name", "teacher__national_id", "training_program__name")
    list_filter = ("training_program", "teacher__stage")
