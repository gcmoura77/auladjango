# Para rodar o servidor: python manage.py runserver
# PAra criar superusuário: python manage.py createsuperuser
# Para criar os arquivos de migração  'python manage.py makemigrations blogs'
# Para aplicar a migração gerada com o makemigrations 'python manage.py migrate'
# Usuário e Senha: gcmoura / 123456

from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.shortcuts import render
from django.contrib import admin
from blogs.models import Blog, BlogPost

admin.site.register((Blog, BlogPost))


def index(request):
    return render(request, "index.html")

# a view function defines what data the user can view on the corresponding page. 
def blogs(request):
    all_blogs = Blog.objects.all()
    # Real-world view functions are almost always more complex than what you see here, and they can pass as much information as needed to render().
    context = {"blogs": all_blogs}
    # When we used the render() function to generate the home page, all the information it needed was already in the template files.
    return render(request, "blogs.html", context)

#  urls definidas para a aplicação
urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", blogs, name="blogs"),    
    path("", index, name="index")
]

application = WSGIHandler()
