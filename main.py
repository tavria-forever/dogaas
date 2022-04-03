import logging

import requests
from fastapi import FastAPI, Response, Request

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
app = FastAPI()


@app.get('/')
async def index(request: Request):
    """Метод возвращает случайную картинку из dog.ceo."""
    endpoint = 'https://dog.ceo/api/breeds/image/random'

    logger.info(f'Хост: {request.client.host}')

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        logger.info(f'Получили ответ API: {response.text}')
        response = response.json()
        image_url = response.get('message')
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        logger.info('Загрузили картинку из dog.ceo')
        return Response(content=image_response.content, media_type='image/jpg')
    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)

        return {
            'error': message,
        }
