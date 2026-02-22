from django.contrib import admin
from .models import Student, Teacher, Subject

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'group', 
                    'session', 'phone_number', 'email')
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'designation', 'subject', 
                    'phone_number', 'email')
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'name', 'code')