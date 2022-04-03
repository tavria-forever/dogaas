# dogaas

**n.b** Работает на python=3.8.13

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
python main.py
```

## Деплой

1. Настроить `yappa`, если раньше этого не делали, если уже, сразу переходим к шагу 2.

```bash
yappa setup
```

2. Загрузка в яндекс.облако

```bash
yappa deploy
```
