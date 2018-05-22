import tornado.web
import random
import json

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"



class MenuHandler(tornado.web.RequestHandler):
    def __create_menu_key(self):
        global seed
        return "V1001_"+"".join(random.sample(seed,5))


    def get(self):
        self.render("menu_page.html")

    def post(self):
        menu1name = self.get_argument("menu1")
        menu1type = self.get_argument("menu1_type")
        menu11name = self.get_argument("menu11")
        menu11type = self.get_argument("menu11_type")
        menu12name = self.get_argument("menu12")
        menu12type = self.get_argument("menu12_type")
        menu13name = self.get_argument("menu13")
        menu13type = self.get_argument("menu13_type")
        menu1value = self.get_argument("menu1_") 
        menu11value = self.get_argument("menu11_") 
        menu12value = self.get_argument("menu12_") 
        menu13value = self.get_argument("menu13_") 
        #
        menu2name = self.get_argument("menu2")
        menu2type = self.get_argument("menu2_type")
        menu21name = self.get_argument("menu21")
        menu21type = self.get_argument("menu21_type")
        menu22name = self.get_argument("menu22")
        menu22type = self.get_argument("menu22_type")
        menu23name = self.get_argument("menu23")
        menu23type = self.get_argument("menu23_type")
        menu21value = self.get_argument("menu21_")
        menu22value = self.get_argument("menu22_")
        menu23value = self.get_argument("menu23_")
        #
        menu3name = self.get_argument("menu3")
        menu3type = self.get_argument("menu3_type")
        menu31name = self.get_argument("menu31")
        menu31type = self.get_argument("menu31_type")
        menu32name = self.get_argument("menu32")
        menu32type = self.get_argument("menu32_type")
        menu33name = self.get_argument("menu33")
        menu33type = self.get_argument("menu33_type")
        menu31value = self.get_argument("menu31_")
        menu32value = self.get_argument("menu32_")
        menu33value = self.get_argument("menu33_")
        #
        menuvalue = {}
        button1 = {}
        button2 = {}
        button3 = {}
        sub_button = []
        if menu1name != "":
            if menu11name == "":
                button1["name"] = menu1name
                if menu1type == "0":
                    button1["type"] = "click"
                    button1["key"] = self.__create_menu_key() 
                elif menu1type == "1":
                    button1["type"] = "view"
                    button1["url"] = menu1value 
            else:
                button11 = {}
                button1["name"] = menu1name
                button11["name"] = menu11name
                if menu11type == "0":
                    button11["type"] = "click"
                    button11["key"] = self.__create_menu_key()
                elif menu11type == "1":
                    button11["type"] = "view"
                    button11["url"] = menu11value
                sub_button.append(button11)
                if menu12name != "":
                    button12 = {}
                    button12["name"] = menu12name
                    if menu12type == "0":
                        button12["type"] = "click"
                        button12["key"] = self.__create_menu_key()
                    elif menu12type == "1":
                        button12["type"] = "view"
                        button12["url"] = menu12value
                    sub_button.append(button12)
                if menu13name != "":
                    button13 = {}
                    button13["name"] = menu13name
                    if menu13type == "0":
                        button13["type"] = "click"
                        button13["key"] = self.__create_menu_key()
                    elif menu13type == "1":
                        button13["type"] = "view"
                        button13["url"] = menu13value
                    sub_button.append(button13)
            if len(sub_button) != 0:
                button1["sub_button"] = sub_button
            print(button1)
        



