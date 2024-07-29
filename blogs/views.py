from django.shortcuts import render
from .models import Blog, BlogPost

def index(request):
    return render(request, "blogs/index.html")

# a view function defines what data the user can view on the corresponding page. 
def blogs(request):
    all_blogs = Blog.objects.all()
    # Real-world view functions are almost always more complex than what you see here, and they can pass as much information as needed to render().
    context = {"blogs": all_blogs}
    # When we used the render() function to generate the home page, all the information it needed was already in the template files.
    return render(request, "blogs/blogs.html", context)

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()
    
    context = {
        "blog": blog,
        "posts": posts,
    }
    return render(request, "blogs/blog.html", context)

def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog

    context = {
        "post": post,
        "blog": blog,
    }
    return render(request, "blogs/post.html", context)
