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

urlpatterns = [
    path("admin/", admin.site.urls),    
    path("", index)
]

application = WSGIHandler()
