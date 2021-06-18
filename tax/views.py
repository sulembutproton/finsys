from django.shortcuts import render
from mainsite.decorators import custom_login_required


@custom_login_required
def get_page(request, data):
    return render(request, 'tax/index.html', data)
