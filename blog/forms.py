from django import forms

from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['tags'].required = False

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'tags', 'is_private')
