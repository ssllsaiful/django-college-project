from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Student, Teacher

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer


def hello_world(request):
    return JsonResponse({
        "message": "Hello World"
    })

def home(request):
    return JsonResponse({
        "message": "Welcome to the Home Page"
    })

def students_list(request):
    students = Student.objects.all()
    data = []
    for student in students:

        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "group": student.group,
            "session": student.session,
            "phone_number": student.phone_number,
            "email": student.email,
        })
    return JsonResponse(data, safe=False)

def teachers_list(request):
    teacher_id = request.GET.get('teacher_id')  # get query param
    if teacher_id:
        teachers = Teacher.objects.filter(teacher_id=teacher_id)
    else:
        teachers = Teacher.objects.all()

    data = []
    for teacher in teachers:
        data.append({
            "teacher_id": teacher.teacher_id,
            "name": teacher.name,
            "designation": teacher.designation,
            "subject": teacher.subject,
            "phone_number": teacher.phone_number,
            "email": teacher.email
        })

    return JsonResponse(data, safe=False)


# API views using DRF for better serialization and response handling
#Swagger list addition

@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    response_data = {
        "total_count": students.count(),
        "students": serializer.data
    }

    # Pretty print JSON
    return Response(
        response_data,
        content_type="application/json"
    )

@api_view(['GET'])
def teachers_list(request):
    teacher_id = request.GET.get('teacher_id')
    teachers = Teacher.objects.all()
    if teacher_id:
        teachers = teachers.filter(teacher_id=teacher_id)
    serializer = TeacherSerializer(teachers, many=True)
    response_data = {
        "total_count": teachers.count(),
        "teachers": serializer.data
    }
    return Response(
    response_data,
    content_type="application/json"
    )


