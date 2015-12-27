from guest_book.models import Entry
from guest_book.forms import EntryForm, RadioForm

from django.shortcuts import render, redirect
from django.contrib import messages
import json as simplejson
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request, sorting=None):
    # creating new entry
    if request.method == "POST":
        form_data = EntryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Please fill necessary fields')
    # handling like button click
    elif request.GET.get('entry_id') is not None:
        _id = request.GET.get('entry_id')
        entry = Entry.objects.get(id=_id)
        entry.likes += 1
        entry.save()

    form = EntryForm()
    radioform = RadioForm()
    if sorting is not None:
        entries = list(Entry.objects.order_by(sorting))
    else:
        entries = list(Entry.objects.all())
    last_4_entries = entries[-4:]
    entries_by_4 = dict()
    entries_by_4['groups'] = []
    temp = []
    count = 0
    entries = list(reversed(entries))
    for index, entry in enumerate(entries):
        temp.append(entry.as_json())
        count += 1
        if count == 4 or index == len(entries) - 1:
            entries_by_4['groups'].append(list(reversed(temp)))
            count = 0
            temp = []
    return render(request, 'guest_book/index.html',
                  {'entries': last_4_entries,
                   'form': form,
                   'radioForm': radioform,
                   'all_entries': simplejson.dumps(entries_by_4),
                   'current_pos': 0})


@csrf_exempt
def sort(request):
    sort_by = request.POST['sort']
    return redirect('index', sorting=sort_by)


def dell_all_entries(request):
    if request.method == "POST":
        Entry.objects.all().delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Successfully deleted all entries')
        return redirect('index')
    return render(request, 'guest_book/delete_entries.html')
