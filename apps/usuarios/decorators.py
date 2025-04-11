from django.core.exceptions import PermissionDenied

def rol_requerido(*roles_permitidos):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'perfilusuario') and request.user.perfilusuario.rol in roles_permitidos:
               return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator
