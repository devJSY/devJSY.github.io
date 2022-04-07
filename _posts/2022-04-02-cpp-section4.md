---
published: true
title:  "따라하며 배우는 C++ Section 4. 변수 범위와 더 다양한 변수형"
excerpt: ""

categories:
  - 따배씨++
tags:
  - [C++]

toc: true
toc_sticky: true
 
date: 2022-04-06
last_modified_at: 2022-04-06
---

# 🤔 학습목표
- 따라하며 배우는 C++ Section 4. 변수 범위와 더 다양한 변수형

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 4. 변수 범위와 더 다양한 변수형**

### **🌱 4.1  지역 변수, 범위, 지속기간**

**범위 (Scope)**
- 변수를 본다라는 표현을 많이씀

- 지속기간 (Duration)
  - 다쓴 메모리를 반납한다는 의미 인데 동적할당 파트에서 다시다룸

___

**블럭의 범위**

```cpp
#include <iostream>

using namespace std;


int main()
{

	apple = 1; // 사용 불가능

	int apple = 5;

	apple = 1; // 사용 가능


	return 0;
}

apple = 3; // 사용 불가능
```

- 변수는 해당 블럭 `{}` 을 벗어나면 없는걸로 인식함

___

**블럭의 적용 범위**

```cpp
#include <iostream>

using namespace std;


int main()
{
	int apple = 5;

	cout << apple << endl; // 5

	{
		apple = 1; 

		cout << apple << endl; // 1
	}

	cout << apple << endl; // 1

	return 0;
}

```
- 더큰 블럭에서 선언된 변수는 작은 변수에서 사용 가능

___

**네임 하이딩**

```cpp
#include <iostream>

using namespace std;


int main()
{
	int apple = 5;

	cout << apple << endl; // 5

	{
		int apple = 1; 

		cout << apple << endl; // 1
	}

	cout << apple << endl; // 5

	return 0;
}

```

- 큰블럭과 작은블럭사이에 선언된 변수명이 같다면 큰블럭은 하이딩 가려져버림
- 이름은 같지만 완전다른 변수임
  - 가급적이면 변수명 다르게 짓기
- 현대적 프로그래밍
  - 가급적 변수가 사용되는 범위를 줄이기위해서 `{}` 으로 쪼겜
    - 객체지향 프로그래밍의 철학임

___

**이름이 동일한 함수 나누기**

```cpp
#include <iostream>

namespace work1
{
	int a = 1;

	void dosomthing() // #1
	{
		a += 3;
	}
}

namespace work2
{
	int a = 1;

	void dosomthing() // #2
	{
		a += 5;
	}
}


using namespace std;


int main()
{
	work1::a;
	work1::dosomthing();

	work2::a;
	work2::dosomthing();

	return 0;
}
```

- 함수 선언은 여러곳에 해도되는데 정의는 한번만 해야함
  - 메모리 할당하는 공간이 하나임
- 함수에 파라메타만 다른 함수는 다른함수로 취급됨
- #1 과 #2는 서로다른 함수임
- 같은 이름함수 쪼겔려면 함수를 `{}` 로 감싸서 나누고 **namespace** 로 구분해주기
- main함수 밖에 선언된함수를 **전역 함수** 라고함
- `::` 영역, 범위 결정 연산자

___

**c17 에 추가된 내용**

```cpp
#include <iostream>

namespace work1
{
	namespace work11
	{ 
		int a = 1;

		void dosomthing() // #1
		{
			a += 3;
		}
	}
}

namespace work2::work22
{
	int a = 1;

	void dosomthing() // #2
	{
		a += 5;
	}
}


using namespace std;


int main()
{
	work1::work11::a;
	work1::work11::dosomthing();

	work2::work22::a;
	work2::work22::dosomthing();

	return 0;
}
```

- 예전엔 #1 처럼 namespace 안에 namespace 를 만들었음
- C++ 17 부터는 #2 처럼 `::`로 만들 수 있음
- 되도록이면 적게 사용하기

### **🌱 전역 변수, 정적 변수, 내부 연결,외부 연결**

**전역 변수(Gloval Variable)**
- 장기적으로 지역변수를 많이 쓰게됨
- 다른파일로 넘어가도 사용할 수 있음
- 가급적 사용을 안하는게 좋음
- 컴파일러가 Obj 파일 만들고 링킹해서 exe 파일을만듬

```cpp
#include <iostream>

using namespace std;

int a = 1; // 전역 변수 선언

void doSomething()
{
	++a;
	cout << a << endl;
}

int main()
{
	doSomething(); // 2
	doSomething(); // 3
	doSomething(); // 4
	doSomething(); // 5
	doSomething(); // 6
	doSomething(); // 7

	return 0;
}
```

- 전역변수는 뒤로가면 위험하고 가급적이면 잘안쓰게됨
  - 관리,추적이 힘듬
- 함수는 설계할때 파라메타(`int a`)를 넣어서 알아보기 편하게 해놓기
- 전역변수이름을 `g_a` 같이 시인성 좋게 짓기
- 객체지향을 사용하여 전역변수를 사용안하는게 제일좋음


___

**전역 변수, 지역 변수 선언**

```cpp
#include <iostream>

using namespace std;

int value = 123;

int main()
{
	cout << value << endl; // 123

	int value = 1; // {} 지역 변수 

	cout << ::value << endl; // 123
	cout << value << endl; // 1

	return 0;
}

```

- `{}` 안에 선언된 변수는 중괄호를 벗어나는 순간 메모리가 os로 반납되고 더이상 사용하거나 접근할 수 없음 스코프도 제한됨 듀레이션도 제한됨

- `::` 영역 연산자 를 사용하여 다른 영역에 정의된 변수에 접근하여 사용할 수 있음

___

**정적 변수 (Static Variable)**

**정적 변수 선언**

```cpp
#include <iostream>

using namespace std;

void doSomething()
{
	// int a =1;
	static int a; // 이렇게는 못씀
	static int a = 1; // 정적 변수 선언
	++a;
	cout << a << endl;
}

int main()
{
	doSomething(); // 2
	doSomething(); // 3
	doSomething(); // 4
	doSomething(); // 5
	doSomething(); // 6
	doSomething(); // 7

	return 0;
}
```

- 전역 변수로 선언했을때의 차이
  - static: 변수 a가 os로 부터 받은 메모리가 static 이라는 뜻임
  - `int a =1;` 같은 경우에는 메모리를 가졌다 반납했다를 반복함
  - `static int a = 1;` 이영역에 변수가 선언할때 같은 메모리를 사용하고 초기화를 한번밖에 안함 
  - static으로 선언된 변수는 한번저장했다가 다음번에 똑같이 static 변수 선언이 되었을때 건너뛰어버림
  - 처음에 static 변수를 초기화를 무조건 해야함 `static int a;` 못씀
  - 같은 메모리를 재사용한다는뜻 
- C 프로그래머 언어를 만든사람의 입장에서 봐야함
- 함수가 몇번호출되는지 세볼때 자주 사용함
- 일반적인 경우 주의해서 사용하기
- 객체지향때 **메모리 관점**에서 생각해보기

___

**내부 연결 (Internal Linkage)**
  - 지역 변수 같은 경우 Linkage가 없다고 표현됨
  - 변수를 선언했을때 이파일안에서는 사용할수 있는 것
  - 개별 cpp파일 안에서만 전역으로 작동하는 전역변수를 의미함
  - 전역변수 선언시 **static** 을 써놓으면 다른 cpp파일에서 접근을 못하게 됨

**내부 연결 선언**

```cpp
#include <iostream>

using namespace std;

static int a = 1; // 내부 연결 전역 변수 선언

void doSomething()
{
}

int main()
{
	return 0;
}
```

___

**외부 연결 (External Linkage)**
  - 한 cpp 에서 선언한 변수를 여러개의 cpp 파일에서 사용할수 있는 것
  - cpp 파일을 직접 include 를 하는 경우도 있긴한데 거의 안함
    - 헤더파일을 inlcue 
    - 전방선언을 하면 링킹할때 갖다 붙이라는 뜻

```cpp
#include <iostream>

using namespace std;

extern int a;

extern void doSomething();

int main()
{
	doSomething();

	return 0;
}

```

- `extern void doSomething();` extern를 생략해서 많이씀
  - 어딘가의 `doSomething` 함수의 정의가 있다는 뜻임
  - 다른곳에서 쓰는 변수는 extern 표시해주기
- 컴파일 할때는 빌드가 잘되는데 링킹할때 a의 메모리 정의된걸 못찾으면 링킹에러가 발생함
- 전역변수가 여러군데에서 초기화하면 링킹 할때 같은 메모리에 여러번 초기화 된걸로 판단되어 링킹에러가 발생함
- 상수를 전역상수로 사용하는 경우가많음
  - pi, gravity 등등...
- 보통 상수들은 묶여있음
- 헤더파일에서 include 해오면 **메모리 주소가 다름** 즉 cpp 파일수 만큼 메모리를 잡아먹음
  - 방지하는 방법: 초기화하지말고 **선언만 하기**

___

**Linking** 
  - cpp파일 여러개를 각각 컴파일애서 obj파일을 만들어서 엮어서 링커가 exe파일을 만드는 것 

**Lnkage**
  - 연결 그자체를 의미함 
  - 링킹 단계에서 로컬 변수끼리 엮을 필요는 없음 각 cpp파일 안에서 처리하면됨
  - 따라서 로컬 변수는 Linkage가 없음

___

**선언 예제 코드**

```cpp
#include <iostream>

using namespace std;

int g_x; // external linkage
static int g_x // internal linkage
const int g_x; // X

extern int g_z;
extern const int g_z;

int g_y(1);
static int g_y(1);
const int g_y(1);

extern int g_w(1);
extern const int g_w(1);

int main()
{

	return 0;
}
```

### **🌱 4.3 Using문과 모호성(Ambiguity)**

- 동일한 이름을 가진 변수나 함수를 여러군데에서 사용하는 경우가 많음
  - class나 namespace 
  - 객체지향 할때는 권장되는 경우가 있음
  - 컴파일러가 어떤걸 사용해야하는지 몰라서 뜨는 에러를 모호성이라고함
    - 이를 해결해주는게 Using 임

```cpp
#include <iostream>

int main()
{
	using namespace std;
	using std::cout; // cout 만 가져오기

	cout << "Hello " << endl; // std::cout, std::endl; 

	return 0;
}
```

- cout, endl; 사용할떄 `iostream` 안에 `namespace` 안에 `std` 라이브러리를 사용하는것을 `using namespace std` 로 std 적는 것을 생략 할 수 있음
- `using std::cout` cout 만 가져올수도 있음
  - 중간에 namespace 를 적으면 에러뜸 
  - 대부분의 경우에는 std를 한번에 가져옴

___

**영역 지정 연산자**

```cpp
#include <iostream>

namespace a
{
	int my_var(20);
	int my_a(123);
}

namespace b
{
	int my_var(20);
	int my_b(456);
}

int main()
{
	using namespace std;

	using namespace a;
	using namespace b;
	
	cout << a::my_var << endl; // 영역 지정 연산자
	cout << b::my_var << endl; // 영역 지정 연산자
	cout << my_a << endl;
	cout << my_b << endl;

	return 0;
}
```

- namespace 에 동일한 이름을가진 연산자라면 `::` 영역 지정 연산자를 사용하여 선언해줘야 사용할 수 있음
- 동일한 이름을 가지지 않은 연산자라면 `::` 을 사용 안해도됨

___

**`{}`로 구분하기**

**잘못된 예제**

```cpp
#include <iostream>

namespace a
{
	int my_var(20);
	int my_a(123);
}

namespace b
{
	int my_var(20);
	int my_b(456);
}

int main()
{
	using namespace std;

	using namespace b;
	
	cout << my_var << endl; // b namespace 값 출력

	{
		using namespace a;

		cout << my_var << endl; // 에러발생
	}

	cout << my_var << endl; // b namespace 값 출력

	return 0;
}
```

- `cout << my_var << endl; // 에러발생` 에러발생하는 이유는 namespace a와 b를 동시에 영향을 받기 때문에 에러가 뜨는것

**올바른 예제**
```cpp
#include <iostream>

namespace a
{
	int my_var(20);
	int my_a(123);
}

namespace b
{
	int my_var(20);
	int my_b(456);
}

int main()
{
	using namespace std;

	{
		using namespace a;

		cout << my_var << endl;
	}

	{
		using namespace b;

		cout << my_var << endl; 
	}

	return 0;
}
```

- namespace 영역을 쪼게서 `{}`를 나누어 각각 영향을 받도록 해줘야함

___

- 헤더파일에 namespace를 넣어버리면 모든 cpp파일에 영향이가니까 위험할 수 있음
  - 헤더파일에 넣는 건 좋지않고 가급적 cpp파일에 넣는게 좋음
  - 가급적 적은 범위에 영향을 주는게 좋음
  - 객체지향할때 좋음
- std 라이브러리 안에 count 가 있으므로 주의


### **🌱 4.4 auto 키워드와 자료형 추론(Type Inference)**

- auto 키워드는 자료형 추론을 통하여 자료형을 정해줌


- 형 추론: 자료형을 상황에따라 스스로 정해주고 만드는것
  - auto 키워드사용
  - 초기화 할때 사용함
  - 초기화를 하지않으면 사용할 수 없음

___

**auto 키워드 초기화 예제**

```cpp
#include <iostream>


int main()
{
	using namespace std;

	auto a = 123; // int
	auto b = 123.0; // double
	auto c = 1 + 2.0; // double

	return 0;
}
```

___

**함수의 리턴값에 대하여 auto 사용**

```cpp
#include <iostream>

auto add(int x, int y)
{
	return x + double(y);
}
int main()
{
	using namespace std;

	auto a = 123; // int
	auto b = 123.0; // double
	auto c = 1 + 2.0; // double
	auto result = add(1, 2); // double 3

	return 0;
}
```

- 함수의 파라메타는 auto가 불가능함 
  - template 를 사용하는 방법이 있음
- auto는 어떠어떠한 계산과정을 통해서 **데이터타입을 지정**할때 사용하는 것

___

**또다른 함수 리턴값 자료형 선언방법**

```cpp
#include <iostream>

auto add(int x, int y) -> int;
auto add(int x, int y) -> double;

auto add(int x, int y) -> int
{
	return x + y;
}

auto add(int x, int y) -> double
{
	return x + y;
}

int main()
{
	using namespace std;

	auto a = 123; // int
	auto b = 123.0; // double
	auto c = 1 + 2.0; // double
	auto result = add(1, 2); // int 3

	return 0;
}
```
- `auto add(int x, int y) -> int` 이런식으로도 리턴값을 지정할 수도 있음
  - 한눈에보기 편함
  - `int add(int x, int y)` 당연히 이렇게 사용하는것도 맞음

### **🌱 4.5 형변환 (Type conversion)**

- 형변환: 다양한 데이터 타입끼리 변환하는 것

___

**암시적 형변환** 
  - lmplicit Type Conversion (coersion)
  - 컴파일러가 알아서 강제로 형변환 시키는 것

```cpp
#include <iostream>
#include <typeinfo>
int main()
{
	using namespace std;

	int a = 123.0; // 암시적 형변환

	cout << typeid(a).name() << endl; 

	return 0;
}
```

- 컴파일러가 형변환 해줄때 비트단위에서 복붙하는게 아닌 뭔가 변화를 시켜주고 있다는것
- 규칙이 있음
  - auto 자동 형 추론시 유용함
___

**데이터 타입 확인하기**

```cpp
#include <iostream>
#include <typeinfo>
int main()
{
	using namespace std;

	cout << typeid(4.0).name() << endl; // double

	int a = 123;

	cout << typeid(a).name() << endl; // int

	return 0;
}
```

- `#include <typeinfo>` 라이브러리
  -  `typeid()` 안에 데이터 리터럴이나 변수형을 넣고 `.name()` 를 호출하면 어떠한 데이터타입인지 출력해줌

___

**numeric promotion**

```cpp
#include <iostream>
#include <typeinfo>
int main()
{
	using namespace std;

	float a = 1.0f;
	double d = a; // numeric promotion

	cout << typeid(d).name() << endl; 

	return 0;
}
```

- **numeric promotion:** float 에서 double 로 상대적으로 작은자료형에서 큰 자료형으로 이동하는 것

___

**numeric conversion**

**예제 1**

```cpp
#include <iostream>
#include <typeinfo>
int main()
{
	using namespace std;

	// 1
	double d = 3; 
	short s = 2;

	cout << typeid(d).name() << endl; 


	// 2
	int i = 30000;
	char c = i;

	cout << static_cast<int>(c) << endl; // 48


	//3


	return 0;
}
```

- `#1` **numeric conversion:** 큰것을 작은것으로 바꾸거나 혹은 타입이 바뀌거나 하는것
- `#2` 들어갈 수 있는 용량을 넘어가면 엉뚱한 48 이 출력되는둥 오류가 발생할 수 있음

**예제 2**

```cpp
#include <iostream>
#include <typeinfo>
#include <iomanip>

int main()
{
	using namespace std;

	// 1
	double d = 0.123456789;
	float f = d;

	cout << std::setprecision(12) << d << endl; // 0.123456789
	cout << std::setprecision(12) << f << endl; // 0.123456791043
	
	// 2
	int i = 1234;
	float g = i;

	cout << std::setprecision(12) << i << endl; // 1234
	cout << std::setprecision(12) << g << endl; // 1234

	// 3
	float h = 3.14f;
	int q = h;

	cout << std::setprecision(12) << h << endl; // 3.1400001049
	cout << std::setprecision(12) << q << endl; // 3


	return 0;
}
```
- `#1` 나름 최대한 비슷하게 저장하긴하지만 정밀도가 떨어져 정확히 저장할 수 없음
- `#2` 동일하게 최대한 비슷하게 저장해줌
- `#3` 반올림을 해주지않고 뒷부분을 잘라내서 저장함
  - 반올림을 해주는 함수가 따로있음

**예제 3**

```cpp
#include <iostream>
#include <typeinfo>
#include <iomanip>

int main()
{
	using namespace std;

	cout << 5u - 10; // 4294967291

	return 0;
}
```
- unsigned 끼리 계산한걸 unsigned에 넣을려고함
- 형변환도 **우선순위**가 있음
  - 4byte 보다작은것은 integer 로 바뀜
  - int
  - unsigend int
  - long
  - unsigned long
  - unsigned long long
  - float
  - double
  - long double 
  - 순서대로 int가 가장낮고 long double 이 가장 높음

___

**명시적 형변환**
  - Explicit Type Conversion (casting)

```cpp
#include <iostream>

int main()
{
	using namespace std;

	// 1
	int i = int(4.0); // C++ 스타일 

	// 2
	int i = (int)4.0; // C 스타일 

	// 3
	int i = static_cast<int>(4.0) 

	return 0;
}
```

- `#1` integer 타입의 인스턴스를 하나 새로만들어 넣는다는 뜻
- `#2` C 스타일의 캐스팅
- `#3` 최근에 많이 사용하는 방식

기능상 차이는 없음

___

**연습문제**

> **numeric conversion 과 numeric promotion의 차이점**

- **numeric promotion:** float 에서 double 로 등 상대적으로 작은자료형에서 큰 자료형으로 이동하는 것

- **numeric conversion:** 큰것을 작은것으로 바꾸거나 혹은 타입이 바뀌거나 하는것


### **🌱 4.6 문자열 std:string 소개**

- 문자열 끝날때 끝난다는걸 표현하는 문자하나가 숨어있음

**string 라이브러리 기본 사용법**

```cpp
#include <iostream>
#include <string>

int main()
{
	using namespace std;

	const char my_strs [] = "Hello, World";
	const string my_hello = "Hello, World";
	const string my_hello("Hello, World"); // 동일하게 초기화 가능
	const string my_hello{"Hello, World"}; // 동일하게 초기화 가능

	string my_ID = "123";
	string my_ID = 123; // 불가능
	cout << my_hello << endl;

	return 0;
}
```

- `#include <string>` include 한뒤 `const string my_hello = "Hello, World";` 처럼 초기화
- C++ 에서 제공해주는건 **한 글자임** 한글자를 여러번 나열해주는 방식으로 문자열을 표현해줌
  - 같은 기능을 string 은 C++ 에서 제공해주는 것임
  - string 은 사용자 정의 자료형이라고 보면됨
- `string my_ID = 123;` 불가능 한이유는 암시적 형변환을 해주는 방법이 없기 때문임
  - string 은 표준 라이브러리에 들어있긴하지만 바로바꿀순 없음
  - 문자열로써 저장됨

___

**문제점 - cin으로 string 입력받을 경우**

```cpp
#include <iostream>
#include <string>

int main()
{
	using namespace std;

	cout << "Your name ? :";
	string name;
	cin >> name;

	cout << "Your age ? :";
	string age;
	cin >> age;

	cout << name << " " << age << endl;


	return 0;
}
```

- cin 은 입력값에 빈칸이 있으면 다 입력받았다 인식함
  - 첫번 째 입력에 `A B` 이렇게 입력하면 name 에 A age 에 B가 자동으로 들어감

**해결법 - getline으로 string 입력받기**

```cpp
#include <iostream>
#include <string>

int main()
{
	using namespace std;

	cout << "Your name ? :";
	string name;
	/*cin >> name;*/
	std::getline(std::cin, name);

	cout << "Your age ? :";
	string age;
	/*cin >> age;*/
	std::getline(std::cin, age);

	cout << name << " " << age << endl;


	return 0;
}
```

- `getline()`에 첫번쨰 파라메타로 cin, 두번째 파라메타로 입력받을 변수 넣기
  - 엔터 칠떄까지 라인을 쭉 입력받음
  - 라인 단위로 읽음

___

**문제점 - 정수를 입력받을 경우**

```cpp
#include <iostream>
#include <string>

int main()
{
	using namespace std;

	cout << "Your age ? :";
	int age;
	cin >> age;
	/*std::getline(std::cin, age);*/

	cout << "Your name ? :";
	string name;
	/*cin >> name;*/
	std::getline(std::cin, name);

	cout << name << " " << age << endl;


	return 0;
}
```

- 정수 입력시 `std::getline(std::cin, name);` 이 스킵되는 현상


**해결법 - `std::cin.ignore(32767, '\n')`**

```cpp
#include <iostream>
#include <string>

int main()
{
	using namespace std;

	cout << "Your age ? :";
	int age;
	cin >> age;
	/*std::getline(std::cin, age);*/

	std::cin.ignore(32767, '\n');


	cout << "Your name ? :";
	string name;
	/*cin >> name;*/
	std::getline(std::cin, name);

	cout << name << " " << age << endl;


	return 0;
}
```

- `'\n'` 을 만날때까지 최대 32767개의 글자를 무시해라 라는 뜻임
  - 32767: 2byte integer 로 표현이 가능한 가장 긴 sigend value 값을 넣어준것 

**`<limits>` 라이브러리로 매직넘버 없애기**

```cpp
#include <iostream>
#include <string>
#include <limits>

int main()
{
	using namespace std;

	cout << "Your age ? :";
	int age;
	cin >> age;
	/*std::getline(std::cin, age);*/

	/*std::cin.ignore(32767, '\n');*/
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	cout << "Your name ? :";
	string name;
	/*cin >> name;*/
	std::getline(std::cin, name);

	cout << name << " " << age << endl;
 
	return 0;
}
```

- 버퍼크기: `streamsize` 

- 나중에 GUI 만들떄 입력기능을 제공해주는 라이브러리를 가져다쓸때 유용함

___

**문자열 더하기**

```cpp
#include <iostream>
#include <string>

int main()
{
	using namespace std;

	string a = "Hello, ";
	string b = "World";
	string hw = a + b; // apend

	hw += "I'm good";

	cout << hw << endl;

	return 0;
}
```

- string 클래스 안에 정의 되어있어서 가능함

___

**문자열 길이 출력하기**

```cpp
#include <iostream>
#include <string>

int main()
{
	using namespace std;

	string a = "Hello, World";
	

	cout << a.length() << endl; // 12

	return 0;
}
```

- string 클래스 안에 들어가있는 기능임
- `변수.length()` 를 사용하여 출력 
  - 맨앞과 맨뒤 `""` 를뺴고 알려줌 
  - `"Hello, World"` 를 마우스로 갖다 냈을때 13으로 나오는 이유는 문자의 array 문자가 메모리안에 저장되어있는 형태로 봤을떄 13글자임 끝부분에 문자의 끝을 의미하는 `Null char`가 하나 숨어있음
  - C스타일의 문자열하고 C++ 의 문자열은 약간의 차이가 있음

### **🌱 4.7 열거형 (Enumerated Types)**


- **enum (열거자 enumerator)**

**열거형 예제 코드**

```cpp
#include <iostream>
#include <typeinfo>

int computeDamange(int weapon_id)
{
	if (weapon_id == 0) // sword
	{
		return 1;
	}

	if (weapon_id == 1) // hamer
	{
		return 2;
	}

	// ....
}

enum Color // user - defined data types
{
	COLOR_BLACK,
	COLOR_RED,
	COLOR_BLUE,
	COLOR_GRREN,
	COLOR_SKYBLUE, // 마지막 , 있어도 상관없음
	/*BLUE*/ // Feeling의 BLUE와 중첩됨
}; // ; 필수

enum Feeling 
{
	HAAPY,
	JOY,
	TIRED,
	BLUE
};

int main()
{
	using namespace std;

	Color paint = COLOR_BLACK;
	Color house(COLOR_BLUE);
	Color appe{ COLOR_RED }; // {}
	
	return 0;
}
```


- `COLOR_BLACK` 등에 마우스 갖다 댔을때 숫자 가 나옴
- 내부적으로 int 로 저장됨
  - 0부터 순서대로 배정됨
- `{}` 초기환는 `()`나 `=`랑 특성이 조금 다름
  - 객체지향 클래스 초기화 할때 자세히설명
- `{}`로 묶여있지만 `Color의 BLUE` 와 `Feeling의 blue` 는 전역처럼 정의되기 때문에 같은 이름으로 사용할 수 없음
  - C+11 에 추가된 enum class로 해결가능

___

**열거형 수동 할당**

```cpp
#include <iostream>
#include <typeinfo>

enum Color // user - defined data types
{
	COLOR_BLACK = -3,
	COLOR_RED, // -2
	COLOR_BLUE = 5, // 5
	COLOR_GRREN = 5, // 5
	COLOR_SKYBLUE, // 6
	
}; // ; 필수

enum Feeling 
{
	HAAPY,
	JOY,
	TIRED,
	BLUE
};

int main()
{
	using namespace std;

	Color my_color = COLOR_BLACK;

	cout << my_color << " " << COLOR_BLACK << endl; // 0 0
	
	return 0;
}

```

- 가능함 위에서부터 1씩 더하면서 배정됨
- `COLOR_BLUE` 과 `COLOR_GRREN` 의 같은 정수로 강제할당하면 구분할수 없기 때문에 문제가 발생할 수 있음
  - 가급적 기본할당 사용
  - 기본적으로 대문자로함

___

**정수형 캐스팅**

```cpp
#include <iostream>
#include <typeinfo>

enum Color // user - defined data types
{
	COLOR_BLACK = -3,
	COLOR_RED, // -2
	COLOR_BLUE = 5, // 5
	COLOR_GRREN = 5, // 5
	COLOR_SKYBLUE, // 6
	
}; // ; 필수

enum Feeling 
{
	HAAPY,
	JOY,
	TIRED,
	BLUE
};

int main()
{
	using namespace std;

	int color_id = COLOR_RED; // 캐스팅은 가능

	Color my_color = 3; // 불가능

	Color my_color = static_cast<Color>(3); // 강제 캐스팅

	cout << color_id << endl;
	
	return 0;
}
```

- 캐스팅은 됨
- `Color my_color = 3;` 등 assignment 는 불가능
  - 이렇게 사용 안하려고 만든데 열거형이기때문임

___

**열거형 cin 우회 입력**

```cpp
#include <iostream>
#include <typeinfo>

enum Color // user - defined data types
{
	COLOR_BLACK = -3,
	COLOR_RED, // -2
	COLOR_BLUE = 5, // 5
	COLOR_GRREN = 5, // 5
	COLOR_SKYBLUE, // 6
	
}; // ; 필수

enum Feeling 
{
	HAAPY,
	JOY,
	TIRED,
	BLUE
};

int main()
{
	using namespace std;

	cin >> my_color; // 불가능

	int in_number;
	cin >> in_number;

	// 1
	if (in_number == COLOR_BLACK) my_color = COLOR_BLACK;
	//...

	//2
	if (in_number == static_cast<Color>(0)) 
		my_color = static_cast<Color>(0);
	//...


	return 0;
}
```

- `cin >> my_color;` 은 불가능 `in_number` 이라는 변수를 만들어서 조건문으로 캐스팅 하는 방법으로 우회 

___

**문자열로 입력받기**

```cpp
#include <iostream>
#include <typeinfo>
#include <string>

enum Color // user - defined data types
{
	COLOR_BLACK,
	COLOR_RED,
	COLOR_BLUE,
	COLOR_GRREN,
	COLOR_SKYBLUE,
	
}; // ; 필수

enum Feeling 
{
	HAAPY,
	JOY,
	TIRED,
	BLUE
};

int main()
{
	using namespace std;

	int my_color;
	string str_input;

	std::getline(cin, str_input);

	if (str_input == "COLOR_BLACK") // color_black
		my_color = static_cast<Color>(0);

	return 0;
}
```

- `#include <string>` 라이브러리의 `std::getline(cin, str_input);` 으로 입력받는 방법이 있음
- 권장하지않음
  - `"COLOR_BLACK"` 에서 오타 발생할수 있음
  - 사용자가 소문자로 입력하는 경우도 있음
- 열거형 은 보통 헤더파일에 넣고 include 해서 사용함
- integer 타입으로 저장되는거같지만 문법상으로 integer 랑 100퍼센트 호환 되진않음 필요에 따라서 캐스팅하여 사용하기

### **🌱 4.8 영역 제한 열거형 (열거형 클래스)**

- Scoped Enumerations (Enum Class)

```cpp
#include <iostream>
#include <typeinfo>
#include <string>

enum Color 
{
	RED,
	BLUE,
	
}; 

enum Fruit 
{
	BANANA,
	APPLE,
};

Color color = RED;
Fruit fruit = BANANA;

int main()
{
	using namespace std;

	if (color == fruit)
		cout << "Color is fruit ?" << endl; // 출력

	return 0;
}
```

- 내부적으로 int 로 저장되어 0이라는값으로 동일하기 때문에 출력
- 실수할 가능성이 있음
- C++ 11 에 적용됨 enum class

___

**enum class 예제 코드**

```cpp
#include <iostream>
#include <typeinfo>
#include <string>

enum class Color 
{
	RED,
	BLUE,
	
}; 

enum class Fruit
{
	BANANA,
	APPLE,
};

Color color = Color::RED;
Fruit fruit = Fruit::BANANA;

int main()
{
	using namespace std;

	if (color == fruit) // 비교가 안되게 막아버림
		cout << "Color is fruit ?" << endl;

	if (static_cast<int>(color) == static_cast<int>(fruit)) // 강제 캐스팅
		cout << "Color is fruit ?" << endl;

	return 0;
}
```

- `enum class Color ` 와같이 class 선언을 하면 `Color color = Color::RED;` 같이 영역이 제한됨

___

**enum type 끼리의 비교**

```cpp
#include <iostream>
#include <typeinfo>
#include <string>

enum class Color 
{
	RED,
	BLUE,
	
}; 

enum class Fruit
{
	BANANA,
	APPLE,
};

Color color1 = Color::BLUE;
Color color2 = Color::BLUE;

int main()
{
	using namespace std;

	if (color1 == color2)
		cout << "Same color " << endl;

	return 0;
}
```

- class 선언시 같은 enum 끼리는 비교가 가능함
- namespace 랑 비슷함


### **🌱 4.9 자료형에게 가명 붙여주기 (Type aliases)**

- 가명: aliases 
- 긴것을 짧게 줄이는데 좋음
- 유지보수할때 편함
- 고정너비정수에서 플랫폼의 독립적인코딩을 할때에 내부적으로 사용함

**typedef 용법 예제 코드 1**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

int main()
{
	using namespace std;

	typedef double distance_t;

	double my_distance;
	distance_t home2work;
	distance_t home2school;

	return 0;
}
```

- typedef 기록을 해두고싶을때 
  - distance_t를 쓸때는 double로 쓸려고 타이핑한것
    - `_t` 타입 이름이라는 의미로 씀
  - 메모, 주석 느낌
- 자료형을 바꿀때 `typedef double distance_t;`의 자료형만 바꾸면 정의해둔 전체에 적용되기 때문에 유지관리하기 편함

**typedef 용법 예제 코드 2**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

int main()
{
	using namespace std;

	vector < pair<string, int> > pairlist1; // 1
	vector < pair<string, int> > pairlist2; 

	typedef vector < pair<string, int> > pairlist_t; // 2

	pairlist_t pairlist1;
	pairlist_t pairlist2;

	return 0;
}
```

- 하나의 자료형으로보면됨
- string과 int의 페어가 vector에 넣어진다는것
- vector는 array같은 것
- `#1` 처럼 사용하던걸 `#2` 처럼 typedef 로 코드길이를 줄여줄수 있음

___

**Using**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

int main()
{
	using namespace std;

	typedef vector < pair<string, int> > pairlist_t; // 1
	using pairlist_t = vector < pair<string, int> >; // 2

	pairlist_t pairlist1;
	pairlist_t pairlist2;

	return 0;
}
```

- `#1` 변수에 초기화하는건 메모리공간을 복사하는 것임
- `#2` 컴파일러에게 알려주는것 이기떄문에 `#1`과는 내부적으로 완전히 다름

### **🌱 4.10 구조체 (struct)**

**구조체:** 다양한 요소를 묶어서 하나의 자료형인것 처럼 사용할수 있게 해주는 것

- C++ 에서는 클래스로 넘어가는 길목임
- 열거형을 사용할수 있음

**구조체를 사용하는 이유**
1. 함수의 파라메타로 모든 변수를 넣어줘야해서 너무 길어짐
2. 같은 변수를 여러번 반복할떄 좋음

___

**구조체 초기화 방법**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height;
	float weight;
	int age;
	string name;
};

int main()
{

	Person me; // 1
	me.age = 20;
	me.name = "Jack Jack";
	me.height = 2.0;
	me.weight = 100.0;

	Person mom{2.0,100.0,20,"Jack Jack"}; // 2
	Person dad;

	return 0;
}
```

- `#1` 기본 초기화 방법
- `#2` 유니폼 이니셜라이징`{}` 를 사용하여 편하게 초기화 할수 있음.

___

**구조체 프린트 방법**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height;
	float weight;
	int age;
	string name;
};

void printPerson(Person ps)
{

	cout << ps.height << " " << ps.weight << " " << ps.age << " " << ps.name;
	cout << endl;
}

int main()
{

	Person me; // 1
	me.age = 20;
	me.name = "Jack Jack";
	me.height = 2.0;
	me.weight = 100.0;

	Person mom{2.0,100.0,20,"Jack Jack"}; // 2
	Person dad;

	printPerson(me); // me 출력하기

	return 0;
}
```

- 구조체 안의 변수를 접근할려면 `.`을 찍게 되어있음
  - `.`을 멤버 셀렉션 오퍼레이터 라고함
  - 구조체 안의 변수들을 멤버라고함

___

**구조체 안의 함수 사용**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height;
	float weight;
	int age;
	string name;

	void print()
	{

		cout << height << " " << weight << " " << age << " " << name;
		cout << endl;
	}
};

int main()
{

	Person me{2.0,100.0,20,"Jack Jack"}; 

	me.print();

	return 0;
}
```

- 구조체 안에 `void print()` 함수를 선언하면 이미 Person 구조체에 속해 있기 떄문에 `ps.` 을 안찍어줘도 바로 접근할수 있음
- `me.print();`로 함수를 실행함
- 이런식으로 짜면 코드의 길이을 줄일수있음

___

**구조체 복사**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height;
	float weight;
	int age;
	string name;

	void print()
	{

		cout << height << " " << weight << " " << age << " " << name;
		cout << endl;
	}
};

int main()
{

	Person me{2.0,100.0,20,"Jack Jack"}; 
	Person me2(me);
	me2.print(); // 1

	Person me{ 2.0,100.0,20,"Jack Jack" };
	Person me2;
	me2 = me;
	me2.print(); // 2

	return 0;
}
```

- `#1` 과 `#2`와 같이 구조체를 복사해서 출력할 수도 있음
- `#2` 단순한 경우에 사용함
  - `=` 사용시 클래스랑 클래스, 구조체와 구조체를 복사해서 넣는 경우 문제가 발생할 수도 있음

___

**구조체 안의 구조체**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height;
	float weight;
	int age;
	string name;

	void print()
	{

		cout << height << " " << weight << " " << age << " " << name;
		cout << endl;
	}
};

struct Family
{
	Person me, mom, dad;
};

int main()
{
	Person me{ 2.0,100.0,20,"Jack Jack" };
	Person me2;
	me2 = me;
	me2.print(); 

	return 0;
}
```

- `struct Family` 의 `Person me, mom, dad;` 와같이 구조체 안의 구조체를 정의할 수 있음

___

**함수에서 구조체를 리턴**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height;
	float weight;
	int age;
	string name;

	void print()
	{

		cout << height << " " << weight << " " << age << " " << name;
		cout << endl;
	}
};

Person getMe()
{
	Person me{ 2.0,100.0,20,"Jack Jack" };

	return me;
}

int main()
{
	Person me_from_func = getMe();
	me_from_func.print();

	return 0;
}
```

- 구조체 를 함수의 리턴값으로 사용할 수 있음
- 파라메타로 넣을수도있음

___

**초기화시 주의사항**

**멤버변수 기본값**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height= 3.0;
	float weight = 200.0;
	int age = 100;
	string name = "Mr. Incredible";
};

int main()
{
	/*Person me{ 2.0,100.0,20,"Jack Jack" };*/
	Person me;
	cout << me.name << endl; // "Mr. Incredible"
	return 0;
}
```

- 직접 초기화를 할수도있음 즉 기본값을 넣어 주는 것
  - 구조체를 초기화하면서 멤버 변수에 초기화를 안해주면 직접초기화된 값이 출력됨

**멤버변수 우선순위**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Person
{
	double height= 3.0;
	float weight = 200.0;
	int age = 100;
	string name = "Mr. Incredible";
};

int main()
{
	Person me{ 2.0,100.0,20,"Jack Jack" };
	cout << me.name << endl; // "Jack Jack"
	return 0;
}
```

- 기본값 보다는 선언하면서 초기화해주는값이 우선순위가 높음

**padding**

```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Employee // 14 byte
{
	short	id;   // 2 byte + 빈칸 2byte
	int		age;  // 4 byte
	double  wage; // 8 byte

};

int main()
{
	Employee emlp;

	cout << sizeof(Employee) << endl; // 16

	return 0;
}
```

- 구조체에도 sizeof를 사용 할 수있음
- 빈칸 2byte 가 추가되어 16이 출력됨
- 순서와 사이즈를 잘맞춰주는게 최적화시 중요한 지식이됨

# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)