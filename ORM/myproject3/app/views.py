from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import (
    Q, F, Value, Func, Count, Avg, Sum, Max, Min, StdDev, Variance,
    ExpressionWrapper, DecimalField, Subquery
)
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class BookQueryViewSet(ViewSet):
    def list(self, request):
        results = {}

        results['filter'] = BookSerializer(Book.objects.filter(price__gt=100), many=True).data
        results['exclude'] = BookSerializer(Book.objects.exclude(stock__lt=10), many=True).data

        results['annotate'] = Author.objects.annotate(book_count=Count('books')).values('name', 'book_count')
        results['aggregate'] = Book.objects.aggregate(
            avg_price=Avg('price'), total_pages=Sum('pages'),
            max_price=Max('price'), min_price=Min('price'),
            std_dev=StdDev('price'), variance=Variance('price')
        )

        results['order_by'] = BookSerializer(Book.objects.order_by('-published_date'), many=True).data
        results['reverse'] = BookSerializer(Book.objects.order_by('published_date').reverse(), many=True).data

        results['distinct'] = Book.objects.values('author').distinct()
        results['values'] = list(Book.objects.values('title', 'price'))
        results['values_list'] = list(Book.objects.values_list('title', flat=True))

        results['none'] = list(Book.objects.none())
        results['all'] = BookSerializer(Book.objects.all(), many=True).data

        b1 = Book.objects.filter(price__lt=200)
        b2 = Book.objects.filter(pages__gt=100)
        results['union'] = list(b1.union(b2).values('id'))
        results['intersection'] = list(b1.intersection(b2).values('id'))
        results['difference'] = list(b1.difference(b2).values('id'))

        results['select_related'] = BookSerializer(Book.objects.select_related('author')[:5], many=True).data
        results['prefetch_related'] = AuthorSerializer(Author.objects.prefetch_related('books')[:5], many=True).data

        results['defer'] = Book.objects.defer('price').values('title')
        results['only'] = Book.objects.only('title').values('title')
        results['using'] = Book.objects.using('default').all().values('title')[:2]

        results['select_for_update'] = list(Book.objects.select_for_update().values('id')[:1])
        results['raw'] = list(Book.objects.raw("SELECT * FROM app_book WHERE price > %s", [100]))

        results['and'] = BookSerializer(Book.objects.filter(Q(price__gt=100) & Q(stock__gt=10)), many=True).data
        results['or'] = BookSerializer(Book.objects.filter(Q(price__lt=50) | Q(pages__gt=200)), many=True).data

        discounted = ExpressionWrapper(F('price') * 0.9, output_field=DecimalField())
        results['f_expression'] = Book.objects.annotate(discounted_price=discounted).values('title', 'discounted_price')

        latest_books = Book.objects.filter(author=F('author')).order_by('-published_date')
        results['subquery'] = Author.objects.annotate(
            latest_book=Subquery(latest_books.values('title')[:1])
        ).values('name', 'latest_book')

        results['lookups'] = Book.objects.filter(
            title__icontains='python',
            published_date__year=2024,
            stock__range=(10, 50),
            title__startswith='D'
        ).values('title', 'published_date')

        return Response(results)
