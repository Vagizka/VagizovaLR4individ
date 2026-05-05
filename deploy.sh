#!/bin/bash

# deploy.sh - Скрипт для развертывания панели безопасности СХД
# Вагизова К.Х., КП-23-11, вариант 84

PORT=${PORT:-8080}
INDEX_FILE="index.html"

# Цвета для вывода
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "========================================="
echo "🔒 Контейнер безопасности СХД - Запуск"
echo "========================================="
echo "Автор: Вагизова К.Х. | КП-23-11"
echo ""

# Проверка наличия index.html
if [ ! -f "$INDEX_FILE" ]; then
    echo "❌ Ошибка: $INDEX_FILE не найден!"
    exit 1
fi

echo -e "${BLUE}📁 Файл $INDEX_FILE найден${NC}"
echo -e "${BLUE}🌐 Запуск сервера на порту $PORT...${NC}"
echo ""

# Запуск сервера
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✅ Сервер запущен!${NC}"
    echo "👉 Откройте в браузере: http://localhost:$PORT"
    echo "👉 Нажмите Ctrl+C для остановки"
    echo ""
    python3 -m http.server $PORT
elif command -v node &> /dev/null; then
    npx serve . -l $PORT
else
    echo "❌ Ошибка: Установите Python 3 или Node.js"
    exit 1
fi