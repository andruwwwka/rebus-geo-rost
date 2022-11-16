"""Кастомные мидлвары."""
from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    """Мидлвара для разрешения кроссайтовых запросов."""

    def process_response(self, req, resp):
        """Обновление заголовка ответа."""
        resp['Access-Control-Allow-Origin'] = '*'
        return resp
