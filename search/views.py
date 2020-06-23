from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView


# Create your views here.

class SearchProductView(ListView):
    template_name='search/view.html'

    def get_context_data(self, *args, **kwargs):
        context=super(SearchProductView, self).get_context_data(*args, **kwargs)
        query=self.request.GET.get('q')
        context['query']=query
        #context['query']=self.request.GET.get('q')
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self,*args, **kwargs):
        request=self.request
        print(request.GET)
        method_dict=request.GET
        query = method_dict.get('q', None)  #method_dict['q']
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()






        '''
        filter()
        title__icontains='x'
        title__iexact='x'
       '''