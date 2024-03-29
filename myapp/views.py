from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view

#python @d으로 시작하는 단어는 decorator라고 하는데 
#실제 함수를 호출하면 특정 내용을 삽입해서 함수를 실행합니다.
#반복적으로 사용하는 내용이나 직접 작성하기 번거로운 내용을 decorator로 만듭니다.
#Get 요청이 오면 함수를 호출
#@ 자동으로 ? html에서 ! tab과 같은 역할
@api_view(['GET']) 
# Create your views here.
def hello(request) :
  return Response("Hello REST API")

from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Book #현재 디렉토리의 models.py에서 Book import 
from .serializers import BookSerializer

#GET과 POST 모두를 처리
@api_view(['GET','POST']) #'POST:삽입, 'GET':조회
def booksAPI(request) :
  #GET 방식의 처리 - 조회를 요청하는 경우
  if request.method == 'GET' :
    #테이블의 데이터를 전부 가져오기
    books = Book.objects.all()
    #출력하기 위해서 브라우저의 형식으로 데이터를 변환
    serializer = BookSerializer(books, many = True)
    #출력
    return Response(serializer.data)

  #POST 방식의 처리 - 삽입하는 경우
  elif request.method == "POST" :
    #클라이언트에서 전송된 데이터를 가지고 Model 인스턴스 생성
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

@api_view(['GET'])
def oneBookAPI(request, bid) :
  #Book 테이블에서 bid 컬럼의 값이 bid인 값을 찾아옵니다.
  book = get_object_or_404(Book, bid = bid)
  #출력할 수 있도록 변환
  serializer = BookSerializer(book)
  return Response(serializer.data)