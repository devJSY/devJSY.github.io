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
last_modified_at: 2022-04-13
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

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **







# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)