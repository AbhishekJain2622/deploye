# In your `urls.py` file

from django.urls import path
from .views import (
    AboutListCreateView,
    AboutRetrieveUpdateDestroyView,
    SkillListCreateView,
    SkillRetrieveUpdateDestroyView,
    ExperienceListCreateView,
    ExperienceRetrieveUpdateDestroyView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    ContactAPIView,
    PostListCreateView,
    PostDetailView,
    CommentCreateView,
    LikeView,ResumeUploadView, ResumeDownloadView 
)

urlpatterns = [
    path('about/', AboutListCreateView.as_view(), name='about-list'),
    path('about/<int:pk>/', AboutRetrieveUpdateDestroyView.as_view(), name='about-detail'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list'),
    path('skills/<int:pk>/', SkillRetrieveUpdateDestroyView.as_view(), name='skill-detail'),
    path('experience/', ExperienceListCreateView.as_view(), name='experience-list'),
    path('experience/<int:pk>/', ExperienceRetrieveUpdateDestroyView.as_view(), name='experience-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('contact/', ContactAPIView.as_view(), name='contact-form'),
    path('blog/', PostListCreateView.as_view(), name='post-list'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/<slug:slug>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('blog/<slug:slug>/like/', LikeView.as_view(), name='like-post'),
    # Resume URLs (Add these new paths)
    path('resume/upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('resume/download/', ResumeDownloadView.as_view(), name='resume-download'),
]