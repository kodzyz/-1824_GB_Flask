from werkzeug.security import generate_password_hash
from gb_blog.app import create_app, db

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )


@app.cli.command('init-db', help="create all db")
def init_db():
    # создать все таблицы
    db.create_all()


@app.cli.command('create-users', help="create users")
def create_users():
    from gb_blog.models import User
    db.session.add(
        User(email='name@email.com', password=generate_password_hash('123'))
    )
    db.session.commit()
