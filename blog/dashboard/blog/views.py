
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categories, SubCategories, Posts, Titulos, Textos, Codigos, Imagenes, Archivos
from django.contrib import messages
from django.shortcuts import get_object_or_404
from itertools import chain
import markdown

@login_required(login_url='/accounts/login/')
def blog(request):
    categories = Categories.objects.all()
    return render(request, 'dashboard/blog/index.html', {'categories': categories})

@login_required(login_url='/accounts/login/')
def add_category(request):
    if request.method == "POST":
        try:
            category_name = request.POST.get('category-name')
            if category_name:
                category = Categories(name=category_name)
                category.save()
                messages.success(request, 'Category successfully added.')
            else:
                messages.error(request, 'Category name cannot be empty.')
        except Exception as e:
            messages.error(request, f'Error adding category: {e}')
    else:
        messages.error(request, 'Error al agregar el post.')
    return redirect('blog')

@login_required(login_url='/accounts/login/')
def delete_category(request):
    if request.method == "POST":
        try:
            category_id = request.POST.get('category-id')
            if Categories.objects.filter(id=category_id).exists():
                category = Categories.objects.get(id=category_id)
                category.delete()
                messages.success(request, 'Category successfully deleted.')
            else:
                messages.error(request, 'Category does not exist.')
        except Exception as e:
            messages.error(request, f'Error deleting category: {e}')
    else:
        messages.error(request, 'Error al agregar el post.')
    return redirect('blog')


@login_required(login_url='/accounts/login/')
def blog_category(request, category_id=None):

    categories = Categories.objects.all()
    try:
        category = get_object_or_404(Categories, id=category_id)
        subcategories = SubCategories.objects.filter(category=category)
        posts_for_subcategories = {}
        for subcategory in subcategories:
            posts_for_subcategories[subcategory.id] = subcategory.posts.all()

    except Categories.DoesNotExist:
        messages.error(request, 'Category not found.')
        return redirect('blog')  

    return render(request, 'dashboard/blog/category/index.html', {'categories': categories, 'subcategories': subcategories,'category': category })

@login_required(login_url='/accounts/login/')
def add_subcategory(request):
    if request.method == 'POST':
        try:
            category_id = request.POST.get('category-id')
            subcategory_name = request.POST.get('subcategory-name')
            category = get_object_or_404(Categories, id=category_id)
            new_subcategory = SubCategories(name=subcategory_name, category=category)
            new_subcategory.save()
            messages.success(request, 'Subcategoría agregada correctamente.')
            return redirect('blog-category', category_id)
        except:
            messages.error(request, 'El nombre de la subcategoría no puede estar vacío.')
    else:
        messages.error(request, 'Error al agregar el post.')

    return redirect('blog')

@login_required(login_url='/accounts/login/')
def delete_subcategory(request):
    if request.method == 'POST':
        try:
            subcategory_id = request.POST.get('subcategory-id')
            subcategory = get_object_or_404(SubCategories, id=subcategory_id)
            category_id = subcategory.category.id
            subcategory_name = subcategory.name
            subcategory.delete()
            messages.success(request, f'Subcategoría "{subcategory_name}" eliminada correctamente.')
            return redirect('blog-category', category_id)
        except:
            messages.error(request, 'Error al eliminar la subcategoría.')
    else:
        messages.error(request, 'Error al agregar el post.')

    return redirect('blog')

@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method == 'POST':
        try:
            subcategory_id = request.POST.get('subcategory-id')
            post_name = request.POST.get('post-name')

            subcategory= SubCategories.objects.get(id=subcategory_id)
            category_id = subcategory.category.id
            new_post = Posts(name=post_name, subcategory=subcategory)
            new_post.save()
            messages.success(request, f'Post "{post_name}" agregado correctamente en la subcategoría "{subcategory.name}".')
            return redirect('blog-category', category_id)
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
            category_id = post.subcategory.category.id
            post_name = post.name
            post.delete()
            messages.success(request, f'Post "{post_name}" eliminado correctamente.')
            return redirect('blog-category', category_id)
        except Exception as e:
            messages.error(request, f'Error al eliminar el post: {e}')
        
    else:
        messages.error(request, 'Error al agregar el post.')

    return redirect('blog')


def post(request, post_id=None):
    try:
        post = get_object_or_404(Posts, id=post_id)
        categories = Categories.objects.all()
        titulos = Titulos.objects.filter(post=post)
        textos = Textos.objects.filter(post=post)
        archivos = Archivos.objects.filter(post=post)
        codigos = Codigos.objects.filter(post=post)
        print(codigos)
        try:
            for codigo in codigos:
                print(codigo.contenido)
                codigo.contenido = markdown.markdown(codigo.contenido)


        except:
            print("no hay contenido")

        imagenes = Imagenes.objects.filter(post=post)

        todos_elementos = list(chain(titulos, textos, archivos, codigos, imagenes))
        todos_elementos_ordenados = sorted(todos_elementos, key=lambda x: x.fecha_creacion)

    except Categories.DoesNotExist:
        messages.error(request, 'Categorie not found.')
        return redirect('blog')

    return render(request, 'dashboard/blog/post/index.html', {
        'categories': categories,
        'post': post,
        'elementos': todos_elementos_ordenados,
    })

@login_required(login_url='/accounts/login/')
def update_or_delete_section(request):
    if request.method == 'POST':
        seccion_id = request.POST.get('seccion_id')
        seccion_tipo = request.POST.get('seccion_tipo')
        nuevo_contenido = request.POST.get('nuevo_contenido')
        action = request.POST.get('action')

        if action == 'update':
            seccion = None
            if seccion_tipo == 'titulo':
                seccion = get_object_or_404(Titulos, id=seccion_id)
            elif seccion_tipo == 'texto':
                seccion = get_object_or_404(Textos, id=seccion_id)
            elif seccion_tipo == 'codigo':
                seccion = get_object_or_404(Codigos, id=seccion_id)
            elif seccion_tipo == 'imagen':
                seccion = get_object_or_404(Imagenes, id=seccion_id)
            elif seccion_tipo == 'archivo':
                seccion = get_object_or_404(Archivos, id=seccion_id)

            if seccion:
                seccion.contenido = nuevo_contenido
                seccion.save()
                messages.success(request, 'Sección actualizada correctamente.')
            else:
                messages.error(request, 'Sección no encontrada.')

        elif action == 'delete':
            if seccion_tipo == 'titulo':
                Titulos.objects.filter(id=seccion_id).delete()
            elif seccion_tipo == 'texto':
                Textos.objects.filter(id=seccion_id).delete()
            elif seccion_tipo == 'codigo':
                Codigos.objects.filter(id=seccion_id).delete()
            elif seccion_tipo == 'imagen':
                Imagenes.objects.filter(id=seccion_id).delete()
            elif seccion_tipo == 'archivo':
                Archivos.objects.filter(id=seccion_id).delete()

            messages.success(request, 'Sección eliminada correctamente.')

    return redirect('post', post_id=request.POST.get('post_id'))

@login_required(login_url='/accounts/login/')
def add_title(request, post_id):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        color = request.POST.get('color', '')
        Titulos.objects.create(contenido=contenido, color=color, post_id=post_id)

    return redirect('post', post_id=post_id)

@login_required(login_url='/accounts/login/')
def add_text(request, post_id):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        Textos.objects.create(contenido=contenido, post_id=post_id)

    return redirect('post', post_id=post_id)

@login_required(login_url='/accounts/login/')
def add_code(request, post_id):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        Codigos.objects.create(contenido=contenido, post_id=post_id)

    return redirect('post', post_id=post_id)

@login_required(login_url='/accounts/login/')
def add_image(request, post_id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        archivo = request.FILES['archivo']  

        Imagenes.objects.create(nombre=nombre, archivo=archivo, post_id=post_id)

    return redirect('post', post_id=post_id)





@login_required(login_url='/accounts/login/')
def add_file(request, post_id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        archivo = request.FILES['archivo'] 
        Archivos.objects.create(nombre=nombre, archivo=archivo, post_id=post_id)

    return redirect('post', post_id=post_id)