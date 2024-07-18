import signal
import socket
import sys

from core.logger_output import logger
from core.reader_config import reader_cfg_dict
from services.backoff import backoff
from sllurp.llrp import LLRPReaderConfig, LLRPReaderClient, LLRP_DEFAULT_PORT

READER_HOST = "192.168.88.249"


def callback(_reader, tags):
    """
    Callback функция для обработки меток, прочитанных считывателем.

    Параметры:
        _reader (LLRPReaderClient): Объект считывателя, вызвавший callback.
        tags (list): Список прочитанных меток.
    """
    logger.info(f'TAGS:{tags}')


# Создание конфигурации считывателя на основе настроек считывания
config = LLRPReaderConfig(reader_cfg_dict)
# Инициализация клиента считывателя с заданным хостом и портом
reader = LLRPReaderClient(READER_HOST, LLRP_DEFAULT_PORT, config)
# Добавление callback функции для обработки прочитанных меток
reader.add_tag_report_callback(callback)


@backoff(exceptions=(socket.timeout, socket.error), start_sleep_time=1, max_attempts=10)
def reader_connect():
    """
    Попытка подключения к считывателю с использованием механизма экспоненциального бэк-оффа.
    Если подключение не удается, повторяет попытку подключения до 10 раз с начальным временем задержки 1 секунда.
    """
    logger.info(f'Connecting to Reader {READER_HOST}')
    reader.connect()
    logger.info('Connected')


def stop_and_exit(*args):
    """
    Отключение от устройства и завершение программы.

    Параметры:
        *args: Аргументы сигналов.
    """
    logger.info("Received KeyboardInterrupt. Cleaning up and exiting...")
    reader.disconnect()
    sys.exit(0)


# Обработка сигналов для корректного завершения программы
signal.signal(signal.SIGINT, stop_and_exit)  # Ctrl+C для завершения программы
signal.signal(signal.SIGTERM, stop_and_exit)  # Завершение программы в Docker


def main():
    """
    Основная функция для запуска процесса подключения и обработки меток.
    """
    reader_connect()
    try:
        # Ожидание завершения или отключения считывателя
        reader.join(None)
    except (KeyboardInterrupt, SystemExit):
        # Обработка прерывания программы и отключение считывателя
        reader.disconnect()


if __name__ == "__main__":
    main()
