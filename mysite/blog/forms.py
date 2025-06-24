# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']
    class Meta:
        model = Post       # 'content' → 'text'로 변경, 이미지 업로드를 위한 'image'도 추가
        fields = ('author', 'title', 'text', 'image',)