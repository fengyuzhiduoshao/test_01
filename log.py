import logging
import os


class Log:
    """日志类"""
    file_name_path = os.path.dirname(__file__) + '/logs/log.text'
    def __init__(self, logger_name='root', level='DEBUG'):
        """
        创建 日志器 对象
        :param logger_name:
        :param level:
        """
        self.level = level
        self.logger = logging.getLogger(logger_name)
        # 给 日志器 添加需要纪录日志的等级
        self.logger.setLevel(level=level)

    def console_handler(self, level="DEBUG"):
        """
        创建 控制台处理器
        :param level: 处理器 处理日志的等级
        :return:self.conso_handler(控制台处理器）
        """
        self.conso_handler = logging.StreamHandler()
        # 给 处理器 添加 处理日志的等级
        self.conso_handler.setLevel(level=level)
        # 给 处理器 添加 格式器
        self.format()
        self.conso_handler.setFormatter(self.format()[0])
        return self.conso_handler

    def file_handler(self, file_name=file_name_path, level="DEBUG"):
        """
        创建 文件处理器
        :param level: 输入文件的日志等级
        :return:self.file_name_handler(文件类处理器）
        """
        self.file_name_handler = logging.FileHandler(filename=file_name, mode='w', encoding='utf-8')
        # 给处理器添加等级
        self.file_name_handler.setLevel(level=level)
        # 给处理器添加格式器
        self.format()
        self.file_name_handler.setFormatter(self.format()[1])
        return self.file_name_handler


    def format(self, console_str="%(name)s--%(module)s--%(asctime)s--%(levelname)s: %(message)s  ",
               file_str="%(name)s--%(module)s--%(asctime)s--%(levelname)s: %(message)s "):
        """
        创建 格式器
        :return: console_format（控制台格式器）,file_format（文件格式器）
        """
        console_format = logging.Formatter(console_str)
        file_format = logging.Formatter(file_str)
        return console_format, file_format

    def get_logger(self):
        """
        给 日志器 添加 处理器
        :return:
        """
        # 添加 控制台处理器
        self.logger.addHandler(self.console_handler())
        # 添加 文件控制器
        self.logger.addHandler(self.file_handler())
        return self.logger


log = Log().get_logger()


if __name__ == '__main__':
    path = os.path.dirname(__file__)
    print(path)
    log = Log().get_logger()
    log.info("info")
    log.debug("debug")
    log.error("error")
