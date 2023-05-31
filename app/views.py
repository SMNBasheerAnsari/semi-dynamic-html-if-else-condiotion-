from django.shortcuts import render

# Create your views here.
def table_data(request):
    d={'name':'BA','age':20,'sal':1000,'name1':'BA1','age1':21,'sal1':1000,'name2':'BA2','age2':22,'sal2':1200,'name3':'BA3','age3':23,'sal3':1500,'a':0}
    d1={'a':1002,'b':200,'c':300}
    return render(request,'oper.html',context=d1)
def loop(request):
    dict={'str':'string_elements'}
    return render(request,'loop.html',dict)