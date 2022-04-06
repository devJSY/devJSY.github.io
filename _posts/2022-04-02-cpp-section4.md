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

### **🌱 **


# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)