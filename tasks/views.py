# Модуль представлений для веб-интерфейса модуля аудита AuditView-84

from django.shortcuts import render

def index(request):
    """
    Функция-представление для главной страницы.
    Возвращает index.html с контекстом данных.
    """

    # Контекст данных для отображения в панели аудита
    context = {
        # Информация о продукте
        'product_name': 'AuditView-84',
        'full_name': 'Веб-интерфейс модуля аудита контейнера безопасности СХД',
        'container_name': 'SecureStorage-84',
        'version': '1.0',
        'student_name': 'Вагизова К.Х.',
        'group': 'КП-23-11',
        'variant': '84',

        # Статистика работы модуля аудита
        'total_requests': 2847,      # Всего запросов к СХД
        'blocked_access': 156,       # Заблокировано НСД
        'legit_access': 2691,        # Легитимных доступов
        'active_threats': 12,        # Активных попыток НСД

        # Журнал аудита (6 событий)
        'audit_events': [
            {
                'time': '14:23:11',
                'source': 'VM-WebServer-01',
                'ip': '10.0.1.55',
                'action': 'Попытка чтения /etc/shadow',
                'description': 'Нарушение прав доступа: субъект не авторизован',
                'status': 'denied',
                'status_text': 'ДОСТУП ЗАПРЕЩЕН (403)'
            },
            {
                'time': '14:20:05',
                'source': 'App-Backend',
                'ip': '172.17.0.3',
                'action': 'Чтение базы данных клиентов',
                'description': 'Аутентификация пройдена, сертификат валиден',
                'status': 'granted',
                'status_text': 'ДОСТУП РАЗРЕШЕН'
            },
            {
                'time': '14:15:42',
                'source': 'VM-Unknown',
                'ip': '10.20.30.5',
                'action': 'Попытка монтирования виртуального диска /dev/vdb1',
                'description': 'Несанкционированное подключение к диску',
                'status': 'denied',
                'status_text': 'БЛОКИРОВАНО (IP добавлен в черный список)'
            },
            {
                'time': '14:10:33',
                'source': 'malicious_process',
                'ip': 'PID 1337',
                'action': 'Обход ACL, чтение сегментов диска',
                'description': 'Эксплуатация слабости распределенного хранилища',
                'status': 'denied',
                'status_text': 'ИНЦИДЕНТ ЗАФИКСИРОВАН, ПРОЦЕСС ОСТАНОВЛЕН'
            },
            {
                'time': '14:05:18',
                'source': 'Backup-Service',
                'ip': '192.168.1.100',
                'action': 'Запись бэкапа в защищенное хранилище',
                'description': 'Шифрование канала TLS 1.3, цифровая подпись проверена',
                'status': 'granted',
                'status_text': 'ДОСТУП РАЗРЕШЕН (шифрование активно)'
            },
            {
                'time': '13:58:22',
                'source': 'external_attacker',
                'ip': '45.67.89.10',
                'action': '5 неудачных попыток аутентификации подряд',
                'description': 'Брутфорс атака на JWT-токен',
                'status': 'denied',
                'status_text': 'АККАУНТ БЛОКИРОВАН НА 30 МИНУТ'
            }
        ]
    }

    return render(request, 'index.html', context)