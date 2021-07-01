from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django .views import View
from django.utils.decorators import method_decorator
from django.views.decorators .csrf import csrf_exempt
# Create your views here.

@method_decorator(csrf_exempt ,name='dispatch')
class Student_api(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body  # to get all data from request
        strem = io.BytesIO(json_data)  # converting data in string
        pythondata = JSONParser().parse(strem)  # convering data in native python
        id = pythondata.get('id', None)  # to get id from parse data
        if id is not None:
            stu = Student.objects.get(id=id)  # filter data to send
            serliazer = StudentSerializer(stu)  # conver in python native
            json_data = JSONRenderer().render(serliazer.data)  # conver data in json format
            return HttpResponse(json_data, content_type='application/json')

        # if id not send then show all data
        stu = Student.objects.all()  # send all data
        serliazer = StudentSerializer(stu, many=True)  # conver in python native
        json_data = JSONRenderer().render(serliazer.data)  # conver data in json format
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body  # to get all data from request
        strem = io.BytesIO(json_data)  # converting data in string
        pythondata = JSONParser().parse(strem)  # convering data in native python
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': ' data post'}
            json_data = JSONRenderer().render(res)  # conver data in json format
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)  # conver data in json format
        return HttpResponse(json_data, content_type='application/json')


    def put(self, request, *args, **kwargs):
        json_data = request.body
        strem = io.BytesIO(json_data)
        pythondata = JSONParser().parse(strem)
        id = pythondata.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        print(stu)
        serializer = StudentSerializer(stu,data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': ' comp..... data upadted'}
            json_data = JSONRenderer().render(res)  # conver data in json format
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)  # it give errors
        return HttpResponse(json_data, content_type='application/json')


    def delete(self, request, *args, **kwargs):
        json_data = request.body
        strem = io.BytesIO(json_data)
        pythondata = JSONParser().parse(strem)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': ' data deleted'}
        json_data = JSONRenderer().render(res)  # conver data in json format
        return HttpResponse(json_data, content_type='application/json')







# FUNCTION base
# def student_api(request):
#     if request.method=='GET':
#         json_data=request.body # to get all data from request
#         strem= io.BytesIO(json_data) # converting data in string
#         pythondata=JSONParser().parse(strem)# convering data in native python
#         id=pythondata.get('id',None) # to get id from parse data
#         if id is not None:
#             stu=Student.objects.get(id=id) # filter data to send
#             serliazer=StudentSerializer(stu) # conver in python native
#             json_data=JSONRenderer().render(serliazer.data) # conver data in json format
#             return HttpResponse(json_data,content_type='application/json')
#
#         # if id not send then show all data
#         stu = Student.objects.all()  # send all data
#         serliazer = StudentSerializer(stu,many=True)  # conver in python native
#         json_data = JSONRenderer().render(serliazer.data)  # conver data in json format
#         return HttpResponse(json_data, content_type='application/json')
#
#     # FOR PARTIALLY UPDATE
#     if request.method=='PATCH':
#         json_data=request.body
#         strem=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(strem)
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data upadted'}
#             json_data = JSONRenderer().render(res)  # conver data in json format
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)  # it give errors
#         return HttpResponse(json_data, content_type='application/json')
#
#         # FOR complte UPDATE
#     if request.method == 'PUT':
#         json_data = request.body
#         strem = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(strem)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': ' comp..... data upadted'}
#             json_data = JSONRenderer().render(res)  # conver data in json format
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)  # it give errors
#         return HttpResponse(json_data, content_type='application/json')
#
#     # for delete
#     if request.method == 'DELETE':
#         json_data = request.body
#         strem = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(strem)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg': ' data deleted'}
#         json_data = JSONRenderer().render(res)  # conver data in json format
#         return HttpResponse(json_data, content_type='application/json')
# # for post
#     if request.method=='POST':
#         json_data=request.body # to get all data from request
#         strem= io.BytesIO(json_data) # converting data in string
#         pythondata=JSONParser().parse(strem)# convering data in native python
#         serializer=StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': ' data creaated'}
#             json_data = JSONRenderer().render(res)  # conver data in json format
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)  # conver data in json format
#         return HttpResponse(json_data, content_type='application/json')
#
#
#
