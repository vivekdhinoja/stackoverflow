from django.conf import settings
from django.contrib.auth import mixins
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views import generic
from question.models import Question


# Create your views here.
class QuestionListView(generic.ListView):
    template_name = 'question/questions.html'
    ordering = ['-created']
    queryset = Question.objects.all()


class QuestionCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Question
    fields = ['title', 'tags', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Question'
        return context


class QuestionUpdateView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    model = Question
    fields = ['title', 'tags', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Question'
        return context


class QuestionDeleteView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.DeleteView):
    model = Question
    success_url = reverse_lazy('question')

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(QuestionDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Question'
        return context


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'question/question_detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        question = get_object_or_404(Question, slug=self.kwargs.get('slug'))
        context['tags'] = question.tags.most_common()
        return context
