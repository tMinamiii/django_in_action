from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bmi
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.


@login_required
def index(request):
    # BmiモデルをとおしてBMIテーブルからログインユーザーに紐づく
    # 全データを取得してcontext辞書に格納
    context = {
        "bmi": Bmi.objects.filter(user=request.user),
    }

    # example.htmlテンプレートにcontextを渡してhtmlを生成
    return render(request, "example.html", context)


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Bmi
    template_name = "example.html"

    def get_queryset(self):
        return Bmi.objects.filter(user=self.request.user)


class DjangoRedirectView(generic.RedirectView):
    url = "https://djangoprocject.com"
