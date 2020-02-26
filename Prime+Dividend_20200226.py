# Prime Number Distinguishment Program & Divisor Displayer ver 1.0
# 소수 판별기 및 약수 계산기 ver 1.0
# Developed by bcchickadee, Feb 26 2020

print('Prime Number Distinguishment Program & Divisor Displayer')
print('소수 판별기 및 약수 계산기')
print('ver 1.0')
print('Developed by bcchickadee - Feb 26 2020\n\n')

# Divisor Calculation Function Definition
# 약수 계산 함수 정의

def DivisorCalculationProcess(TargetInteger):
    for Dividend in range(1, int(TargetInteger)+1):
        if round(int(TargetInteger) / float(Dividend))==int(TargetInteger) / float(Dividend):
            print(Dividend)
        # Displays Divisor for when calculation result exhibits a natural number when divided by the Dividend
        # 자연수로 나누어떨어지는 Dividend에 대하여 그 Dividend 값을 표시

# Prime Number Distinguishment Process Function Definition
# 소수 판별 함수 정의

DivisorList=[]
# List of Divisors, automatically added to the list by the function below
# 함수로부터 산출되는 약수들을 자동으로 담을 목록

def PrimeNumberDistinguishmentProcess(TargetInteger):
    for Dividend in range(1, int(TargetInteger)+1):
        if round(int(TargetInteger) / float(Dividend))==int(TargetInteger) / float(Dividend):
            DivisorList.append(Dividend)
        # Adds Divisors to the DivisorList list
        # 약수들을 DivisorList 목록에 추가합니다.
    if len(DivisorList)==2:
        print('이 수는 소수입니다.\n')
        DivisorList.clear()
    # If there are 2 divisors, then it is a prime number - therefore, the function prints a message indicating that it is a prime number.
    # 약수가 2개이면 그 수는 소수이므로, 소수라는 메시지가 표시됩니다.
    elif len(DivisorList)==1:
        print('이 수는 1로, 소수와 합성수 모두에 해당되지 않는 수입니다.\n')
        DivisorList.clear()
    # If there is 1 divisor, then that number is 1 - therefore, the function prints a message indicating that it is 1.
    # 약수가 1개이면 그 수는 1이므로, 1이라는 메시지가 표시됩니다.
    elif len(DivisorList)!=1 or 2:
        print('이 수는 합성수입니다.\n')
        DivisorList.clear()
    # If there are more than 2 divisors, that number is a composite number - therefore, the function prints a message indicating that it is a composite number.
    # 3개 이상의 약수가 있으면 그 수는 합성수이므로, 합성수라는 메시지가 표시됩니다.

# Initial Integer Input Phase
# 초기 타깃 자연수 입력 과정
while True:
    TargetInteger=input('판별하고자 하는 자연수를 입력하여 주십시오.\n프로그램을 종료하시려면 "quit"을 입력하십시오.\n주의: 매우 큰 자연수에 대해서 결과값을 표시하기 어렵습니다.\n\n')
    if str(TargetInteger)=='quit':
        quit()
    # Exit Program Option when the user inputs string 'quit'
    # 사용자가 'quit'라고 입력할 때 프로그램을 종료할 수 있음.
    elif float(TargetInteger)<=0:
        print('오류: 자연수를 입력해야 합니다.\n')
    # Calculation unavaliable for negative numbers
    # 음수는 입력 불가
    elif round(float(TargetInteger), 0)==float(TargetInteger):
        print(TargetInteger+'의 양의 약수는:\n')
        DivisorCalculationProcess(TargetInteger)
        print('입니다.\n')
        PrimeNumberDistinguishmentProcess(TargetInteger)
        print('\n================================\n\n')
    # Calculation available only when user enters a natural number
    # 자연수일 때만 계산을 실행함.
    else:
        print('오류: 자연수를 입력해야 합니다.\n')
    # Other numbers are not accepted, and exhibits an error
    # 올바르지 않은 형식의 다른 숫자는 거부되고 에러 메시지가 표시됨.



