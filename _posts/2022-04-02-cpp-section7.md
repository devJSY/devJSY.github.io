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

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **







# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)