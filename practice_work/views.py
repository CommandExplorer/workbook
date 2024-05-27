from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from workbook.models import SpreadsheetData
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(csrf_exempt, name='dispatch')
class PracticeWorkView(LoginRequiredMixin, View):
    template_name = 'work.html'

    def get(self, request):
        return render(request, 'practice_work_select.html')

    def post(self, request):
        level_selected = request.POST.get('level_work')
        num_questions = int(request.POST.get('num_work', 10))
        questions = SpreadsheetData.objects.filter(level=level_selected).order_by('?')[:num_questions]
        context = {'work_selected': questions}
        return render(request, self.template_name, context)