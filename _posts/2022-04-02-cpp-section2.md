---
published: true
title:  "따라하며 배우는 C++ Section 2. 변수와 기본적인 자료형"
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
- 따라하며 배우는 C++ Section 2. 변수와 기본적인 자료형

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 2. 변수와 기본적인 자료형**

### **🌱 2.1 기본 자료형 소개 (Fundamental Data Types)**
- **자료형**
  - 자료의 형태를 의미함
  - **char** 
    - 캐릭터, 문자를 저장하는 자료형
    - `char a = "H";`
    - 문자를 숫자로 변환하여 저장함 (아스키코드)
      - 그것을 다시 2진수로 바꿈
    - char 타입은 1byte만 씀 

- **비트를 8개 묶으면 1 byte**

- **4byte당 정수 1개 를 저장함**
- 메모리 주소는 매번 바뀜
  - 32비트, 64비트로 컴파일할때 마다바뀜

**데이터 타입마다 메모리의 저장되는 크기와 방식이 다르다**

___

> **C++ 자료형표**

![cpp자료형](https://user-images.githubusercontent.com/90514882/161422825-68a1aa78-93cf-41eb-8fd9-7e85acb2ba70.PNG)

**Character types**

> **문자 데이터를 저장할때 사용**

- char16_t 이나 char32_t 가 존재하는 이유는 이모티콘등의 표현할 데이터가 많아져서 사용됨
- wchar_t 는 문자를 저장하는 방식이 char등과 다름 
- 문장데이터를 저장할때는 String 타입을 쓰는게 기본 자료형은 아니고 스탠다드 라이브러리임

**Character types 초기화**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	char chValue = 'A';

	cout << chValue << endl;

	return 0;
}
```
- `(int)chValue` 로바꾸면 아스키코드인 65 가 출력됨

**Character types 숫자로 초기화**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	char chValue = 65;

	cout << chValue << endl;

	return 0;
}
```
- 동일하게 `A` 가 출력이 됨

___

**Interger types (signed)**

> **음의 정수, 0, 양의 정수(자연수)를 포함함**

- 기울어진 글자는 코딩할때 생략해도된다는 뜻
- 종류가 다양한 이유는 메모리 범위 차이 임
- Char 이 Character types, signed, unsigned 에도 있는 이유는 **내부적으로 저장할때 int 형으로 저장하기 때문임**
- 최소 데이터로 규정 지어짐 컴파일러에 따라서 사이즈가 달라질 수 있음

**Interger types (unsigned)**

> **0, 양의 정수(자연수)를 포함함**

**signed 와 unsigned 의 차이점**
1. 서로 저장되는 방식이 다름
2. 특정 연산에서 속도 차이가 나는 경우가 있음

- **[참고] 수학 용어에서 양의 정수 (positive interger) 나 음의 정수 (negative integer)는 0을 포함 하지 않음**

___

**Floating - point types**

> **부동 소수점이 있는 숫자들(실수)**

- 실수를 부동 소수점이라고 부르는 이유
  - 숫자를 저장하는 방식 때문
- 실수 표현의 정밀도 측면에서 float 를 single precision, double 을 double precision 이라고도 함
- float: 32비트
- double: 64비트

**Floating type 초기화**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	float fValue = 3.141592f;
	double dValue = 3.141592;

	cout << fValue << endl;
	cout << dValue << endl;

	return 0;
}
```

- **float** 는 초기화 할때 끝에 **f를 붙이게끔 되어있음**
  - 컴파일러에서는 f를 빼면 double로 인식하고 경고가 뜸
- **double 은 f를 안붙임**
- float 나 double 은 우리가 생각하는 것만큼 정밀하게 저장하지 않음
    - 2진수를 숫자로 표현하는 법으로 바꿔서 저장하기 때문임

___

**Boolean type**

> **True or False 를 의미함**

**Boolean type 초기화**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	bool bValue = false;

	cout << (bValue ? 1 : 0) << endl;

	return 0;
}
```

-  `bValue = false` 0 출력  
-  `bValue = True`  1 출력
- Boolean type 도 내부적으로 숫자로 바꾸어 저장을함
- 단위가 1비트임에도 **메모리 구조에서 주소가 부여되는 단위가 1바이트**여서 최소 1바이트를 사용함

___

**Void type**

> **파라메타가 없을때 사용함**

- 포인터 다룰때 설명

___

**Null pointer**

- 포인터 다룰때 설명


**모던 C++ 에는 auto 가 있음**

> 컴파일할때 자동으로 자료형을 결정해줌

```cpp
#include <iostream>

int main()
{

	using namespace std;

	auto aValue = 3.141592; // double
	auto aValue2 = 3.141592f; // float

	cout << aValue << endl;
	cout << aValue2 << endl;

	return 0;
}
```
___

**변수의 사이즈를 출력하는 방법**

> **변수 앞에 sizeof() 를 붙여주면 byte 크기로 사이즈를 출력해줌**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	auto aValue = 3.141592;
	auto aValue2 = 3.141592f;

	cout << sizeof(aValue) << endl; // 8 출력
	cout << sizeof(aValue2) << endl; // 4 출력

	return 0;
}
```

- **sizeof() 는 데이터 타입을 넣어도 되고 변수를 넣어도됨**
  - `sizeof(bool)`
  - `sizeof(aValue)`

___

**C++ 의 3가지 초기화 방법**

```cpp
#include <iostream>

int main()
{

	int a = 123; // copy initalization
	int b(123); // direct initalization
	int c{ 123 }; // uniform initalization

	return 0;
}
```

- 객체 지향이라는건 **데이터 타입을 직접만들어 쓰는 것** 
  - copy initalization, direct initalization, uniform initalization 은 객체 지향에서 내가 직접 만든 데이터 타입을 초기화 할때 많이 사용함

```cpp
#include <iostream>

int main()
{

	int b(3.14); // direct initalization
	int c{ 3.14 }; // uniform initalization

	return 0;
}
```
- 위와 같이 int 자료형에 실수 데이터를 넣었을때 
  - direct initalization 에서는 **경고**
    - 3.14 같은 데이터를 넣었을때 에러는 안나고 경고가 뜨는이유
      - 내부적으로 0.14 를 떼버리고 **3이라는 데이터로 전환해서** 저장함 이를 **캐스팅** 이라고함
  - uniform initalization 에서는 **에러** 처리됨
  - 즉 uniform initalization 이 더 엄격함

___

**강제 캐스팅처리**

```cpp
#include <iostream>

int main()
{
	using namespace std;
	int i = (int)3.1415; // copy initalization

	cout << i << endl;

	return 0;
}
```

- `int i = (int)3.1415;` 이런식으로 앞에 `(int)` 를 붙여 int 형으로 변환해서 초기화 할 수 있다
- i 의 출력값 `3`

___

**여러개의 변수를 동시에 초기화 하기**

```cpp
#include <iostream>

int main()
{
	int k, l, m; // #1
	int k, l, m = 123; // #2
	int k = 0, l = 456, m = 123; // #3
  int k = 0, l(456), m{123}; // #4
}
```

- *#1* -  같은 자료형 끼리 콤마(`,`)로 구분하여 동시에 초기화 할 수 있음
- 서로 다른 자료형을 동시에 초기화는 만약에 되더라도 **하면 안됨**
- *#2* - 이런 방식으로 초기화 할순 있지만 권장하지않음
  - 사람들이 보기에 k와 l 과 m 이 동시에 123으로 초기화 된 것 처럼 보이기때문에 *#3* 와 같이 초기화 하는 것이 좋음
- *#4* - 이런 방식으로 초기화 해도 되긴한데 가독성이 별로 안좋기 때문에 권장하진 않음

___

- 옛날 C 컴파일러 에서는 사용할 변수들을 맨 앞에 다 선언하고 했었음
- 최근에는 반대로 사용 할 변수는 사용 할 직전에 선언하는걸 선호함
  - 변수랑 실제 사용하는 부분이랑 같아야 디버깅할 때 편함
  - 이후에 리팩토링 할때 편함

### **🌱 2.2 정수형 (Integers) **

- char 타입을 1바이트 저장소 개념으로 사용하는 경우가 있음

**문자**
- char - 1바이트

**정수**
- short - 2바이트
- int - 2바이트 (대부분 4바이트)
- long - 4바이트
- long long - 8 바이트

`int i = 1;`

- 00000000 00000000 00000000 00000001
  - 첫번째 0 비트는 부호에 사용
___

**데이터의 크기 확인하기**

```cpp
#include <iostream>
#include <cmath>

int main()
{
	using namespace std;

	short s = 1; // 2 byte = 2 * 8 bits = 16 bits

	cout << std::pow(2, sizeof(short) * 8 - 1) - 1 << endl; // 결과값 32767

	return 0;
}
```
- 처음 8 - 1 에서 - 1 을 뺸건 맨앞에 0과 1 은 양수인지 음수 인지 확인 하기 위해서 빼준것이고
- 두번째 소괄호 밖에 - 1 은 0 표현하는 부분을 뺀 것
- 이번 강의의 포인트는 데이터 타입마다 제한이 있고 넘어가면 문제가 생긴다는 것

___

**변수에 1 더하는 방법**

1. `s += 1`
2. `s = s + 1`
3. `++s`
4. `s++`

- 각각의 의미는 다름 연산자 파트에서 자세히 다룸

___

**Overflow 예제 코드 1**

```cpp
#include <iostream>
#include <cmath>
#include <limits>

int main()
{
	using namespace std;

	short s = 1; // 2 byte = 2 * 8 bits = 16 bits

	s = 32767;
	s = s + 1;

	cout << s << endl; // overflow -32768

	return 0;
}
```

- short 자료형의 최대 양수 값인 32767 을 넘어가서 최대 음수값인 -32768이 출력됨

**Overflow 예제 코드 2**

```cpp
#include <iostream>
#include <cmath>
#include <limits>

int main()
{
	using namespace std;

	short s = 1; // 2 byte = 2 * 8 bits = 16 bits

	s = std::numeric_limits<short>::min();

	cout << s << endl;  // -32768

	s = s - 1;

	cout << s << endl;  // overflow 32767

	return 0;
}
```

- 반대로 short 자료형의 최대 음수 값인 -32768 을 넘어가서 최대 양수 값인 32787이 출력됨
- 2진수로 표현할때 가장 큰값을 넘어가면 가장 작은값이 되버리는 현상을 overflow 라고함

___

**unsigned int 의 overflow**

```cpp
#include <iostream>
#include <cmath>
#include <limits>

int main()
{
	using namespace std;

	unsigned int i = -1;

	cout << i << endl; // 4294967295

	return 0;
}
```
- 음수 값이없는 unsigned int 자료형 에다가 음수값인 -1 을 넣어버리면 2진수 표현법 때문에 overflow 현상이 발생되어 4294967295라는 값이 반환됨
- 여기서 중요한건 **C++ 에서는 오류메세지도 경고메세지도 안뜬다는점**

___

**정수 간의 연산**

```cpp
#include <iostream>
#include <cmath>
#include <limits>

int main()
{
	using namespace std;

	int i = 22 / 4; // 5

	cout << 22 / 4 << endl; // 5

	return 0;
}
```

- `cout << 22 / 4 << endl;` 의 값이 5.5 가아닌 5인 이유는 **정수끼리의 연산은 정수값으로 저장**하기때문에 소수점 부분을 떼고 저장하기때문에 5가 출력되는 것

**해결 방법**

```cpp
#include <iostream>
#include <cmath>
#include <limits>

int main()
{
	using namespace std;

	int i = 22 / 4; // 5

	cout << (float)22 / 4 << endl; // 5

	return 0;
}
```
- 22를 float 자료형으로 변환한 뒤에 4라는 정수형 데이터와 연산 함 이때 **둘중 하나라도 float 면 float 자료형으로 메모리에 저장됨**


### **🌱 2.3 C++ 11 고정 너비 정수 (Fixed-width lntegers) **

- C++ 에서는 데이터 사이즈를 최소사이즈만 규정하기때문에 플랫폼, 컴파일러 마다 실제 구현된 사이즈가 다를수 있음
  - 평균은 4바이트
  - 2바이트, 8바이트일 경우도 있음
- C++ 11 부터는 어떤 플랫폼 이던지 똑같은 데이터 사이즈를 사용하는 **고정 너비 정수**가 사용됨

**사용법**

- `#include <cstdint>` 를 include 하여 사용 할 수 있음
  - `#include <iostream>` 를 이미 inclide 했다면 안해도됨 포함되어있기때문에

```cpp
#include <iostream>
//#include <cstdint>

int main()
{
	using namespace std;

	std::int16_t i(5); // short 2 byte
	std::int8_t myint = 65; // char 1 byte

	// myint 가 정수 자료형이아닌 char 자료형이기때문에 A가 출력됨
	cout << myint << endl; 

	std::int_fast8_t fi(5); // int 중에서 8비트 사이즈 중에 제일 빠른것
	std::int_fast64_t fl(5); // int 중에서 8바이트 데이터사이즈를 가지는 것

	return 0;
}
```

### **🌱 2.4 무치형 (보이드, Void)**

- **함수에서의** void
  - 리턴 타입이 없을때 void 를써줘야함
  - 파라메타에 값이 없다면 void 를 넣어주거나 비워놔도됨
    - 옛날 방식에선 void를 넣어 줬었음

- **변수에서의** void
  - `void my_void;` 이런식으론 사용불가
    - void 는 메모리를 차지하지 않기 때문에 변수 할당이 불가능함


```cpp
#include <iostream>

int main()
{
	int i = 123;
	float f = 123.456f;

	void* my_void;

	my_void = (void*)&i;
	my_void = (void*)&f;
	return 0;
}
```

> **데이터 타입이 다르고 데이터 타입의 사이즈가 다르더라도 그 데이터의 주소를 표현하는 데이터양은 동일함**

- i 와 f의 주소의 데이터 타입이 동일하기 때문에 `(void*)` 로 캐스팅 할 수 있음 (형변환)



### **🌱 2.5 부동소수점 수 (Floating Point Numbers)**

- 컴퓨터가 실수를 다루는 방법을 **부동소수점 수** 라고 함
  - float 가 떠다닌다 라는 뜻 숫자니까 `.` 이 둥둥 떠다니면서 숫자를 바꾼다 라는 뜻

**부동소수점 수**

- float - 4 byte
- double - 8 byte
- Long double - 8 byte

> int 와 동일하게 플랫폼, 컴파일러 마다 크기가 다름

- 나중에 템플릿으로 코딩을 한번하면 float, double, Long double 에서도 돌아가게 하게 함
___

**내부적으로 float 를 32 비트를 세부분으로 나눔**

0(부호 sign) 00000111(지수 exponent) 11000000000000000000000(가수 nantissa)

- 0 (0 일경우엔 양수 1일 경우엔 음수)
- 00000111 = 7 (10진수)
- 11000000000000000000000 = 0.75 (10진수)
  - 2의 -1승(0.5) + 2의 -2승(0.25)

**메모리 저장법**

`+(1 + 0.75) x 2의(7-127) = +1.316554 x 10의(-36)`
- -127 바이어스라고 부름 메모리의 저장하는 방식과 저장하는 규칙임 
- 바이어스에 지수의 7 을뺌 

___

```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
	using namespace std;

	float f;
	double d;
	long double ld;

	cout << numeric_limits<float>::min() << endl;
	cout << numeric_limits<float>::lowest() << endl;


	return 0;
}
```

- float 에서 min() 값은 절대값을 의미함
- float 숫자의 범위를 보고싶다면 lowest()로 확인해야함

**초기화 방법**

```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
	using namespace std;

	float f(3.141592f); // 3.14 = 31.4 * 0.1
	double d(3.141592);
	long double ld(.3141592);

	return 0;

}
```
- float 를 초기화 할때 f를 안붙이면 리터럴은 double 인데 C나 C++에서 강제로 float로 변경함
  - 컴퓨터 내부에서 사용하는 메모리가 2배나 차이남

- **31.4e-1** 은 **31.4 x 10의(-1승)** 을 의미함
  - `float f(3.14e3);` 이런식으로 초기화 할 수도있음 

___

**부동 소수점의 기본 출력 자릿수**

```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
	using namespace std;

	cout << 1.0 / 3.0 << endl; // 0.333333

	return 0;

}
```

- 0.333333 까지만 출력됨
- #include <iomanip>
  - io 를 manip(Manipulate 조작) 한다는뜻 
  - 디폴트는 6자릿수임

___

**부동 소수점 자리수 늘리기**

```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
	using namespace std;

	cout << std::setprecision(16) << endl;
	cout << 1.0 / 3.0 << endl;

	return 0;

}
```
- `cout << std::setprecision(16) << endl;` 으로 자릿수를 지정할 수 있음

___

**float의 정밀도**

```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
	using namespace std;

	float f(123456789.0f); // 10 significant digits

	cout << std::setprecision(16);
	cout << f << endl; // 출력값 123456792

	return 0;

}
```

- 출력값이 123456792 인 이유는 마찬가지로 2진수표현법때문임
- float 를 double 로 바꾸면 해결되는 문제이긴한데 대신 메모리용량이 2배차지함

___

**부동소수점으로 표현 할 수 있는 0.1의 값**

```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
	using namespace std;

	double d(0.1); // 10 significant digits

	cout << d << endl; // 0.1
	cout << std::setprecision(17); // 0.10000000000000001
	cout << d << endl;

	return 0;

}
```

- 부동 소수점으로 표현할 수 있는 0.1의 제일 가까운 값이 0.10000000000000001 이라는 뜻

___

**오차의 누적**
```cpp
#include <iostream>
#include <iomanip>
#include <limits>

int main()
{
	using namespace std;

	double d(1.0); 
	double d2(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1);

	cout << std::setprecision(17); 
	cout << d << endl; // 1
	cout << d2 << endl; // 0.99999999999999989

	return 0;
}
```
___

**변수가 무한대 값인지 확인하는 방법**

```cpp
#include <iostream>
#include <iomanip>
#include <limits>
#include <cmath>

int main()
{
	using namespace std;

	double zero(0.0); 
	double posinf = 5.0 / zero;
	double neginf = -5.0 / zero;
	double nan = zero / zero;

	cout << posinf << " " << std::isnan(posinf) << endl; // inf 1
	cout << neginf << " " << std::isnan(neginf) << endl; // -inf 0
	cout << nan << " " << std::isnan(nan) << endl; // -nan(ind) 1
	cout << 1.0 << " " << std::isnan(1.0) << endl; // 1 0

	return 0;

}
```
- `#include <cmath>` 라이브러리 include 후 `std::isinf()` 함수 사용
  - 무한대 확인 할때 사용
- `#include <cmath>` 라이브러리 include 후 `std::isnan()` 함수 사용
  - 1 이라는 bool값으로 반환 해줌
  - 0 이면 inf 가 아니라는것
- `-nan(ind)`중 ind 의 뜻은 indeterminate 결정할수 없다는 뜻


### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)