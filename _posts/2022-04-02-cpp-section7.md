---
published: true
title:  "따라하며 배우는 C++ Section 7. 함수형"
excerpt: ""

categories:
  - 따배씨++
tags:
  - [C++]

toc: true
toc_sticky: true
 
date: 2022-04-13
last_modified_at: 2022-04-17
---

# 🤔 학습목표
- 따라하며 배우는 C++ Section 7. 함수

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 7. 함수**

### **🌱 7.1 매개변수와 실인자의 구분**

**예제 코드**

```cpp
#include <iostream>

using namespace std;

int foo(int x, int y);

int foo(int x, int y)
{
	return x + y;
} // x and y are destroyed

int main()
{
	int x = 1, y = 2;

	foo(6, 7); // 6, 7 : arguments (actual parameter)
	foo(x, y + 1);

	return 0;
}
```

- 매개변수 (Parameter)
  - 함수가 어떤기능을 하는지를 조절해주는 바꿔주는 기능임
  - 변수가 선언되는것과 비슷한 형태임
  - 함수가 끝나는 경우 os한테 메모리를 반납함
  - 지역변수라는 뜻임

- 인자 (Argument)
  - 실매개변수, 실인자 라고도함

- 항상 x에있는 값만 전달되는 건아님
  - 값에 의한전달
  - 참조의 의한 전달
  - 주소에 의한 전달

- 인자값이 파라메타에 복사되어 들어감

### **🌱 7.2 값에 의한 전달**

- Passing Arguments by Value (Call by Value)

**예제 코드**

```cpp
#include <iostream>

using namespace std;

void doSomething(int y)
{
	cout << "In func " << y << " " << &y << endl;
}

int main()
{
	doSomething(5);

	int x = 6;

	cout << "In main " << x << " " << &x << endl;

	doSomething(x); // 6
	doSomething(x +1); // 7
	return 0;
}
```

- `doSomething()` 이 실행되면 내부적으로 int y가 선언되고 y변수의 메모리에 5 라는 값에 **복사**가 되어 초기화가 됨

- `doSomething()` 안에 변수를 넣었을때 x라는 변수가 아닌 x안에있는 **value**가 전달이됨
  - 즉 `x + 1` 등 연산도 가능함

- 값에 의한 전달을 할때는 `doSomething()` 안에서 변수를 바꿔도 main 함수에 영향을 못줌

### **🌱 7.3 참조에 의한 인수 전달**

- Passing Arguments by Reference (Call by Reference)

**예제 코드 1**

```cpp
#include <iostream>

using namespace std;

void addOne(int& y)
{
	cout << y << " " << &y << endl;
	y = y + 1;
}

int main()
{
	int x = 5;

	cout << x << " " << &x << endl;

	addOne(x);
	
	cout << x << " " << &x << endl;

	return 0;
}
```

- 레퍼런스로 전달하게되면 y로 레퍼런스가 넘어오기 때문에 변수 자체가 넘어감

- x라는 변수 자체가 넘어간것임
  - `addOne()` 함수의 변수 y와 `main()`의 변수 x는 동일함
  - 참조에의한 호출에선 복사를 안함
  - 주소도 똑같음 

___

**예제 코드 2**

```cpp
#include <iostream>
#include <cmath> // sin(), cos()

using namespace std;

void getSincos(const double degress, double& sin_cou, double& cos_out)
{
	static const double pi = 3.141592;

	const double radians = degress * pi / 100.0;
	sin_cou = std::sin(radians);
	cos_out = std::sin(radians);

}

int main()
{
	double sin(0.0);
	double cos(0.0);

	getSincos(30.0, sin, cos);

	cout << sin << " " << cos << endl;

	return 0;
}
```

- `getSincos()` 의 `double degrees` 는 함수가 끝나면 사라지기 때문에 입력이라는것을 알수 있음
- `getSincos()` 의 `double& sin_cou`,  `double& cos_out` 는 레퍼런스로 받아서 바꿀수 있는 값이란 것을 알 수 있음

- C와 C++ 에선 리턴값을 하나밖에 못줌
  - 레퍼런스를 사용하여 함수안에서 값을 변경 하고 실제로 리턴값이 나오는것 처럼 사용할수 있음

- 파라메타에 입력을 보통 앞에부고 출력으로 나갈 레퍼런스를 뒤에 둠
  - 입력 변수에 const 를 붙여서 입력이라는것 을 알려줄수 있음

- 계산식 수식중 값이 한번 계산되고 안바뀔것은 const를 해놔야 실수를 줄일수 있음 
  - `const double radians = degress * pi / 100.0;`
- `const double degress` → `const double &degress` 로 바꿔 레퍼런스로 만들어도됨

**before**

```cpp
	static const double pi = 3.141592;

	const double radians = degress * pi / 100.0;
```

**After**

```cpp
	static const double pi = 3.141592 / 100.0;

	const double radians = degress * pi;
```

- 위와같이 수정하면 static 변수가 정의 될떄 딱 한번만 연산되기 때문에 효율이 더좋아짐

___

**레퍼런스의 단점**

```cpp
#include <iostream>

using namespace std;

void foo(int& x)
{	
	cout << x << endl;
}

int main()
{
	foo(6); // Error

	return 0;
}
```

- 레퍼런스, 주소로 받아야하는데 리터럴은 주소가 없기 때문에 에러 

**해결방법**

```cpp
#include <iostream>

using namespace std;

void foo(const int& x)
{	
	cout << x << endl;
}

int main()
{
	foo(6);

	return 0;
}
```

- x의 값이 내부에서 변경이 되지않을 경우 파라메타에 const를 붙여서 사용할수 있음

___

- 모던 C++ 에서 리턴 value 옵티마이저, 여러개의 리턴타입을 구현하는게 복잡하지 않게 되었음
- `void foo(const int& x)`와 같이 매개변수를 넣을때 `const` 와 `&` 를 붙이는게 일반적임 

___

**포인터에 대한 레퍼런스**

```cpp
#include <iostream>

using namespace std;

void foo(int *&ptr)
{	
	cout << ptr <<" " << &ptr <<endl;
}

int main()
{
	int x = 5;
	int* ptr = &x;

	cout << ptr << " " << &ptr << endl;

	foo(ptr);

	return 0;
}
```

- `void foo(int *&ptr)` 를 `void foo((int *)&ptr)` 로 해석하면 편함

```cpp
#include <iostream>

using namespace std;

typedef int* pint;

void foo(pint &ptr)
{	
	cout << ptr <<" " << &ptr <<endl;
}

int main()
{
	int x = 5;
	// int* ptr = &x;
	pint ptr = &x;

	cout << ptr << " " << &ptr << endl;

	foo(ptr);

	return 0;
}
```

- `pint` 실제로는 포인터인데 사용자 정의 레퍼런스로만 보임
- 포인터가 인수로 변수자체가 넘어갔기 때문에 포인터변수의 주소 자체가 같음 
  - 포인터에 담겨있는 주소도 같음
- 이중 포인터 사용시 많이 사용함

___

**Array를 파라메타로 전달하는 방법**

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printElement(const vector<int>& arr)
//void printElement(int (&arr)[4]) 
{	

}

int main()
{
	/*int arr[] = { 1,2,3,4 };*/
	vector<int> arr{ 1,2,3,4 };


	printElement(arr);
	
	return 0;
}
```

- 파라메타의 배열의 요소의 갯수 가 꼭 들어가줘야함 `[4]`
- 배열을 보내야할떄는 보통 동적 배열을 많이씀
  - class를 별도로 만들어서 보냄
- `std::array` , `std::vector` 를 사용하면 데이터타입을 보내는것과 똑같기떄문에 레퍼런스로 보내기 편함


### **🌱 7.4 주소에 의한 인수 전달**

- Passing Arguments by Address (Call by Address)
- 매개변수를 인수를 전달하는 방법중 포인터를 이용하는 방법

```cpp
#include <iostream>

using namespace std;

typedef int* pint;

void foo(pint ptr)
{
	cout << *ptr << " " << ptr << &ptr << endl;

}

int main()
{
	int value = 5;

	cout << value << " " << &value << endl; // 5 00F8FDFC

	int* ptr = &value;

	cout << &ptr << endl; // 00F8FDF4

	foo(ptr); // 5 00F8FDFC00F8FDF8
	foo(&value); // 5 00F8FDFC00F8FDF8
	//foo(5); // Error
	
	return 0;
}
```

- 주소만 넣어줄수 있음
- main의 ptr과 함수의 ptr 의 주소는 다름
  - 포인터 변수도 변수임
  - 주소값이 복사가 되고있을뿐임

```cpp
#include <iostream>

using namespace std;

typedef int* pint;

void foo(int* ptr)
{
	cout << *ptr << " " << ptr << &ptr << endl;

	*ptr = 10;
}

int main()
{
	int value = 5;

	cout << value << " " << &value << endl; // 5 00F8FDFC

	int* ptr = &value;

	cout << &ptr << endl; // 00F8FDF4

	foo(ptr); // 5 00F8FDFC00F8FDF8

	cout << value << endl; // 10

	foo(&value); // 5 00F8FDFC00F8FDF8
	//foo(5); // Error
	
	return 0;
}
```

- de-reference 한 값을 바꿀수 있음
- `void foo(int* ptr)` 를 `void foo(const int* ptr)` 처럼 const 를 붙이면 de-reference 한값을 변경할수 없게 막아줌

___

**포인터로 출력바꾸기**

```cpp
#include <iostream>

using namespace std;

typedef int* pint;

void foo(const double degress, double * sin_out, double* cos_out)
{
	*sin_out = 1.0;
	*cos_out = 2.0;
}

int main()
{
	int value = 5;

	cout << value << " " << &value << endl; // 5 00F8FDFC

	int* ptr = &value;

	cout << &ptr << endl;

	double degrees = 30;
	double sin, cos;

	foo(degrees, &sin, &cos);

	cout << sin << " "<< cos << endl; // 1 2

	return 0;
}
```

- 참조에 의한 호출과달리 넣어줄때 포인터이기 때문에 인수값으로 주소를 넣어줘야함
- 실용적인 부분에선 레퍼런스를 사용하는게 좋음
- 레퍼런스랑 착각하기 쉬운데 내부적으로 **값에의한 전달**로 주소가 복사되서 들어간것임

___

**포인터로 배열 받기**

```cpp
#include <iostream>

using namespace std;

typedef int* pint;

void foo(int *arr, int length)
{
	for (int i = 0; i < length; ++i)
		cout << arr[i] << endl;

	arr[0] = 1.0; // de-reference
}

int main()
{
	
	
	return 0;
}
```

- 이후에 입력으로 들어온 배열도 값이 바뀜
- `arr[0] = 1.0;` 는 de-reference 이기때문에 `int *arr` 에 const 를 붙이면 값 변경이 불가능 함

```cpp
void foo(const int * ptr)
{
	int x = 1;

	ptr = &x;
}
```

- 앞에 const 가 붙어도 포인터 자체 주소를 바꾸는건 가능함


```cpp
void foo(const int * const ptr)
{
	int x = 1;

	ptr = &x; // Error
}
```

- 포인터 변수 자체에 const를 넣으면 변경이 불가능함
  - 안쓰는 경우가 많음
  - 결국 값에의한 전달이고 지역 변수 인것 처럼 작동하기 때문임 
  - 실수를 방지하기위해 적어놓는 경우가 있음

### **🌱 7.5 다양한 반환 값들 (값,참조,주소,구조체,튜플)**

- Returning Values
- 반환값을 어떻게 돌려받을 것

**값을 리턴받는 방법**

```cpp
#include <iostream>

using namespace std;

int getValue(int x)
{
	int value = x * 2;
	return value;
}

int main()
{
	int value = getValue(3);
	
	return 0;
}
```

- 함수의 리턴값인 6 이 복사해서 value의 들어감
- 단점으로 값이 여러번복사해서 들어가기떄문에 느려짐
- 클래스나,구조체를 사용할때 데이터가 많거나,배열을 사용할때 복사가 많이되기 떄문에 문제가됨

___

**포인터로 리턴 받기**

**함수의 리턴값을 de-reference 하여 받기**

```cpp
#include <iostream>

using namespace std;

int* getValue(int x)
{
	int value = x * 2;
	return &value;
}

int main()
{
	int value = *getValue(3);
	
	cout << value << endl;

	return 0;
}
```

- 함수리턴값을 de-reference 를 해서 받을수 있음
- 하지만 권장하지않음
  - 사라질 변수를 de-reference 를 하는게 문제가 될수도 있기 떄문임


**함수의 리턴값을 주소로 직접 받기**

```cpp
#include <iostream>

using namespace std;

int* getValue(int x)
{
	int value = x * 2;
	return &value;
}

int main()
{
	int *value = getValue(3);
	
	cout << *value << endl;

	return 0;
}
```

- 굉장히 위험함
- 주소를 가지고있는데 이미 사라진 주소임
- 변수는 사라졌는데 메모리 주소만 갖고있는 상태임

___

**공장 패턴(factory pattern)**

```cpp
#include <iostream>

using namespace std;

int* allocateMemory(int size)
{
	return new int[size];
}

int main()
{
	int* array = new int[10]; // 기본 동적 배열 할당

	int* array = allocateMemory(1024);

  delete[] array;

	return 0;
}
```

- 공장 패턴(factory pattern)은 게임팩에서 다룸
- new가 있으면 delete 가 있어야하는데 delete가 어디서할지 막막함
- 일반적으로 이런식으로 동적메모리 할당하면 프로그래머에게 힘드므로 비추천

___

**reference로 리턴 받기**

```cpp
#include <iostream>

using namespace std;

int& getValue(int x)
{
	int value = x * 2;
	return value;
}


int main()
{
	int value = getValue(5);

	cout << value << endl;

	
	return 0;
}
```

- 레퍼런스를 반환해서 레퍼런스가 가르키고있는 변수의 값이 반환되어 value에 들어감
- 비교적 안전함
- `int &value = getValue(5);` 와같이 받는 쪽도 레퍼런스면 문제가 발생할 수 있음
  - `getvalue()` 에서 반환된값은 사라지는데 사라지는값에대한 레퍼런스를 담으면 문제가 발생할 수 있음
  - 매우 안좋은 방법임
  - `const int& getValue(int x)` const를 넣어도 의미가 없음

___

**reference로 배열의 요소 바꾸기**


```cpp
#include <iostream>
#include <array>

using namespace std;

int& get(std::array<int, 100>& my_array, int ix)
{
	return my_array[ix];
}

int main()
{
	std::array<int, 100> my_array;
	my_array[30] = 10;

	get(my_array, 30) = 1024;

	cout << my_array[30] << endl; // 1024

	return 0;
}
```

- 이런패턴으로 사용하는 경우가 아주 많음
- 메모리는 어딘가 안전하게 저장되어 있고 레퍼런스만 보내서 바꾸는 방식임
- 수학 라이브러리 구현시 클래스나 사용자 정의 데이터 형이 수학 식과 비슷하게 코딩이 되도록 구현할떄 많이 사용할 수 있음

___

**여러개의 리턴**

**구조체**

```cpp
#include <iostream>
#include <array>

using namespace std;

struct S
{
	int a, b, c, d;
};

S getStruct()
{	
	S my_s{1,2,3,4};
	return my_s;
}

int main()
{
	S my_s = getStruct();
	cout << my_s.b << endl;

	return 0;
}
```

- 여러개로 리턴 받을땐 구조체로 받는게 일반적임
- 구조체를 통해서 리턴값을 받으면 여러개의 반환값을 받는 효과를 낼수 있음
- 함수하나를 만들때마다 구조체를 하나씩 만들어야함
- 다이렉트X 라이브러리
  - 게임,그래픽스 관련 라이브러리
  - 내부 구조체가 엄청 많음
  - 함수 호출할때 구조체의 포인터로 넣고 받을때도 구조체로 받거나 구조체의 포인터로 받거나 하는 경우가 아주 많았음

**튜플**

```cpp
#include <iostream>
#include <array>
#include <tuple>

using namespace std;

std::tuple<int, double> getTuple()
{
	int a = 10;
	double d = 3.14;
	return std::make_tuple(a, d);
}

int main()
{
	std::tuple<int, double> my_tp = getTuple();
	cout << std::get<0>(my_tp) << endl; // a
	cout << std::get<1>(my_tp) << endl; // d

	return 0;
}
```

- 리턴 받을 자료형을 적어주기
- `std::tuple<int, double>`중  자료형에 구조체를 넣을수 있음
- `std::tuple<int, double>` 자체가 사용자 정의 자료형 처럼 작동함

**C++17 이후 개선된 코드**

```cpp
#include <iostream>
#include <array>
#include <tuple>

using namespace std;

std::tuple<int, double> getTuple()
{
	int a = 10;
	double d = 3.14;
	return std::make_tuple(a, d);
}

int main()
{
	auto [a, d] = getTuple();
	cout << a << endl;
	cout << d << endl;

	return 0;
}
```

- a,d 가 변수로 선언되면서 `getTuple()` 의 반환값을 초기화해줌

### **🌱 7.6 인라인 함수**

**inline 기본 문법**

```cpp
#include <iostream>

using namespace std;

inline int min(int x, int y)
{
	return x > y ? y : x;
}

int main()
{
	cout << min(5, 6) << endl;
	cout << min(3, 2) << endl;

	// inline part
	cout << (5 > 6 ? 6 : 5) << endl;
	cout << (3 > 2 ? 2 : 3) << endl;

	return 0;
}
```

- 인라인 함수 Inline Functions
- 최적화
- 함수이름 앞에 inline 을 붙여서 사용함
  - 헤더파일에 함수를 정의할때 많이 사용함
- 인라인으로 바꾸게되면 함수가 아닌것처럼 작동함
  - inline part 부분처럼 컴파일이 됨
  - 컴파일러가 하는 일임
  - 함수가 호출되거나 복사같은것을 안해도되서 속도가 빨라짐
- inline 키워드는 강제로 inline 으로 바꾸는게 아닌 권장, 권유 뉘앙스임
- 모든 함수를 inline으로 바꿔도 다 빨라지는것이아님
- 최근에는 컴파일러가 알아서 inline 을 적용해주는 경우도 있음 
- 연구 하는 사람은 코딩테크니컬보다는 소프트웨어의 구조를 바꿈 
- 객체지향 설계방식, 데이터 드리븐등으로 하드웨어 가속을 잘받는 식으로 캐쉬 미스를 중이는 방식, gpu가속,병렬처리를 해서 최적화를함
- 컴파일러가 실제로 inline으로 해줄지 안해줄지 알수 없음
- 컴파일러가 정말 inline으로 구현을 하면 컴파일된 프로그램이 많이 커짐

### **🌱 7.7 함수 오버로딩**

- Function Overloading

```cpp
#include <iostream>

using namespace std;

int add(int x, int y)
{
	return x + y;
}

double add(double x, double y)
{
	return x + y;
}

int main()
{
	add(1, 2);
	add(3.0, 4.0);


	return 0;
}
```


- 들어오는 매개변수가 다른데 수행하는 기능이 비슷할때 함수 오버로딩을 할 수있음
  - 기능이 판이하게 다른경우에도 사용할 수 있음


- 주의사항
- 함수가 서로 다르다 같다는 함수의 이름,매개변수 를 보고 판단함
- 그것들 중에서 매개변수 타입이 가장 잘 맞는 주어진 인자와 매개변수가 가장 조합이 좋은 함수를 찾아서 컴파일러가 알아서 찾아서 컴파일 해줌

**주의사항**

```cpp
#include <iostream>

using namespace std;

int add(double x, double y)
{
	return x + y;
}

double add(double x, double y) // Error
{
	return x + y;
}

int main()
{
	add(1, 2);
	add(3.0, 4.0);


	return 0;
}
```

- 어떤 함수를 사용할지 **컴파일할떄** 결정이 되야함
- 리턴타입이 달라도 매개변수가 같으면 문제가 생김

___

**함수의 이름이 같은 경우**
```cpp
#include <iostream>

using namespace std;

void getRandom(int& x) {}
void getRandom(double& x) {}

int main()
{
	int x;
	getRandom(x);

	//int x = getRandom(x);
	//int x = getRandom(int());

	return 0;
}
```

- 함수의 이름을 바꾸기
- 리턴값을 void 로 바꾸기 매개변수의 타입을 reference로 받기
   - **단점:** 리턴값을 못받으니 얼핏봤을때 리턴으로 값을 가져오는지 입력인지 구분이 안됨 

___

**typedef**

```cpp
#include <iostream>

using namespace std;

typedef int my_int;

void print(int x) {}
void print(my_int x) {} // Error

int main()
{

	return 0;
}
```

- 컴파일러 입장에선 같은 함수로 판단됨

___

**매치가 정확히 안되는 경우**

```cpp
#include <iostream>

using namespace std;

void print(char* value) {}
// void print(const char* value) {} 문자열 해결방법
void print(int value) {}

int main()
{
	print(0); // int 로 인식
	print('a'); // int 로 인식
	print("sadsa") // Error

	return 0;
}
```

- 데이터 타입에 대해서 주의를 해야함
- 매치를 못찾을때 함수를 못찾는다고 Error 가 발생함
- 모든타입에 다 정의를해주고 사용할때도 데이터타입을 정리해주는게 좋음
- 잘맞는게 없어서 억지로 있는것들 중에 가장 가까운걸 맞추는데 잘 안맞았는 경우임

___

**매치가 모호한 경우**

```cpp
#include <iostream>

using namespace std;

typedef int my_int;

void print(unsigned int value) {}
void print(float value) {}

int main()
{
	print('a'); // Error 
	print(0); // Error 
	print(3.14159); // Error 

  print((unsigned int)'a');
	print(0u);
	print(3.14159f);

	return 0;
}
```

- 함수 두개중에 어떤걸 선택할지 몰라서 뜨는 에러임
  - 모호하다는 에러가나옴
- 함수 오버로딩할떄 명확하게 사용하기 

### **🌱 7.8 매개변수의 기본값**

- Default Parameters

**Default Parameter**

```cpp
#include <iostream>

using namespace std;

void print(int x = 0)
{
	cout << x << endl;
}

int main()
{
	print();
	
	return 0;
}
```

- 파라메타 값이 안들어왔을때 이값을 넣어주세요라는뜻으로 파라메타에 `= value` 를 넣을 수 있음
- 디폴트 파라메타, 옵셔널 파라메타, 디폴트 아규먼트 라고도 부름


**파라메타 여러개일때 기본값**

```cpp
#include <iostream>

using namespace std;

void print(int x=10, int y =20, int z = 30)
{
	cout << x << " " << y << " " << z << endl;
}

int main()
{
	print();
	print(100);
	print(100, 200);
	print(100, 200, 300);

	return 0;
}
```

- 파라메타의 기본값을 넣을때 맨마지막값은 무조건 넣어줘야함

```cpp
#include <iostream>

using namespace std;

void print(int x = 10, int y = 20, int z = 30);

void print(int x=10, int y =20, int z = 30) // Error
{
	cout << x << " " << y << " " << z << endl;
}

int main()
{
	print();
	print(100);
	print(100, 200);
	print(100, 200, 300);

	return 0;
}
```

- 선언과 정의를 분리할때는 둘중에 하나만 사용할 수 있음
  - 즉 기본값은 한곳에서만 할수 있음 
  - 보통은 선언부분에 넣어둠

___

**파라메타 함수 오버로딩**

```cpp
#include <iostream>
#include <string>

using namespace std;

void print(std::string str) {}
void print(char ch = ' '){}

int main()
{
	print(); // char

	return 0;
}
```

- 빈파라메타를가진 함수와 디폴트 파라메타가 선언된함수 것중에 디폴트 파라메타가 선언된 함수를 선택함


```cpp
#include <iostream>
#include <string>

using namespace std;

void print(int x) {} // ambiguous
void print(int x, int y = 20){}

int main()
{
	print(10); // Error

	return 0;
}
```

- 뒷쪽 파라메타에 기본값을 넣으면 어떤 함수를 선택해야할지 몰라 컴파일러가 에러를 띄움 
- 디폴트 파라메타가 함수 오버로딩에도 영향을 줌

### **🌱 7.9 함수 포인터**

- Function Pointers

```cpp
#include <iostream>

using namespace std;

int func()
{
	return 5;
}
int main()
{
	cout << func << endl; // 000C1030

	return 0;
}
```

- 함수도 포인터 임
- 함수도 주소를 갖고있다
- 함수도 메모리에 들어감
- 메인에서 펑션을 호출하게 되면 함수가 어느 메모리 주소에 있는 지 알아내고 그 주소에 있는 프로그램을 가져다가 실행함 돌아올때 어디로 돌아와야하는지도 알아야함

**함수 포인터 선언**

```cpp
#include <iostream>

using namespace std;

int func()
{
	return 5;
}
int main()
{
	int (*fcnptr)();  // 선언
	int (*fcnptr)() = func; // 초기화

	return 0;
}
```

- fcnptr은 맘대로 정하면됨

___

**함수 바꿔치기**

```cpp
#include <iostream>

using namespace std;

int func()
{
	return 5;
}

int goo()
{
	return 10;
}

int main()
{
	int (*fcnptr)() = func; 

	cout << fcnptr() << endl; // 5

	fcnptr = goo;

	cout << fcnptr() << endl; // 10

	return 0;
}
```

- 포인터인데 `()`로 함수의 기능을 실행

```cpp
#include <iostream>

using namespace std;

int func(int x)
{
	return 5;
}

int goo(int x)
{
	return 10;
}

int main()
{
	int (*fcnptr)(int) = func; 

	cout << fcnptr(0) << endl; // 5

	fcnptr = goo;

	cout << fcnptr(0) << endl; // 10

	return 0;
}
```
- 함수 포인터 변수의 타입은 대입하려는 함수의 리턴타입의 타입과 정확히 일치해야함
- 매개변수와 리턴타입을 맞춰줘야 함수포인터를 사용할 수 있음

___

**배열의 홀수,짝수 값 출력하는 코드**

```cpp
#include <iostream>
#include <array>

using namespace std;

void printNumbers(const array<int, 10>& my_array, bool print_even)
{
	for (auto element : my_array)
	{
		if (print_even && element % 2 == 0) cout << element;
		if (!print_even && element % 2 == 1) cout << element;
	}
	cout << endl;
}

int main()
{
	std::array<int, 10> my_array = { 0,1,2,3,4,5,6,7,8,9 };

	printNumbers(my_array, true);
	printNumbers(my_array, false);

	return 0;
}
```

- `&` 를 앞에 붙이는 이유
  - 파라메타는 앞으로붙여도 문제가 안생김


**함수 포인터로 바꾼 코드**

```cpp
#include <iostream>
#include <array>

using namespace std;

bool isEven(const int& number)
{
	if (number % 2 == 0) return true;
	else return false;
}

bool isOdd(const int& number)
{
	if (number % 2 != 0) return true;
	else return false;
}

void printNumbers(const array<int, 10>& my_array, bool (*check_fcn)(const int&))
{
	for (auto element : my_array)
	{
		if (check_fcn(element) == true) cout << element;
	}
	cout << endl;
}

int main()
{
	std::array<int, 10> my_array = { 0,1,2,3,4,5,6,7,8,9 };

	printNumbers(my_array, isEven);
	printNumbers(my_array, isOdd);

	return 0;
}
```

- bool 대신 기능을 넣어줌 함수를 넣어주기
- 함수를 넣어서 다른 함수의 기능을 바꿔버림
- 다형성 이해시 도움이됨

**기본 매개변수 넣은 코드**

```cpp
#include <iostream>
#include <array>

using namespace std;

bool isEven(const int& number)
{
	if (number % 2 == 0) return true;
	else return false;
}

bool isOdd(const int& number)
{
	if (number % 2 != 0) return true;
	else return false;
}

void printNumbers(const array<int, 10>& my_array, 
	bool (*check_fcn)(const int&) = isEven)
{
	for (auto element : my_array)
	{
		if (check_fcn(element) == true) cout << element;
	}
	cout << endl;
}

int main()
{
	std::array<int, 10> my_array = { 0,1,2,3,4,5,6,7,8,9 };

	printNumbers(my_array);
	printNumbers(my_array);

	return 0;
}
```

**함수포인터 typedef , using 사용하기**

```cpp
#include <iostream>
#include <array>

using namespace std;

bool isEven(const int& number)
{
	if (number % 2 == 0) return true;
	else return false;
}

bool isOdd(const int& number)
{
	if (number % 2 != 0) return true;
	else return false;
}

typedef bool (*check_fcn_t)(const int&); // 1
using check_fcn_t = bool(*)(const int&); // 2

void printNumbers(const array<int, 10>& my_array, 
	check_fcn_t check_fcn = isEven)
{
	for (auto element : my_array)
	{
		if (check_fcn(element) == true) cout << element;
	}
	cout << endl;
}

int main()
{
	std::array<int, 10> my_array = { 0,1,2,3,4,5,6,7,8,9 };

	printNumbers(my_array);
	printNumbers(my_array);

	return 0;
}
```

**C++ 11 `#include <functional>`**

```cpp
#include <iostream>
#include <array>
#include <functional>

using namespace std;

bool isEven(const int& number)
{
	if (number % 2 == 0) return true;
	else return false;
}

bool isOdd(const int& number)
{
	if (number % 2 != 0) return true;
	else return false;
}

//typedef bool (*check_fcn_t)(const int&);
using check_fcn_t = bool(*)(const int&);

void printNumbers(const array<int, 10>& my_array, 
	std::function<bool(const int&)> check_fcn)
{
	for (auto element : my_array)
	{
		if (check_fcn(element) == true) cout << element;
	}
	cout << endl;
}

int main()
{
	std::array<int, 10> my_array = { 0,1,2,3,4,5,6,7,8,9 };

	std::function<bool(const int&)> fcnptr = isEven;

	printNumbers(my_array, fcnptr);

	fcnptr = isOdd;

	printNumbers(my_array, fcnptr);

	return 0;
}
```

### **🌱 7.10 스택과 힙 the stack and the heap**

- 컴퓨터가 메모리를 사용하는 방법
- 우리가 작업한 프로그램을 실행하면 os가 메모리를 넘겨줌
- 메모리는 여러구역으로 나뉨 세그먼트 라고 부름
	- code: 우리가 작성한 프로그램이 올라감
	- 데이터 영역
    	- bss: uninitlaltzed data segment
        	- 초기화가 되지않은글로벌 변수, 스태틱 변수 가 저장됨
        	- zero-initlaltzed 0으로된 데이터가 저장됨
    	- data: initlaltzed data segment
        	- 초기화된 정역변수, 스태틱 변수가 저장됨
	- stack
	- heap

___

**stack**

```cpp
#include <iostream>

int g_i = 0;

int second(int x)
{
	return 2 * x;
}

int first(int x)
{
	int y = 3;
	return second(x+y);
}

int main()
{
	using namespace std;
	
	int a = 1, b;
	b = first(a);
	cout << b << endl;

	return 0;
}
```

1. 전역변수가 먼저 메모리에 저장됨
2. sktack frame 안에 메인함수와 메인함수의 변수가 저장이됨
3. first() 가 생겨서 위에 쌓이게됨 매개변수와 지역변수가 선언되어 저장됨
4. second() 가 생기고 위에쌓이고 매개변수가 선언되어 저장됨
5. second() 함수가 끝나는 순간 위에서부터 하나씩 os로 반납됨
   - second() → first() → main() → 전역변수 순서  
- 스택은 차례대로 쌓여있고 현재 실행시켜야하는게 제일 위에있기때문에 비교적 속도가 빠름

**stack의 단점**

```cpp
#include <iostream>

int main()
{
	//... ...

	int array[10000000];

	return 0;
}
```

- 크기가 작음
- 배열이 너무커서 메모리 할당을 못함
  - 로컬변수, 정적array
  - 스택 오버플로우 라고함
- 재귀함수 등 사용할때 주의해야함

___

**Heap 동적 메모리 할당**

```cpp
#include <iostream>

int main()
{
	int* ptr = nullptr;
	ptr = new int[10000000];

	delete[] ptr;

	// ptr = nullptr;

	return 0;
}
```

- 지역변수는 스택에 저장되고 스택은 비교적 속도가 빠른대신 용량이 작음
- 힙 메모리는 힙 자료구조와는 상관없음
- 힙은 사이즈가 커서 큰데이터를 넣을수 있는 공간을 마음껏 확보할수 있음
- 메모리가 어디에 생길지 예측하기 힘듬
  - 그메모리 공간의 첫 주소를 포인터에 저장함
1. `main()` 함수의 포인터 변수 (`int *ptr`)가 stack에 저장됨
2. 동적 메모리 할당이되면 heap에 요구한만큼의 사이즈 (`int[10000000]`)가 잡힘
3. `delete[] ptr` 이되어 Heap 에있는 메모리가 os로 반납됨
   - 포인터는 사라진 배열의 주소를 갖고있는 상태임 
   - `ptr = nullptr;` 를 넣어서 포인터가 갖고있는 주소를 없애는 방법으로 문제를 방지할수있음

___

**delete 를 안하는 경우**

```cpp
#include <iostream>

void initArray()
{
	int* ptr2 = new int[1000];
	// delete [] ptr2
}
int main()
{
	initArray();

	return 0;
}
```

1. `main()` 실행됨
2. `initArray()` 이 실행되고 `int* ptr2` 포인터가 stack 에 자리저장됨
3. Heap 에 `sizeof(int ) * 1000 Bytes` 의 배열이 저장됨
4. `initArray()` 가 끝나면 stack 에있던 `int* ptr2` 가 사라져버림
   - Heap 메모리 에는 `sizeof(int ) * 1000 Bytes` 가 남아있긴 하지만 주소를 알수없어 사용할 수 없는 데이터가 됨

- Heap 메모리도 쓸데없는 메모리로 꽉차서 문제가 생김 작은 메모리라도 이런식으로 메모리 누수가 반복되면 다른프로그램이 사용할 메모리를 잠식해버려 문제가 생김

### **🌱 std vector 를 스택처럼 사용하기**

- 동적 할당 메모리를 직접 관리하는것보다 std::vector를 사용하면 편함

**배열의 사이즈에 맞춰서 for-each문을 돌아 요소들을 출력해주는 코드**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	std::vector<int> v{ 1,2,3 };

	for (auto &e : v)
		cout << e << " ";
	cout << endl; // 1 2 3

	cout << v.size() << endl; // 3

	return 0;
}
```


- 백터안엔 메모리에 대한 포인터 외의 사이즈를 관리하는 변수가 또있고 여러가지 기능들이 들어가있음

- vector
  - size
  - capacity: 용량을 뜻함
- capacity 갯수만큼 메모리를 갖고 size 만큼 메모리를 사용한다는 느낌임


- 힙은 메모리를 어디에 저장할지 오래걸림   
  - new,delete 많이 사용안하는게 좋음   

- 백터를 잘사용하는 방법은 new,delete를 적게 호출하는 방법을 생각하고 사용하는 것임

___


**resize**

**resize 로 배열 늘리기**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	std::vector<int> v{ 1,2,3 };

	v.resize(10);

	for (auto &e : v)
		cout << e << " ";
	cout << endl; // 1 2 3 0 0 0 0 0 0

	cout << v.size() << " " << v.capacity() << endl; // 10 10

	return 0;
}
```

**resize 로 배열 줄이기**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	std::vector<int> v{ 1,2,3 };

	v.resize(2);

	for (auto &e : v)
		cout << e << " ";
	cout << endl; // 1 2

	cout << v.size() << " " << v.capacity() << endl; // 2 3

	cout << v[2] << endl; // runtime Error
	cout << v.at(2) << endl; // runtime Error

	// 억지로 가져오기
	int* ptr = v.data();

	cout << ptr[2] << endl; // 3

	return 0;
}
```
- 용량은 3을 유지하고 출력할때는 2만 출력해주는것
- 포인터로 억지로 갖고온 것
- 3개를 2개로 줄일때 os 한테 2개를 받아놓고 3개짜리 원래 메모리를 delete로 지우면 깔끔함
  - vector는 설계가 될때 속도를 중시하여 더 작은쪽으로 resize를 할때 메모리를 반납하고 지우는 걸 하면 느려지니까 메모리는 갖고있고 원래 데이터를 숨기고있는 것임
- vector 는 실제 갖고있는 데이터와 사용하는 데이터가 다르다는 뜻임


**모던 C++ 방식**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	std::vector<int> v{ 1,2,3 };

	v.resize(2);

	for (unsigned int i = 0; i < v.size(); ++i)
		cout << v[i] << " ";
	cout << endl; // 1 2

	cout << v.size() << " " << v.capacity() << endl; // 2 3


	int* ptr = v.data();

	cout << ptr[2] << endl;

	return 0;
} 
```

- 모던 C++ 에선 주로 unsigned 를 사용했었음

___

**reserve**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	std::vector<int> v{ 1,2,3 };

	v.reserve(1024);

	for (unsigned int i = 0; i < v.size(); ++i)
		cout << v[i] << " ";
	cout << endl; // 1 2 3 

	cout << v.size() << " " << v.capacity() << endl; // 3 1024


	int* ptr = v.data();

	cout << ptr[2] << endl; // 3

	return 0;
}
```
- `v.reserve();` 메모리의 용량을 미리 확보해 놓겠다는 뜻임
- size는 그대로고 capacity가 늘어남
- 뒤에 원소가 추가될때 reserve된 공간이 많이 남아있으면 새로 메모리를 가져오고 바꾸고 하는 동작을 안해도되서 훨씬 빠름

___

**vector 로 stack 구현 코드**

```cpp
#include <iostream>
#include <vector>

using namespace std;

void printStack(const std::vector<int>& stack)
{
	for (auto& e : stack)
		cout << e << " ";
	cout << endl;
}	


int main()
{
	std::vector<int> stack;

	/*stack.reserve(1024);*/

	stack.push_back(3);
	printStack(stack); //3

	stack.push_back(5);
	printStack(stack); // 3 5

	stack.push_back(7);
	printStack(stack); // 3 5 7

	stack.pop_back();
	printStack(stack); // 3 5

	stack.pop_back();
	printStack(stack); // 3

	stack.pop_back();
	printStack(stack); // 

	return 0;
}
```

- 재귀 호출할때 스택오버플로우가 발생함 
  - 백터를 스택으로 사용하고 reserve 를 사용함
- stack
  - push
  - pop
- reserve 를 해놓으면 push(100)을 할때 capacity를 늘릴 필요가 없기 때문에 new 하고 delete 를 안해도 되서 효율이 좋아짐 pop 할때는 capacity는 유지한채로 pop을해서 size만 줄어들게되어 효율이 좋음
- reserve를 너무 크게해놓으면 capacity를가 너무커서 메모리가 낭비될 수 있음
  - gpu
  - 빅데이터

### **🌱 7.12 재귀적 함수 호출**

- Recursice Function Call
  - recursion 이라고함

**recursion 기본 예제 코드**

```cpp
#include <iostream>
#include <vector>

using namespace std;

void countDown(int count)
{
	cout << count << endl;
	countDown(count - 1);

}

int main()
{
	countDown(5);

	return 0;
}
```

- 자기가 자기를 호출함
- 함수를 호출할때는 그 메모리의 주소를 가지고 호출함
  - 같은 코드를 따로따로 실행시킴
- 이게 가능한 이유는 코드를 다른데 저장되어있고 함수를 호출할때에는 주소를 보고가는거라서 어떤 함수가 메모리에서 cpu로 올라가서 cpu에서 호출하는 동안에 주소로 다른 함수를  호출시키는건지 자기자신을 시키는건지 상관없어서 가능함
- **종료하는 조건**을 반드시 있어야함
- recursion 을 너무많이 하면 stack over flow 가 발생함
  - stack이 너무많이쌓이기때문임
  - std vector를 array 처럼사용하여 예방할수 있음

___

**recursion으로 재귀적으로 더하기**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int sumTo(int sumto)
{
	if (sumto <= 0)
		return 0;
	else if (sumto <= 1)
		return 1;
	else
	{
		const int sum_minus_one = sumTo(sumto - 1);
		return sum_minus_one + sumto;
	}
		
}

int main()
{

	cout << sumTo(10) << endl; // 55
	
	return 0;
}
```

- 자주사용하는 경우 **피보나치 수열** 을 많이씀
- Iteration 은 for문과 같은 반복
- recursion 은 위와같은 재귀적
  - 구현하기 더 쉽지만 stack 을 사용해야하기때문에 호출하는 depth 가 한계가 있기때문에 Iteration로 바꿔 사용하는 편이 좋음
  - 퍼포먼스가 중요할때 사용하지않는것이 좋음

### **🌱 7.13 방어적 프로그래밍의 개념**

- Defensive Programming

- 오류가 있다면 컴파일러가 잡아줄수 있을도록 코딩하는게 좋음

___

**syntax error**
  - 문법 오류


```cpp
#include <iostream>

using namespace std;

int main()
{
	int x // error

	return 0;
}
```

___

**semantic errors**
  - 문맥 오류, 의미 오류

**논리 오류**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x;
	cin >> x;

	if (x >= 5)
		cout << "x is freater then 5" << endl;
	
	return 0;
}
```

- 5 를 입력해도 `=`때문에 출력이됨

___

**violated assumption**
  - 가정을 위반함
  - 사용자가 내가 작성한것과 전혀 다른방식으로 사용됨

```cpp
#include <iostream>

using namespace std;

int main()
{
	string hello = "Hellom my name is Jack jack";

	int ix;
	cin >> ix;

	cout << hello[ix] << endl;
	
	return 0;
}
```

- 사용자가 문자열의 길이보다 많은 길이를 입력하면 런타임에러 발생함

**개선 코드**

```cpp
#include <iostream>

using namespace std;

int main()
{
	string hello = "Hellom my name is Jack jack";

	cout << "Input from 0 to " << hello.size() - 1 << endl;

	while (true)
	{
		int ix;
		cin >> ix;

		if (ix >= 0 && ix <= hello.size() - 1)
			{
				cout << hello[ix] << endl;
				break;
			}
		else
			cout << "Please try again" << endl;
	}

	return 0;
}
```

___

**문자열 출력**

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()

{

	string hello = "Hello, my name is Jack Jack";

	cout << hello << endl;

	cout << &hello[0] << endl;

	cout << &hello[1] << endl;

	cout << &hello[2] << endl;

	return 0;

	/*
	->

	Hello, my name is Jack Jack

	Hello, my name is Jack Jack

	ello, my name is Jack Jack

	llo, my name is Jack Jack
	*/
}
```

- cout 에서 문자열 특성항 `\0` 을 만날때까지 출력 하도록 되어있음
- `&hello[2]` 는 `l` 을 가르키게되고 여기서부터 `\0` 을 만날때까지 출력하여 위와같은 출력을 내게됨  

### **🌱 7.14 단언하기 assert**

- 컴파일러 도움을 받을때 사용 

**기본적인 사용법**

```cpp
#include <iostream>
#include <cassert> // assert.h

using namespace std;

int main()
{
	assert(false);

	return 0;

}
```

- run time error 
  - 어디서 에러났는지 알려줌
- release 모드에서는 작동하지않음
- Debug mode 에서만 프로그래머가 테스트할때 사용할수 있음
- 옵션 - C/C++ - 전처리기 - 전처리기 정의 
  - Debug 설정이 되어있으면 assert 가 작동을 안함
- 모드에 따라 작동 할수도 있고 안할수도 있음

**예제 1**

```cpp
#include <iostream>
#include <cassert> // assert.h

using namespace std;

int main()
{
	const int number = 5;

	//...
	//number should be 5
	assert(number == 5);

	return 0;

}
```

- 주석만 남겨놓으면 결국은 프로그래머가 찍어봐야함
- 주석대신 `assert()` 를 해놓으면 디버그모드에선 오류를 잡아주고 릴리즈 모드에선 `assert()` 를 실행을 안시킴
  - `assert()` 실행 시키는 것도 연산량을 먹기 때문에 느려짐 릴리즈모드에서는 가급적 프로그램이 빠르게 실행되야되기 때문에 릴리즈모드에서는 실행을 안함 

**예제 2**

```cpp
#include <iostream>
#include <cassert> // assert.h
#include <array>

using namespace std;

void printValue(const std::array<int, 5>& my_array, const int& ix)
{
	assert(ix >= 0);
	assert(ix <= my_array.size() - 1);

	std::cout << my_array[ix] << std::endl;
}

int main()
{
	std::array<int, 5> my_array{ 1,2,3,4,5 };

	printValue(my_array, 100);

	return 0;

}
```

- Assertion failed: ix <= my_array.size() - 1, file C:\Users\JSY\Desktop\Github\myfirstHelloWorld\myfirstHelloWorld\소스.cpp, line 10
- 위와같이 어디서 무엇때문에 에러가났는지 알려줌
- 보통 쪼게서 사용함
- 런타임에 체크해줌

___

**static asesrt**

```cpp
#include <iostream>
#include <cassert> // assert.h
#include <array>

using namespace std;

int main()
{
	int x = 5;

	// x = 10;

	assert(x == 5);
	static_assert(x == 5, "x should be 5"); // Error

	return 0;
}
```

- 컴파일 타임에 에러가 발생하게 끔 할수 있음
- 문구를 남길수 있음
- `x = 10;` 과 같이 값이 변경될 가능성이 있으면 Error 사용못함
- 변수가 const 인경우 사용할 수 있음

### **🌱 7.15 명령줄 인수 command line arguments**

```cpp
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	for (int count = 0; count < argc; ++count)
	{
		cout << argv[count] << endl;
	}

	return 0;
}
```

- os가 메인함수를 호출할때 2가지를 넣을 수 있음
- `argc` 는 갯수
- `*argv[]` 은 내용 
- 위 프로그램 실행시 실행파일 이름이 뜸


**cmd**
- cmd 에서 exe프로그램 실행시 실행시킨 명령문이 출력이됨

___

**string 으로 출력하기**

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	for (int count = 0; count < argc; ++count)
	{
		std::string argv_single = argv[count];
		cout << argv_single << endl;
	}

	return 0;
}
```

___

**숫자 자료형 변환 방법**

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	for (int count = 0; count < argc; ++count)
	{
		std::string argv_single = argv[count];

		if (count == 1)
		{
			int input_number = std::stol(argv_single);
			cout << input_number +1 << endl;
		}
		else
			cout << argv_single << endl;
	}

	return 0;
}
```

- `std::stol()` 를 사용 하여 정수로 바꿀수 있음
___

**단점**

- 사용자가 입력을 잘못 했을때마다 오류처리를 매번 자세히 해줘야함
  - boost 라이브러리
    - 준표준
    - Program_options
- 갯수가 안맞게 입력시 문제됨

### **🌱 7.16 생략부호 Ellipsis**

**count 갯수 만큼의 인수를 평균을 내주는 코드**

```cpp
#include <iostream>
#include <cstdarg> // for ellipsis

using namespace std;

double findArerage(int count, ...)
{
	double sum = 0;

	va_list list;

	va_start(list, count);

	for (int arg = 0; arg < count; ++arg)
		sum += va_arg(list, int);

	va_end(list);

	return sum / count;
}

int main()
{
	cout << findArerage(1, 1, 2, 3, "Hello", 'c') << endl; // 1
	cout << findArerage(3, 1, 2, 3) << endl; // 2
	cout << findArerage(5, 1, 2, 3, 4, 5) << endl; // 3
	cout << findArerage(10, 1, 2, 3, 4, 5) << endl; // 3.25651e+08

	return 0;
}
```

- 매개변수 갯수가 정해져있지않았으면 좋겠다고 생각 할때 사용
- 함수 파라메타에 `...` 을 넣어주면됨
- 파라메타의 갯수를 알려줘야 함
	- 첫번쩨 인수의 값만큼만 적용됨
	- 인수 갯수 보다 더 높은 값을 적어주면 오류가 발생함
- 어떤 타입으로 들어갈지 미리 정해 줘야함


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)