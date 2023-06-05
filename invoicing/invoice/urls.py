from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns =[
    path("invoices",csrf_exempt(AllInvoices.as_view()),name="AllInvoices"),
    path("invoices/new",csrf_exempt(AllInvoices.as_view()),name="newinvoices"),
    path("invoces/<int:id>",SpecificInvoices.as_view(),name="specificinvoices"),
    path("invoces/<int:id>/items",csrf_exempt(Additems.as_view(),name="Additems")),
    path("signup",csrf_exempt(SignUpView.as_view()),name="SignUpView"),
        path("signin",csrf_exempt(SignInView.as_view()),name="SignInView"),
    ]
    