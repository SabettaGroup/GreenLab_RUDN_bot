# Инструкция по запуску Telegram‑бота на ПК (Windows и macOS)


Репозиторий: https://github.com/SabettaGroup/GreenLab_RUDN_bot


Примечания
- Бот написан на Python; Docker не требуется.
- VS Code не обязателен (достаточно Python, Git и терминала/PowerShell), но при желании можно использовать.
- На iOS (iPhone/iPad) запустить бота нельзя. Для компьютеров Apple используйте инструкции для macOS.
- Файл .env по безопасности не хранится в репозитории — его нужно создать вручную (см. ниже).


Структура файла: две главы — для Windows и для macOS. В каждой есть раздел «BotFather» с пометкой «уже сделано».


---


## Глава 1. Windows (PowerShell)


1) Предварительные требования
- BotFather: получение токена и создание бота — уже сделано.
- Установить Python 3.10–3.12: https://www.python.org/downloads/
  - Во время установки отметьте галочку «Add Python to PATH».
- Установить Git: https://git-scm.com/download/win


2) Скачивание проекта
Откройте PowerShell (Пуск → PowerShell):
```powershell
# Клонировать репозиторий
git clone https://github.com/SabettaGroup/GreenLab_RUDN_bot.git
cd GreenLab_RUDN_bot
```
Если Git не используете, можно скачать ZIP: на странице репозитория нажмите «Code → Download ZIP», распакуйте и зайдите
папку проекта.


3) Создание и активация виртуального окружения
```powershell
python -m venv .venv
# активация окружения
.\.venv\Scripts\Activate.ps1
# если появится предупреждение об исполнении скриптов, выполните в PowerShell (от имени пользователя):
# Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```


4) Создание файла окружения .env (важно)
Создайте в корне проекта файл с именем .env (имя начинается с точки).
- Блокнот → вставьте строки ниже → Файл → Сохранить как → имя: .env, тип: «Все файлы», кодировка: UTF‑8 → сохранить в 
папку проекта.


Минимальный пример содержимого .env:
```env
BOT_TOKEN=ВАШ_ТОКЕН_ОТ_BOTFATHER
# при необходимости добавьте другие переменные, если они используются в коде, например:
# ADMIN_IDS=123456789,987654321
# DATABASE_URL=sqlite:///bot.db
# DEBUG=true
```
Подсказка: чтобы узнать точные имена переменных, можно поискать в исходниках по os.getenv( или environ[. Если не уверен
достаточно начать с BOT_TOKEN.


5) Установка зависимостей
```powershell
pip install -r requirements.txt
# при ошибках сборки сначала обновите инструменты:
# pip install -U pip setuptools wheel
```


6) Запуск бота
Запустите файл входа проекта. Чаще всего это main.py или bot.py в корне.
```powershell
python main.py
# или, если основной файл называется иначе:
python bot.py
```
Как понять, какой файл запускать:
- Посмотрите, в каком файле есть блок: if __name__ == "__main__":
- Или ориентируйтесь на README проекта.


Остановка — Ctrl+C в окне терминала.


7) Проверка
- Откройте Telegram, найдите своего бота (@username) и отправьте команду /start.
- Если бот отвечает — всё работает.


8) Повторный запуск в следующий раз
```powershell
cd Путь\к\GreenLab_RUDN_bot
.\.venv\Scripts\Activate.ps1
python main.py   # либо другой файл входа, если отличается
```


9) Обновление проекта до новой версии
Если папка была получена через git clone:
```powershell
cd Путь\к\GreenLab_RUDN_bot
.\.venv\Scripts\Activate.ps1
git pull
pip install -r requirements.txt  # если зависимости изменились
# перезапустите бота (Ctrl+C и снова команда python main.py)
```
Если проект скачивали ZIP‑архивом, для обновления заново скачайте ZIP, распакуйте и замените файлы проекта, сохранив ва
env (и при желании папку .venv).


10) Частые проблемы
- Команда python не найдена:
  - Закройте/откройте PowerShell после установки Python или используйте команду `py -3` (например, `py -3 -m venv .venv
- Ошибка прав при активации .venv:
  - Выполните `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` в PowerShell.
- Бот не отвечает:
  - Проверьте корректность BOT_TOKEN в .env (без пробелов и скрытых символов), перезапустите.
  - Проверьте ошибки в терминале.


---


## Глава 2. macOS (Terminal)


1) Предварительные требования
- BotFather: получение токена и создание бота — уже сделано.
- Установить Python 3.10–3.12.
  - Рекомендуется через Homebrew: https://brew.sh/
  - Установите: `brew install python` (по желанию также `brew install git`).
- Установить Git (если не установлен): `brew install git` или из Xcode Command Line Tools (`xcode-select --install`).


2) Скачивание проекта
Откройте Terminal:
```bash
git clone https://github.com/SabettaGroup/GreenLab_RUDN_bot.git
cd GreenLab_RUDN_bot
```
Либо скачайте ZIP с GitHub, распакуйте и зайдите в папку проекта.


3) Создание и активация виртуального окружения
```bash
python3 -m venv .venv
source .venv/bin/activate
```


4) Создание файла окружения .env (важно)
Создайте файл .env в корне проекта:
- Через TextEdit: Формат → Сделать обычный текст → вставьте содержимое → Сохранить как .env.
- Или в терминале: `touch .env && open -e .env`.


Пример содержимого .env:
```env
BOT_TOKEN=ВАШ_ТОКЕН_ОТ_BOTFATHER
# при необходимости:
# ADMIN_IDS=123456789,987654321
# DATABASE_URL=sqlite:///bot.db
# DEBUG=true
```


5) Установка зависимостей
```bash
pip install -r requirements.txt
# при ошибках: pip install -U pip setuptools wheel
```


6) Запуск бота
```bash
python3 main.py
# или, если основной файл называется иначе:
python3 bot.py
```
Подсказки по выбору файла входа — смотрите пункт в главе для Windows.


Остановка — Ctrl+C в терминале.


7) Проверка
- В Telegram отправьте боту /start и убедитесь, что он отвечает.


8) Повторный запуск
```bash
cd /путь/к/GreenLab_RUDN_bot
source .venv/bin/activate
python3 main.py   # либо соответствующий файл входа
```


9) Обновление проекта до новой версии
Если папка была получена через git clone:
```bash
cd /путь/к/GreenLab_RUDN_bot
source .venv/bin/activate
git pull
pip install -r requirements.txt  # если зависимости обновились
# перезапустите бота (Ctrl+C и снова команда python3 main.py)
```
Если скачивали ZIP — скачайте свежий ZIP, распакуйте и замените файлы, сохранив ваш .env (и при желании папку .venv).


10) Частые проблемы
- Команда python3/pip не найдена:
  - Установите Python через Homebrew: `brew install python`.
- Бот не отвечает:
  - Проверьте BOT_TOKEN в .env, перезапустите, посмотрите ошибки в терминале.


---


Дополнительно
- Как определить имена переменных окружения, если кроме BOT_TOKEN нужны ещё:
  - Поиск по исходникам: `os.getenv("...")`, `os.environ["..."]`.
  - Если увидите в репозитории файл `.env.example`, скопируйте его как `.env` и заполните значениями.
- Автозапуск (необязательно):
  - Windows: можно создать задачу в Планировщике заданий, которая запускает `python main.py` внутри активированного 
окружения.
  - macOS: можно использовать `launchd` или менеджеры процессов (например, `pm2` — работает и с Python-командами).
- Webhook vs polling: локально обычно используется polling; если проект изначально на webhook, локально удобнее временн
переключиться на polling или использовать ngrok.

