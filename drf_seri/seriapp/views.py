from django.shortcuts import render
from .serilalizer import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer  
from django.http import HttpResponse

# Create Model object - single student data.

def student_detail(request, ak):
    stu = Student.objects.get(id=ak)
    print("vvv   :- ",   stu)
    serializer = StudentSerializer(stu)
    print("sss   :- ",   serializer)
    print("ddd   :- ",   serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print("jjj   :- ",    json_data)
    return HttpResponse(json_data , content_type = 'application/json')


#   Query set - All student data  


def student_list(request):
    stu = Student.objects.all()
  #  print("vvv   :- ",   stu)
    serializer = StudentSerializer(stu, many = True)
  #  print("sss   :- ",   serializer)
  #  print("ddd   :- ",   serializer.data)
    json_data = JSONRenderer().render(serializer.data)
  #  print("jjj   :- ",    json_data)
    return HttpResponse(json_data , content_type = 'application/json')    
