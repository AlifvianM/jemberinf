from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# Create your views here.


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	paginate_by = 5
	ordering = ['-waktu']


class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin ,CreateView):
	model = Post
	fields = [
		'judul',
		'isi',
		'foto',
	]

	def form_valid(self, form):
		form.instance.penulis = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
	model = Post
	fields = [
		'judul',
		'isi',
		'foto',
	]

	# def form_valid(self, form):
	# 	form.instance.penulis = self.request.user
	# 	return super().form_valid(form)
	
	extra_context ={
			'title':'update',
	}

	def get_context_data(self, **kwargs):
		self.kwargs.update(self.extra_context)
		return super().get_context_data(**kwargs)


	def test_func(self):
		post = self.get_object()
		if self.request.user==post.penulis:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user==post.penulis:
			return True
		return False


def home(request):
	posts = Post.objects.all()
	context = {
		'posts' : posts
	}
	print(Post)
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})