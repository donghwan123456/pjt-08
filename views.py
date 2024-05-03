from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
from django.http import JsonResponse

##########################################################
import csv
import numpy as np
import pandas as pd



array_length = 1000
random_range = 5000

## csv파일 읽어오기

def read_csv(request):
    # pandas를 사용하여 CSV 파일 읽기
    df = pd.read_csv('test_data.CSV', encoding='utf-8')
    df.head()
    # 데이터프레임을 딕셔너리 형태로 변환하여 템플릿으로 전달
    data = df.to_dict('records')

    return JsonResponse({ 'dat': data })

###############################################################

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

################################################################
def replace_empty_with_null(request):

    # pandas를 사용하여 CSV 파일 읽기
    df = pd.read_csv('test_data.CSV', encoding='utf-8')
    df.head()
    # 빈 값을 Null 문자열로 치환
    df.replace('', pd.NA, inplace=True)

    # 데이터프레임을 JSON 형태로 변환
    json_data = df.to_json(orient='records')

    return JsonResponse(json_data, safe=False)

##################################################################

df = pd.read_csv('test_data.CSV', encoding='utf-8')

def find_similar_age_rows(request):
    global df

    # "나이" 필드에 대한 결측치를 제외한 데이터들의 평균 계산
    avg_age = df['나이'].dropna().mean()

    # 각 행의 나이와 평균 나이 사이의 차이 계산
    df['나이와의 차이'] = abs(df['나이'] - avg_age)

    # 차이를 기준으로 정렬하여 가장 비슷한 나이인 10개 행 선택
    similar_age_rows = df.sort_values(by='나이와의 차이').head(10)

    # 새로운 데이터프레임을 JSON 형태로 변환
    json_data = similar_age_rows.to_json(orient='records')

    return JsonResponse(json_data, safe=False)

    #####################################################################