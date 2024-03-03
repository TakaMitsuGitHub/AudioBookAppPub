from abc import ABCMeta, abstractmethod
from book.models import BookModel
import config
import pyttsx3
import sounddevice as sd
import numpy as np
import wave


# 抽象クラス
class AudioProcess(metaclass=ABCMeta):

    @abstractmethod
    def change(self, request):
        pass


class SentenceChanger(AudioProcess):

    def __init__(self, request):
        self.request = request

    def change(self):
        book_id = self.request.book_id
        sentence = BookModel.objects.get(id=book_id).fields('sentence')

        # 音声変換処理

        # 音声データ保存
