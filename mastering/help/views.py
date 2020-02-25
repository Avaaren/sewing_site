from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Comment
from .forms import NewTopicForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from slugify import slugify


class TopicListView(ListView):
    model = Topic
    paginate_by = 5
    context_object_name = 'topic_list'
    template_name = 'help/forum.html'


class TopicDetailView(DetailView):
    template_name = 'help/topic_detail.html'
    queryset = Topic.objects.all()
    context_object_name = 'topic'
# Мы ебашим в строке поиска урл, туда пишем какой то адерс, и бац, он совпадает с шаблоном нашим, где указаны пареметры
# Мы параметрам задали ИМЕНА ИХ  int: year , int: month итд и именно это и есть KWARGS в нашем get object
# и потом мы посто возвращем объект который соответствует нашим тербованиям

    def get_object(self):
        slug = self.kwargs.get('slug')
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        
        return get_object_or_404(Topic,
                                 slug=slug, created__year=year,
                                 created__month=month, created__day=day)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        topic = self.get_object()
        data['comments'] = topic.comments.all()
        return data


class TopicCreateView(CreateView):
    form_class = NewTopicForm
    model = Topic
    template_name = 'help/create_topic.html'
    # success_url = 'help/forum/'

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TopicCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.slug = slugify(instance.title)
        instance.save()
        return super().form_valid(form)