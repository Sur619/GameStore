from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Store.models import Question, Products, ProductType, Customer, Order, Sale


def show_main_page(request, question_id):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    selected_question = Question.objects.get(pk=question_id)
    template = loader.get_template('store/main_page.html')
    context = {
        'latest_question_list': latest_question_list,
        'selected_question': selected_question,
    }
    return render(request, 'store/main_page.html', context)


def detail_product(request, product_id):
    searched_product = Products.objects.get(pk=product_id)
    categories = searched_product.type_id.category.all()

    context = {
        'searched_product': searched_product,
        'category_product': categories,
    }
    return render(request, 'store/detail_product.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def Order_details(request, order_id):
    order_info = Order.objects.get(pk=order_id)

    customer_info = order_info.customer_id

    all_customer_orders = customer_info.order_set.all()

    context = {
        'customer': customer_info,
        'order_info': order_info,
        'all_customer_orders': all_customer_orders
    }

    return render(request, 'store/order_details.html', context)

# def sales_info(request, product_id, order_id):
#     product = Products.objects.get(pk=product_id)
#     order_info = Order.objects.get(pk=order_id)
#     customer_info = order_info.customer_id
#     all_customer_orders = customer_info.order_set.all()
#     sales_info = Sale.objects.get(product_id=product_id, order_id=order_id)
#
#