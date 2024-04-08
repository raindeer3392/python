class AgeInfo:
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age
    
def main():
    fa = AgeInfo()
    fa.age = 39

    #int 해서 만들어볼까

    print("아빠 : ", fa.get_age())
    print("다음해..")
    fa.up_age()
    print("아빠: ", fa.get_age())

main()