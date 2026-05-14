import tkinter as Tk
from tkinter import *
from tkinter import messagebox
import requests

try:
    requests.get('http://10.23.23.119:5000', timeout=10)
except requests.exceptions.ConnectionError:
    print('无法连接到主机')
    exit()
