from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import redis
from common.decorators import ajax_required
from actions.utils import create_action
from .forms import ImageCreateForm
from .models import Image

r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)

@method_decorator(login_required, name='dispatch')
class ImageCreateView(FormView):
    form_class = ImageCreateForm
    template_name = 'images/image/create.html'

    def get_initial(self):
        initial = super(ImageCreateView, self).get_initial()
        initial['url'] = self.request.GET.get('url', "")
        initial['title'] = self.request.GET.get('title', "")
        return initial

    def form_valid(self, form):
        new_item = form.save(commit=False)
        new_item.user = self.request.user
        new_item.save()
        create_action(self.request.user, 'bookmarked image', new_item)
        messages.success(self.request, 'Image added successfully')
        return redirect(new_item.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(ImageCreateView, self).get_context_data(**kwargs)
        context['section'] = 'images'
        return context


class ImageDetailView(DetailView):
    template_name = "images/image/detail.html"
    context_object_name = "image"
    pk_url_kwargs = "id"
    slug_url_kwargs = "slug"
    model = Image

    def get_queryset(self):
        queryset = Image.objects.filter(
            pk=self.kwargs['id'], slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        total_views = r.incr('image:{}:views'.format(self.get_object().id))
        context['section'] = 'images'
        context['total_views'] = total_views
        return context


@method_decorator([login_required, ajax_required, require_POST], name='dispatch')
class ImageLikeView(View):
    def post(self, request, *args, **kwargs):
        image_id = request.POST.get('id')
        action = request.POST.get('action')
        if image_id and action:
            image = get_object_or_404(Image, pk=image_id)
            if action == 'like':
                image.user_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'ko'})

def image_list(request):
    images = Image.objects.filter(user=request.user)
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer return the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # if the request is AJAX and page is out of range
            # return the empty page
            return HttpResponse('')
        # if page is out of delivery last page of result
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {'images': images})
    return render(request,
                  'images/image/list.html',
                  {'section': 'images', 'images': images})