from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MessageSerializer, MessageListSerializer
from .models import Message


def message1(request):
    return Response(data='String')


class MessageAPI(APIView):
    authentication_classes= []
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all()

    def get(self,request,*args,**kwargs):
        version = kwargs.get('version', 'v2')
        if version == 'v1':
            serializer = MessageListSerializer(self.get_queryset(), many=True)
        else:
            serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        data = request.data
        serializer= self.serializer_class(data = data, many=False)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

