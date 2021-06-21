from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from rest_framework import filters
from rest_framework.authtoken.views import APIView
from rest_framework import permissions, status 
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .models import LoanRequest ,LoanOffer
from wallet.models import Wallet
from .serializers import CreateRequestSerializer ,LoanOfferSerializer
from django.shortcuts import get_object_or_404

class CreateRequestView(generics.CreateAPIView):
    #permission_classes = [AllowAny]
    query_set = LoanRequest.objects.all()
    serializer_class = CreateRequestSerializer

class LoanOfferView(APIView):
    #permission_classes = [AllowAny]

    def post(self, request, format='json', id=id):
        data = request.data.copy()
        data['request']=id
        data['user']=request.user.id
        serializer = LoanOfferSerializer(data=data)
        if serializer.is_valid():
            user_wallet= get_object_or_404(Wallet,user=request.user)
            post_user=get_object_or_404(LoanRequest,pk=id)
            if user_wallet.current_balance >= post_user.loan_ammount+(post_user.loan_ammount*0.03) :
                print(post_user)
                serializer.save()
                json_obj = serializer.data
                return Response(json_obj, status=status.HTTP_201_CREATED)
            return Response("insufficient balance" ,status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AprroveRequestView(APIView):

    def post(self, request, format='json', id=id):
        post=get_object_or_404(LoanOffer,pk=id)
        if(request.user==post.request.user):
            post.status="Approved"
            post.request.status="Funded"
            post.save()
            user_wallet= get_object_or_404(Wallet,user=request.user)
            post_user_wallet=get_object_or_404(Wallet,user=post.user)
            post_user_wallet.transfer(user_wallet,post.request.loan_ammount)
            return Response("Offer Approved" ,status=status.HTTP_202_ACCEPTED)
        return Response("Unauthrized access" ,status=status.HTTP_401_UNAUTHORIZED)

class RefusedRequestView(APIView):
    def patch(self, request, format='json', id=id):
        post=get_object_or_404(LoanOffer,pk=id)
        if(request.user==post.request.user):
            post.status="Refused"
            post.save()
            return Response("Offer Refused" ,status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response("Unauthrized access" ,status=status.HTTP_401_UNAUTHORIZED)