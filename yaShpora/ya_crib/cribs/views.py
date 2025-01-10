from typing import Any
from django.shortcuts import get_object_or_404
from django.http import Http404

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Crib


class IndexListView(ListView):
    model = Crib
    template_name = 'crib/index.html'
    context_object_name = 'cribs'

    def get_queryset(self):
        return Crib.objects.all()
    

class CribForSpintView(DetailView):

    model = Crib
    template_name = 'crib/detail.html'
    context_object_name = 'crib'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        crib = get_object_or_404(
            Crib.objects.all(),
            pk=self.kwargs['pk']
        )
        context['crib'] = crib
        return {**context}

