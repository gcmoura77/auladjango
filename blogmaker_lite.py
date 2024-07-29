# Para rodar o servidor: python manage.py runserver
# PAra criar superusuário: python manage.py createsuperuser
# Para criar os arquivos de migração  'python manage.py makemigrations blogs'
# Para aplicar a migração gerada com o makemigrations 'python manage.py migrate'
# Usuário e Senha: gcmoura / 123456

from django.urls import path, include
from django.core.handlers.wsgi import WSGIHandler
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),    
    path("", include("blogs.urls")),
]

application = WSGIHandler()
