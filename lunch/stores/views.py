from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import StoreForm
from .models import Store


def home(request):
    return render(request, 'home.html')


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores': stores})


def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    return render(request, 'stores/store_detail.html', {'store': store})


def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, submit_title='建立')
        if form.is_valid():
            store = form.save(commit=False)
            if request.user.is_authenticated():
                store.owner = request.user
            store.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(submit_title='建立')
    return render(request, 'stores/store_create.html', {'form': form})


def store_update(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store, submit_title='更新')
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(instance=store, submit_title='更新')
    return render(request, 'stores/store_update.html', {
        'form': form, 'store': store,
    })


@login_required
@require_http_methods(['POST'])
def store_delete(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    if (not store.owner or store.owner == request.user or
            request.user.has_perm('store_delete')):
        store.delete()
        return redirect('store_list')
    return HttpResponseForbidden()
