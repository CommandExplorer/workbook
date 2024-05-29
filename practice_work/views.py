from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from workbook.models import SpreadsheetData
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(csrf_exempt, name='dispatch')
class PracticeWorkView(LoginRequiredMixin, View):
    template_name = 'work.html' # 「練習問題を開始する」を選択すると使用される

    def get(self, request): # practice_work/work/にアクセスすると呼ばれる
        return render(request, 'practice_work_select.html')

    def post(self, request):
        level_selected = request.POST.get('level_work') # フォームから送信されたデータの中から「level_work」というフィールドの値を取得
        num_questions = int(request.POST.get('num_work', 10)) # フォームから送信されたデータの中から「num_work」というフィールドの値を取得
        questions = SpreadsheetData.objects.filter(level=level_selected).order_by('?')[:num_questions]
        context = {'work_selected': questions} # レンダリングするテンプレートに渡すコンテキストを作成する
        return render(request, self.template_name, context)