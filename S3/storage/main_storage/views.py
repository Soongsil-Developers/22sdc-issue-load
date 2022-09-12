# from django.shortcuts import render
import boto3
import requests
import storage.my_settings as my_settings

from django.http import JsonResponse


# Create your views here.


def crawl_data():
    s3_client = boto3.client(
        service_name="s3", aws_access_key_id=my_settings.ACCESS_KEY_ID, aws_secret_key=my_settings.SECRET_ACCESS_KEY
    )
    obj = s3_client.get_object(Bucket="버킷 이름", key="키 이름")
    requests.post("보낼 곳의 주소 입력", data=obj)


def result(request):
    requests.post("보낼 곳의 주소 입력", data=request.body)
    return JsonResponse("Success", safe=False, status=201)
