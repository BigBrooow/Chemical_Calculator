from config import TOKEN
from utils import get_sub, check, divide, get_sum
import telebot
#bot = telebot.TeleBot('TOKEN')


sub = input("Введите вещество: ")
sub = check(sub)
el = divide(sub)[0]
ind = divide(sub)[1]
sum = round(get_sum(el, ind), 3)
print(f"Молярная масса вещества равна {sum} г/моль")
