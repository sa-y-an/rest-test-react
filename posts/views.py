from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from .models import Posts, Vote
from .serializers import PostSerializer, VoteSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

class PostDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        post = Posts.objects.filter(pk = kwargs['pk'], poster = self.request.user)
        if post.exists():
            return self.destroy(request,*args,**kwargs)
        else :
            raise ValidationError("this isn't your post to delete")
        # return super().delete(request, *args, **kwargs)
    


class PostView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(poster = self.request.user)

class VoteCreate(generics.CreateAPIView , mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) :
        user = self.request.user
        post = Posts.objects.get(pk = self.kwargs['pk'])
        return Vote.objects.filter(voter = user , post = post)

    def perform_create(self,serializer):
        if self.get_queryset().exists():
            raise ValidationError("You have already Voted :))")
        serializer.save(voter = self.request.user, post = Posts.objects.get(pk = self.kwargs['pk']))

    def delete(self, request, *args , **kwargs) :
        if self.get_queryset().exists() :
            self.get_queryset().delete()
            return Response(status = status.HTTP_204_NO_CONTENT)

        else :
            raise ValidationError('You have never voted on this post !!!')