#오늘의 강의 : 모듈(라이브러리)과 딕셔너리(중괄호)

def Hu_R_U(name, age):
    print("이름:",name)
    print("나이:",age)

Hu_R_U("김감자" ,20)
Hu_R_U(name="김감자" ,age=20) #변수지정으로 순서를 섞어도 사용가능

def Hu_R_U(name, age):
    print("이름:",name, sep='') #변수간 텍스트
    print("나이:",age, end=' \nnone') #함수끝 텍스트 
    
Hu_R_U("김감자" ,20)

def Hu_R_U(name, age = 0): #함수의 변수 기본값을 지정할수 있음 (없어도 이미 값을 지정해서 실행이 될수 있도록 해줌)
    print("이름:",name)
    print("나이:",age)

Hu_R_U("김감자")