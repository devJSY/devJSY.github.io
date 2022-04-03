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
 
date: 2022-04-03
last_modified_at: 2022-04-03
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
    - 수학적 의미에서의 함수뜻이고 프로그래밍에선 입력이나 출력이 없는 경우도 있음
  - main 함수를 바꿀순없음
    - OS가 프로그램을 실행할떄 main부터 찾음
  - 컴파일러는 빈줄을 안읽음
  - 함수에 아무것도 안넣을때는 void를 넣거나`(void)` 아무것도 안넣음`()`

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

- **비쥬얼 스튜디오에서는 Ctrl + K → Ctrl + C 로 주석 처리** 
- **비쥬얼 스튜디오에서는 Ctrl + K → Ctrl + U 로 주석 해제**

- 주석을 달때는 내가지금 왜하는지 무엇을 하는지 기록해두기
  - 구현 단계에서는 어떻게 구현한다고 쓰는게 좋음
- 주석은 기능에 대한 설명보다는 어떻게 되어서 이 기능이 되는지 적어야함
  - `// set sight to be 0` 이렇게 코드를 봤을때 동작하는 걸 알수있는건 금지
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

> **출력결과 예측하기**

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

- `std::cout << "abc" << "\t" << "def" << std::endl;`
  - `"\t"` 탭기능임
  - \t 어떠한 기능을 의미

- `std::cout << "I love this lecture\n";// << std::endl;`
  - `\n` 은 줄바꿈 기능

- `using namespace std;` 사용하면 std 를 안붙여도됨
  - 컴파일러가 엔드라인이나 세미콜론을 만났을때 네임스페이스안에서 찾아서 컴파일해줌
- `cout << "\a";`
  - 띵동 소리를 출력해줌
- C언어에서는 `prinf("문자열");` 이렇게 출력함

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

> **입출력이 있는 예제코드**

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

> **입출력이 없는 예제코드**

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

> **함수 리턴값으로 바로 초기화 하기**

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
> **사용자로 부터 여러번 입력받아서 여러번 출력하는 코드 작성하기**

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

### **🌱 1.6 키워드와 식별자 이름짓기**

- **식별자 (Identifier)**
  - 변수의 이름, 함수의 이름, 객체의 이름을 뜻함
  - 메모리 주소를 프로그래머가 인식할수있는 문자로 바꿔줌

- **변수 이름**
  - 변수 이름은 지을때 정해져 있는 명령어는 쓰면안됨
    - main 같은것
  - 변수명은 숫자로 시작하면 안됨
  - 세미콜론(`;`), 포인터(`->`), 점(`.`) 같은걸로 하면안됨
  - **너무 길지 않으면서 의미를 충분히 표현할수있는 이름을 짓는게 좋음** 
  - 변수는 띄어쓰기가안됨
    - 대신 언더바(언더스코어) 를씀(_)
  - of 나 이런건 잘안씀 문자 수를 줄이는게 좋음
  - 대문자같은건 잘 안씀  
    - value는 매크로에 많이씀
    - 프로그래머들끼리 관습적으로 사용하는 규칙 중 하나
  - **변수명은 속해있는 소속에 규칙에 따라 맞추는게 좋음**

- **함수 이름**
  - 함수 명도 속해있는 소속에 규칙에 따라 맞추는게 좋음 
  - 첫 문자는 대문자로 많이 시작함
  - 앞에는 동사 뒤에는 명사 인게 읽기 좋음
    - 지을수 없다면 그냥 명사로 사용
  - **함수명이나 변수명이 길어지면 주석을 달기**

- 시스템 프로그래밍 할때 저수준 언어 변수명 지을때 언더바를 먼저 붙여서 사용했었음
  - 윈도우나 리눅스 개발
  - 클래스에 맴버를 앞에 꼭 붙여서 구분하는 경우가 있음
    - 클래스안에 있는 변수는 맴버 변수라고함
      - `int m_variable;` 이런식으로 지음
      - `int _variable;` 이런 경우도있음
      - `int variable_;` 구글 스타일

- **원칙은 편한거 장기적으로 같이 프로그래밍할때 의사소통이 잘되게끔 짓기** 


**연습문제**
> **올바른 변수명인지 구분하기**

```cpp
int total; // ✔️
int _orange; //❌ 언더바로 시작잘안함
int mt variable name; // ❌ 띄어쓰기 불가 언더바로 바꿔야함
int TotalCustomers; // ❌ 변수는 대문자로 시작 잘안함
int void; // ❌ void 는 사용못함
int numFruit; // ✔️ 되긴하는데 가능하면 대문자 안넣는게 타이핑하기편함
int 2some; // ❌ some 도 정해진 명령어가 사용안됨
int meters_of_pipe; // ✔️ 되긴하는데 of 나 이런걸 빼서 줄이는게 좋음
```

### **🌱 1.7 지역 범위**
- Local Scope
- 범위는 {} 중괄호 를 기준으로함
  - 중괄호를 넘어가면 사라져버림

```cpp
int main()
{
  int x(0); // x = 0;

  {
      int x = 0;
  }

  {
      int x = 1;
  }

  return 0;
}
```

- x 가 메모리공간에 할당받고 0 이라는값이 자리잡음
  - 이를 **인스턴스**라고함

- 중괄호 안에 중괄호를 넣을수있음
  - **영역을 구분하는 목적임**
  - 소스코드의  `int x(0);` 와 `int x = 1;` 의 **메모리 주소는 다름!**
  - 궁금하면 `&x` 로 주소 찍어보기

- **[참고]** 지역 변수는 영역을 벗어나면 사용 할 수 없게 됨
  - 지역 변수가  차지하고 있던 메모리는 그 지역 변수가 영역을 벗어날 때 **스택 (stack)** 메모리로 반납됨
  - 반납된 메모리는 다음 지역 변수가 사용할 수 있도록 대기함
  - 스택과 힙에서 더 자세히 다룸

```cpp
{
int main()
{
  int x(0); // x = 0;

  {
      x = 1;
  }

  return 0;
}
```

- **`{x = 1;}` 같이 지역변수에서 초기화 하지 않고 바로 인스턴스 해버리면 `int x(0);` 에서 선언된 메모리로 할당함!**

**연습문제**
> **어떤 값이 나올지 예측해보기**

```cpp
#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

using namespace std;

void dosomething(int x)
{
	x = 123;
	cout << x << endl; // #2
}

int main()
{
	int x = 0;

	cout << x << endl; // #1
	dosomething(x);
	cout << x << endl; // #3

	return 0;
}
```

**1. 0**
   - main 에서 x=0; 으로 초기화 한 값 그대로 보여주기때문에 0 

**2. 123**
   - `void dosomething(int x)` 함수에서 `x = 123;` 이라고 할당한 뒤 `cout << x << endl;` 으로 출력했으니 123 출력 

**3. 0**
  - 함수의 반환값이아닌 그대로 출력했으니 0이나옴

### **🌱 1.8 연산자와의 첫 만남**

```cpp
#include <iostream> // cout, cin, endl, ...

using namespace std;

int main()
{
  int x = 2; // x is a variavle, 2 is a literal

  int y = (x > 0) ? 1 : 2; // 3항 연산자

  cout << x + 2 << endl;

  cout << "my home" << endl;

  return 0;
}
```

**연산자 (Operators)**
- 변수로 연산 할땐 변수가 현재 가지고있는 값으로 연산함
- `=` 는 대입 연산자로 **Assignment** 라고함
- 같다라는건 `==` 로 씀

**리터럴 (Literal)**
- 문자열도 리터럴임
- 1 도 리터럴 2 도 리터럴
- 1 + 2 는 표현식임

**피연산자 (Operand)**
-  `cout << x + 2 << endl;` 중 x 나 2 같은 값을 피연산자라고함

**단항 (unary)**
- -2
- -x
  - x를 -로 바꾸는 연산자

**이항 (binary)**
-  `cout << 1 + 2 << endl;`  1 + 2 같이 피연산자(항)이 두개인 연산을 이항 연산이라고함

**삼항 (ternary)**
- 조건 연산자 (Conditional operator)는 C++언어의 유일한 삼항 연산자(Ternary operator)임
- `int y = (x > 0) ? 1 : 2;` 
  - x가 0보다 클때 (참이면) 왼쪽에있는 1을 실행시킴
  - 반대로 거짓이면 2 임




### **🌱 1.9 기본적인 서식 맞추기 (Formatting)**

- 보기좋은 코드를 보고 베끼기
- 여백을 어떻게 정하냐가 문제임
  - 여백을 너무 많이 주면 보기 불편함
  - 뭐가 됐든 최소화 하는게 제일 좋음

- 컴퓨터는 줄바꿈을 하든 말든 상관 없음

```cpp
#include <iostream> // cout, cin, endl, ...

using namespace std;

int add(int x, int y) {return x+y;}

int main()
{
    cout << "Hello, World" << "abcdef " <<
      "Hello Home" << endl;
}
```
- 줄바꿈 할때 **오퍼레이터(`<<`)를 남기는게** 프로그래머가 인식하기 좋음
- 비주얼 스튜디오 에선 `{return x+y;}` 이렇게 다닥다닥 붙어진걸 Ctrl + x → Ctrl + v 하면 `{ return x + y; }` 이렇게 자동으로 포멧팅 해줌

> **중괄호 포멧팅 스타일 1**

```cpp
int add(int x, int y) {return x+y;}
```

> **중괄호 포멧팅 스타일 2**

```cpp
int add(int x, int y) {
  return x+y;
}
```

> **중괄호 포멧팅 스타일 3**

```cpp
int add(int x, int y) 
{
  return x+y;
}
```

- 포멧팅 스타일은 그룹 규칙에 맞춰서!
  - 개인적으론 3번을 선호

- **빈칸 만들어서 띄우는걸 indenting 이라고함**
  - 스페이스 4번이 일반적
  - 탭 TAP 키 를쓰기도 함

```cpp

int main()
{
    int my_v        = 1;
    int x           = 4;
    int num_apples  = 123; 

    // this is inportant
    int x = 1 + 2;

    // this is inportant, too
    int y = 3 + 4;
}
```

- **[참고]** 하드(Hard) 코딩은 프로그래머가 코드에서 변수값을 리터럴 같이 고정된 값으로 직접 대입해주는 방식임
  - 반대로 소프트(soft) 코딩은 프로그램 실행 중에 사용자의 입력이나 외부 파일, 인터넷 통신 등으로 데이터를 가져오는 방식임

- **주석은 짧을때는 오른쪽**에 다는것이 좋고 **주석이 길면 위에** 다는게 좋음

### **🌱 1.10 선언과 정의의 분리**

```cpp
#include <iostream>

using namespace std;

int add(int a, int b); // Forward declaration

int main()
{
    cout << add(1, 2) << endl;

    return 0;
}

// Definition
int add(int a, int b)
{
  return a + b;
}
```

**선언 (Declaration)**

- **전방 선언 (Forward declaration)**
  - **프로토 타입(`int add(int a, int b);`)을 메인함수 위에 적어 줌으로써 함수를 통째로 위로 안올려도됨**


**정의 (Definition)**

- 컴파일러는 위에서 부터 순서대로 읽음
  - 메인에서 사용하는 함수가 아래에있으면 안됨 따라서 전방 선언을 해줘야함
  - 함수의 최소한의 정보를 담고있는 것을 프로토 타입이라고함
    - `int add(int a, int b);` 

- 비주얼 스튜디오에선 함수에 **마우스 우 클릭 → 선언으로 이동 버튼**으로 전방선언 쪽으로 바로갈수 있음
-  함수에 **마우스 우 클릭 → 정의로 이동 버튼**으로 정의 쪽으로 바로갈수 있음

- 비주얼 스튜디오에서 함수에 Alt + f12 또는 **마우스 우 클릭 → 정의 피킹** 버튼으로 함수 정의 코드를 읽어올수있음
  - 다른 문서에서 열때 유용함


### **🌱 1.11 헤더 파일 만들기**
- 클래스를 쪼게거나 비슷한 함수를 모아둘때 파일로 구분을함

- #pragma once
  - 헤더파일을 처음 만들면 뜨는 것
  - 전처리기의 일종

**소스.cpp**
```cpp
#include <iostream>
#include "add.h"

using namespace std;

int main()
{
    cout << add(1, 2) << endl;

    return 0;
}
```

**add.cpp 파일**
```cpp
// Definition
int add(int a, int b)
{
    return a + b;
}
```

**add.h 헤더파일**
```cpp
int add(int a, int b);
```

**`<iostream>` 에는 <> 쓰고 `#include "add.h"` 에는 "" 쓰는 이유**
- #include <iostream> 
  - 애는 표준에 들어있는 특별한거라 <> 를 사용함
  - 들어있는 파일 위치가 달라서 그럼
- #include "add.h"

**헤더파일 옮길때 해줘야하는 작업**
1. 파일을 옮김
2. 비주얼 스튜디오에서 remove 해야함
   - delete 하면 파일까지 삭제되고 remove하면 비주얼 스튜디오 내에서만 삭제됨
3. 드래그 앤 드롭으로 파일을 비주얼 스튜디오에 넣어줌 
4. 소스.cpp에서 빌드하는 하위 폴더에 주소를 적어줘야함
   - `#include "폴더이름/add.h"`

- 헤더파일에서 **함수를 정의** 해도되지만 **선언만**하고 따로 **cpp 파일 만들어서 정의** 해주는게 좋음

___
- cpp 파일은 include 할 수 있는 대상이 아닙니다. include 해야하는건 헤더파일입니다.
- 같은 프로젝트 내에 있는 cpp 파일은 어차피 include 안해도 서로 알고 있는 사이가 돼요! 빌드하면 같이 묶입니다.  즉, 같이 컴파일 됩니다.

### **🌱 1.12 헤더 가드가 필요한 이유 (Header Guardes)**

**Header Guardes**
- `#pragma once` 이게 헤더가드임
- `#pragma once` 의 뜻은 `#include "add.h"` 했을때 `add.h` 안에 있는 파일 내용을 가져온다는 뜻이 됨
- 주의할 점 include 가 중복으로 호출되면 같은 내용이 반복되어서 빌드 오류가 발생할 수 있음 

___
- cpp 파일이 없어지거나 하면 링킹에러가 발생함
- 컴파일에러는 몸체 cpp 파일과 헤더파일만 있으면 빌드는 함
  - 근데 이어지는 add.cpp 같은 파일이 없으면 링킹 에러가 발생함

- 헤더파일에서 **함수를 정의** 해도되지만 **선언만**하고 따로 **cpp 파일 만들어서 정의** 해주는게 좋음
  - 원래 이렇게하는 게좋은데 테스트하거나 뭐하거나 하다보면 헤더파일에서 **정의** 해버려서 문제가 생기는 경우가 종종 있음
  - 이때 `#pragma once` 가 있으면 문제가 안생김

> **전처리기의 표준**

```cpp
#ifndef MY_ADD
#define MY_ADD
int add(int a, int b)
{
    return a + b;
}

#endif
```
- 위 코드는 만약 정의 되어있다면 다시 include 하지 말라는 뜻임

```cpp
#pragma once 
```
- 위 코드는 전처리기의 표준 코드랑 동일한 효과임
- 헤더파일에는 다 넣기

### **🌱 1.13 네임스페이스 (Namespace)**

- 명칭 공간, 네임스페이스, Namespace 라고부름

- 중복된 함수의 이름을 그대로 가져가고 싶을때 사용

```cpp
#include <iostream>

namespace Myspacel
{
    int dosomething(int a, int b)
    {
        return a + b;
    }
}

int dosomething(int a, int b)
{
    return a * b;
}

using namespace std;

int main()
{
    cout << Myspacel::dosomething(3, 4) << endl; // 결과값 7
    cout << dosomething(3, 4) << endl; // 결과값 12

    return 0;
}
```

- namespace 를 사용하고 싶다면 `Myspacel::dosomething(3, 4)` 이런식으로 함수앞에 네임스페이스의 이름을 적어 주면 됨
- 당연히 동일한 이름의 네임스페이스를 쓰면안됨

```cpp
#include <iostream>

namespace Myspacel
{
    int dosomething(int a, int b)
    {
        return a + b;
    }
}

int dosomething1(int a, int b)
{
    return a * b;
}

using namespace std;

int main()
{
    using namespace Myspacel;
    
    dosomething(3, 4);

    // cout << Myspacel::dosomething(3, 4) << endl; // 결과값 7
    // cout << dosomething(3, 4) << endl; // 결과값 12

    return 0;
}
```
- `Myspacel::` 를 없애고 싶다면 `using namespace Myspacel;` 를 붙이고 쓰면 생략이 됨

> **네임스페이스 안에 네임스페이스 사용법**

```cpp
#include <iostream>

namespace Myspacel
{
    namespace InnerSpace
    {
        int my_function()
        {
            return 0;
        }
    }

    int dosomething(int a, int b)
    {
        return a + b;
    }
}

int dosomething1(int a, int b)
{
    return a * b;
}

using namespace std;

int main()
{
    using namespace Myspacel::InnerSpace;
    
    my_function();

    // cout << Myspacel::dosomething(3, 4) << endl; // 결과값 7
    // cout << dosomething(3, 4) << endl; // 결과값 12

    return 0;
}
```
- `using namespace Myspacel::InnerSpace;` 이런식으로 접근 하여 동일하게 사용하면됨

**`#include <iostream>` 속 `using namespace std` 찾기**
- `#include <iostream>` 문서안에 `_STD_BEGIN` 이 내부에 `using namespace std` 가 존재함

### **🌱 1.14 전처리기와의 첫 만남 (Preprocessor)**

```cpp
#include <iostream>
#define MAX(a, b) (((a)>(b)) ? (a) : (b))

using namespace std;

int main()
{
	cout << MAX(1 + 3, 2) << endl;
}
```

- `#include <iostream>`
- `#define MY_NUMBER 9` 
  - 매크로 라고함
  - 거의 대문자로씀
  - `MY_NUMBER` 를 만나면 `9`로 바꿔버리는것
  - `9` 대신 `Hello, World` 같은것도 됨
  - 요즘은 매크로 많이 안씀

> **MAX 값 찾아주는 라이브러리** `#include <algorithm>`

```cpp
#include <iostream>
#include <algorithm>
//#define MAX(a, b) (((a)>(b)) ? (a) : (b))

using namespace std;

int main()
{
	/*cout << MAX(1 + 3, 2) << endl;*/
	cout << std::max(1 + 3, 2) << endl;
}
```

> **전처리기**

```cpp
#include <iostream>
#include <algorithm>
#define LIKE_APPLE
using namespace std;

int main()
{
#ifdef LIKE_APPLE
	
	cout << "Apple " << endl;
#endif

#ifndef LIKE_APPLE

	cout << "Orage " << endl;
#endif
	
	return 0;
}
```
- 전처리기란 빌드 들어가기 전에 한다는 의미
  - 빌드 할때 결정됨
  - 윈도우인지 리눅스인지 결정할때
  - 멀티 플렛폼 할때 사용함
- `#ifdef ~ #endif` 정의가 되있으면 실행
- `#ifndef ~ #endif` 정의가 안되있으면 실행

**else문 처리**
```cpp
#include <iostream>
#include <algorithm>
#define LIKE_APPLE
using namespace std;

int main()
{
#ifdef LIKE_APPLE
	
	cout << "Apple " << endl;
#else
	cout << "Orage " << endl;
#endif

}
```
- `# else` 기능도 있음

- 기본적으로 `#define MY_NUMBER 9` 에서는 `MY_NUMBER` 를 만나면 `9`로 바꿔버리는것이지만 **전처리기 에서는 그렇게 동작안함**

- `#define` 는 **정의 되어있는 파일** 에만 적용이 됨


# 😊 배우게 된 점
2022-04-03 TIL - 챕터 1이 끝났다 강의 듣는 내용들은 다 이해가 되는데 손에 익거나 실제로 사용할려면 여러번 만져봐야할것같다 우선은 **지식**을 쌓는 과정이라고 생각하고 하나하나 필기해뒀다가 나중에 틈틈히 꺼내보면서 다시 상기시키면서 **정보**로 만들어야겠다

- 강의가 파트 별로 잘쪼게져 있어서 한 챕터의 한파트 듣고 쉬고 하기가 좋고 구분하기도 매우 편해서 나중에 복습할때도 좋을 것같다!

# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)