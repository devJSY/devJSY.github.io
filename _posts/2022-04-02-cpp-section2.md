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

### **🌱 2.2 정수형 (Integers)**

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


### **🌱 2.3 C++ 11 고정 너비 정수 (Fixed-width lntegers)**

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


### **🌱 2.6 불리언 자료형과 조건문 if**

- Boolean의 B 수학자이름임
- Boolean 은 조건문에서 많이 사용함
  - true (1)
  - false (0)

___

**Bollean 의 초기화 방법**

```cpp
#include <iostream>

int main()
{
	using namespace std;

	bool b1 = true; // copy initialization
	bool b2(false); // direct '''
	bool b3{ 1 }; // uniform ini..
	bool b4 = 0;


	return 0;
}
```
___

**Bollean ture or false 로 출력**
```cpp
#include <iostream>

int main()
{
	using namespace std;

	bool b1 = true; // copy initialization
	bool b2(false); // direct '''
	bool b3{ 1 }; // uniform ini..
	bool b4 = 0;

	cout << std::boolalpha;
	cout << b1 << endl; // true
	cout << b2 << endl; // false
	cout << b3 << endl; // true
	cout << b4 << endl; // false

	cout << std::noboolalpha;
	cout << b1 << endl; // 1
	cout << b2 << endl; // 0
	cout << b3 << endl; // 1
	cout << b4 << endl; // 0
	return 0;
}
}
```

- 기본출력은 1, 0 임
- `cout << std::boolalpha;` 를 사용하면 출력이 1, 0 이 아닌 true, false 로 출력됨
- 다시 1, 0 출력으로 바꾸고 싶다면 `cout << std::noboolalpha;` 사용
  
___

**not 연산자**

```cpp
#include <iostream>

int main()
{
	using namespace std;

	bool a(true);

	cout << !a << endl; // 0
	cout << a << endl; // 1

	cout << !true << endl; // 0
	cout << !false << endl; // 1

	return 0;
}
```

- true 나 false 앞에 !가 not 연산자임 즉 반대로 바뀜
- 변수로도 사용 가능
- 웬만하면 안씀 버그가 생기면 찾기 힘듬

___

**and 연산자**

- 논리연산자 and 
  - `&&` 로 표현
- 왼쪽 항과 오른쪽 항을 비교해서 Boolean 값 으로 반환해줌

```cpp
#include <iostream>

int main()
{
	using namespace std;

	bool a(true);

	cout << std::boolalpha;

	cout << (true && true) << endl; // true
	cout << (true && false) << endl; // false
	cout << (false && true) << endl; // false
	cout << (false && false) << endl; // false

	return 0;
}
```
- 둘다 true 인 경우에만 true 를 반환해줌

___

**or 연산자**

- 논리연산자 or
  - `||` 로 표현
- 둘중 하나만 true 면 true값을 반환 해줌

```cpp
#include <iostream>

int main()
{
	using namespace std;

	bool a(true);

	cout << std::boolalpha;

	cout << (true || true) << endl; // true
	cout << (true || false) << endl; // true
	cout << (false || true) << endl; // true
	cout << (false || false) << endl; // false

	return 0;
}
```

___

**if문**

- 어떤 문장을 조건에 따라서 실행이 될지 안될지 결정해줌
  - 조건은 () 안에 Bool 타입에따가 결정됨

```cpp
#include <iostream>

int main()
{
	using namespace std;

	if (1 > 3)
		cout << "this is true" << endl;
	else
		cout << "this is false" << endl;

	if (true) // (false)
		cout << "this is true" << endl;
	else
		cout << "this is false" << endl;

	// 여러 문장을 실행 시킬 경우 {} 로 표현
	if (3 > 1)
	{
		cout << "this is true" << endl;
		cout << "True sencond line" << endl;
	}
	else
	{
		cout << "this is false" << endl;
	}	
	return 0;
}
```

- 여러줄을 실행시킬때는 {} 로 묶어줘야함
  - 한줄도 {} 써도됨

___

**서로 같은 값인지 확인하는 함수**

```cpp
#include <iostream>


bool isEqual(int a, int b)
{
	bool result = (a == b);

	return result;
}

int main()
{
	using namespace std;

	cout << std::boolalpha;
	cout << isEqual(1, 1) << endl; // true
	cout << isEqual(0, 3) << endl; // false
}
```
___

**if 문의 규칙**

```cpp
int main()
{
	using namespace std;

	if (5)
	{
		cout << "True" << endl; // 출력됨
	}
	else
		cout << "false" << endl; // 출력안됨
	return 0;
}
```

- if ()  
  - **() 안에 값은 0 이외에는 전부 true임**
- 식별하기 편하게 true나 false를 넣어 주는게 좋음
- Boolean 값을 입력할때 true, false 로 입력하면 안됨
  - 컴파일러 버전 마다 다를수 있음 
- 오직 숫자 0과 1 만 인식함

___

**연습문제**

> 정수 하나를 입력받고 그 숫자가 홀수인지 짝수인지 출력하는 프로그램을 만들어 봅시다.

```cpp
#include <iostream>


bool remain(int a, int b)
{
	bool result = (a % 2);
	if (result == 0)
		return true;
	else
		return false;
}

int main()
{
	using namespace std;
	int a;

	cin >> a;
	cout << std::boolalpha;
	cout << remain(a, 2) << endl;

	return 0;
}
```
- C와 C++에서의 % 나머지 연산자는 정수형에 대해서만 수행할 수 있음


### **🌱 2.7 문자형 char type**

- **ASCII TABLE**
  - 어떤 숫자가 어떤 문자에 대응하는 지 정해놓음
  - 0 ~ 32 까지 화면에 표현되진 않음
  - 33~127 까지 화면에 표현됨

___

**char 초기화**

```cpp
#include <iostream>

int main()
{
	using namespace std;

	char c1(65); // 1 = 65;, c1{65}; 등등 다됨
	char c2('A'); // "Hello, World", std::string 

	// A A 65 65 출력
	cout << c1 << " " << c2 << " " << int(c1) << " " << int(c2) << endl;

	// c-style casting
	cout << (char)65 << endl; // A
	cout << (int)'A' << endl; // 65

	// c++-style casting
	cout << char(65) << endl; // A
	cout << int('A') << endl; // 65

	// static casting
	cout << static_cast<char>(65) << endl; // A
	cout << static_cast<int>('A') << endl; // 65

	// casting 시 변수의 값
	char ch(97);
	cout << ch << endl; // a
	cout << static_cast<int>(ch) << endl; // 97
	cout << ch << endl; // a
}
```

- `char c2('A');`
	- 한 글자를 사용할때는 따옴표를 사용함
	- 문자열을 표현 할때는 겹따옴표 `" "` 를사용

- 1 byte 짜리 아주작은 정수를 저장하는 다른 타입이 없어서 char 타입을 int 처럼 사용하는 경우가 있음


- **c++-style casting**
  - 65로 초기화되는 char 를 새로 만든다는 의미

- c-style casting, c++-style casting, static casting 기능은 다 동일함
  -  c-style casting, c++-style casting 는 강제로 변환하는 개념임
  -  static casting 은 기본 타입간의 변환 할때 컴파일러 한테 미리 체크 해달라는 뜻 
  - static casting의 `<>` 안에는 변환할 대상이되는 타입을 넣어주는 것임 


- **casting 시 변수의 값**
  - 원래 변수의 값은 변하지 않음

- 현업에선 `static_cast<int>` 이 길어서 잘 사용 안함
  - 가독성이 좋기떄문에 알아보기 힘든코드에서 사용하기 좋음

___

**버퍼**

```cpp
#include <iostream>

int main()
{
	using namespace std;

	char c1(65);
	cin >> c1;
	cout << c1 << " " << static_cast<int>(c1) << endl; 

	cin >> c1;
	cout << c1 << " " << static_cast<int>(c1) << endl;

	return 0;
}
```

- abc 를 입력하면 아래와 같이 출력됨
  - a 97
  - b 98
 
- `cin >>` 에 두글자 입력시 첫 글자만 출력해줌
  - 두번쨰 글자는 `버퍼`에 저장됨 

- **버퍼링**
  -  데이터가 들어올떄 **버퍼**라는 임시저장소에 저장하고 임시저장소에 있는것들이 처리가 끝나면 일부 데이터를 가져와 사용하는 

___

**char 타입의 크기**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	char c1(65);

	cout << sizeof(char) << endl; // 1
	cout << (int)std::numeric_limits<char>::max() << endl; // 127
	cout << (int)std::numeric_limits<char>::lowest() << endl; // -128

	cout << sizeof(unsigned char) << endl; // 1
	cout << (int)std::numeric_limits<unsigned char>::max() << endl; // 255
	cout << (int)std::numeric_limits<unsigned char>::lowest() << endl; // 0

	return 0;
}
```
___

**줄바꿈**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	cout << int('\n') << endl; // 10
	cout << "This is first lin \nsenond line";
	cout << "This is first lin " << endl;
	cout << "This is flush lin " << std::flush;

	return 0;
}
```

- `\n` 줄바꿈 아스키코드 10번
  - n 이 new line 의 약자라고 추측됨

- **이스케이프 시퀀스**: 화면에 표시가 안되는데 의미를 갖는 문자
- `\n` 은 단순히 줄바꿈이라는 의미
  -  `\n` 뒤에 문자가 버퍼에 안들어갈수도 있음
- `endl;` 은 줄바꿈과 동시에 cout 버퍼에 있는 내용을 전부 다 출력해라 라는뜻  
	- 출력하고 줄바꿈 
	- `<< std::flush;` : 버퍼에있는걸 출력하고 줄바꿈을 하지않을떄 사용

___

**탭**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	cout << "This is first lin \tsenond line";

	return 0;
}
```

___

**겹따옴표(") 출력하기**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	cout << int('\n') << endl; // 10
	cout << "This is first lin \tsenond line \"";

	return 0;
}
```

- 문자열사이에 \ 를 넣어주면됨

___

**OS 경고음 출력하기**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	cout << "This is first lin \a senond line";

	return 0;
}
```

- `\a` 사용하면 os 에서 설정된 경고음이 나옴

___

**유니코드용 자료형**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	wchar_t c;
	char16_t c;
	char32_t c3;

	return 0;
}
```

### **🌱 2.8 리터럴 상수 (Literal Constants)**

- C++ 14 Binary Literals
- 상수
  - 변하지않는 숫자
  - ex) pi = 3.14; 등

**리터럴**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	float pi = 3.14f;
	int a = -1234u;
	const float b = 3.14;
	long double c = 1234l; // l, L, ul, lu, LL 등등 가능함
	unsigned int n = 5u;
	long n2 = 5L;
	double d = 6.0e-10; // 6.0e100;

	return 0;
}
```

- 글자를 적어서 표현하는 상수를 **리터럴**이라고 부름
- const
  - pi 값이 변하지 않도록 해줌
- `int i = -1234u;`
	- -1234가 unsigned 로 캐스팅 되어 i 에 저장된다는 뜻
  	- 별로 안좋음 차라리 바꿀꺼면 `int i = (unsigned int)1234;` 이런식으로 명확하게 캐스팅하는게 가독성이 좋음
- 대부분 f나 l 을 주로씀

___

**8진수,10진수,16진수 초기화**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	int p = 0b1010;
	int m = 0b1010'1111'1010;
	int a = 8;
	int x = 012; 
	int f = 0xf;

	cout << p << endl; // 10
	cout << m << endl; // 2810
	cout << a << endl; // 8
	cout << x << endl; // 10
	cout << f << endl; // 15

	return 0;
}
```

- **2진수**
  - `int p = 0b1010;`
  - C++ 14 부터 바이너리 리터럴이 가능해짐
- **10진수 (Decimal)**: 0 1 2 3 4 5 6 7 8 9 10
  - `int X = 12;`
- **8 진수 (Octal)**: 0 1 2 3 4 5 6 7 10 11 12 13
  - `int X = 012;`
  - 앞에 0 붙이면 10진수가아닌 8 진수로 저장이됨
- **16진수 (hexa)**: 0 1 2 3 4 5 6 7 8 9 A B C D E F 10 
  - `int X = 0xF12;`
  - 2진수를 16진수로 줄이면 글자수가 많이 줄어들기때문에 많이사용함

- `int m = 0b1010'1111'1010;`
  - `'` 를 중간중간에 넣을수있음 컴파일러가 무시함 단시 사람이 읽기 편하게 지원해주는 기능임 
  - 10진수도 가능함
- **cout 은 기본적으로 10진수로 출력이됨**

___

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	int num_items = 123;
	int price = num_items * 10; // 10 is ...

	// 심볼릭 상수
	const int price_per_item = 10;
	int num_items = 123;
	int price = num_items * price_per_item;

	return 0;
}
```

- 10을 매직 넘버라고 부름
  - 코드에 남겨놓는건 좋지않음
- 심볼릭 상수를 사용하는 방법이 있음

### **🌱 2.9 심볼릭 상수 (symbolic constants)**

```cpp
#include <iostream>
#include <limits>

int main()
{
	using namespace std;

	const double gravity{ 9.0 };
	double const gravity{ 9.0 };

	const double gravity; // 불가능
	return 0;
}
```

- C++ 11 constexpr
- 변수 초기화 할때 앞이나 뒤에 const 를 붙여서 변수값을 변경할 수없음
  - 강제로 바꾸는 방법이 있긴한데 권장하지않음
  - 주고 const 를 앞에 붙임
  - const 는 변수만 선언이 불가함 **const 사용시 initalization** 필수임

___

**함수의 파라메타 const 선언**

```cpp
#include <iostream>
#include <limits>

using namespace std;


void printNumber(const int my_number)
{
	cout << my_number << endl;
}

// 이런식으로 사용하는 경우가 더많음
//void printNumber(const int& my_number) 

int main()
{
	printNumber(123);

	return 0;
}
```

- 함수의 파라메타를 함수내에서 바꾸는 경우는 드뭄
  - 차라리 복사해서 사용하기
- **보통 함수의 파라메타를 const 로 막아버림**

___

```cpp
#include <iostream>
#include <limits>

using namespace std;


int main()
{
	const int my_const(123); // 컴파일 타임 상수
	constexpr int my_const(123); // 컴파일 타임 상수 라는 표시

	int number;
	cin >> number;

	const int special_number(number); // 런타임 상수

	return 0;
}
```

- 컴파일 시에 결정되는 것을 **컴파일 타임 상수** 라고 부름
- 실행후에 결정되는 것을 **런타임 상수** 라고 부름
- 문법상 둘을 구분할 수 없음
  - 하지만 constexpr 을 사용하여 컴파일 타임 상수를 표시할 수 있음

___

**매직넘버 - 매크로로 해결하는 방법(C스타일)**

```cpp
#include <iostream>
#define PRICE_PER_ITEM 30

using namespace std;


int main()
{
	int num_item = 123;

	int price = num_item * PRICE_PER_ITEM;

	return 0;
}
```

- c++ 에서는 거의 안씀
- 디버깅이 힘듬
- 매크로는 대문자로 많이 사용
- define 을 해버리면 정의 범위가 너무 넓어져서 안쓰는게 좋음

___

**매직넘버 const**

```cpp
#include <iostream>

using namespace std;


int main()
{
	const int price_per_item = 30;

	int num_itemm = 123;

	int price = num_itemm * price_per_item;

	return 0;
}
```

- 물리에서는 변수명중 상수를 k로 많이 사용함

___

**const 헤더파일에 모아놓기**

**MY_CONSTANTS.h**

```cpp
#pragma once

namespace constants
{
	constexpr double pi(3.141592);
	constexpr double avogadro(6.0221413e23);
	constexpr double moon_gravity(9.8 / 6.0);
	//...
}
```

1. MY_CONSTANTS.h 파일 생성

**practice.cpp**

```cpp
#include <iostream>
#include "MY_CONSTANTS.h"

using namespace std;


int main()
{
	double radius;

	cin >> radius;

	double circumference = 2.0 * radius * constants::pi;

	return 0;
}
```

2. include하여 사용하기


- 다른 cpp파일에서도 헤더파일을 사용 할 수있으니 재사용이 용이함

# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)