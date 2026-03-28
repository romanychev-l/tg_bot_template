# Telegram Bot Template

Шаблон для создания Telegram-ботов на Python с использованием aiogram 3.

## Стек

- **aiogram 3** — асинхронный фреймворк для Telegram Bot API
- **aiogram_dialog** — управление диалогами и inline-клавиатурами
- **pymongo (async)** — асинхронный драйвер MongoDB
- **pydantic-settings** — конфигурация через переменные окружения
- **fluentogram** — интернационализация (i18n) с Fluent-форматом
- **Docker** — контейнеризация и деплой

## Быстрый старт

### Локальный запуск

```bash
cp .env.example .env
# Отредактируйте .env — укажите TOKEN от @BotFather

pip install -r requirements.txt
python -m bot
```

### Запуск через Docker

```bash
cp .env.example .env
# Отредактируйте .env

docker compose up -d
```

### Makefile

```bash
make build       # Собрать Docker-образ
make run         # Запустить контейнер
make build-run   # Собрать и запустить
make up          # docker compose up -d
make down        # docker compose down
make logs        # docker compose logs -f
```

## Структура проекта

```
bot/
├── __main__.py              # Точка входа
├── config_data/
│   └── config.py            # Конфигурация и подключение к БД
├── dialogs/
│   └── start/
│       ├── dialogs.py       # Определение диалогов (aiogram_dialog)
│       ├── getters.py       # Получение данных для диалогов
│       └── handlers.py      # Обработчики событий диалогов
├── handlers/
│   ├── commands.py          # Обработчики команд (/start)
│   └── other.py             # Обработчики прочих сообщений
├── locales/                 # Файлы переводов (ru, en)
├── middlewares/
│   └── i18n.py              # Middleware для интернационализации
├── states/                  # FSM-состояния
└── utils/
    └── i18n.py              # Настройка переводчика
```

## Переменные окружения

| Переменная     | Описание               | По умолчанию |
|----------------|------------------------|--------------|
| `TOKEN`        | Токен бота от BotFather | —            |
| `MONGO_HOST`   | Хост MongoDB           | `localhost`  |
| `MONGO_PORT`   | Порт MongoDB           | `27017`      |
| `MONGO_DB_NAME`| Имя базы данных        | `bot_db`     |
| `LOG_LEVEL`    | Уровень логирования    | `INFO`       |

## CI/CD

GitHub Actions автоматически собирает Docker-образ и деплоит на сервер при push в `main`. Настройте секреты в репозитории:

- `SSH_HOST`, `SSH_USER`, `SSH_PRIVATE_KEY`, `SSH_PORT` — для SSH-доступа к серверу
- `DEPLOY_PATH` — путь к проекту на сервере
