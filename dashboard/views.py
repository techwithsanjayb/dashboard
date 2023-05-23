from django.shortcuts import render
import json
from bs4 import BeautifulSoup
import requests
from .utils import *
from bhashanet_dashbaord.logger import log
from bhashanet_dashbaord import logger
from .models import *
from django.http import JsonResponse


# Create your views here.
def dashboard(request):
    f = open('domainlist.json')
    data = json.load(f)
    f.close()

    # Now you can use data as a normal dict:
    for (k, v) in data.items():
        # print(v)
        Hindi_Url = str(v[0]["Hindi_url"])
        Marathi_url = str(v[0]["Marathi_url"])
        Bengali_url = str(v[0]["Bengali_url"])
        Kannada_url = str(v[0]["Kannada_url"])
        Malayalam_url = str(v[0]["Malayalam_url"])
        Manipuri_url = str(v[0]["Manipuri_url"])

        # CHECKING HINDI URL STATUS FROM HERE--------------
        v[0]["Hindi_status"] = check(Hindi_Url)
        # HINDI URL STATUS IS SET--------------------------

        # CHECKING MARATHI URL STATUS FROM HERE--------------
        v[0]["Marathi_status"] = check(Marathi_url)
        # MARATHI URL STATUS IS SET-------------------------

        # CHECKING BENGALI URL STATUS FROM HERE--------------
        v[0]["Bengali_status"] = check(Bengali_url)
        # BENGALI URL STATUS IS SET-------------------------

        # CHECKING KANNADA URL STATUS FROM HERE--------------
        v[0]["Kannada_status"] = check(Kannada_url)
        # KANNADA URL STATUS IS SET-------------------------

        # CHECKING MALAYALAM URL STATUS FROM HERE--------------
        v[0]["Malayalam_status"] = check(Malayalam_url)
        # MALAYALAM URL STATUS IS SET--------------------------

        # CHECKING MALAYALAM URL STATUS FROM HERE--------------
        v[0]["Manipuri_status"] = check(Manipuri_url)
        # MALAYALAM URL STATUS IS SET-------------------------

        ###############################################################################

        # CHECKING HINDI CONTENT STATUS FROM HERE--------------
        v[0]["Hindi_content"] = check_lang(Hindi_Url)
        # HINDI URL CONTENT IS SET--------------------------

        # CHECKING MARATHI CONTENT STATUS FROM HERE--------------
        v[0]["Marathi_content"] = check_lang(Marathi_url)
        # MARATHI URL CONTENT IS SET--------------------------

        # CHECKING BENGALI CONTENT STATUS FROM HERE--------------
        v[0]["Bengali_content"] = check_lang(Bengali_url)
        # BENGALI URL CONTENT IS SET--------------------------

        # CHECKING KANNADA CONTENT STATUS FROM HERE--------------
        v[0]["Kannada_content"] = check_lang(Kannada_url)
        # KANNADA URL CONTENT IS SET--------------------------

        # CHECKING MALAYALAM CONTENT STATUS FROM HERE--------------
        v[0]["Malayalam_content"] = check_lang(Malayalam_url)
        # MALAYALAM URL CONTENT IS SET--------------------------

        # CHECKING MANIPURI CONTENT STATUS FROM HERE--------------
        v[0]["Manipuri_content"] = check_lang(Manipuri_url)
        # MANIPURI URL CONTENT IS SET--------------------------

    resultList = list(data.items())
    # log(request, resultList)
    logger.info(resultList)
    return render(request, 'dashboard/dashboard.html', {'data': resultList})
    # return render(request, 'dashboard/dashboard.html', {'data': data})


def dashboard2(request):
    Domain_obj = Domain_Information.objects.all()
    list_obj = list(Domain_Information.objects.values())
    # print(list_obj)
    # json_obj = JsonResponse(list_obj, safe=False)
    # print(type(json_obj))
    print(JsonResponse(list_obj, safe=False))
    return JsonResponse(list_obj, safe=False)
    # return render(request, 'dashboard/dashboard2.html',{'Domain_obj':Domain_obj})


def dashboard3(request):
    Domain_obj = Domain_Information.objects.values()
    # print(Domain_obj)
    for value in Domain_obj:
        Hindi_URL_Status = check(value['Hindi_URL'])
        Marathi_URL_Status = check(value['Marathi_URL'])
        Bengali_URL_Status = check(value['Bengali_URL'])
        Kannada_URL_Status = check(value['Kannada_URL'])
        Malayalam_URL_Status = check(value['Malayalam_URL'])
        Manipuri_URL_Status = check(value['Manipuri_URL'])

        Domain_Information.objects.filter(Eng_URL=value['Eng_URL']).update(
            Hindi_Status=Hindi_URL_Status,
            Marathi_Status=Marathi_URL_Status,
            Bengali_Status=Bengali_URL_Status,
            Kannada_Status=Kannada_URL_Status,
            Malayalam_Status=Malayalam_URL_Status,
            Manipuri_Status=Manipuri_URL_Status
        )
        print("########################################################")
        print(Domain_obj)
    Domain_obj = Domain_Information.objects.values()
    return render(request, 'dashboard/dashboard3.html', {'Domain_obj': Domain_obj})
