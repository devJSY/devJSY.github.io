---
published: true
title:  "따라하며 배우는 C++ Section 1. C++의 기초적인 사용법"
excerpt: ""

categories:
  - 따배씨++
tags:
  - [C++]

toc: true
toc_sticky: true
 
date: 2022-04-02
last_modified_at: 2022-04-02
---

# 🤔 학습목표
- 따라하며 배우는 C++ Section 1. C++의 기초적인 사용법

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 1. C++의 기초적인 사용법**

### **🌱 1.1 프로그램의 구조**

- 표현식 (Expressions)
- 명령문 (Statements)
- 함수 (Functions)
- 라이브러리, 표준 라이브러리

- 숫자 0 은 0안에 막대기가 그어짐 O랑 구분할때좋음
- 운영체제가 실행시켜주는것
- 프로그램의 최소단위를 함수라고함
  - 함수: 입력이 주어지면 함수에서 처리를 해서 출력이 나오는것
  - main 함수를 바꿀순없음
    - OS가 프로그램을 실행할떄 main부터 찾음
  - 컴파일러는 빈줄을 안읽음
  - 함수에 아무것도 안넣을때는 void 나 아무것도 안넣음

```cpp
#include <iostream>

int main(void)
{
	int x = 2;
	x = 5;
	int y = x + 3;

	std::cout << y << std::endl;

	return 0;
}
```

- return 은 main 함수의 출력값을 돌려주는 것
  - 리턴 스테이트먼트 라고불름
  - 관습적으로 명령문이라고 부름
  - C나 C++에서는 문장의 끝을 표현하는걸 ; 로 표현함 

- 1+1 이런 요소들을 Expressions 이라고함
- int x;
  - int 라는 정수형 데이터를 x라는 이름으로 메모리를 할당하는것

- 숫자 2 나 5 이런것들을 리터럴 (literal) 이라고 부름

- iostream
  - 입출력을 가능하게 해주는 기능을 포함 시킴
- `#include` 이 붙는걸 전처리기 (preprocessor directive) 라고부름
- 네임스페이스
  - 비슷한 기능들을 하는 걸 묶어놓거나
  - 이름이 겹칠수 있는것들을 다른공간에 모아두는것

- :: 네임스페이스 안에 들어있는 cout에 접근 하는것
- << 아웃풋 오퍼레이터 연산자다 라는 것
- `std::endl` 띄어 쓰기됨

**문제**
- **Q.표현식과 명령문의 차이는 뭘까?**
  - A. 
    - 표현식 (Expression)은 ‘수식’이라는 뜻으로 하나 이상의 값으로 표현(reduce)될 수 있는 코드를 말한다 `1+1`이나 `2+5` 등등
    - 명령문(statement)는 ‘진술’, ‘서술’의 의미로 프로그래밍에서는 실행가능한(executable) 최소의 독립적인 코드 조각을 일컫는다 `return 3` 같은 것들
    -  **expression은 statement의 부분집합이다**
- **Q. 함수와 라이브러리의 차이는 뭘까?**
  - A. 
    - 함수란 어떠한 기능을 수행해주는 것 입출력이 없을수도있음
    - 라이브러리는 기존에 다른 프로그래머들이 만들어놓은 함수의 집합체 
- **Q. C++에서 문장을 끝내는 기호는 뭘까?**
  - A. 세미콜론 `;`
- **Q. 문법 오류란 무엇인가?**
  - A. 컴파일러가 이해할수 없는 오류를 말함

### **🌱 1.2 주석 comments**

**주석 잘 다는 방법**
- 주석이란 컴파일러가 코드를 무시하게 하는 것
- C 나 C++ 에서 주석다는법
  - `//x = 5;`
  - `/*x = 5;*/`

- **비쥬얼 스튜디오에서는 Ctrl + K → Ctrl + C 로 주석 처리 할수있음** 
- **비쥬얼 스튜디오에서는 Ctrl + K → Ctrl + U 로 주석 처리 할수있음**

- 주석을 달때는 내가지금 왜하는지 무엇을 하는지 기록해두기
  - 구현 단계에서는 어떻게 구현한다고 쓰는게 좋음
- 주석은 기능에 대한 설명보다는 어떻게 되어서 이 기능이 되는지 적어야함
  - `// set sight to be 0` 이런거 금지
- 내가 헷갈릴 만한것들에 주석 달기
```cpp
	int sight = 10;

	//...

	// 마법의 물약을 먹어서 시야 거리가 0
	// set sight to be 0
	sight = 0;
```

### **🌱 1.3 변수와의 첫 만남**
- 객체 (object)
  - 메모리에 저장이 되어있는 어떠한 정보
- 변수 (variavles)
  - 메모리에 담겨있는 객체의 이름
- Left-values 과 Right-values
  - L-Values
  - R-Values
  - 구분하는 기준도 메모리 주소를 프로그래머가 직접적으로 접근할수 있는지 없는지
- 초기화(initialization)와 대입(assignment)
- 초기화를 안 했을 때의 문제점
- 컴퓨터 프로그래밍은 정보를 다루는것

**변수의 종류**

**int** 
  - integer의 약자
  - `int x = 123;`
    - x라는 변수를 선언했다 라는 뜻
    - x라는 변수이름이 가르키고있는 메모리 공간에 123이라는 정수를 저장 한다 라는 의미
  - `int x; x = 123;`
  - `=` 을 assignment 라고함 대입에 가까움
  - `&` 를 ampersand 라고함
    - `std::cout << &x << std::endl;` 내부적으로 x의 메모리 주소를 표현할때 &을 사용함
  - `x = 123`
    - x가 L-values
    - 123이 R-values
  - `x = x + 2;`
    - 오른쪽에 있는 x는 변수로써 작동하는게 아닌 현재 가지고있는 값이 R-values 가됨
  - `int x;` 이렇게 선언만하고 초기화`X=3`를 안해주면 Warring 이 발생함
  - 릴리즈모드에서도 워닝은 뜸 OS 에서 자기 맘대로 값을 넣음 변수는 꼭 초기화하기

- **런타임에러**
  - 메모리에 접근할때 뭔가 석연찮을때 뜸
  - OS 에서 경고해주는것


```cpp
#include <iostream>

int main(void)
{
	int x = 123; // initaliztion
	x = 5; // assignment

	std::cout << &x << std::endl;
	return 0;
}
```
- `int x = 123` 
  - 메모리 자리를 할당받을때 123을 바로 넣어버리는 것(initaliztion) ,assignment 랑 다름 꼭 구분하기
  - `int x(123)` 이렇게 사용할수도 있음 

**출력결과 예측하기**
```cpp
#include <iostream>

int main(void)
{
	int x = 1;
	x = x + 2;
	std::cout << x << std::endl; //#1

	int y = x;
	std::cout << y << std::endl; //#2

	//is (x + y) ;-value or r-value ?
	std::cout << x + y << std::endl; //#3

	std::cout << x << std::endl; //#4

	int z;
	std::cout << z << std::endl; //#1

	return 0;
}
```
1. 3
2. 3
3. 6
4. 3
5. 0
    - 초기화를 안해줘서 os에서 임의로 할당할텐데 vs에서 에러가 떠서 빌드 자체가 안됨 

### **🌱 1.4 입출력 스트림과의 첫 만남 cin,cout**

**cin**
- 콘솔 인을 의미함
- `std::cin >> x;` 이런식으로 사용함
- 정수형데이터에 큰값을 넣으면 정수형데이터의 최대 데이터가 출력됨

```cpp
#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

int main(void)
{
	using namespace std;

	int x = 1;

	cout << "Before your input, x was" << x << endl;

	cin >> x;

	cout << "Your input is" << x << endl;

	return 0;
}
```

**cout**
- 콘솔 아웃을 의미함
- `#include <iostream> // cout, cin, endl, ...`
  - 인풋 아웃풋 스트림을 포함(include) 해줘야 사용가능
  - `std::cout`
    - std 는 네임 스페이스 안에 정의 되어있는 cout을 사용하기 위해서 :: 를 사용함 
  - `std::cout << "I love this lecture" << std::endl;`
    - << 를 아웃풋 오퍼레이터 라고함

- std::cout << "abc" << "\t" << "def" << std::endl;
  - `"\t"` 탭기능임
  - \t 어떠한 기능을 의미

- std::cout << "I love this lecture\n";// << std::endl;
  - `\n` 은 줄바꿈 기능

- `using namespace std;` 사용하면 std 를 안붙여도됨
  - 컴파일러가 엔드라인이나 세미콜론을 만났을때 네임스페이스안에서 찾아서 컴파일해줌
- `cout << "\a";`
  - 띵동 소리를 출력해줌
- C언어에서는 prinf("문자열"); 이렇게 출력함

```cpp
#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

int main(void)
{
	using namespace std;
	int x = 1024;
	double pi = 3.141592;

	cout << "I love this lecture\n";// << std::endl;
	cout << "x is" << x << "pi is"<< pi << std::endl;

	cout << "abc" << "\t" << "def" << std::endl;
	cout << "ab" << "\t" << "cdef" << std::endl;

	cout << "\a";
	return 0;
}
```

**endl**
- 엔드라인을 의미함

### **🌱 1.5 함수와의 첫 만남**

**입출력이 있는 예제코드1**

```cpp
#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

using namespace std;

int addTwoNumbers(int num_a, int num_b)
{
	int sum = num_a + num_b;

	return sum;
}

int main(void)
{

	cout << addTwoNumbers(1, 2) << endl;
	cout << addTwoNumbers(3, 4) << endl;
	cout << addTwoNumbers(8, 13) << endl;

	return 0;
}
```

**입출력이 없는 예제코드**
```cpp
#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

using namespace std;

void printHelloWorld()
{
	cout << "Hello World" << endl;

	return;

	cout << "Hello World" << endl; // 실행되지않음
}
int main(void)
{
	printHelloWorld();

	return 0;
}
}
```

**함수 리턴값으로 바로 초기화 하기**
```cpp
#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

using namespace std;

int addTwoNumbers(int a, int b)
{
	return a + b;
}


int main(void)
{
	int sum = addTwoNumbers(1, 2);

	return 0;
}

```
**함수 (Function)**
- 한가지 패턴이 여러번 나타나면 함수로 구분
- 함수의 자료형과 리턴 자료형은 같아야함 

**리턴값 (return values)**
- 함수에서 계산된 값을 돌려주는 값
- `return 0;`이 리턴값임


**매개변수 (parameters)**
- 함수에 들어와서 사용되는값
- `int addTwoNumbers(int num_a, int num_b)` 중 `(int num_a, int num_b)`가 매개변수임

**인수 (arguments)**
- 함수를 호출,콜 할때 사용되는 값 `cout << addTwoNumbers(1, 2) << endl;` 중 `(1, 2)` 가 인수임 

>**함수명에 마우스 우클릭 → 이름바꾸기(Ctrl + R, Ctrl + R) 눌러서 이름 전체 바꾸기 가능**
- 비쥬얼 스튜디오에서 숫자 왼쪽에 브레이크 포인트 찍어서 확인 가능, F9눌러서 찍어도됨
    - F10, F11 으로 한단계 씩 넘어가며 확인가능 
    - 한단계 씩 넘어가면서 변수에 마우스 갖다대면 현재 변수값이 뜸

- 출력값이 없는 함수에는 void 값을 넣어줌
  - `void printHelloWorld(void)` 
    - `(void)` 는 `()` 처럼 아무것도 안넣어도됨
    - 출력해줄 값이 없다면 `return;` 을 넣어도됨
    - return 값을 만나면 바로 값을 반환해주기 때문에 return 아래의 구문은 실행되지 않음

- 함수 끼리 호출 가능
  - **C++ 은 함수안에서 함수를 정의 할 수 없음!**

**연습문제**
- 사용자로 부터 여러번 입력받아서 여러번 출력하는 코드 작성하기

```cpp
#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

using namespace std;

int addTwoNumbers(int a, int b)
{
	return a + b;
}

int main(void)
{
	int a;
	int b;
	cin >> a;
	cin >> b;
	cout << addTwoNumbers(a, b) << endl;

	return 0;
}
```





### **🌱 1.**
### **🌱 1.**
### **🌱 1.**
### **🌱 1.**


# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)