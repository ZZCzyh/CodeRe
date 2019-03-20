from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.http import HttpResponse
from interfaces import utils
from django.http import HttpResponse,HttpResponseRedirect
from backends.personal_info.interfaces import *
from backends.code_info.interfaces import *
import json

def index(request):
    print('in function index')
    if request.method == 'GET':
        return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        print("in function search")
        # print(request.POST.get('scriteria'))
        response = HttpResponse()
        response.set_cookie('scriteria', request.POST.get('scriteria'))
        response.set_cookie('license', request.POST.get('license'))
        #his_storage(username=request.POST.get('username'), content=request.POST.get('scriteria'))

        '''
        增加一个对search_result 的判断，如果其不符合预期，则返回错误
        此return值应当能够显示在网页当中 张雨豪负责下增加内容
        '''
        return response

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        registresult = utils.regist(request.POST.get('reg_username'), request.POST.get('reg_password'))
        print(request.POST.get('reg_username'))
        print("in function signup")
        if registresult['status']:
            # 注册成功
            print('注册成功')
            username = registresult['username']
            return HttpResponse("0")
        else:
            print("账号重复 注册失败")
            return HttpResponse("1")

def login(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        loginresult = utils.login(request.POST.get('username'), request.POST.get('password'))
        print(loginresult)
        # 应当跳转到search界面
        if loginresult['status']:
            # 登录成功
            print("登录成功")
            username = loginresult['username']
            return HttpResponse("0")
        elif loginresult['username'] != None:
            # 密码错误
            print("密码错误")
            return HttpResponse("1")
        else:
            # 账号不存在
            print('账号不存在')
            return HttpResponse("2")


def regist(request):
    if request.method == 'POST':
        registresult = utils.regist(request.POST.get('username'), request.POST.get('password'))
        '''
        注册成功，应当跳转到search界面
        注册失败，应当返回错误值
        '''
        return

def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


def result(request):
    if request.method == 'GET':
        return render(request, 'result.html')
    if request.method == 'POST':
        print("in function result")
        re = utils.get_search_result(request.COOKIES["scriteria"], request.COOKIES["license"])
        print(type(re))
        re_json = json.dumps(re)
        return HttpResponse(re_json, content_type="application/json,charset=utf-8")

def single(request):
    if request.method == 'GET':
        # 需要从request中读取接口的名称以返回详细信息
        #print(request.COOKIES["scriteria"])
        #search_result = utils.get_search_result(request.COOKIES["scriteria"], request.COOKIES["license"])
        #interface_name = request.GET.get('interface_name')
        #interface_name = 'numpy.array'
        #info = get_interface_info(interface_name)
        '''
        运用info字典进行处理，返回带有详细信息的single页面
        '''
        return render(request, 'single.html')
    if request.method == 'POST':
        print("in function single")
        re=utils.get_detail_result(request.POST.get('name'))
        response = HttpResponse()
        response.set_cookie('detail',re)
        return response
def handle(request):
    if request.method == 'GET':
        print("in function handle get")
        return render(request, 'single.html')
    if request.method == 'POST':
        print("in function handle post")
        res_json=eval(request.COOKIES['detail'])
        result = {
            're': res_json,
        }
        resu_json = json.dumps(result)
        print(resu_json)
        return HttpResponse(resu_json,content_type="application/json,charset=utf-8")


def question(request):
    if request.method == 'GET':
        return render(request, 'question.html')