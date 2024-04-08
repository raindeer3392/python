class friend_call_numb:

    #과제 제출란
    #조건: get_name, get_phone, set_phone, show_info 사용

    def __init__set_phone(self):
        return self.get_name()
    def __init__get_phone(self):
        return self.get_phone


def main():
    
    def get_phone():
        friend_name = input("이름을 입력하세요: ")
    
        def call_number():
            while True:
                try:
                    friend_call_number = int(input("전화번호를 입력하세요: "))
                except ValueError:
                    print("숫자가 아님.")