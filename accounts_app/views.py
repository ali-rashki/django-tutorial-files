from django.shortcuts import render, HttpResponse
from django.http import Http404

users = [
    {
        'username': 'amir',
        'name': 'amirhossein',
        'lastname': 'amir',
        'phone': '0912345213',
        'city': 'cfz'
    },

    {
        'username': 'mamad80',
        'name': 'mohamad',
        'lastname': 'mamadzadeh',
        'phone': '0992313255',
        'city': 'mhd'
    },

    {
        'username': 'farshad80',
        'name': 'fashad',
        'lastname': 'moti',
        'phone': '0941239111',
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
