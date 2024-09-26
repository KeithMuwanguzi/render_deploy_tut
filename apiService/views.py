from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from students.models import Student
from students.serializers import StudentSerializer

@api_view(['GET'])
def testEnd(request):
    data = {
        "status":"success",
        "message": "This is working properly"
    }
    return Response(data)

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':'success',
                'data': serializer.data,
            })
        else:
            return Response({
                'status':'error',
                'error':serializer.errors,
            })

@api_view(['GET'])
def get_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({
            'status': 'success',
            'data': serializer.data
        })

@api_view(['GET'])
def get_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({
            'status': 'error',
            'data': 'Student not found'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response({
            'status': 'success',
            'data': serializer.data
        })

