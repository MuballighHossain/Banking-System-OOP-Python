#import from same directory -> import class_name

import bank_system

#if different folder -> from folder_name import class_name
# from OOP import book


johan = bank_system.Bank("Johan", 21, "Male")
johan.show_details()

johan.deposit(1000)

johan.withdraw(1200)

johan.deposit(500)

johan.withdraw(1200)

johan.view_balance()

print(johan.balance)