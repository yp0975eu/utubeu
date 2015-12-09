from rest_framework import serializers

from viewer.models import Chatroom, InvitedEmails


class ChatroomInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ('name', 'description')

    def create(self, validated_data):
        owner = self.context.get('request').user
        return Chatroom(owner=owner, name=validated_data.get('name'),
                        description=validated_data.get('description'))



class ChatroomOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ('id', 'name', 'description')


class ChatroomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ('id', 'name', 'description', 'users')

    def update(self, instance, validated_data):
        new_user = validated_data.get('users')
        instance.users.add(new_user)
        instance.save()
        return instance


class InvitedEmailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvitedEmails
        fields = '__all__'


