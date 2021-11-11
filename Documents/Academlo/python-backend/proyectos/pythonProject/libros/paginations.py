from rest_framework.pagination import PageNumberPagination, CursorPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_params = 'pagina'


class CustomPagination(CursorPagination):
    ordering = '-id'
