import os
import django
import gspread
from google.oauth2 import service_account

# DJANGO_SETTINGS_MODULE環境変数が未設定の場合、settings.pyのパスを渡す
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming_learning.settings") 
django.setup() # Djangoの設定を行う

from workbook.models import SpreadsheetData

def load_data(): # GoogleSheetsからデータを取得する
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] # スコープの作成
    json_file_path = 'model-caldron-407203-3961eadddac6.json' # JSONファイルのパス
    SPREADSHEET_KEY = '1ZkprGY-V4V-uRORfPE6bw_0I1pCgBheLIAYrDyBx3k4' # 共有設定したスプレッドシートキー

    credentials = service_account.Credentials.from_service_account_file(json_file_path, scopes=scope) # 認証情報設定
    gc = gspread.Client(auth=credentials)  # サービスアカウントを使ってログインする
    gc.verify = True  # SSL証明書の検証を有効にする（必要に応じて）

    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1 # シート1で作業を行う
    records = worksheet.get_all_records()  # 各行を辞書として取得する

    # 問題IDを0埋めする
    for record in records:
        record["問題ID"] = str(record["問題ID"]).zfill(6)
    return records

def update_data(): # データベースのデータを更新する
    latest_data = load_data() # スプレッドシートから最新のデータを取得
    existing_data = SpreadsheetData.objects.all() # SpreadsheetDataモデルの全データを取得

    for row in latest_data: # スプレッドシートの各行を順に処理
        # データベースのテーブルに既存のデータがあれば更新し、テーブルに何もなければ新規追加する
        obj, created = SpreadsheetData.objects.update_or_create(
            question_id=row["問題ID"],
            defaults=
            {
                'added_date': row["追加日"],
                'manager': row["担当者"],
                'category': row["カテゴリー"],
                'question_number': row["問題番号"],
                'chapter': row["章"],
                'heading': row["問題の見出し"],
                'question': row["問題の本文"],
                'level': row["レベル"],
                'hint': row["ヒント"],
                'answer': row["回答例"],
                'explanation': row["解説"],
                'remarks': row["備考"],
                'question_c_plus_plus': row["C++verの問題"],
                'answer_c_plus_plus': row["C++verの回答例"],
            },
        )

    # データベースに存在しているがスプレッドシートにないデータは削除
    for existing_obj in existing_data:
        if all(existing_obj.question_id != row["問題ID"] for row in latest_data):
            existing_obj.delete()
            
def save_to_database(data): # 取得したデータをDjangoのモデルに保存する
    for row in data:
        spreadsheet_data = SpreadsheetData(
            added_date=row["追加日"],
            manager=row["担当者"], 
            category=row["カテゴリー"], 
            question_id=row["問題ID"], 
            question_number=row["問題番号"], 
            chapter=row["章"], 
            heading=row["問題の見出し"], 
            question=row["問題の本文"], 
            level=row["レベル"], 
            hint=row["ヒント"], 
            answer=row["回答例"], 
            explanation=row["解説"], 
            remarks=row["備考"], 
            question_c_plus_plus=row["C++verの問題"], 
            answer_c_plus_plus=row["C++verの回答例"])
        spreadsheet_data.save() # Djangoモデルのインスタンスをデータベースに保存する

if __name__ == "__main__": # load_into_database.pyが直接実行された時にのみ実行される
    # save_to_database(load_data())
    update_data()
