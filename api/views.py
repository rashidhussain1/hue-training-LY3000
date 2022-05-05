from rest_framework.response import Response
from rest_framework.decorators import api_view
from myApp.models import Project, User, Issue
from .serializers import UserSerializer, ProjectSerializer, IssueSerializer
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

#view for user table for GET and POST method
class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

#view for Issue table for GET and POST method

class IssueView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

#view for Project table for GET and POST method
class ProjectView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


