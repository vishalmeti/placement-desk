from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



from .models import Post
from .forms import PostForm

from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = "posts" #its the same name of the model

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        searchInput=self.request.GET.get('search-area') or ''
        if searchInput:
            context['posts'] = context['posts'].filter(CompanyName__icontains=searchInput)
        context['searchInput']=searchInput
        return context
class AboutPage(TemplateView):
    template_name='feed/about.html'

class AllMyPost(LoginRequiredMixin,ListView):
    http_method_names=["get"]
    template_name = "feed/allMyPost.html"
    context_object_name="posts"
    model=Post
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user).order_by('-id')
        searchInput=self.request.GET.get('search-area') or ''
        if searchInput:
            context['posts'] = context['posts'].filter(CompanyName__icontains=searchInput)
        context['searchInput']=searchInput
        return context

class PostDetailView(DetailView):
    http_method_names=["get"]
    template_name="feed/detailview.html"
    model=Post
    context_object_name = "post" #its the same name of the model. we use this in the html page

class CreateNewPost(LoginRequiredMixin,CreateView):
    model=Post
    form_class = PostForm
    template_name="feed/createPost.html"
    # fields=['CompanyName','Experience','ctc','Difficulty','department']
    success_url='/'


    def dispatch(self, request,*args,**kwargs):
        self.request=request
        return super().dispatch(request, *args,*kwargs)


#dispatch always runs before any other functions
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form )

    # def post(self,request,*args,**kwargs):
    #     post=Post.objects.create(
    #         CompanyName = request.POST.get('Cname'),
    #         Difficulty=request.POST.get('difficulty'),
    #         department=request.POST.get('branch'),
    #         ctc=request.POST.get('ctc'),
    #         Experience = request.POST.get('experience')
    #     )

    #     return render(
    #         request,"homepage.html"
    #     )

class EditPost(LoginRequiredMixin,UpdateView):
    
    template_name='feed/edit.html'
    success_url='/'
    model=Post
    
    fields=['CompanyName','Difficulty','department','ctc','Experience',]
    

    def form_valid(self, form):
        author=self.object.author
        loginUser=self.request.user
        if author==loginUser:
            print(self.object.author)
            print(self.request.user)
        
            self.object = form.save()
            return super().form_valid(form)
        else:
            print("NOt authorised")

            return self.render_to_response(self.get_context_data(form=form))


