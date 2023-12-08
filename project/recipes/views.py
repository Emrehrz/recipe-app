from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Recipe, Category, Comment, CommentForm
from .forms import NewRecipeForm, EditRecipeForm


def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = Comment.objects.filter(recipe_id=pk, status='True')
    context = {"recipe": recipe, "comments": comments}
    return render(request, 'tarifSayfasi.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()

            return redirect('recipes:detail', pk=recipe.id)
    else:
        form = NewRecipeForm

    return render(request, 'tarifEkle.html', {'form': form})


@login_required
def dashboard(request):
    recipes = Recipe.objects.filter(created_by=request.user)

    context = {"recipes": recipes}
    return render(request, 'myRecipes.html', context)


@login_required
def delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    recipe.delete()
    return redirect('recipes:dashboard')


@login_required
def edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()

            return redirect('recipes:detail', pk=recipe.id)

    else:
        form = EditRecipeForm(instance=recipe)

    return render(request, 'tarifEkle.html', {'form': form})


@login_required
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()  # create relation with model
            data.content = form.cleaned_data['content']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.recipe_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()  # save data to table

            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)
