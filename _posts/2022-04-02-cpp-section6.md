---
published: true
title:  "따라하며 배우는 C++ Section 6. 행렬,문자열,포인터,참조"
excerpt: ""

categories:
  - 따배씨++
tags:
  - [C++]

toc: true
toc_sticky: true
 
date: 2022-04-08
last_modified_at: 2022-04-08
---

# 🤔 학습목표
- 따라하며 배우는 C++ Section 6. 행렬,문자열,포인터,참조

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 6. 행렬,문자열,포인터,참조**

### **🌱 6.1 배열 기초 [1 of 2] array**

**영어에서 array:** 비슷한것들이 쭉 나열되어있는것

- 동기 
- 변수가 여러개면 관리하기힘듬


**배열의 기본 문법**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int one_student_score; // 1 variable
	int student_scores[5]; // 5 int

	cout << sizeof(one_student_score) << endl; // 4
	cout << sizeof(student_scores) << endl; // 20

  student_scores = 100; // Error
	student_scores[0] = 100; // 1st element
  student_scores[1] = 80; // 2nd element
  student_scores[3] = 90; // 3rd element
  student_scores[3] = 50; // 4th element
  student_scores[4] = 0; // 5th element
  student_scores[5] = 30; // Error

  cout << student_scores[0] << endl;
  cout << (student_scores[0] + student_scores[1]) / 2.0 << endl; // 90

	return 0;
}
```

- 대괄호 안의 5개의 int 만큼의 메모리를 한꺼번에 빌려온다는뜻
- 다붙어있는 메모리를 빌려옴
- 빅데이터등 에서 어떠한경우 너무커서 일렬로된 메모리를 못가져오는 경우가 있음
- 초기화 할때 `[]` 에다가 몇번째 원소(element) 인지 지정해줘야 초기화가능
- `[0]`를 인덱스, 서브스크립트 라고부름
  - 대부분 0부터 시작함
- 배열을 초과하는 원소에 접근할 경우 **런타임 에러** 가 발생할수 있음
- 디버그 모드에서 런타임에러 발생시 Retry 버튼을 눌러서 추적할 수 있음
- 배열을 어떠한 변수 처럼 사용할 수 있음

___

**구조체의 array**

```cpp
#include <iostream>

using namespace std;

struct Rectangle
{
	int length;
	int width;

};

int main()
{
	
	cout << sizeof(Rectangle) << endl; // 8

	Rectangle rect_arr[10];

	cout << sizeof(rect_arr) << endl; // 80

	rect_arr[0].length = 1;
	rect_arr[0].width = 2;

	return 0;
}
```

- 배열을 함수 파라메타로 주고받을때 sizeof 가 문제가 생길수 있음

___

**array 초기화 방법**

```cpp
#include <iostream>

using namespace std;

int main()
{
	// 1
	int my_array[5];
	my_array[0] = 0;

	//2
	int my_array[5] = { 1,2,3,4,5 };
								 
	//3
	int my_array[5] = { 1,2, }; // 1, 2, 0, 0, 0

	//4
	int my_array[] = { 1,2,3,4,5 };

	//5
	int my_array[]{ 1,2,3,4,5 };

	return 0;
}
```


- 오래된 컴파일러 vs2010 등 사용시 `{}` 유니폼 이니셜라이징이 안될수 도 있음

___

**enum 과 array**

```cpp
#include <iostream>

using namespace std;

enum StudentName
{
	JACKJACK,		// = 0
	DASH,			// = 1
	VIOLET,			// = 2
	NUM_STUDENTS,	// = 3

};

int main()
{
	// 1
	int my_array[]{ 1,2,3,4,5 };

	cout << my_array[JACKJACK] << endl; // 1

	// 2
	int students_scores[NUM_STUDENTS];

	students_scores[JACKJACK] = 0;
	students_scores[DASH] = 100;

	return 0;
}
```

- JACKJACK이 0 이니까 0번째 원소인 1이 출력됨
- enum은 사람이름으로 사용하는건 권장하지 않음
  - 보통 클래스로 묶어버림
- `#2` 서브스크립트,인덱스로 배열선언을 할 수 있음

___

**주의사항**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int num_students = 0;
	cin >> num_students;

	int students_scores[num_students]; // 에러

	return 0;
}
```

- 배열의 `[]` 안에 들어가는 것이 size나 length 라고부름
  - length를 조금더 많이사용함
  - std의 vector 에서는 size를 사용
- 배열은 컴파일타임의 길이가 정의가 되어있어야함
- 배열의 length는 컴파일타임에 고정이되야함
  - 배열의 length가 cin등의 런타임에의해 결정이되면 안됨

**C스타일의 해결법**

```cpp
#include <iostream>

using namespace std;

#define NUM_SYUDENTS 100000


int main()
{
	/*int num_students = 0;
	cin >> num_students;*/

	int students_scores[NUM_SYUDENTS];

	return 0;
}
```

- C에선 이런식으로 처리함
- C++에선 동적할당을 하기때문에 이방법은 권장하지 않음

**변수로 배열의 크기를 지정하기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_students = 5;

	int students_scores[num_students];

	return 0;
}
```

- 변수로 배열의 length를 지정하려면 **const 변수** 여야함

### **🌱 6.2 배열 기초 [2 of 2] array**

**array의 메모리 주소**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_students = 5;

	int students_scores[num_students];

	cout << (int)&students_scores << endl; // 193984904
	cout << (int)&students_scores[0] << endl; // 193984904
	cout << (int)&students_scores[1] << endl; // 193984908
	cout << (int)&students_scores[2] << endl; // 193984912
	cout << (int)&students_scores[3] << endl; // 193984916

	cout << sizeof(students_scores) << endl; // 20

	return 0;
}
```

- array는 내부적으로 첫번째 주소를 갖고있음
- 한집당 4byte 씩 건너감

___

**함수의 파라메타에 array 집어넣기**

```cpp
#include <iostream>

using namespace std;

void dosomething(int students_scores[20]) // 20을 안넣어도됨
{
	cout << (int)&students_scores << endl; // -1643120552
	cout << &students_scores[0] << endl; // 0000001A49EFFC98
	cout << students_scores[1] << endl; // 2
	cout << students_scores[2] << endl; // 3
	cout << "Size of dosomething : " << sizeof(students_scores) << endl; // 8
}

int main()
{
	const int num_students = 5;

	int students_scores[num_students] = {1,2,3,4,5};

	cout << (int)students_scores << endl; // -1643120624
	cout << (int)&students_scores << endl; // -1643120624
	cout << &students_scores[0] << endl; // 0000001A49EFFC98
	cout << students_scores[1] << endl; // 2
	cout << students_scores[2] << endl; // 3
	cout << "Size of main : " << sizeof(students_scores) << endl; // 20

	dosomething(students_scores);

	return 0;
}
```

- array를 함수의 파라메타로 넣을수 있음
- main에서 사용하는 array와 함수에서 사용한 array의 **메모리 주소는 다름**
- 배열의 식별자(students_scores)가 내부적으로 **주소로 사용**됨
  - 주소 데이터를 주고받고하는것이 원소들을 전부 복사하는것보다 효과적이기 때문임
- `int students_scores[num_students] = {1,2,3,4,5};` 의 `students_scores` 는 선언될때 배열로 선언되어 **이름자체가 주소임**
  - 따라서 주소 연산자 `&`를 붙이지 않아도 주소를 찍어볼수 있음
- `void dosomething(int students_scores[20])` 은 문법상 배열이아닌 **포인터**임

- `void dosomething(int students_scores[20])` 는 배열의 모든 원소를 복사해서 가져오는 것이 아니라 `배열의 첫번째 주소값만 복사함`
  - 따라서 `students_scores` 의 주소값을 저장하는 포인터 변수이기 때문에 그자체가 **다른 주소값을 가짐**

- `students_scores[0]` 의 값이 같은 이유는 포인터변수의 주소값을 출력하기 때문임

- main 함수와 dosomething함수에서 호출한 `students_scores` 의 사이즈가 다른이유
  - main 함수에선 포인터로 사이즈가 출력됨
  - dosomething함수에선 **포인터**로 사이즈가 출력되었음
    - int의 사이즈가 아닌 포인터 사이즈임
- 64비트 → 32비트 로 바꿔서 빌드하면 포인터 변수의 사이즈가 달라짐
  - 64비트 - 4byte
  - 32비트 - 8byte

- 배열과 포인터는 붙어다님
- 배열의 인덱스,서브스크립트는 정수형데이터면 들어갈수 있음
  - char
  - long
  - int


### **🌱 **

### **🌱 **

### **🌱 **


# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)