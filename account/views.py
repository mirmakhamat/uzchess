from rest_framework import generics
from rest_framework.response import Response
from .models import User, Cart
from .serializers import UserSerializer, CartSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from courses.serializers import CourseListSerializer
from library.serializers import BookListSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        user = User.objects.get(email=request.data.get('email'))
        if user.check_password(request.data.get('password')):
            serializer = UserSerializer(user)
            data = {
                'user': serializer.data,
                'token': user.auth_token.key
            }
            return Response(data)
        else:
            return Response(data={'detail': 'Invalid credentials'}, status=401)


class UserInfoView(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(email=request.user.email)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserUpdateView(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def put(self, request):
        user = User.objects.get(email=request.user.email)
        old_password = request.data.get('old_password')
        new_password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        if old_password or new_password or confirm_password:
            if user.check_password(old_password) is False:
                return Response(data={'detail': 'Old password is incorrect'}, status=400)
            if new_password != confirm_password:
                return Response(data={'detail': 'Passwords do not match'}, status=400)

            user.set_password(new_password)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserCoursesView(generics.ListAPIView):
    serializer_class = CourseListSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.email)
        return user.courses.all()


class UserSavedBooksView(generics.ListAPIView):
    serializer_class = BookListSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.email)
        return user.saved_books.all()


class UserSavedCoursesView(generics.ListAPIView):
    serializer_class = BookListSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.email)
        return user.saved_courses.all()


class UserCartView(generics.ListAPIView):
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.email)
        return user.cart.all()
