from rest_framework import serializers

from MessageBoard.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('title', 'sender','content')