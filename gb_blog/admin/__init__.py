
def register_views():
    from gb_blog import models
    from gb_blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
    from gb_blog.extensions import admin, db

    admin.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
    admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
    admin.add_view(UserAdminView(models.User, db.session, category='Models'))
