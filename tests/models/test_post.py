import pytest

from blog.factories import PostFactory

<<<<<<< HEAD

=======
>>>>>>> 7e72e91 (ajustes na documentação da branch django-admin)
@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

<<<<<<< HEAD

=======
>>>>>>> 7e72e91 (ajustes na documentação da branch django-admin)
@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'