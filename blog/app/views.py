from django.shortcuts import render, redirect
from dashboard.blog.models import Categories, SubCategories, Posts, Titulos, Textos, Codigos, Imagenes, Archivos
import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def index(request):

    categories = Categories.objects.all()

    data = {
        'categories' : categories
    }
    return render(request, 'app/index/index.html', data)


def subcategories(request, category_id=None):
    
    subcategories = SubCategories.objects.filter(category__id=category_id)

    data = {
        'subcategories' : subcategories
    }
    return render(request, 'app/subcategories/index.html', data)


def posts(request, subcategory_id=None):
    try:
        # Filtrar los posts por subcategoría
        posts = Posts.objects.filter(subcategory__id=subcategory_id)
        categories = Categories.objects.all()

        # Iterar sobre los posts y recuperar los elementos asociados a cada uno
        for post in posts:
            titulos = Titulos.objects.filter(post=post).order_by('fecha_creacion')
            textos = Textos.objects.filter(post=post).order_by('fecha_creacion')
            codigos = Codigos.objects.filter(post=post).order_by('fecha_creacion')
            imagenes = Imagenes.objects.filter(post=post).order_by('fecha_creacion')

            # Lista para almacenar los elementos de este post
            elementos_post = []
            for codigo in codigos:
                original_contenido = codigo.contenido
                lexer = get_lexer_by_name("python", stripall=True)
                formatter = HtmlFormatter(linenos=True, cssclass="code")
                codigo.contenido = highlight(original_contenido, lexer, formatter)
                
                # Aplicar Markdown al contenido del código
                codigo.contenido = markdown.markdown(codigo.contenido)

                # Agregar impresiones para depurar
                print(f"Antes de Markdown: {original_contenido}")
                print(f"Después de Markdown: {codigo.contenido}")

            # Agregar todos los elementos a la lista
            elementos_post.extend(titulos)
            elementos_post.extend(textos)
            elementos_post.extend(codigos)
            elementos_post.extend(imagenes)

            # Ordenar los elementos por fecha
            elementos_post = sorted(elementos_post, key=lambda x: x.fecha_creacion)

            # Asignar la lista de elementos al post actual
            post.elementos = elementos_post

    except Categories.DoesNotExist:
        messages.error(request, 'Category not found.')
        return redirect('blog')

    return render(request, 'app/posts/index.html', {
        'categories': categories,
        'posts': posts,
    })