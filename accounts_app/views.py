from django.shortcuts import render, HttpResponse
from django.http import Http404

users = [
    {
        'username': 'amir',
        'name': 'amirhossein',
        'lastname': 'amir',
        'phone': '09385412818',
        'city': 'cfz'
    },

    {
        'username': 'mamad80',
        'name': 'mohamad',
        'lastname': 'mamadzadeh',
        'phone': '099155469428',
        'city': 'mhd'
    },

    {
        'username': 'farshad80',
        'name': 'fashad',
        'lastname': 'moti',
        'phone': '09151901234',
        'city': 'esf'
    },
]

def profile(request, username):
    for user in users:
        if user['username'] == username:
            return render(request, "accounts_app/profile.html", context={"user": user})
        # user سمت راست = همون متغیر حلقه 
        # "user" سمت چپ = نامی که در template صدا می‌زنی ({{ user.name }}

    raise Http404('This User Is Not Exist')


def users_list(request):
    return render(request, "accounts_app/users_list.html", context={"users": users})
