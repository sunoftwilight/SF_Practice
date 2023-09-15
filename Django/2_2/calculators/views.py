from django.shortcuts import render

# Create your views here.
def calculator(request, num1, num2):
    mul = num1 * num2
    minus = num1 - num2
    if num2 != 0:
        div = num1 / num2
    else:
        div = None

    context = {
        'num1': num1,
        'num2': num2,
        'mul': mul,
        'minus': minus,
        'div': div,
    }
    return render(request, 'calculators/calculator.html', context)