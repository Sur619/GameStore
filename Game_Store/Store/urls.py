from django.urls import path

from . import views

urlpatterns = [

    path('main/<int:question_id>/', views.show_main_page, name='main'),
    path('<int:product_id>/', views.detail_product, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('sales/<int:sale_id>/', views.sales_info),
    path('customer_order/<int:order_id>/', views.Order_details, name='customer_order'),
]