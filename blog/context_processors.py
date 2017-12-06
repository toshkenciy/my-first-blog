
from django.contrib.auth.models import User

def return_list_of_users(request):
    return {
        'userlist': User.objects.all()
    }
