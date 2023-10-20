from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Post


class BlogCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'image', 'is_published')
    success_url = reverse_lazy('blog:blog')
    extra_context = {
        'title': 'Create Post'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    fields = ('title', 'description', 'image', 'is_published')
    extra_context = {
        'title': 'Update Post'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.pk])


class BlogListView(ListView):
    model = Post
    extra_context = {
        'title': 'Blog'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {
            'object': post,
            'title': f'{post.title}'
        }
        return render(request, 'blog/post_detail.html', context)


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog')
    extra_context = {
        'title': 'Delete Post'
    }
