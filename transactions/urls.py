from django.urls import path
from . import views
urlpatterns = [
    path('deposite/', views.DepositMoneyView.as_view(), name = 'deposite' ),
    path('borrow_book/<int:id>', views.BorrowBookView.as_view(), name = 'borrow_book' ),
]
