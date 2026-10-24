# Pure ASCII Logger Stream (§3.4.24)
class LoggerStream:
    @staticmethod
    def info(msg: str):
        print('[INFO] ' + str(msg))

    @staticmethod
    def warn(msg: str):
        print('[WARN] ' + str(msg))

    @staticmethod
    def error(msg: str):
        print('[ERROR] ' + str(msg))
