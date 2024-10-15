from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
# from api.models import Product
# from api.serializers import ProductSerializer
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from rest_framework.response import Response

# Path to your self-signed certificate
CA_CERT_PATH = 'C:\ELK 2\elasticsearch-8.15.2\config\certs\http_ca.crt'

# Create Elasticsearch client with SSL verification and your certificate
es = Elasticsearch(
    ['https://192.168.56.1:9200'],
    http_auth=('elastic', 'elastic'),
    verify_certs=True,
    ca_certs=CA_CERT_PATH
)

class ProductView(APIView):
    def get(self, request):
        # Fetch all products from Elasticsearch
        result = es.search(index='my-index', body={"query": {"match_all": {}}})
        products = [doc['_source'] for doc in result['hits']['hits']]
        return Response(products)

# # Create your views here.
# class ProductCBV(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer