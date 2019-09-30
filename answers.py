ides_list = []
servs_list = []


def preprocess():
    global ides_list, servs_list
    ides = open("ides.txt")
    ides_t = ides.read()
    ides_list = ides_t.split("\n")
    ides.close()

    servs = open("servs.txt")
    servs_t = servs.read()
    servs_list = servs_t.split("\n")
    servs.close()


def answer(ide):
    print("\nДля web-разработки Вам подойдет:")
    ide_s_file = open("ide descriptions/" + ide + ".txt")
    ide_s_data = ide_s_file.read()
    print(ide_s_data)


def answer2(serv):
    print("\nСкорее всего Вам подойдет локальный сервер:")
    serv_s_file = open("ide serv/" + serv + ".txt")
    serv_s_data = serv_s_file.read()
    print(serv_s_data)


def jb_pycharm():
    answer("JetBrains PyCharm")


def jb_php():
    answer("JetBrains PhpStorm")


def jb_clion():
    answer("JetBrains CLion")


def jb_webstorm():
    answer("JetBrains WebStorm")


def brackets():
    answer("Brackets")


def codeanywhere():
    answer("Codeanywhere")


def cloud9():
    answer("Cloud9")


def eclipse():
    answer("Eclipse")


def netbeans():
    answer("NetBeans")


def sublime():
    answer("Sublime Text 3")


def vs():
    answer("Visual Studio")


def iis():
    answer2("IIS")


def openserv():
    answer2("OpenServer")


def xampp():
    answer2("XAMPP")
