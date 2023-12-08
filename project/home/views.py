from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Q

from user.forms import SignupForm
from recipes.models import Recipe, Category


# tarifler goruntulenir


def index(request):
    query = request.GET.get('query', '')
    recipes = Recipe.objects.all()
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()

    if category_id:
        recipes = recipes.filter(category_id=category_id)

    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) | Q(description__icontains=query))

    context = {"recipes": recipes, "categories": categories,
               "query": query, "category_id": int(category_id)}
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'kayitOl.html', {
        'form': form
    })


def login(request):
    return HttpResponse('giris yapma')


def logout_user(request):
    logout(request)
    return redirect('/')
