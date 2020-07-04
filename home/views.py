from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import upload_form, update_form
from .models import make
from django.urls import reverse_lazy, reverse
from taggit.models import Tag
from django.views.generic.edit import FormView
# Create your views here.


def con(a):
    hr = a//60
    min = a % 60
    if hr is 0:
        return str(min)+" min"
    else:
        return str(hr)+" hr "+str(min)+" min"


class all_post(ListView):
    model = make
    paginate_by = 6
    context_object_name = 'post'
    template_name = 'all_post.html'
    ordering = ['-data']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for x in context['post']:
            stuff = get_object_or_404(make, pk=x.pk)
            comman_tags = stuff.tags.most_common()[:1]
            for p in comman_tags:
                stuff.comman = str(p)
            # print(stuff.comman)
            stuff.save()
            # stuff.m2m()
        # print(context)
        return context


class blog_detail(DetailView):
    model = make
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(blog_detail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(make, id=self.kwargs['pk'])
        common_tags = stuff.tags.most_common()[:5]
        is_liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            is_liked = True
        text_time = con(stuff.preparation_time)
        context['text_time'] = text_time
        context["liked"] = is_liked
        context["common_tags"] = common_tags
        return context


class add_post(CreateView):
    model = make
    form_class = upload_form
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context


class update_post(UpdateView):
    model = make
    form_class = update_form
    template_name = 'update_post.html'
    # fields = ('recipe_name', 'author')


class delete_post(DeleteView):
    model = make
    template_name = 'delete_post.html'
    success_url = reverse_lazy('all_post')

    # fields = ('recipe_name', 'author')


def base(request):
    list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, 'base.html', {'list_example': list_example})


def about(request):
    return render(request, 'about.html')


def error(request, exception):
    return render(request, 'error.html')


def title(request):
    return render(request, 'title.html')


def coursel(request):
    list_example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return render(request, 'coursel.html', {'list_example': list_example})


def home(request):
    list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, 'home.html', {'list_example': list_example})


def LikeView(request, pk):
    post = get_object_or_404(make, pk=pk)
    liked = False
    print(request.user.id)
    if request.user.id == None:
        return HttpResponseRedirect(reverse('login'))

    else:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))


class user_view(ListView):
    model = make
    # paginate_by = 5
    context_object_name = 'post'
    template_name = 'author.html'
    ordering = ['-data']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = (self.kwargs['name'])
        context['id'] = (self.kwargs['id'])
        context['user_post'] = (
            context['post'].filter(author=self.kwargs['id']))
        # print(context)

        return context


class recipes_view(ListView):

    model = make
    # paginate_by = 18
    context_object_name = 'post'
    template_name = 'recipes.html'
    ordering = ['-data']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = (self.kwargs['name'])
        context['recipes'] = (context['post'].filter(menu=self.kwargs['name']))
        print(context)
        return context


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    posts = make.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'posts': posts,
        'slug': slug,
    }
    return render(request, 'tagged.html', context)
