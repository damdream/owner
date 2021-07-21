#import 목록
import json

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dog

# Class 구현해내기
class OwnerListView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            name = data['name']
            email = data['email']
            age = data['age']
            Owner.objects.create(name=name, email=email, age = age)
            
        except KeyError:
            return JsonResponse ({'MESSAGE':'IVALID_KEY'}, status=400)
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self,requset):
        owners = Owner.objects.all()
        results = []

        for owner in owners :
            dogs = [
            
                {"이름":dog.name} for dog in Dog.objects.filter(owner_id=owner.id)
            ]
            results.append(
                {
                    "name": owner.name,
                    "email" : owner.email,
                    "dog_list": dogs
                }
            )
            return JsonResponse({'result': results}, status =200)


class DogListView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            name = data['name']
            owner = Owner.objects.get(name=data['owner'])
            age = data['age']
            dog = Dog.objects.create(age=age,name = name, owner = owner)
        except KeyError:
            return JsonResponse ({'MESSAGE':'IVALID_KEY'}, status=400)
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self,request):
        dogs=Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    'owner': dog.owner.name,
                    'name': dog.name,
                    'age': dog.age
                }
            )
        return JsonResponse({'MESSAGE':results}, status = 200)    



