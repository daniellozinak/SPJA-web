from django_tables2 import tables
from .models import Tweet,Comment

class TweetTable(tables.Table):

    content = tables.columns.TemplateColumn('<a href="/detail/{{ record.id }}">{{record.content}}</a>')
    
    class Meta:
        model = Tweet
        fields=['user','content','date']
        template_name='django_tables2/bootstrap4.html'
        attrs= {'class' : 'table table-dark table-striped'}

class CommentTable(tables.Table):
    class Meta:
        model = Comment
        fields=['user','content','date']
        template_name='django_tables2/bootstrap4.html'