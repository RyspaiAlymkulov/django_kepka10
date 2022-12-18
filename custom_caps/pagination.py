from rest_framework.pagination import PageNumberPagination


class CapsPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 4000
    page_query_param = "page_size"