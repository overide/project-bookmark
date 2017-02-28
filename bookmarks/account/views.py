from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# from django.utils.decorators import method_decorator
from common.decorators import ajax_required
from actions.utils import create_action
from .forms import UserRegistrationForm
from .models import Profile, Contact
from actions.models import Action
from .forms import UserEditForm, ProfileEditForm
# from .forms import LoginForm

class Register(FormView):
    form_class = UserRegistrationForm
    template_name = 'account/registration/register.html'

    def form_valid(self, form):
        cd = form.cleaned_data
        new_user = form.save(commit=False)
        new_user.set_password(cd['password'])
        new_user.save()
        profile = Profile.objects.create(user=new_user)
        login(self.request, new_user)
        return redirect('dashboard')


class UserListView(ListView):
    template_name = 'account/user/list.html'
    model = User
    context_object_name = 'users'
    queryset = User.objects.filter(is_active=True)
    # paginated_by = 10

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['section'] = 'people'
        return context


class UserDetailView(DetailView):
    template_name = 'account/user/detail.html'
    model = User
    context_object_name = 'user'

    def get_object(self, queryset=None):
        uname = self.kwargs.get('username', None)
        obj = User.objects.get(username=uname, is_active=True)
        return obj

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['section'] = 'people'
        return context


@login_required
def dashboard(request):
    page = request.GET.get('page')
    following = request.user.following.all()
    actions = Action.objects.exclude(user=request.user)
    if following:
        actions = actions.filter(user__in=following)\
            .select_related('user__profile')\
            .prefetch_related('target')
    paginator = Paginator(actions,4)
    try:
        actions = paginator.page(page)
    except PageNotAnInteger:
        actions = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        actions = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, "actions/action/detail.html",
                      {'actions': actions})
    return render(request, "account/dashboard.html",
                  {'section': 'dashboard', 'actions': actions})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error("Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')

    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user,
                    user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})

# class UserLoginView(FormView):
#   template_name = "account/login.html"
#   success_url = "."
#   form_class = LoginForm

#   def form_valid(self, form):
#       cd = form.cleaned_data
#       user = authenticate(username=cd['username'],
#                           password=cd['password'])
#       if user is not None:
#           if user.is_active:
#               login(self.request, user)
#               return HttpResponse('Authenticated successfully!')
#           else:
#               return HttpResponse('Disabled Account!')
#       else:
#            return HttpResponse("Invalid login!")
