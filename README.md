1. detail.html
   - home으로 가기 링크 추가

2. CREATE
   - post.html 생성
       {% extends 'base.html' %}
       {% block content %}
       <div class="container">
           <form action="{% url 'create' %}">
               <hr>
               제목 : <input type='text' name='title'>
               <hr>
               내용 : <textarea name='body'></textarea>
               <hr>
               <input class='btn btn-dark' type='submit' value='제출하기'>
               <hr>
           </form>
       </div>
       {% endblock %}
   - views.py
       from django.shortcuts import render, get_object_or_404, redirect
       from django.utils import timezone
       
       def post(request):
           return render(request, 'blog/post.html')
       
       def create(request):
           post = Post()
           post.title = request.GET['title']
           post.body = request.GET['body']
           post.pub_date = timezone.datetime.now()
           post.save()
           return redirect('/blog/' + str(post.id))
   - urls.py
       urlpatterns = [
           path('post/', views.post, name='post'),
           path('create/', views.create, name='create'),
       ]

3. UPDATE
   - edit.html 생성
       {% extends 'base.html' %}
       {% block content %}
       <div class="container">
           <form action="{% url 'update' post.id %}">
               <hr>
               {% csrf_token %}
               제목 : <input type='text' name='title' value='{{post.title}}'>
               <hr>
               내용 : <textarea name='body'>{{post.body}}</textarea>
               <hr>
               <input class='btn btn-dark' type='submit' value='제출하기'>
               <hr>
           </form>
       </div>
       {% endblock %}
   - views.py
       def edit(request, post_id):
           post = get_object_or_404(Post, pk=post_id)
           return render(request, 'blog/edit.html', {'post':post})
       
       def update(requestk, post_id):
           post = get_object_or_404(Post, pk=post_id)
           post.title = reuqest.GET['title']
           post.body = reuqest.GET['body']
           post.pub_date = timeqone.datetime.now()
           post.save()
           return redirect('/blog/' + str(blog.id))
   - urls.py
       urlpatterns = [
           path('edit/<int:post_id>/', views.edit, name='edit'),
           path('update/<int:post_id>/', views.update, name='update'),
       ]

3. DELETE
   - views.py

    def delete(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return redirect('home')	
   - urls.py
       urlpatterns = [
           path('delete/<int:post_id>/', views.edit, name='edit'),
       ]
   
