import os

from flask import request, Response, redirect

from flask_restful import Resource

from main.services.shortcut import get_url, save_new_short_url, check_for_free
from main.utils.common import generate_random_name, url_validator


class ShortCutCreate(Resource):

    def post(self):
        short_name = request.form.get('short_name')
        url = request.form.get('url')
        if not (short_name or url):
            return Response("{'error': 'Ссылка и короткое название обязательны'}", status=400,
                            content_type='application/json')
        if not check_for_free(short_name):
            return Response("{'error': 'Такое название уже занято. Попробуйте сгенерировать'}", status=400)

        new_url = save_new_short_url(url=url, short_url=short_name)

        if not new_url:
            return Response("{'error': 'Не получилось сохранить ссылку'}", status=400)

        return Response(short_name, status=200)


class ShortCutGenerate(Resource):

    def get(self, *args, **kwargs):
        name = generate_random_name()
        url = self.get_free_url(name)
        if not url:
            return Response(status=400)

        return Response(name, status=200)

    def get_free_url(self, url, step=10):
        if step == 1:
            return None
        if check_for_free(url):
            return url
        else:
            self.get_free_url(url, step - 1)


class ShortCutRedirect(Resource):

    def get(self, content):
        url, is_valid = url_validator(get_url(content))
        if not is_valid:
            return redirect(os.environ['FRONTEND_URL'])
        return redirect(url)