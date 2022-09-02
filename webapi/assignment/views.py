from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

import json
# import pandas as pd
import csv
from django.conf import settings

# Create your views here.

def transaction(request, transaction_id=None):
    if (request.method == "GET"):
        data = {}
        file_name = settings.MEDIA_ROOT+ '/' + 'Transaction_20180101101010.csv'
        with open(file_name) as input_file:
            reader = csv.reader(input_file)
            for row_number, row in enumerate(reader):
                if row_number == 0:
                    continue
                else:
                    if row[0] == transaction_id:
                        data['transactionId'] = row[0]
                        data['productId'] = row[1]
                        data['transactionAmount'] = row[2]
                        data['transactionDatetime'] = row[3]
        if len(data) > 0:
            print(data)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message':'Transaction Id Does not Exist'})

def transactionSummaryByProducts(request, last_n_days=None):
    if (request.method == "GET"):
        data = {}
        file_name = settings.MEDIA_ROOT+ '/' + 'Transaction_20180101101010.csv'
        with open(file_name) as input_file:
            reader = csv.reader(input_file)
            for row_number, row in enumerate(reader):
                if row_number == 0:
                    continue
                else:
                    if row[0] == last_n_days:
                        data['transactionId'] = row[0]
                        data['productId'] = row[1]
                        data['transactionAmount'] = row[2]
                        data['transactionDatetime'] = row[3]

        file_name1 = settings.MEDIA_ROOT+ '/' + 'ProductReference.csv'
        with open(file_name1) as input_file:
            reader1 = csv.reader(input_file)
            for row_number, row1 in enumerate(reader1):
                if row_number == 0:
                    continue
                else:
                    if row1[0] == data['productId']:
                        dict_data = { "Summary": [ {"productName": row1[1], "totalAmount":data['transactionAmount']}]}

        if len(dict_data) > 0:
            return JsonResponse(dict_data, safe=False)
        else:
            return JsonResponse({'message':'Production Does not Exist'})

def transactionSummaryByManufacturingCity(request, last_n_days=None):
    if (request.method == "GET"):
        data = {}
        file_name = settings.MEDIA_ROOT+ '/' + 'Transaction_20180101101010.csv'
        with open(file_name) as input_file:
            reader = csv.reader(input_file)
            for row_number, row in enumerate(reader):
                if row_number == 0:
                    continue
                else:
                    if row[0] == last_n_days:
                        data['transactionId'] = row[0]
                        data['productId'] = row[1]
                        data['transactionAmount'] = row[2]
                        data['transactionDatetime'] = row[3]

        file_name1 = settings.MEDIA_ROOT+ '/' + 'ProductReference.csv'
        with open(file_name1) as input_file:
            reader1 = csv.reader(input_file)
            for row_number, row1 in enumerate(reader1):
                if row_number == 0:
                    continue
                else:
                    if row1[0] == data['productId']:
                        dict_data = { "Summary": [ {"cityName": row1[2], "totalAmount":data['transactionAmount']}]}
        if len(dict_data) > 0:
            return JsonResponse(dict_data, safe=False)
        else:
            return JsonResponse({'message':'Production Does not Exist'})
