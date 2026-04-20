from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app import db
from app.blog import blog
from app.models import Post
from app.blog.forms import PostForm


@blog.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(
        page=page, per_page=5, error_out=False
    )
    return render_template('blog/index.html', posts=posts)


@blog.route('/post/<int:id>')
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('blog/detail.html', post=post)


@blog.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            published=form.published.data
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('blog.index'))
    return render_template('blog/form.html', form=form, title='New Post')


@blog.route('/post/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.published = form.published.data
        db.session.commit()
        flash('Post updated!', 'success')
        return redirect(url_for('blog.post_detail', id=post.id))
    return render_template('blog/form.html', form=form, title='Edit Post')


@blog.route('/post/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.', 'success')
    return redirect(url_for('blog.index'))


@blog.route('/my-posts')
@login_required
def my_posts():
    posts = Post.query.all()
    return render_template('blog/my_posts.html', posts=posts)
