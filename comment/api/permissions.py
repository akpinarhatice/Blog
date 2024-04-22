from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        print("İstek ne olursa olsun has_permission çalışır.")
        return request.user and request.user.is_authenticated
    message = "You must be owner this project"
    #has_permission sayesinde kullanıcı giriş yapamadan has_object_permission'ı çalıştıramaz.

    def has_object_permission(self, request, view, obj):
        print("İlgili ve çalışması gereken istek doğrultusunda has_object_permission çalışır.")
        return (obj.user == request.user)

