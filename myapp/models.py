from django.db import models

# Create your models here.

#myapp_book이라는 테이블을 생성 > mysql은 앱명_소문자로 클래스명
class Book(models.Model) :
  bid = models.IntegerField(primary_key = True)
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  publisheddate = models.DateField()