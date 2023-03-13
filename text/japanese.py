import re
from unidecode import unidecode
import ctypes

dll = ctypes.cdll.LoadLibrary('cleaners/JapaneseCleaner.dll')
dll.CreateOjt.restype = ctypes.c_uint64 
dll.PluginMain.restype = ctypes.c_uint64 
floder = ctypes.create_unicode_buffer("cleaners")
dll.CreateOjt(floder)

def clean_japanese(text):
    input_wchar_pointer = ctypes.create_unicode_buffer(text)
    result = ctypes.wstring_at(dll.PluginMain(input_wchar_pointer))
    return result

