admin = {"name": "Ravi", "logged_in": True}
guest = {"name": "Anon", "logged_in": False}

def require_login(func):
    def wrapper(user, *args, **kwargs):
        if user.get("logged_in"):
            return func(user, *args, **kwargs)
        else:
            return "Access denied. Please log in."
    return wrapper

@require_login
def view_dashboard(user):
    return f"Welcome {user['name']}!"

print(view_dashboard(admin))
print(view_dashboard(guest))