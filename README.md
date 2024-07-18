# Быстрый запуск

Проверялось на python:3.9 или старше

1) В файле `main.py` установить правильный хост считывателя `READER_HOST = "192.168.88.249"`
2) Запуск программы `python main.py`


3) По желанию* настроить считыватель (частота, мощность и тд.)

# Конфигурация для считывателя

### Файл конфигурации `reader_config.py` в папке `core` содержит настройки для считывателя:

- duration: Время считывания (1 для бесконечного считывания)
- tx_power_dbm: Мощность передачи в dBm
- frequencies: Настройки частотного диапазона
- mode_identifier: Режим работы считывателя
- session: Сессия
- impinj_search_mode: Режим поиска
- tag_population: Предполагаемое количество меток в зоне считывания
- report_every_n_tags: Отчет каждые N меток
- report_timeout_ms: Таймаут отчета в миллисекундах
- antennas: Используемые антенны (0 - все антенны)
- tag_content_selector: Параметры выбора содержимого меток

## Impinj R420

Для выбора правильных настроек режима, сессии и режима поиска,
посетите: https://support.impinj.com/hc/en-us/articles/360017167239-What-Reader-Mode-Session-and-Search-Mode-should-I-use-for-my-application

![режимы считывателя.png](%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D1%8B%20%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F.png)

# Исходники

Для работы использовался модуль: https://github.com/sllurp/sllurp