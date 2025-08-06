
Com base na série lançada neste blog:

https://www.mostlypython.com/django-from-first-principles-2/

- Para rodar o projeto:

`python manage.py runserver`

## Uso do Django ORM ##

Para entrar no console interativo do projeto no Django 

```
~/blogmaker_project$ python manage.py shell 

Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from blogs.models import Blog, BlogPost
>>> all_blogs = Blog.objects.all()
>>> all_blogs
<QuerySet [<Blog: Cinema Mudo>, 
<Blog: Musique Non Stop>, 
<Blog: Blog de Tecnologia>]>
>>> 

>>> blog = all_blogs[1]
>>> blog.title
'Musique Non Stop'
>>> blog.description
'Blog de assuntos relacionados a música'
>>> blog.date_added
datetime.datetime(2024, 5, 7, 17, 50, 56, 20653, tzinfo=datetime.timezone.utc)
>>> blog.date_added.isoformat()
'2024-05-07T17:50:56.020653+00:00'
>>> blog.__dict__.keys()
dict_keys(['_state', 'id', 'title', 'description', 'date_added'])
>>> blog.id
2
>>> my_music_blog = Blog.objects.get(id=2)

>>> my_music_blog
<Blog: Musique Non Stop>
>>> blog
<Blog: Musique Non Stop>
>>> 

>>> all_posts = BlogPost.objects.all()
>>> all_posts
<QuerySet [<BlogPost: Inteligência Artificial: Transformando Negócios e >, 
<BlogPost: Do Planejamento à Execução: As Chaves da Gestão de>, 
<BlogPost: Dominando a Gestão de Produtos: Estratégias para o>, 
<BlogPost: O incrível álbum do Tortoise>]>

>>> post = all_posts[2]
>>> post.__dict__.keys()
dict_keys(['_state', 'id', 'title', 'body', 'blog_id', 'date_added'])
>>> post.blog_id
3
>>> post.title
'Dominando a Gestão de Produtos: Estratégias para o Sucesso no Mercado Atual'

>>> blog
<Blog: Musique Non Stop>
>>> posts = blog.blogpost_set.all()
>>> posts
<QuerySet [<BlogPost: O incrível álbum do Tortoise>]>

<!-- Pegar os últimos 5 registros cadastrados -->
>>> posts = blog.blogpost_set.order_by("-date_added")[:5]

>>> str(all_blogs.query)
'SELECT "blogs_blog"."id", "blogs_blog"."title", "blogs_blog"."description", "blogs_blog"."date_added" FROM "blogs_blog"'

>>> str(posts.query)
'SELECT "blogs_blogpost"."id", "blogs_blogpost"."title", "blogs_blogpost"."body", "blogs_blogpost"."blog_id", "blogs_blogpost"."date_added" FROM "blogs_blogpost" WHERE "blogs_blogpost"."blog_id" = 2 ORDER BY "blogs_blogpost"."date_added" DESC LIMIT 5'

```


export DJANGO_SUPERUSER_PASSWORD=fake_pw

- Para rodar o servidor: python manage.py runserver
- Para criar superusuário: python manage.py createsuperuser
- Para criar os arquivos de migração  'python manage.py makemigrations blogs'
- Para aplicar a migração gerada com o makemigrations 'python manage.py migrate'
- Usuário e Senha: gcmoura / 123456

# Para o deploy

- exemplo usando Fly.io
- utilizado django-simple-deploy

## Passos necessários

- Install the host platform's CLI.
- Install django-simple-deploy.
- Add simple_deploy to INSTALLED_APPS.
- Create a project on the host platform.
- Run the simple_deploy command to configure the project for a specific host.
- Review the changes that were made, and commit those changes.
- Push the project to the remote server.
- Open the deployed project in a browser tab.

# Fly.io:
export FLYCTL_INSTALL="/home/gcmoura/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"

$ fly auth login

## Criar um projeto com nome aleatório:
fly apps create --generate-name

```automatically selected personal organization: gcmoura@gmail.com
New app created: sparkling-pine-8996```

pip install django-simple-deploy[fly_io]
python manage.py deploy