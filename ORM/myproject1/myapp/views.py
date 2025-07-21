from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.models import Book, Author, Profile, Store
from myapp.serializers import BookSerializer, AuthorSerializer, ProfileSerializer, StoreSerializer
from django.db.models import Avg

class QuerySetDemoRelationView(APIView):
    def get(self, request):
        result = {}

        # create()
        author = Author.objects.create(name="George Orwell")
        book = Book.objects.create(title="1984", published_year=1949, author=author)
        result['create'] = BookSerializer(book).data

        # one-to-one
        profile = Profile.objects.create(author=author, biography="Dystopian author")
        result['one_to_one'] = ProfileSerializer(profile).data

        # get_or_create()
        author, created = Author.objects.get_or_create(name="Aldous Huxley")
        result['get_or_create'] = AuthorSerializer(author).data

        # update_or_create()
        book, created = Book.objects.update_or_create(
            title="Brave New World",
            defaults={"published_year": 1932, "author": author}
        )
        result['update_or_create'] = BookSerializer(book).data

        # bulk_create()
        books = [
            Book(title="Book A", published_year=2001, author=author),
            Book(title="Book B", published_year=2002, author=author),
        ]
        Book.objects.bulk_create(books)
        result['bulk_create'] = '2 books created'

        # bulk_update()
        books = Book.objects.filter(author=author)
        for b in books:
            b.published_year += 1
        Book.objects.bulk_update(books, ['published_year'])
        result['bulk_update'] = 'published_year incremented'

        # many-to-many
        store = Store.objects.create(name="Central Library")
        store.books.set(Book.objects.all())
        result['many_to_many'] = StoreSerializer(store).data

        # count()
        result['count'] = Book.objects.count()

        # in_bulk()
        books_dict = Book.objects.in_bulk([1, 2])
        result['in_bulk'] = list(books_dict.keys())

        # latest() and earliest()
        result['latest'] = Book.objects.latest('published_year').title
        result['earliest'] = Book.objects.earliest('published_year').title

        # first() and last()
        result['first'] = Book.objects.order_by('title').first().title
        result['last'] = Book.objects.order_by('title').last().title

        # aggregate()
        result['average_year'] = Book.objects.aggregate(Avg('published_year'))['published_year__avg']

        # exists()
        result['exists'] = Book.objects.filter(title="1984").exists()

        # update()
        Book.objects.filter(title="Book A").update(title="Book A - Updated")
        result['update'] = 'Book A updated'

        # delete()
        Book.objects.filter(title="Book B").delete()
        result['delete'] = 'Book B deleted'

        # as_manager()
        recent_books = Book.objects.recent()
        result['recent_books'] = BookSerializer(recent_books, many=True).data

        # explain()
        explanation = Book.objects.filter(published_year__gte=2000).explain()
        result['explain'] = explanation

        return Response(result)
