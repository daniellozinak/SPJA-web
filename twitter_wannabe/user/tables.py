from django_tables2 import tables
from .models import Profile

class ProfileTable(tables.Table):

    class Meta:
        model = Profile
        template_name='django_tables2/bootstrap4.html'