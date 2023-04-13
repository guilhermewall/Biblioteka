from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.serializers import UserSerializer
from users.permissions import IsCollaboratorOrOwner
from copies.models import Loan
from datetime import date, timedelta
import ipdb


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        loans = Loan.objects.filter(is_receipt=False)
        day = date.today()

        for loan in loans:
            if loan.date_devolution < day:
                loan.user.is_blocked = True
                loan.user.save()

        return User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaboratorOrOwner]

    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        loans = Loan.objects.filter(is_receipt=False, user=self.kwargs.get("user_id"))

        day = date.today()

        for loan in loans:
            if loan.date_devolution < day:
                loan.user.is_blocked = True
                loan.user.save()

        return User.objects.all()
