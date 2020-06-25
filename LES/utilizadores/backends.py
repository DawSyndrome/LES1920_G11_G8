from django.contrib.auth.backends import BaseBackend

from django.contrib.auth.hashers import check_password

from .models import Utilizador

class AuthBackend(BaseBackend):
	
	def authenticate(self, request, email_p=None, password_p=None):
		print("attempting authentication")
		try:
			user = Utilizador.objects.get(email=email_p)
			return user if check_password(password_p, user.password) else None
		except Utilizador.DoesNotExist:
			return None
	
	def get_user(self, user_id):
		try:
			return Utilizador.objects.get(id=user_id)
		except Utilizador.DoesNotExist:
			return None

	# def has_perm(self, user_obj, perm, obj=None):
	# 	if obj is None or type(obj) is not Utilizador:
	# 		return False;
	# 	return bool(obj.user_type & perm)

	