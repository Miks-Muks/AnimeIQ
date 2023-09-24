from django.views.generic import TemplateView, CreateView, ListView, FormView, DetailView

from polls.forms import PollForm
from polls.models import TopFollowers


class HomeView(TemplateView):
    template_name = 'polls/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'AnimeIQ'
        return context


class PollCreateView(FormView):
    template_name = 'polls/create.html'
    form_class = PollForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Узнай свой результат'
        return context


class FollowersListView(ListView):
    model = TopFollowers
    template_name = 'polls/list.html'
    paginate_by = 3
    context_object_name = 'followers_polls'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Топ последователей'
        return context


class FollowerTopDetailView(DetailView):
    template_name = 'polls/detail.html'
    context_object_name = 'follower'
    model = TopFollowers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Топ последователя'
        return context
