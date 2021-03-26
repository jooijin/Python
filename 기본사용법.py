# 기본 출력
a = 2

b = 3

c = 1+2j

print(a, b, b/a)

s1 = "Life is too short, You need Python"

s2 = "Python's favorite food is perl" # 문자열 안에 작은 따옴표가 있다면 큰 따옴표로 감싸기 (반대 경우에는 따옴표도 반대로)

multiline = "Life is too short, You need Python\nPython's favorite food is perl"

# 문자열 더하기
print(s1+"\n"+s2)
print(multiline)

# 문자열 곱하기
print("="*50)
print("My Program")
print("="*50)

# 인덱싱
print(s1[3])
print(s1[-1])
print(s1[-2])
print(s1[-0])

# 슬라이싱: 시작번호<=문자열인덱스<끝번호 !!끝번호는 포함 안됨에 유의!!
print(s1[0:4])
print(s1[12:17])
print(s1[19:])
print(s1[:17])
print(s1[:])
print(s1[19:-7])

# 포매팅
apple = "I eat %d apples" % 3
print(apple)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))

print("%10s" % "hi")
print("%-10sjane" % "hi")
print("%10.4f" % 4.1234567)

# 문자열 관련 함수들
print(s1.count('y'))
print(s1.find('Python'))
print(s1.find('Java'))

print(s1.index('P'))
a = ","
print(a.join(s1))
print(s1.upper())
print(s1.lower())

# lstrip, rstrip, strip 공백 지워줌

a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())
print(a.split('too'))
