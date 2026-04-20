from flask import render_template
from app.main import main
from app.models import Post


@main.route('/')
def index():
    recent_posts = Post.query.filter_by(published=True).order_by(
        Post.created_at.desc()
    ).limit(3).all()
    return render_template('index.html', recent_posts=recent_posts)


@main.route('/about')
def about():
    return render_template('about.html')
