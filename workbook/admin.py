from django.contrib import admin
from .models import SpreadsheetData

class SpreadsheetDataAdmin(admin.ModelAdmin):
    list_display = ("question_id", "question_number") # レコード一覧に問題IDと問題番号を表示する
    list_display_links = ("question_id", "question_number") # 問題IDと問題番号にリンクを設定する
    
admin.site.register(SpreadsheetData, SpreadsheetDataAdmin) # djangoの管理サイトにモデルを登録し、SpreadsheetDataAdminを適用する