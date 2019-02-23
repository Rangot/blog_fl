from flask import Blueprint, render_template, request

from models import Post, Tag


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        posted = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posted = Post.query.all()
    return render_template('posts/index.html', posted=posted)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posted = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posted)
