from libs import pyProxy, pyAutoUpdate

li = pyAutoUpdate.lib_installer(["colorama"])
fu = pyAutoUpdate.file_updater(["/libs/pyProxy", "/libs/pyAutoUpdate"], ["https://raw.githubusercontent.com/eel-primo/pyProxy/main/pyProxy.py","https://raw.githubusercontent.com/eel-primo/pyAutoUpdate/main/pyAutoUpdate.py"])
app_update = pyAutoUpdate.file_updater(["bomber.py"], [""])

try:
    from colorama import init, Fore, Back, Style
    import os
    import sys
    import time
    import requests
except ImportError:
    li.install()
    fu.install()
    print("[!] Restart app to apply changes")
    exit()

init(autoreset=True) 

class menu:
    def __init__(self, content, navigation, navigation_link):
        self.content = content
        self.navigation = navigation
        self.nav_link = navigation_link

class ui:
    def __init__(self):
        self.current_page = 0
        self.action_result = ""
        self.input_immune = False
        self.hohol_mode = False

        self.main_menu = menu(["[1] Start SPAM", "   \__Supports RU", "[2] Config", "   \__Configure bomber", "[3] Links", "   \__Links to creators", "[4] Reinstall app", "   \__Do this if you do smth wrong...", "[5] Exit", "   \__Leave app"], [1,2,3,4,5], [5,1,7,3,4])
        '''
        Page id's
        0 - main menu
        1 - settings
        2 - links
        3 - reinstall
        4 - exit
        5 - bomber settings
        6 - bombing state
        7 - about
        '''        

    def tick(self):
        self._clear_scr_()
        self.logo()
        print()
        self.content(self.current_page)
        if self.current_page > 0:
            print("[0] Back")
            print("   \__Returns you to upper menu")
        print()
        
        if len(self.action_result) > 0:
            print(self.action_result)
        
        self.navigation(int(input(">>")))
        
    def _print_content_(self, content):
        for string in content.content:
            print(string)
    
    def _clear_scr_(self):
        for i in range(48):
            print("")
         #os.system('cls' if os.name=='nt' else 'clear')
        
    def logo(self):
        print(Back.RED + "                                                  " + Back.RESET)
        print(Back.RED + " ░█████╗░░█████╗░███████╗███████╗███████╗███████╗ " + Back.RESET)
        print(Back.RED + " ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝ " + Back.RESET)
        print(Back.RED + " ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝ " + Back.RESET)
        print(Back.RED + " ██║░░╚═╝██║░░██║█████╗░░█████╗░░█████╗░░█████╗░░ " + Back.RESET)
        print(Back.RED + " ██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░ " + Back.RESET)
        print(Back.RED + " ╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░███████╗███████╗ " + Back.RESET)
        print(Back.RED + " ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝ " + Back.RESET)
        print(Back.RED + "                                                  " + Back.RESET)
        if self.hohol_mode:
            print(Style.BRIGHT + Back.BLUE + "B0MB3R by VolodyaHoi          " + Back.RESET)
            print(Style.BRIGHT + Back.YELLOW + "Supplied by eel-primo (cd-con)" + Back.RESET)
        else:
            print(Style.BRIGHT + "B0MB3R by VolodyaHoi          " + Back.RESET)
            print(Style.BRIGHT + "Supplied by eel-primo (cd-con)" + Back.RESET)

    def content(self, page_id):
        if page_id == 0:
              self._print_content_(self.main_menu)  
        #implement
        pass

    def navigation(self, result):
        self.action_result = ""
        if self.current_page == 0:
            if result in self.main_menu.navigation:
                self.current_page = self.main_menu.nav_link[result - 1]
                self.input_immune = True
            else:
                self.action_result = "This action is not supposed here."
                
        if self.current_page == 1:
            if result == 0:
                self.current_page = 0
            #elif False:
                #pass
            else:
                if not self.input_immune:
                    self.action_result = "This action is not supposed here."

        if self.current_page == 2:
            if result == 0:
                self.current_page = 0
            #elif False:
                #pass
            else:
                if not self.input_immune:
                    self.action_result = "This action is not supposed here."

        if self.current_page == 3:
            if result == 0:
                self.current_page = 0
            else:
                li.install()
                fu.install()
                self.action_result = "Strongly recommended to restart app"

        if self.current_page == 4:
            self._clear_scr_()
            exit()

        if self.current_page == 5:
            if result == 0:
                self.current_page = 0
            #elif False:
                #pass
            else:
                if not self.input_immune:
                    self.action_result = "This action is not supposed here."

        if self.current_page == 6:
            if result == 0:
                self.current_page = 0
            #elif False:
                #pass
            else:
                if not self.input_immune:
                    self.action_result = "This action is not supposed here."

        if self.current_page == 7:
            if result == 0:
                self.current_page = 0
            #elif False:
                #pass
            else:
                if not self.input_immune:
                    self.action_result = "This action is not supposed here."
        self.input_immune = False

user_interface = ui()
while True:
    user_interface.tick()
