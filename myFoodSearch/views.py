#coding:utf-8
from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse
# from myFoodSearch import idToFood


def tmpsearch(request):
    return render(request,'List_of_cakes/Angel_cake.html')
#通过相应的网址直接显示这个html

def search(request):
    return render(request,'search.html')


dic= {'egg':(1,2,3,5,),'chicken':(4,6,)}
listtot=[
    {'ID':'0', 'name':'foodname0'},
    {'ID':'1', 'name':'foodname1'},
    {'ID':'2', 'name':'foodname2'},
    {'ID':'3', 'name':'foodname3'},
    {'ID':'4', 'name':'foodname4'},
    {'ID':'5', 'name':'foodname5'},
    {'ID':'6', 'name':'foodname6'},
    ]
#############################################
lis = []
myfile = open('myFoodSearch/list.txt','r')
data = myfile.readlines()
myfile.flush()
for item in data:
    i = 0
    while 1:
        if item[i] == ',':
            break
        i += 1
    lis.append(item[i+1:-1])
myfile.close()


def cal(list1,list2):
    tmp = []
    for i in range(1,279):
        if(i in list1 and i in list2):
            tmp.append(i)
    return tmp

def findID(foodname):
    tmplist = []
    file = open('dataList.txt','r')
    data = file.readlines()
    file.close()
    for line in data:
        if(foodname == (line.split(','))[0]):
            for i in line.split(',')[1:]:
                tmplist.append(int(i))
            return tmplist



############################################
#
# def foodToID(food):
#     mylist = []
#     IDlist = list(dic[food])
#     for i in range(len(IDlist)):
#         mylist.append(listtot[int(IDlist[i])])
#     return mylist

################################################################################
def searched(request):
    info = ''
    lhydata = []
    if(request.GET.has_key('food')):
        info = str(request.GET['food']).lower()
    infolist = info.split(" ")
    tmpinfo = findID(infolist[0])
    if(len(infolist)>1):
        for item in infolist:
            tmpinfo = cal(tmpinfo,findID(item))
    for num in tmpinfo:
        try:
            lhydata.append({'ID':num,'name':lis[num]})
        except:
            return HttpResponse("Not Found")
    return render_to_response('search.html', {'list':lhydata})

def openhtml(request):
    id = request.GET['id']
    url = id + ".html"
    return render(request, url)



