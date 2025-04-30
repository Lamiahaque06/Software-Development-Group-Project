from apps.core.models import User

def current_user(request):
    user = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            user = None
    return {'current_user': user}
