from core.models.userModel import User


def get_users():
    posts = User.query.all()
    return posts
