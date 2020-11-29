from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from ..decorators import *
from ..models import *
from ..schema import BookSchema

book_bp = Blueprint('book_bp', __name__)


@book_bp.route('/dashboard/books', methods=['POST'])
@required_login
@required_admin
def add_book(user=None):
    data = request.get_json()
    new_book_data = dict(
        title=data['title'],
        author=data['author'],
        pub_year=data['pub_year'],
        programming_language=data['programming_language'],
        publisher=data['publisher'],
        topic=data['topic'],
        number_of_pages=data['number_of_pages'],
        creator_id=user
    )
    new_book = Book(**new_book_data)
    db.session.add(new_book)
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(message="book with provided data already exist", error_message=str(e.orig)), 403
    return jsonify(message='book - {} has been created'.format(new_book.title)), 201


@book_bp.route('/dashboard/books', methods=['GET'])
@required_login
def get_books(user=None):
    books_list = Book.query.all()
    books_schema = BookSchema(many=True)
    return jsonify({'books': books_schema.dump(books_list)}), 200


@book_bp.route('/dashboard/books/<book_id>', methods=['GET'])
@required_login
def get_book(user=None, book_id=None):
    book = Book.query.filter_by(id=book_id).first()
    if book is None:
        return jsonify(message="book doesn't exist in db"), 404
    books_schema = BookSchema()
    return jsonify({'book': books_schema.dump(book)}), 200


@book_bp.route('/dashboard/books/<book>/put', methods=['PUT'])
@required_login
@required_admin
def put_book(user=None, book=None):
    data = request.get_json()
    book_data = Book.query.filter_by(title=book).first()
    book_data.title = data['title']
    book_data.author = data['author']
    book_data.pub_year = data['pub_year']
    book_data.programming_language = data['programming_language']
    book_data.publisher = data['publisher']
    book_data.topic = data['topic']
    book_data.number_of_pages = data['number_of_pages']
    book_data.creator_id = user.id
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(message="db error", error_message=str(e.orig)), 404
    return jsonify(message='book - {} has been changed'.format(book_data.title))


@book_bp.route('/dashboard/books/<book>/delete', methods=['DELETE'])
@required_login
@required_admin
def delete_book(user=None, book=None):
    book_data = Book.query.filter_by(title=book).first()
    if book_data is None:
        return jsonify(message="book doesn't exist in db"), 404
    db.session.delete(book_data)
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(message="db error", error_message=str(e.orig)), 404
    return jsonify(message='book - {} has been deleted'.format(book_data.title)), 200


@book_bp.route('/dashboard/books/<book>/like', methods=['GET'])
@required_login
def like_book(user=None, book=None):
    book_data = Book.query.filter_by(title=book).first()
    book_data.like()
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(message="db error", error_message=str(e.orig)), 404
    return jsonify(message='book - {} has been liked'.format(book.title)), 200


@book_bp.route('/dashboard/books/<book>/dislike', methods=['GET'])
@required_login
def dislike_book(user=None, book=None):
    book_data = Book.query.filter_by(title=book).first()
    book_data.dislike()
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(message="db error", error_message=str(e.orig)), 404
    return jsonify(message='book - {} has been disliked'.format(book.title)), 200
