from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Faqat autentifikatsiyalangan foydalanuvchilar ro'yxatni ko‘ra oladi
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # O'qish ruxsatlari har qanday so‘rovga beriladi, shuning uchun
        # GET, HEAD yoki OPTIONS so‘rovlariga har doim ruxsat beramiz
        if request.method in permissions.SAFE_METHODS:
            return True
        # Tahrir ruxsatlari faqat post muallifiga beriladi
        return obj.author == request.user
