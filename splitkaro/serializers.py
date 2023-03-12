


from rest_framework import serializers

from .models import User,Expanse,ExpanseGroup,ExpanseGroupUser,LinkExpanseGroupUser

class UserSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = User
            fields = '__all__'


class ExpanseSerializer(serializers.ModelSerializer):
    Expanse_user_id=UserSerializer(many=False, read_only=True)
    class Meta:
        model = Expanse
        fields = ['Expanse_user_id','Expanseamount','Expanse_description','Expanse_is_active','Expanse_created_at','Expanse_updated_at','Expanse_name']


class ExpanseGroupUserSerializer(serializers.ModelSerializer):
    Expanse_group_id=ExpanseSerializer(many=True, read_only=True)
    class Meta:
        model = ExpanseGroupUser
        fields = '__all__'


class ExpanseGroupSerializer(serializers.ModelSerializer):
    ExpanseGroupUser_group_id=ExpanseGroupUserSerializer(many=True, read_only=True)
    class Meta:
        model = ExpanseGroup
        fields = [
            'id',
            'ExpanseGroup_name',
            'ExpanseGroup_description',
            'ExpanseGroup_image',
            'ExpanseGroup_is_active',
            'ExpanseGroup_created_at',
            'ExpanseGroup_updated_at',
            'ExpanseGroup_amount',
            'ExpanseGroupUser_group_id'
        ]

class LinkExpanseGroupUserSerializer(serializers.ModelSerializer):
    LinkExpanseGroupUser_group_id=ExpanseGroupSerializer(many=False, read_only=True)
    LinkExpanseGroupUser_user_id=UserSerializer(many=False, read_only=True)
    class Meta:
        model = LinkExpanseGroupUser
        fields = '__all__'
    












