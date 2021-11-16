# from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.mail import send_mail

from api.coronavstech.companies.models import Company
from api.coronavstech.companies.serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by('-last_update')
    pagination_class = PageNumberPagination


@api_view(http_method_names=['POST'])
def send_company_email(request:Request) -> Response:
    '''
        sends email with request payload
        sender: whosyerdady2007@gmail.com
        receiver: whosyerdady2007@gmail.com
    '''
    send_mail(subject=request.data.get('subject'), message=request.data.get('message'), from_email='whosyerdady2007@gmail.com', recipient_list=['whosyerdady2007@gmail.com'])
    return Response({
        'status': 'success',
        'info': 'email sent successfully'
    },
                    status=200)
