import re # 正規表現モジュール
from django.views.generic import ListView, DetailView # ListView、DetailViewをインポートする
from .models import SpreadsheetData

class ChapterListView(ListView): # 一覧を簡単に作るためのView
    template_name = "chapter_list.html" # chapter_list.htmlをレンダリングする
    context_object_name = "chapters" # object_listキーの別名を設定
    model = SpreadsheetData

    def get_queryset(self): # 自動的に呼び出される
        chapters = SpreadsheetData.objects.values('chapter').distinct() # 一意のchapterフィールドの値を持つオブジェクトを取得する

        def sort_key(chapter):
            chapter_match = re.match(r'基礎編ー第(\d+)章|応用編ー第(\d+)章', chapter['chapter'])
            
            if chapter_match.group(1): # 基礎編ー第〇章にマッチした場合
                return int(chapter_match.group(1)) # 整数に変換して返す
            else: # 基礎編ー第〇章にマッチしなかった場合
                if chapter_match.group(2): # 応用編ー第〇章にマッチした場合
                    return int(chapter_match.group(2)) + 1000 # 整数に変換して1000を加えて返す
                else: # 応用編ー第〇章にマッチしなかった場合
                    return float('inf') # 無限大を返す

        sorted_chapters = sorted(chapters, key=sort_key)
        return sorted_chapters

class QuestionListView(ListView):
    template_name = "question_list.html"
    context_object_name = "questions"
    model = SpreadsheetData
    
    def get_queryset(self):
        get_chapter = self.kwargs['chapter']  # URLから抽出されたchapterというキーワード引数の値を取得(選択された章の名前を取得)
        questions = SpreadsheetData.objects.filter(chapter=get_chapter).values('pk', 'question_number', 'category', 'level')
        
        def sort_key(question):
            question_match = re.match(r'(\d+)-(\d+)|応用(\d+)-(\d+)', question['question_number'])
            
            if question_match and question_match.group(1):  # ◇ー〇にマッチした場合
                return int(question_match.group(2))  # 〇の部分を整数に変換して返す
            elif question_match and question_match.group(3):  # 応用◇ー〇にマッチした場合
                return int(question_match.group(4))  # 〇の部分を整数に変換して返す
            else:  # マッチしなかった場合
                return float('inf')  # 無限大を返す

        sorted_questions = sorted(questions, key=sort_key)
        return sorted_questions
    
class QuestionDetailView(DetailView):
    template_name = "question_detail.html"
    context_object_name = "question"
    model = SpreadsheetData

class AnswerDetailView(DetailView):
    template_name = "answer_detail.html"
    context_object_name = "answer"
    model = SpreadsheetData
