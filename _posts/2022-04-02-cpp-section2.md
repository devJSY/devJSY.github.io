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

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)