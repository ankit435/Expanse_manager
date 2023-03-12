


from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .models import ExpanseGroup,Expanse,User,ExpanseGroupUser,LinkExpanseGroupUser
from .serializers import   ExpanseGroupSerializer,ExpanseSerializer,UserSerializer,ExpanseGroupUserSerializer,LinkExpanseGroupUserSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
)

from rest_framework.response import Response



class ExpanseGroupView(ListAPIView):
    
    serializer_class = ExpanseGroupSerializer
    def get(self, request, pk=None):
        if pk is None:
            ExpanseGroups = ExpanseGroup.objects.all()
            serializer = ExpanseGroupSerializer(ExpanseGroups, many=True)
            return Response({"success": True, "data": serializer.data})
        else:
            ExpanseGroups = ExpanseGroup.objects.get(pk=pk)
            serializer = ExpanseGroupSerializer(ExpanseGroups)
            return Response({"success": True, "data": serializer.data})
    
    def post(self, request, pk=None):
      
        if pk is not None:
            return Response({"success": False, "message": "ExpanseGroup with id `{}` already exists.".format(pk)},status=400)
        else:
            ExpanseGroups = request.data.get('ExpanseGroup')
            serializer = ExpanseGroupSerializer(  data=ExpanseGroups)
            if serializer.is_valid(raise_exception=True):
                ExpanseGroup_saved = serializer.save()
            
            # link=LinkExpanseGroupUserSerializer(data={
            #     'LinkExpanseGroupUser_group_id':ExpanseGroup_saved.id,

            # })
            
            # if link.is_valid(raise_exception=True):
            #     link_saved = link.save()
            
            
            return Response({"success": True, "data": serializer.data})
    
    def put(self, request, pk=None):
        if pk is None:
            return Response({"success": False, "message": "ExpanseGroup with id `{}` not found.".format(pk)},status=404)
        else:
            ExpanseGroups_org = ExpanseGroup.objects.get(pk=pk)
            ExpanseGroups = request.data.get('ExpanseGroup')
            print(ExpanseGroups)
            serializer = ExpanseGroupSerializer(ExpanseGroups_org, data=ExpanseGroups)
            if serializer.is_valid(raise_exception=True):
                ExpanseGroup_saved = serializer.save()
            return Response({"success": True, "data": serializer.data})
            
    
        
    
    def delete(self, request, pk):
        if pk is None:
            return Response({"success": False, "message": "ExpanseGroup with id `{}` not found.".format(pk)},status=404)
        ExpanseGroups = ExpanseGroup.objects.get(pk=pk)
        ExpanseGroups.delete()
        return Response({"success": True, "message": "ExpanseGroup with id `{}` has been deleted.".format(pk)},status=204)
    


class ExpanseView(ListAPIView):
    
    serializer_class = ExpanseSerializer
    def get(self, request, pk=None):
        if pk is None:
            Expanses = Expanse.objects.all()
            serializer = ExpanseSerializer(Expanses, many=True)
            return Response({"success": True, "data": serializer.data})
        else:
            Expanses = Expanse.objects.get(pk=pk)
            serializer = ExpanseSerializer(Expanses)
            return Response({"success": True, "data": serializer.data})
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({"success": False, "message": "Expanse with id `{}` already exists.".format(pk)},status=400)
        else:
            Expanses = request.data.get('Expanse')
            
            serializer = ExpanseSerializer(data=Expanses)
            if serializer.is_valid(raise_exception=True):
                Expanse_saved = serializer.save()
        
           
            return Response({"success": True, "data": serializer.data})
    
    def put(self, request,pk=None):
        if pk is None:
            return Response({"success": False, "message": "Expanse with id `{}` not found.".format(pk)},status=404)
        else:
            Expanses_org = Expanse.objects.get(pk=pk)
            Expanses = request.data.get('Expanse')
            serializer = ExpanseSerializer(Expanses_org, data=Expanses)
            if serializer.is_valid(raise_exception=True):
                Expanse_saved = serializer.save()
            return Response({"success": True, "data": serializer.data})
       
    
    def delete(self, request, pk):
        if pk is None:
            return Response({"success": False, "message": "Expanse with id `{}` not found.".format(pk)},status=404)
        Expanses = Expanse.objects.get(pk=pk)
        Expanses.delete()
        return Response({"success": True, "message": "Expanse with id `{}` has been deleted.".format(pk)},status=204)


class ExpanseUserView(ListAPIView):
    
    serializer_class = UserSerializer
    def get(self, request, pk=None):
        if pk is None:
            ExpanseUsers = User.objects.all()
            serializer = UserSerializer(ExpanseUsers, many=True)
            return Response({"success": True, "data": serializer.data})
        else:
            ExpanseUsers = User.objects.get(pk=pk)
            serializer = UserSerializer(ExpanseUsers)
            return Response({"success": True, "data": serializer.data})
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({"success": False, "message": "User with id `{}` already exists.".format(pk)},status=400)
        else:
            ExpanseUsers = request.data.get('User')
            serializer = UserSerializer(data=ExpanseUsers)
            if serializer.is_valid(raise_exception=True):
                ExpanseUser_saved = serializer.save()
            return Response({"success": True, "data": serializer.data})
    
    def put(self, request,pk=None):
        if pk is None:
            return Response({"success": False, "message": "User with id `{}` not found.".format(pk)},status=404)
        else:
            ExpanseUsers_org = User.objects.get(pk=pk)
            ExpanseUsers = request.data.get('User')
            serializer = UserSerializer(ExpanseUsers_org, data=ExpanseUsers)
            if serializer.is_valid(raise_exception=True):
                ExpanseUser_saved = serializer.save()
            return Response({"success": True, "data": serializer.data})
       
    
    def delete(self, request, pk):
        if pk is None:
            return Response({"success": False, "message": "ExpanseUser with id `{}` not found.".format(pk)},status=404)
        ExpanseUsers = User.objects.get(pk=pk)
        ExpanseUsers.delete()
        return Response({"success": True, "message": "ExpanseUser with id `{}` has been deleted.".format(pk)},status=204)
    


class ExpanseUserGroupView(ListAPIView):
        
        serializer_class = ExpanseGroupUserSerializer
        def get(self, request, pk=None):
            if pk is None:
                ExpanseUserGroups = ExpanseGroupUser.objects.all()
                serializer = ExpanseGroupUserSerializer(ExpanseUserGroups, many=True)
                return Response({"success": True, "data": serializer.data})
            else:
                ExpanseUserGroups = ExpanseGroupUser.objects.get(pk=pk)
                serializer = ExpanseGroupUserSerializer(ExpanseUserGroups)
                return Response({"success": True, "data": serializer.data})
        
        def post(self, request, pk=None):
            if pk is not None:
                return Response({"success": False, "message": "ExpanseGroupUser with id `{}` already exists.".format(pk)},status=400)
            else:
                ExpanseUserGroups = request.data.get('ExpanseGroupUser')
                serializer = ExpanseGroupUserSerializer(data=ExpanseUserGroups)
                if serializer.is_valid(raise_exception=True):
                    ExpanseUserGroup_saved = serializer.save()
                return Response({"success": True, "data": serializer.data})
        
        def put(self, request,pk=None):
            if pk is None:
                return Response({"success": False, "message": "ExpanseGroupUser with id `{}` not found.".format(pk)},status=404)
            else:
                ExpanseUserGroups_org = ExpanseGroupUser.objects.get(pk=pk)
                ExpanseUserGroups = request.data.get('ExpanseGroupUser')
                serializer = ExpanseGroupUserSerializer(ExpanseUserGroups_org, data=ExpanseUserGroups)
                if serializer.is_valid(raise_exception=True):
                    ExpanseUserGroup_saved = serializer.save()
                return Response({"success": True, "data": serializer.data})
        
        
        def delete(self, request, pk):
            if pk is None:
                return Response({"success": False, "message": "ExpanseGroupUser with id `{}` not found.".format(pk)},status=404)
            ExpanseUserGroups = ExpanseGroupUser.objects.get(pk=pk)
            ExpanseUserGroups.delete()
            return Response({"success": True, "message": "ExpanseGroupUser with id `{}` has been deleted.".format(pk)},status=204)
        

class getGroupUserView(ListAPIView):
    serializer_class = LinkExpanseGroupUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['LinkExpanseGroupUser_group_id', 'LinkExpanseGroupUser_user_id','id']
    def get(self, request, pk=None):
        if pk is None:
            ExpanseUserGroups = LinkExpanseGroupUser.objects.all()
            serializer = LinkExpanseGroupUserSerializer(ExpanseUserGroups, many=True)
            return Response({"success": True, "data": serializer.data})
        ExpanseUserGroups = LinkExpanseGroupUser.objects.all().filter(LinkExpanseGroupUser_user_id=request.GET.get('LinkExpanseGroupUser_user_id'))
        serializer = LinkExpanseGroupUserSerializer(ExpanseUserGroups, many=True)
        return Response({"success": True, "data": serializer.data})
       
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({"success": False, "message": "LinkExpanseGroupUser with id `{}` already exists.".format(pk)},status=400)
        else:
            ExpanseUserGroups = request.data.get('LinkExpanseGroupUser')
            print(ExpanseUserGroups)
            serializer = LinkExpanseGroupUserSerializer(data=ExpanseUserGroups)
            if serializer.is_valid(raise_exception=True):
                ExpanseUserGroup_saved = serializer.save()
            return Response({"success": True, "data": serializer.data})
    
    def put(self, request,pk=None):
        if pk is None:
            return Response({"success": False, "message": "LinkExpanseGroupUser with id `{}` not found.".format(pk)},status=404)
        else:
            ExpanseUserGroups_org = LinkExpanseGroupUser.objects.get(pk=pk)
            ExpanseUserGroups = request.data.get('LinkExpanseGroupUser')
            serializer = LinkExpanseGroupUserSerializer(ExpanseUserGroups_org, data=ExpanseUserGroups)
            if serializer.is_valid(raise_exception=True):
                ExpanseUserGroup_saved = serializer.save()
            return Response({"success": True, "data": serializer.data})
        



