from guest_book.models import Entry
from guest_book.forms import EntryForm

from django.shortcuts import render, redirect
from django.contrib import messages
import json as simplejson


def index(request):
    if request.method == "POST":
        form_data = EntryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Please fill necessary fields')
    form = EntryForm()
    entries = list(Entry.objects.all())
    last_4_entries = entries[-4:]
    entries_by_4 = dict()
    entries_by_4['groups'] = []
    temp = []
    count = 0
    entries = list(reversed(entries))
    for index, entry in enumerate(entries):
        print type(entry)
        temp.append(entry.as_json())
        count += 1
        if count == 4 or index == len(entries) - 1:
            entries_by_4['groups'].append(list(reversed(temp)))
            count = 0
            temp = []
    print entries_by_4
    return render(request, 'guest_book/index.html',
                  {'entries': last_4_entries,
                   'form': form,
                   'all_entries': simplejson.dumps(entries_by_4),
                   'current_pos': 0})


def dell_all_entries(request):
    if request.method == "POST":
        Entry.objects.all().delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Successfully deleted all entries')
        return redirect('index')
    return render(request, 'guest_book/delete_entries.html')
