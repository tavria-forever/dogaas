# dogaas

Работает на python@3.7.12

1. Создать и активировать venv

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Установить зависимости

```bash
pip install -r requirements.txt
```

3. Локальный запуск

```bash
uvicorn main:app --reload
```
