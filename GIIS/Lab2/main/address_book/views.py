from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views, generics
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import ContactModel
from .serializers import ContactSerializer


# Create your views here.
class ContactView(views.APIView):
    def get(self, request):
        try:
            Contact = ContactModel.objects.get(id=request.query_params.get('id'))
        except ContactModel.DoesNotExist:
            return Response({'id': "Contact not found."}, status=404)
        serializer = ContactSerializer(instance=Contact)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request):
        try:
            contact = ContactModel.objects.get(id=request.data.get('id'))
        except ContactModel.DoesNotExist:
            return Response({'id': "Contact not found."}, status=404)
        serializer = ContactSerializer(data=request.data, instance=contact)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        try:
            contact = ContactModel.objects.get(id=request.data.get('id'))
        except ContactModel.DoesNotExist:
            return Response({'id': "Contact not found."}, status=404)
        contact.delete()
        return Response({'message': "Contact deleted successfully."}, status=200)


class ContactPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ContactListView(generics.ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    pagination_class = ContactPagination
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'surname', 'phone', 'address']


@api_view(['GET'])
def get_all_contacts(request):
    contacts = ContactModel.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)
