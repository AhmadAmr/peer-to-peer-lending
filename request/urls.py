from django.urls import  path
from .views import  CreateRequestView , LoanOfferView ,AprroveRequestView,RefusedRequestView
urlpatterns = [
    
    path('create/', CreateRequestView.as_view()), 
    path('offer/<int:id>',LoanOfferView.as_view()),
    path('offer/approve/<int:id>',AprroveRequestView().as_view()),
    path('offer/refused/<int:id>',RefusedRequestView().as_view()),
]