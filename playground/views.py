from django.shortcuts import render
from django.http import HttpResponse

this_dict = {'age':23}

def check_prime(input_value):
    if(input_value == 2):
        return 'Prime'
    else:
        for i in range(2,input_value):
            if(input_value%i == 0):
                return 'Not Prime'
        return 'Prime'
def testing_hello(request):
    detest = check_prime(2)
    dict_1 = {'prime':detest}
    return render(request,'hello.html',dict_1)