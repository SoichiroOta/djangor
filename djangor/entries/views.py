import django

from djangor import entries


class EntryListView(django.views.generic.ListView):

    model = entries.models.Entry

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['form'] = entries.forms.EntryCreationForm
        context['objects'] = entries.forms.Entry.objects.all()
        return context


entry_list_view = EntryListView.as_view()


class EntryCreateView(django.views.View):
    def post(self, request, *args, **kwargs):
        form = entries.forms.EntryCreationForm(request.POST)
        if not form.is_valid():
            return django.shortcuts.render(
                request,
                'entries/entry_list.html',
                {'form': form, 'objects': entries.models.Entry.objects.all()}
            )
        title = request.POST.get('title')
        text = request.POST.get('text')
        entry = entries.models.Entry(title=title, text=text)
        entry.save()
        return django.shortcuts.redirect(
            django.urls.reverse('entries:list'),
            form=form,
            objects=entries.models.Entry.objects.all()
        )


entry_create_view = EntryCreateView.as_view()
