
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categories, SubCategories, Posts
from django.contrib import messages
from django.shortcuts import get_object_or_404


@login_required(login_url='/accounts/login/')
def blog(request):
    categories = Categories.objects.all()
    return render(request, 'dashboard/blog/index.html', {'categories': categories})

@login_required(login_url='/accounts/login/')
def add_categorie(request):
    if request.method == "POST":
        try:
            categorie_name = request.POST.get('categorie-name')
            if categorie_name:  # check if name is not empty
                categorie = Categories(name=categorie_name)
                categorie.save()
                messages.success(request, 'Categorie successfully added.')
            else:
                messages.error(request, 'Categorie name cannot be empty.')
        except Exception as e:
            messages.error(request, f'Error adding categorie: {e}')
    else:
        messages.error(request, 'Error al agregar el post.')
    return redirect('blog')

@login_required(login_url='/accounts/login/')
def delete_categorie(request):
    if request.method == "POST":
        try:
            categorie_id = request.POST.get('categorie-id')
            if Categories.objects.filter(id=categorie_id).exists():
                categorie = Categories.objects.get(id=categorie_id)
                categorie.delete()
                messages.success(request, 'Categorie successfully deleted.')
            else:
                messages.error(request, 'Categorie does not exist.')
        except Exception as e:
            messages.error(request, f'Error deleting categorie: {e}')
    else:
        messages.error(request, 'Error al agregar el post.')
    return redirect('blog')


@login_required(login_url='/accounts/login/')
def blog_categorie(request, categorie_id=None):

    categories = Categories.objects.all()
    try:
        categorie = get_object_or_404(Categories, id=categorie_id)
        subcategories = SubCategories.objects.filter(categorie=categorie)
        posts_for_subcategories = {}
        for subcategorie in subcategories:
            posts_for_subcategories[subcategorie.id] = subcategorie.posts.all()

    except Categories.DoesNotExist:
        messages.error(request, 'Categorie not found.')
        return redirect('blog')  

    return render(request, 'dashboard/blog/categorie/index.html', {'categories': categories, 'subcategories': subcategories,'categorie': categorie })

@login_required(login_url='/accounts/login/')
def add_subcategorie(request):
    if request.method == 'POST':
        try:
            categorie_id = request.POST.get('categorie-id')
            subcategorie_name = request.POST.get('subcategorie-name')
            categorie = get_object_or_404(Categories, id=categorie_id)
            new_subcategorie = SubCategories(name=subcategorie_name, categorie=categorie)
            new_subcategorie.save()
            messages.success(request, 'Subcategoría agregada correctamente.')
            return redirect('blog-categorie', categorie_id)
        except:
            messages.error(request, 'El nombre de la subcategoría no puede estar vacío.')
    else:
        messages.error(request, 'Error al agregar el post.')

    return redirect('blog')

@login_required(login_url='/accounts/login/')
def delete_subcategorie(request):
    if request.method == 'POST':
        try:
            subcategorie_id = request.POST.get('subcategorie-id')
            subcategorie = get_object_or_404(SubCategories, id=subcategorie_id)
            categorie_id = subcategorie.categorie.id
            subcategorie_name = subcategorie.name
            subcategorie.delete()
            messages.success(request, f'Subcategoría "{subcategorie_name}" eliminada correctamente.')
            return redirect('blog-categorie', categorie_id)
        except:
            messages.error(request, 'Error al eliminar la subcategoría.')
    else:
        messages.error(request, 'Error al agregar el post.')

    return redirect('blog')

@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method == 'POST':
        try:
            subcategorie_id = request.POST.get('subcategorie-id')
            post_name = request.POST.get('post-name')

            subcategorie= SubCategories.objects.get(id=subcategorie_id)
            categorie_id = subcategorie.categorie.id
            new_post = Posts(name=post_name, subcategorie=subcategorie)
            new_post.save()
            messages.success(request, f'Post "{post_name}" agregado correctamente en la subcategoría "{subcategorie.name}".')
            return redirect('blog-categorie', categorie_id)
        except:
            messages.error(request, 'La subcategoría o el nombre del post no pueden estar vacíos.')
    else:
        messages.error(request, 'Error al agregar el post.')

    return redirect('blog')

@login_required(login_url='/accounts/login/')
def delete_post(request):
    if request.method == 'POST':
        
        try:
            post_id = request.POST.get('post-id')
            post = get_object_or_404(Posts, id=post_id)
            categorie_id = post.subcategorie.categorie.id
            post_name = post.name
            post.delete()
            messages.success(request, f'Post "{post_name}" eliminado correctamente.')
            return redirect('blog-categorie', categorie_id)
        except Exception as e:
            messages.error(request, f'Error al eliminar el post: {e}')
        
    else:
        messages.error(request, 'Error al agregar el post.')

    return redirect('blog')

@login_required(login_url='/accounts/login/')
def post(request, post_id=None):
    print(post_id)
    try:
        post = get_object_or_404(Posts, id=post_id)
        categories = Categories.objects.all()

    except Categories.DoesNotExist:
        messages.error(request, 'Categorie not found.')
        return redirect('blog')  

    return render(request, 'dashboard/blog/post/index.html', {'categories': categories, 'post' : post })
