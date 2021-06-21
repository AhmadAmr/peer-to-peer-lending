from rest_framework import serializers
from .models import LoanOffer, LoanRequest


class CreateRequestSerializer(serializers.ModelSerializer):
    user= serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model=LoanRequest
        exclude = ['status']
        readonly_field = ['user']
        lookup_field = 'id'


class LoanOfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=LoanOffer
        exclude =['status']
        lookup_field = 'id'


