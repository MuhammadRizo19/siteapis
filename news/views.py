# views.py
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

# ✅ Create
class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# ✅ Read All (List)
class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-posted_time')
    serializer_class = NewsSerializer

# ✅ Read Single (Retrieve)
class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'

# ✅ Update
class NewsUpdateView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'

# ✅ Delete
class NewsDeleteView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'
