from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Topic, Comment
from .forms import NewTopicForm, NewCommentForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from slugify import slugify


class TopicListView(ListView):
    model = Topic
    paginate_by = 5
    context_object_name = 'topic_list'
    template_name = 'help/forum.html'


class TopicDetailView(DetailView, CreateView):
    template_name = 'help/topic_detail.html'
    context_object_name = 'topic'
    # Declare fields for ModelFormMixin
    form_class = NewCommentForm
    model = Comment

    # When comment form is submitted with POST, writing comment to database
    def post(self, request, year, month, day, slug):
        topic = get_object_or_404(Topic,
                                 slug=slug, created__year=year,
                                 created__month=month, created__day=day)

        form = NewCommentForm(data=request.POST)
        comment = form.save(commit=False)
        comment.author = request.user
        comment.topic = topic
        comment.save()
        return redirect(topic.get_absolute_url()) 
    # Overriding default get_object to get topic with custom parameters
    def get_object(self):
        slug = self.kwargs.get('slug')
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        
        return get_object_or_404(Topic,
                                 slug=slug, created__year=year,
                                 created__month=month, created__day=day)


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

def likes(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    if request.user in topic.likes.all():
        topic.likes.remove(request.user)
    else:
        topic.likes.add(request.user)
    return redirect(topic.get_absolute_url())