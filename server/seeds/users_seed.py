from models.user import User
from exts import db


default_picture = (
    "https://www.pphfoundation.ca/wp-content/uploads/2018/05/default-avatar.png"
)
user1 = User(
    username="samuel nyamekesse",
    user_email="nyamekesse@phoenixtechvault.com",
    display_picture=default_picture,
    password="00195433Kk!",
    role="admin",
)
user2 = User(
    username="mary jane",
    user_email="jane@yahoo.com",
    display_picture=default_picture,
    password="pass123",
    role="user",
)
user3 = User(
    username="john nketia",
    user_email="nketia@gmail.com",
    display_picture=default_picture,
    password="pass123",
    role="creator",
)
user4 = User(
    username="prince ampori",
    user_email="ampori@yahoo.com",
    display_picture=default_picture,
    password="pass123",
    role="user",
)
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.commit()
