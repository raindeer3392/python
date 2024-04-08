class AgeInfo:
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age
    
def main():
    x = input("입력:")
    x = AgeInfo()
    x.age = 39

    #int 해서 만들어볼까

    print("아빠", x.get_age())
    print("다음해..")
    x.up_age()
    print("아빠", x.get_age())

main()