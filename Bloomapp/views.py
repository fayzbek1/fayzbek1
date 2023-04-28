from rest_framework import viewsets,generics,permissions,status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# class RegisterApiView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
    
#     def post(self,request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
        
#         user_data = serializer.data
        
#         return Response(user_data, status.HTTP_201_CREATED)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return super().get_token(user)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
#class UserViewSet(viewsets.ViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

class LavashListApiView(generics.ListAPIView):
    queryset = Lavash.objects.all()
    serializer_class = LavashSerializers

class LavashCreateApi(generics.ListCreateAPIView):
    queryset = Lavash.objects.all()
    serializer_class = LavashSerializers
    
class LavashRetrieveApi(generics.RetrieveAPIView):
    queryset = Lavash.objects.all()
    serializer_class = LavashSerializers
    
class LavashDestroyApi(generics.DestroyAPIView):
    queryset = Lavash.objects.all()
    serializer_class = LavashSerializers
    
class BurgerListApiView(generics.ListAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializers
    
class BurgerCreateApi(generics.ListCreateAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializers
    
class BurgerRetrieveApi(generics.RetrieveAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializers
    
class BurgerDestroyApi(generics.DestroyAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializers
    
class SalatListApiView(generics.ListAPIView):
    queryset = Salat.objects.all()
    serializer_class = SalatSerializers
    
class SalatCreateApi(generics.ListCreateAPIView):
    queryset = Salat.objects.all()
    serializer_class = SalatSerializers
    
class SalatRetrieveApi(generics.RetrieveAPIView):
    queryset = Salat.objects.all()
    serializer_class = SalatSerializers
    
class SalatDestroyApi(generics.DestroyAPIView):
    queryset = Salat.objects.all()
    serializer_class = SalatSerializers

class SandvichListApiView(generics.ListAPIView):
    queryset = Sandvich.objects.all()
    serializer_class = SandvichSerializers

class SandvichCreateApi(generics.ListCreateAPIView):
    queryset = Sandvich.objects.all()
    serializer_class = SandvichSerializers
    
class SandvichRetrieveApi(generics.RetrieveAPIView):
    queryset = Sandvich.objects.all()
    serializer_class = SandvichSerializers
    
class SandvichDestroyApi(generics.DestroyAPIView):
    queryset = Sandvich.objects.all()
    serializer_class = SandvichSerializers
    
class HotdogListApiView(generics.ListAPIView):
    queryset = Hotdog.objects.all()
    serializer_class = HotdogSerializers
    
class HotdogCreateApi(generics.ListCreateAPIView):
    queryset = Hotdog.objects.all()
    serializer_class = HotdogSerializers
    
class HotdogRetrieveApi(generics.RetrieveAPIView):
    queryset = Hotdog.objects.all()
    serializer_class = HotdogSerializers
    
class HotdogDestroyApi(generics.DestroyAPIView):
    queryset = Hotdog.objects.all()
    serializer_class = HotdogSerializers
    
class KartoshkaListApiView(generics.ListAPIView):
    queryset = Kartoshka.objects.all()
    serializer_class = KartoshkaSerializers
    
class KartoshkaCreateApi(generics.ListCreateAPIView):
    queryset = Kartoshka.objects.all()
    serializer_class = KartoshkaSerializers
    
class KartoshkaRetrieveApi(generics.RetrieveAPIView):
    queryset = Kartoshka.objects.all()
    serializer_class = KartoshkaSerializers
    
class KartoshkaDestroyApi(generics.DestroyAPIView):
    queryset = Kartoshka.objects.all()
    serializer_class = KartoshkaSerializers
    
class IchimlikListApiView(generics.ListAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializers
    
class IchimlikCreateApi(generics.ListCreateAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializers
    
class IchimlikRetrieveApi(generics.RetrieveAPIView):
    queryset = Ichimliklar
    serializer_class = IchimliklarSerializers

class IchimlikDestroyApi(generics.DestroyAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializers
    
class ShirinlikListApiView(generics.ListAPIView):
    queryset = Shirinliklar.objects.all()
    serializer_class = ShirinliklarSerializers

class ShirinlikCreateApi(generics.ListCreateAPIView):
    queryset = Shirinliklar.objects.all()
    serializer_class = ShirinliklarSerializers

class ShirinlikRetrieveApi(generics.RetrieveAPIView):
    queryset = Shirinliklar.objects.all()
    serializer_class = ShirinliklarSerializers
    
class ShirinlikDestroyApi(generics.DestroyAPIView):
    queryset = Shirinliklar.objects.all()
    serializer_class = ShirinliklarSerializers

class CustomerCRUDApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Custumer.objects.all()
    serializer_class = CustumersSerializers    
    
