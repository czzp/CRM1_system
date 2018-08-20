# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jsonpickle
from django.core import serializers
from django.core.paginator import Paginator
from django.urls import reverse

from crm.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from crm.models import UserInfo


def login(request):

    return render(request,'login.html')

def index(request):
    
    return render(request,'main.html')


def others(request,addr):
    return render(request,addr)


class Login(View):

    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        userNum = request.POST.get('userNum')
        userPw = request.POST.get('userPw')
        if not UserInfo.objects.filter(user_num=userNum,user_pw=userPw):
            return render(request, 'login.html',{'flag': 1 })
        return render(request, 'main.html')


def main(request,addr):
    return render(request, 'main.html',{'addr':addr})


def noticeDel(request,num):
    num = int(num)
    NoticeInfo.objects.filter(notice_id = num).delete()
    return render(request,'notice_list.html')


def noticeAdd(request):
    user = request.POST.get('user','')
    notice_item = request.POST.get('notice_item')
    notice_content = request.POST.get('notice_content')
    notice_time = request.POST.get('notice_time')
    notice_endtime = request.POST.get('notice_endtime')
    if '' in [user,notice_time,notice_item,notice_endtime,notice_content]:
        return render(request,'notice_add.html',{'flag5':1})
    NoticeInfo.objects.create(user=user,notice_content=notice_content,notice_endtime=notice_endtime,notice_time=notice_time,notice_item=notice_item)
    return HttpResponseRedirect('/crm/notice_list.html')

def getUser(request):
    user = request.GET.get('user')
    result = UserInfo.objects.filter(user_name=user)
    # result=jsonpickle.dumps(result)
    # result=serializers.serialize('json',result)
    # print result
    result = None if len(result) == 0 else 1
    return JsonResponse({'result':result})


def noticeQuery(request):
    flag = int(request.POST.get('queryType',''))
    word = request.POST.get('noticeInput','')
    if flag == 1 :
        noticeList=NoticeInfo.objects.filter(notice_item__contains=word)
    elif flag == 2:
        noticeList = NoticeInfo.objects.filter(notice_content__contains=word)
    else:
        noticeList = []
    print noticeList
    return render(request,'notice_list.html',{'noticeList':noticeList})


def departmentAdd(request):
    department_name = request.POST.get("departmentName",'')
    department_desc = request.POST.get("departmentDesc",'')
    list1 = ['',None]
    flag = {}
    if department_desc in list1 or department_name in list1:
        flag['项目不能为空'] = -1
        return render(request, 'dept_add.html', {'flag': flag})
    try:
        dep = DepartmentInfo.objects.get(department_name=department_name.encode(encoding='UTF-8'))
        flag['已存在此部门'] = 1
        return render(request, 'dept_add.html', {'flag': flag})
    except:
        dep = DepartmentInfo.objects.create(department_name=department_name,department_desc=department_desc,is_used = 1)
        flag['添加成功']= 2
        return render(request,'dept_add.html',{'flag':flag})


def departmentDel(request):
    department_id = request.GET.get('id')
    try:
        userList = UserInfo.objects.filter(department_id = department_id)
        departmentList = DepartmentInfo.objects.filter(department_id=department_id)
        for i in departmentList:
            i.userinfo_set.clear()
        DepartmentInfo.objects.filter(department_id=int(department_id)).delete()
    except Exception as e:
        return HttpResponse(e)
    return render(request,'dept_add.html')


def get_userNum(request):
    num = request.GET.get('num')
    l1 = UserInfo.objects.filter(user_num=num)
    num1 = True if len(l1) == 0 else False
    return JsonResponse({'res':num1})


def userAdd(request):
    fieldsDict = request.POST
    fieldsDict = fieldsDict.items()
    dict1 = {}
    try:
        for i,j in fieldsDict:
            if i == 'department':
                j = DepartmentInfo.objects.get(department_id = j)
            if i == 'role':
                j = UserRole.objects.get(role_id= j)
            if i not in ['csrfmiddlewaretoken']:
                dict1[i] = j
        UserInfo.objects.create(is_used = 1,**dict1)
        return render(request,'emp_add.html',{'flag3': 1})
    except:
        return render(request, 'emp_add.html', {'flag3': 0})


def roleAdd(request):
    powerDict = {'太阳':-5,'月亮':0,'一星':1,'两星':2,'三星':3,}
    roleNameList = [role.role_name for role in UserRole.objects.all()]
    roleName = request.POST.get('roleName')
    if roleName in ['',None]:
        return render(request, 'role_add.html', {'flag': -1})
    if roleName in roleNameList:
        return render(request, 'role_add.html', {'flag': 0})
    rolePower = request.POST.get('rolePower')
    try:
        UserRole.objects.create(role_name = roleName,role_power = rolePower,is_used = 1)
        return render(request,'role_add.html',{'flag':1})
    except:
        return HttpResponse('出现问题')


def userRoleDel(request):
    num = request.GET.get('num')
    try:
        UserRole.objects.filter(role_id=num).delete()
    except:
        return render(request, 'role_add.html',{'flag':-2})
    return render(request,'role_add.html')


def getCustomer(request):
    try:
        customer_id = int(request.GET.get('id'))
        cus = CustomerInfo.objects.filter(customer_id=customer_id)[0]
    except:
        return HttpResponse('出现小问题')
    return render(request,'customer_detail.html',{'cus':cus})


def editCustomer(request):
    try:
        customer_id = int(request.GET.get('id'))
        cus = CustomerInfo.objects.filter(customer_id=customer_id)[0]
    except:
        return HttpResponse('出现小问题')
    return render(request,'customer_edit.html',{'cus':cus})


def delCustomer(request):
    try:
        customer_id = int(request.GET.get('id'))
        cus = CustomerInfo.objects.filter(customer_id=customer_id).delete()
    except:
        return HttpResponse('删除失败，检查数据库Cascade字段')
    return render(request,'customer_list1.html',{'flag':1})


def addCustomer(request):
    cusDict = request.POST
    cusDict1={}
    try:
        con = CustomerCondition.objects.get(condition_id=cusDict['condition'])
        tp = CustomerType.objects.get(type_id=cusDict['type'])
        sou = CustomerSource.objects.get(source_id=cusDict['source'])
        for i ,j in cusDict.items():
            if i != 'csrfmiddlewaretoken':
                cusDict1[i]=j
        cusDict1.update({'condition':con,'type':tp,'source':sou,})
        CustomerInfo.objects.create(**cusDict1)
        return render(request,'customer_add.html',{'flag4':1,'mesg':'添加成功'})
    except Exception as e:
        return render(request,'customer_add.html',{'flag4':2,'mesg':e})


def updateCustomer(request):
    print request.POST.get('customer_id')
    cusDict = request.POST
    cusDict1 = {}
    try:
        user = UserInfo.objects.get(user_id=cusDict['user'])
        con = CustomerCondition.objects.get(condition_id=cusDict['condition'])
        tp = CustomerType.objects.get(type_id=cusDict['type'])
        sou = CustomerSource.objects.get(source_id=cusDict['source'])
        for i, j in cusDict.items():
            if i != 'csrfmiddlewaretoken':
                cusDict1[i] = j
        cusDict1.update({'condition': con, 'type': tp, 'source': sou,'user':user })
        cus1 = CustomerInfo.objects.filter(customer_id=cusDict1['customer_id']).update(**cusDict1)
        return render(request, 'customer_list1.html', {'flag4': 1, 'mesg': '修改成功'})
    except Exception as e:
        print e
        return render(request, 'customer_list1.html', {'flag4': 2, 'mesg': e})

# def pageCus(request,objectList,pagenum,html='customer_list2.html'):
#     paginator = Paginator(objectList, per_page=2)
#     page = paginator.page(int(pagenum))
#     try:
#         proPageNum = int(page.previous_page_number())
#     except:
#         proPageNum = 1
#     try:
#         nextPageNum = page.next_page_number()
#     except:
#         nextPageNum = paginator.num_pages
#     return render(request, html,
#                   {'customerList': page, 'pageNums': paginator.num_pages, 'num': pagenum, 'page': page,
#                    'proPageNum': proPageNum, 'nextPageNum': nextPageNum})


def pageCustomer(request,num):
    # pageNum = 2 #一页的条数
    customerList = CustomerInfo.objects.all().order_by('-customer_addtime')
    # return pageCus(request,customerList,num,'customer_list1.html')
    paginator = Paginator(customerList,per_page=3)
    page = paginator.page(int(num))
    try:
        proPageNum= int(page.previous_page_number())
    except:
        proPageNum = 1
    try:
        nextPageNum= page.next_page_number()
    except:
        nextPageNum = paginator.num_pages
    return render(request,'customer_list1.html',{'customerList':page,'pageNums': paginator.num_pages,'num':num,'page':page,'proPageNum':proPageNum,'nextPageNum':nextPageNum})

# def pageFunction():
def queryCustomer(request,num=1):
    customerInput = request.GET.get('customerInput')
    queryType = request.GET.get('queryType')
    dict1 = {CustomerCondition: "2",CustomerSource: "3",CustomerType: "4",UserInfo: "5",}
    if queryType == "1":
        customerList2 = CustomerInfo.objects.filter(customer_name__contains=customerInput).order_by('-customer_addtime')
    elif queryType == "6":
        customerList2 = CustomerInfo.objects.filter(customer_company__contains=customerInput).order_by('-customer_addtime')
    elif queryType == "2":
        customerList1 = CustomerCondition.objects.filter(condition_name__contains=customerInput)
        customerList2=[]
        for i in customerList1:
            for j in i.customerinfo_set.all():
                customerList2.append(j)
    elif queryType == "3":
        customerList1 = CustomerSource.objects.filter(source_name__contains=customerInput)
        customerList2 = []
        for i in customerList1:
            for j in i.customerinfo_set.all():
                customerList2.append(j)
    elif queryType == "4":
        customerList1 = CustomerType.objects.filter(type_name__contains=customerInput)
        customerList2 = []
        for i in customerList1:
            for j in i.customerinfo_set.all():
                customerList2.append(j)
    elif queryType == "5":
        customerList1 = UserInfo.objects.filter(user_name__contains=customerInput)
        customerList2 = []
        for i in customerList1:
            for j in i.customerinfo_set.all():
                customerList2.append(j)
    # return pageCus(request,customerList2,num,'customer_list2.html')
    paginator = Paginator(customerList2, per_page=3)
    page = paginator.page(int(num))
    try:
        proPageNum = int(page.previous_page_number())
    except:
        proPageNum = 1
    try:
        nextPageNum = page.next_page_number()
    except:
        nextPageNum = paginator.num_pages
    return render(request, 'customer_list2.html',{'customerList': page, 'pageNums': paginator.num_pages, 'num': num, 'page': page,
     'proPageNum': proPageNum, 'nextPageNum': nextPageNum,"customerInput": customerInput,"queryType":queryType})