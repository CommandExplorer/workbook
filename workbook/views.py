import re # 正規表現モジュール
from django.views.generic import ListView # ListViewをインポートする
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