from django.shortcuts import render
from .models import Bank_Details
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    bank = Bank_Details.objects.all()[:10]
    return render(request,'index.html',{'bank':0})

def about(request):
    return render(request,'about.html',{'bank':0})

def contact(request):
    return render(request,'contact.html',{'bank':0})


def showifsc(request):
    bankname = request.GET.get('Name').lower()
    city = request.GET.get('City').lower()
    print(bankname,city)
    # bankname = 'STATE'.lower()
    # city = 'mumbai'
    ifsc = Bank_Details.objects.filter(bank_name__icontains = bankname).filter(city__icontains=city)
    ifsc = len(ifsc)
    return render(request, 'index.html',{'bank': False,
                                         'ifsc':ifsc})
def showdetail(request):
    ifsc = request.GET.get('ifsc')
    detail = Bank_Details.objects.filter(ifsc=ifsc)
    return render(request, 'bank_details.html',{'bank': True,
                                         'detail':detail[0]})

class ifsc_detail(DetailView):
    model = Bank_Details
    template_name = 'bank_details.html'
    context_object_name = 'detail'
    queryset = Bank_Details.objects.all()[:10]
    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        ans  = Bank_Details.objects.filter(ifsc=id_)
        if len(ans) > 0:
            return ans[0]
        else:
            return []
    def get_context_data(self, **kwargs):
        context = super(ifsc_detail, self).get_context_data(**kwargs)
        order = ['ifsc', 'bank_name', 'branch','address','city','district','state']
        id_ = self.kwargs.get('id')
        ans = Bank_Details.objects.filter(ifsc=id_)[0]
        d = {}
        for x in order:
            d[x] = getattr(ans, x)

        context['order']  = d
        return context

class bank_in_town(ListView):
    model = Bank_Details
    template_name = 'bank_town.html'
    context_object_name = 'allbanks'
    paginate_by = 10
    def get(self, request, *args, **kwargs):
        self.bankname = request.GET.get('Name').lower()
        self.city = request.GET.get('City').lower()
        self.page_num =  request.GET.get('page')
        return super(bank_in_town, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(bank_in_town, self).get_context_data(**kwargs)
        bankname = self.bankname
        city =  self.city
        context['bankname'] = bankname
        context['city'] = city
        bank_list = Bank_Details.objects.filter(bank_name__icontains=bankname).filter(city__icontains=city)[:100]

        paginator = Paginator(bank_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            film_page = paginator.page(page)
        except :
            film_page = paginator.page(1)

        context['page_obj'] = film_page
        return context