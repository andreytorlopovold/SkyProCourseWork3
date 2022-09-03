from flask import Blueprint, request, render_template

from app.modules.app_dao import AppDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

appDao = AppDAO('./static/data/posts.json','./static/data/bookmarks.json','./static/data/comments.json')

@main_blueprint.route('/')
def page_index():
    posts = appDao.load_posts()
    return render_template("index.html", posts=posts)