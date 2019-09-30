import rules2 as pr2
import answers as ans

print("\t\tЭкспертная система по выбору инструментальныйх средст при создании Web сайтов")

start = input("Хотите пройти опрос?\nДа/Нет: ")
if start == 'Да' or start == 'y' or start == 'да':
    ans.preprocess()
    pr2.start()

else:
    print("Завершение")
    exit()


