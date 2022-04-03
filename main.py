import logging
import tempfile

import uvicorn
import requests
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

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
        with tempfile.NamedTemporaryFile(mode='w+b', suffix='.jpeg') as outfile:
            logger.info('Загрузили картинку из dog.ceo')
            content = requests.get(image_url).content
            outfile.write(content)
            return FileResponse(outfile.name, media_type='image/jpeg')

    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)

        return {
            'error': message,
        }

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info',
                reload=True)
