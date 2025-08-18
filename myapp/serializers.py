# In your `serializers.py` file

from rest_framework import serializers
from .models import Contact, About, Skill, Experience, Project, Post, Comment, Like

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'text', 'created_at'] # No need for 'post' here, as it's passed in the view
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'session_id']

class PostSerializer(serializers.ModelSerializer):
    # This correctly retrieves all comments because of the `related_name='comments'`
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'image', 'published_date', 'updated_date', 'comments', 'likes_count']
        
    def get_likes_count(self, obj):
        return obj.likes.count()