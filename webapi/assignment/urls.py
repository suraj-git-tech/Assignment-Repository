from .import views
from django.urls import include, path

app_name = "assignment"

urlpatterns = [
    path('transaction/<transaction_id>/', views.transaction, name="transaction"),
    path('transactionSummaryByProducts/<last_n_days>/', views.transactionSummaryByProducts, name="transactionSummaryByProducts"),
    path('transactionSummaryByManufacturingCity/<last_n_days>/', views.transactionSummaryByManufacturingCity, name="transactionSummaryByManufacturingCity"),
]