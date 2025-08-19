# In your `views.py` file

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import About, Skill, Experience, Project, Post, Comment, Like,Resume
from .serializers import (
    AboutSerializer, SkillSerializer, ExperienceSerializer, 
    ProjectSerializer, ContactSerializer, PostSerializer, 
    CommentSerializer,ResumeSerializer
)

class AboutListCreateView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all().order_by('category', 'name')
    serializer_class = SkillSerializer

class SkillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all().order_by('-start_date') 
    serializer_class = ExperienceSerializer

class ExperienceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all().order_by('-start_date')
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Message sent successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Blog Views ---
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    
class CommentCreateView(APIView):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(post=post) 
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeView(APIView):
    def post(self, request, slug, format=None):
        post = get_object_or_404(Post, slug=slug)
        session_id = request.session.session_key
        if not session_id:
            request.session.save()
            session_id = request.session.session_key
        
        existing_like = Like.objects.filter(post=post, session_id=session_id).first()
        
        if existing_like:
            existing_like.delete()
            return Response({"message": "Post unliked successfully.", "liked": False, "likes_count": post.likes.count()}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(post=post, session_id=session_id)
            return Response({"message": "Post liked successfully.", "liked": True, "likes_count": post.likes.count()}, status=status.HTTP_201_CREATED)
        
class ResumeUploadView(generics.CreateAPIView):
    """
    View to upload a new resume.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeDownloadView(APIView):
    """
    View to retrieve the latest uploaded resume.
    """
    def get(self, request, *args, **kwargs):
        # Get the latest uploaded resume
        resume = Resume.objects.order_by('-uploaded_at').first()
        
        if not resume:
            return Response({"error": "No resume found."}, status=status.HTTP_404_NOT_FOUND)
        
        # You can get the URL of the file here
        file_url = resume.file.url
        
        # This will return a JSON response with the file URL. The frontend will then
        # use this URL to initiate the download.
        return Response({"resume_url": file_url}, status=status.HTTP_200_OK)