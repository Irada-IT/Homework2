import requests

def test_create_post():
    url = 'https://test-stand.gb.ru/api/posts'
    post_data = {'title': 'Новый пост', 'description': 'Описание нового поста', 'content': 'содержание нового поста'}

    response = requests.post(url, json=post_data)
    assert response.status_code == 201

def test_check_post_existence():
    url = 'https://test-stand.gb.ru/api/posts'
    check_description = 'Описание нового поста'


    response = requests.get(url)
    assert response.status_code ==200

    posts = response.json()
    post_found = False
    for post in posts:
        if post['description'] == check_description:
            post_found = True
            break

    assert post_found
test_create_post()
test_check_post_existence()