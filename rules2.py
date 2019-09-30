import answers as ans

new = 0
pro = 0
vs = 0

# Start the expert system
def start():
    print("\n\nВыберите вид платформы: ")
    print("1. Текстовый редактор (для небольших и несложных проектов) ")
    print("2. Полноценная IDE")

    platform = input("\nВведите число: ")

    if platform == '1':
        text1()
    elif platform == '2':
        ide()
    else:
        print("invalid")


def text1():
    print("Хотите редактировать web-страницы прямо в браузере? ")
    print("1. Да ")
    print("2. Нет ")

    bracket = input("\nВыберите: ")

    if bracket == '1':
        choose_serv()
        ans.brackets()
    elif bracket == '2':
        cloud()


def text2():
    print("Вам нужна кроссплатформенность? ")
    print("1. Да ")
    print("2. Нет ")

    bracket = input("\nВыберите: ")

    if bracket == '1':
        choose_serv()
        ans.sublime()

    elif bracket == '2':
        choose_serv()
        ans.notepadpp()



def cloud():
    print("Как насчет разработки в облаке? ")
    print("1. Да ")
    print("2. Нет ")

    Cloud = input("\nВыберите: ")

    if Cloud == '1':
        cloud2()
    elif Cloud == '2':
        text2()


def cloud2():
    print("Вам нужны Dropbox и SFTP для резервного копирования и обмена файлами с разработчиками? ")
    print("1. Да ")
    print("2. Нет ")

    Cloud_code = input("\nВыберите: ")

    if Cloud_code == '1':
        ans.codeanywhere()
    elif Cloud_code == '2':
        ans.cloud9()


def ide():
    print("Вам нужна IDE с поддержкой нескольких языков или разработанная для одного конкретного? ")
    print("1. С поддержкой нескольких популярных языков")
    print("2. Для определнного языка ")

    ide_lang = input("\nВыберите: ")

    if ide_lang == '1':
        ide2()
    elif ide_lang == '2':
        jetbrains()


def jetbrains():
    print("Выберите язык: ")
    print("1. Python")
    print("2. C/C++/C#")
    print("3. PHP")
    print("4. HTML + CSS + JavaScript")

    lang = input("\nВыберите: ")

    if lang == '1':
        ans.jb_pycharm()
    elif lang == '2':
        ans.jb_clion()
    elif lang == '3':
        ans.jb_php()
    elif lang == '4':
        ans.jb_webstorm()



def ide2():
    global new, pro
    print("Вам нужна среда разработки для новичков или профессионалов? ")
    print("1. Для новичков (понятный интерфейс)")
    print("2. Для профессионалов (многофункциональность)")

    diff = input("\nВыберите: ")

    if diff == '1':
        new += 1
        free()
    elif diff == '2':
        pro += 1
        free()


def free():
    global vs
    print("Вам нужна абсолютно бесплатная IDE? ")
    print("1. Да ")
    print("2. Нет ")

    Free = input("\nВыберите: ")

    if Free == '1' and new > 0:
        choose_serv()
        ans.netbeans()

    elif Free == '1' and pro > 0:
        choose_serv()
        ans.eclipse()

    elif Free == '2':
        vs += 1
        ans.vs()


def choose_serv():
    print("Теперь выберем локальный сервер.")
    print("Вам нужна кроссплатформенность программы сервера? ")
    print("1. Да ")
    print("2. Нет ")

    Serv = input("\nВыберите: ")

    if vs > 0:
        print("В Visual Studio уже используется IIS")
        ans.iis()
    elif vs == 0 and Serv == '1':
        ans.xampp()
    elif vs == 0 and Serv == '2':
        ans.openserv()
