from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import numpy as np

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

@csrf_exempt
def calculatePercentile(request):
    data=request.body
    data_in_dic=json.loads(data)
    str_data=data_in_dic['data']
    str_data.replace(',',' ')
    list=str_data.split()
    new_list=[]
    final_result=[]
    for i in range(len(list)):
        if(isfloat(list[i])):
            x=float(list[i])
            new_list.append(x)
    percent=int(data_in_dic['percentile'])
    arr=np.array(new_list)
    result=round(np.percentile(arr,percent),2);
    for i in range(0,20):
        final_result.append(round(np.percentile(arr,i*5),2))
    return JsonResponse({'ans': result,'finalresult':final_result})
