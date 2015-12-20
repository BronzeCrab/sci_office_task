from django.views.generic import ListView
from guest_book.models import Entry


class EntryList(ListView):
    model = Entry
