from django.shortcuts import render

foods = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
drinks = ["cider","coke","miranda","fanta", "eye of finetree"]

# Create your views here.
# foods와 drinks 모두 한 페이지에서 출력되어야 하는 요소임
# 두 값의 key를 동일한 이름으로 설정하면 receipts 페이지에서 
# food와 drink 중 무엇이 들어오든 items 하나로 처리 가능하다

def food(request):
    context = {
        'items': foods,
        # (방법 2) 분리를 위함
        # food 함수는 종류를 'food'라는 문자열로 넘겨줌
        'fnd': 'food',
    }
    return render(request, 'menus/food.html', context)


def drink(request):
    context = {
        'items': drinks,
        # (방법 2) 분리를 위함
        # drink 함수는 종류를 'drink'라는 문자열로 넘겨줌
        'fnd': 'drink'
    }
    return render(request, 'menus/drink.html', context)


def receipt(request):
    # 입력 받을 때 lower()를 적용해줬기 때문에 input란에 fanta를 FANTA로 입력해도 문제 X
    thing = request.GET.get('thing').lower()
    # (방법 1) 아래 처럼 하면 /food/에서 drinks 원소 입력해도 receipt에서 정상 출력됨
    # => 분리가 필요 (방법 2)
    fnd = request.GET.get('fnd')
    context = {
        'thing': thing,
        # (방법 1)
        # 'items': foods + drinks,
        # (방법 2)
        'foods': foods,
        'drinks': drinks,
        # 종류
        # order에서 받아온 fnd를 receipt의 fnd key의 값으로 넣어줌
        'fnd': fnd,
    }
    return render(request, 'menus/receipt.html', context)