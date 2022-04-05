import logging

import uvicorn
import requests
from fastapi import FastAPI, Request, Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()

ENDPOINT = 'https://dog.ceo/api/breeds/image/random'


@app.get('/')
async def index(request: Request):
    """Метод возвращает случайную картинку из dog.ceo."""
    logger.info(f'Хост: {request.client.host}')

    try:
        response = requests.get(ENDPOINT)
        response.raise_for_status()
        logger.info(f'Получили ответ API: {response.text}')
        response = response.json()
        image_url = response.get('message')
        logger.info('Загрузили картинку из dog.ceo')
        content = requests.get(image_url).content
        return Response(content=content, media_type='image/jpeg')
    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)
        return {'error': message}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8001, log_level='info',
                reload=True)
