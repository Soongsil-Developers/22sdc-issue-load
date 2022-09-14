import datetime
import json
import boto3
import requests

s3 = boto3.client('s3', region_name='ap-northeast-2')
BUCKET_NAME = "issue-keyword-storage"


def upload_json(file_path):
    now = datetime.datetime.now()
    key = "json/" + datetime.datetime.strftime(now, "%Y-%m-%d %H:%M") + ".json"
    s3.upload_file(file_path, BUCKET_NAME, key)


def send_json_to_model():
    #latest file 10
    file_list = (s3.list_objects(Bucket=BUCKET_NAME, Prefix='json/')['Contents'])[-10:-1]
    s3_objects = [s3.get_object(Bucket=BUCKET_NAME, Key=content['Key']) for content in file_list]
    json_objects = [json.loads(obj_dict['Body'].read().decode()) for obj_dict in s3_objects]
    title_contents = [article['title'] + " " + article['content'] for j_obj in json_objects for article in j_obj]
    
    model_json = {'articles': title_contents}
    model_api = "http://10.0.2.208:8000/keyword"
    res = requests.post(model_api, json=model_json)
    print(res.text)