from django.db import models

class SpreadsheetData(models.Model):
    
    added_date = models.CharField( 
        verbose_name= "作成日",
        max_length=12,
    )

    manager = models.CharField( 
        verbose_name= "担当者",
        max_length=8,
    )

    category = models.CharField( 
        verbose_name= "カテゴリー",
        max_length=30,
    )

    question_id = models.TextField( 
        verbose_name= "問題ID",
    )

    question_number = models.CharField( 
        verbose_name= "問題番号",
        max_length=12,
    )

    chapter = models.CharField( 
        verbose_name= "章",
        max_length=12,
    )

    heading = models.CharField( 
        verbose_name= "見出し",
        max_length=30,
    )

    question = models.TextField( 
        verbose_name= "問題の本文",
        blank=True,
        null=True,
    )

    level = models.CharField( 
        verbose_name= "レベル",
        max_length=1,
    )

    hint = models.TextField( 
        verbose_name= "ヒント",
        blank=True,
        null=True,
    )

    answer = models.TextField( 
        verbose_name= "回答例",
        blank=True,
        null=True,
    )

    explanation = models.TextField( 
        verbose_name= "解説",
        blank=True,
        null=True,
    )
    
    remarks = models.TextField( 
        verbose_name= "備考",
        blank=True,
        null=True,
    )

    question_c_plus_plus = models.TextField( 
        verbose_name= "問題の本文(C++)",
        blank=True,
        null=True,
    )

    answer_c_plus_plus = models.TextField( 
        verbose_name= "解答例(C++)",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs): 
        if isinstance(self.question_id, int): # question_idがint型である場合
            self.question_id = f"{self.question_id:06d}" # 保存前に6桁の0埋めして問題IDを更新
        super().save(*args, **kwargs)

    def __str__(self):
        # 表示時にも0埋めされた形で問題IDを表示
        if isinstance(self.question_id, int):
            return f"{self.question_id:06d}"
        return str(self.question_id)