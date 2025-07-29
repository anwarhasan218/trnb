from django.urls import path
from . import views
from .views import report_view, export_report_excel, export_report_pdf, attendance_sheet_pdf, attendance_sheet_print, attendance_sheet_excel

urlpatterns = [
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_add, name='teacher_add'),
    path('teachers/<int:pk>/edit/', views.teacher_edit, name='teacher_edit'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    path('teachers/import/', views.teacher_import, name='teacher_import'),
    path('teachers/template/', views.download_teacher_template, name='download_teacher_template'),
    path('teachers/delete_all/', views.delete_all_teachers, name='delete_all_teachers'),
    # برامج تدريبية
    path('programs/', views.program_list, name='program_list'),
    path('programs/add/', views.program_add, name='program_add'),
    path('programs/<int:pk>/edit/', views.program_edit, name='program_edit'),
    path('programs/<int:pk>/delete/', views.program_delete, name='program_delete'),
    path('programs/<int:pk>/', views.program_detail, name='program_detail'),
    path('programs/<int:pk>/enroll/', views.enroll_teacher, name='enroll_teacher'),
    path('programs/<int:pk>/unenroll/<int:teacher_id>/', views.unenroll_teacher, name='unenroll_teacher'),
    path('reports/', report_view, name='report_dashboard'),
    path('reports/export/excel/', export_report_excel, name='export_report_excel'),
    path('reports/export/pdf/', export_report_pdf, name='export_report_pdf'),
    path('programs/<int:pk>/attendance_sheet/pdf/', attendance_sheet_pdf, name='attendance_sheet_pdf'),
    path('programs/<int:pk>/attendance_sheet/print/', attendance_sheet_print, name='attendance_sheet_print'),
    path('programs/<int:pk>/attendance_sheet/excel/', attendance_sheet_excel, name='attendance_sheet_excel'),
    path('programs/<int:pk>/attendance_sheet/download_options/', views.attendance_sheet_download_options, name='attendance_sheet_download_options'),
    path('programs/<int:pk>/introduction_sheet/print/', views.introduction_sheet_print, name='introduction_sheet_print'),
    path('programs/<int:pk>/pretest_sheet/print/', views.pretest_sheet_print, name='pretest_sheet_print'),
    path('programs/<int:pk>/posttest_sheet/print/', views.posttest_sheet_print, name='posttest_sheet_print'),
    path('programs/<int:pk>/behavior_sheet/print/', views.behavior_sheet_print, name='behavior_sheet_print'),
    path('programs/<int:pk>/call_sheet/print/', views.call_sheet_print, name='call_sheet_print'),
    path('programs/<int:pk>/training_completion_notice/print/', views.training_completion_notice_print, name='training_completion_notice_print'),
    path('programs/<int:pk>/training_completion_notice/pdf/', views.training_completion_notice_pdf, name='training_completion_notice_pdf'),
] 