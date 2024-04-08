class FriendCallNumb:
    def __init__(self):
        self.g_name = ""
        self.g_numb = ""

    def get_name(self):
        return self.g_name
    
    def get_numb(self):
        return self.g_numb
    
    def set_phone(self, g_numb):
        while True:
            try: 
                int_numb = int(g_numb)
                break
            except ValueError:
                print("입력 오류")
                return

        print("전화번호는", '{}-{}-{}'.format(str(g_numb)[:3], str(g_numb)[3:7], str(g_numb)[7:]) , "입니다.")

    def show_info(self):
        print("이름은", self.get_name(), "입니다.")
        self.set_phone(self.g_numb)
        

def main():

    name = FriendCallNumb()
    
    name.g_name = input("입력 이름:")
    name.g_numb = input("입력 전번:")

    name.show_info()

main()