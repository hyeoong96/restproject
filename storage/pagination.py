from rest_framework.pagination import PageNumberPagination


class Fpagination(PageNumberPagination):
    page_size = 5

class Tpagination(PageNumberPagination):
    page_size = 3