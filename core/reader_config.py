reader_cfg_dict = {
    'duration': 1,  # для бесконечного считывания
    'tx_power_dbm': 31.5,  # Мощность передачи dBm
    'frequencies': {
        'HopTableId': 1,
        'Channelist': [866.9],  # Частотный диапазон в МГц
        'Automatic': False
    },
    'mode_identifier': 1004,  # Режим работы считывателя
    'session': 2,  # Сессия
    'impinj_search_mode': 2,  # Установка режима Single Target (по документации вашего устройства)
    'tag_population': 1,  # Предполагаемое количество меток в зоне считывания
    'antennas': [0],  # Какие антенны использовать (0 - все антенны)
    # какие данные о метках будут включены в отчеты:
    'tag_content_selector': {
        'EnableROSpecID': False,
        'EnableSpecIndex': False,
        'EnableInventoryParameterSpecID': False,
        'EnableAntennaID': True,  # Включение идентификатора антенны
        'EnableChannelIndex': False,
        'EnablePeakRSSI': False,
        'EnableFirstSeenTimestamp': False,
        'EnableLastSeenTimestamp': False,
        'EnableTagSeenCount': False,
        'EnableAccessSpecID': False
    }
}
