from rest_framework.urls import path
from .views import LoanView, LoanDetailView, UserLoansView
from django.urls import path
from .views import CopyCreatelView, CopyDateilView

urlpatterns = [
    path("loans/", LoanView.as_view()),
    path("loans/<int:pk>/", LoanDetailView.as_view()),
    path("user/loans/<int:pk>/", UserLoansView.as_view()),
    path("copies/", CopyCreatelView.as_view()),
    path("copies/<int:copy_id>/", CopyDateilView.as_view()),
]
