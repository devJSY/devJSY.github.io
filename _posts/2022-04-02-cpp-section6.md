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

### **🌱 6.3 배열과 반복문**

- 배열은 같은 타입의 데이터가 메모리안에 일렬로 쭉 나열되어있음

**#1 정수 나눗셈**

```cpp
#include <iostream>

using namespace std;


int main()
{
	const int num_students = 5;
	int score0 = 84;
	int score1 = 92;
	int score2 = 76;
	int score3 = 81;
	int score4 = 56;

	int total_score = score0 + score1 + score2 + score3 + score4;

	double avg_score = static_cast<double>(total_score) / num_students;
	//Note: double(total_score) / num_students != double(total_score / num_students);

	return 0;
}
```

- int 형 의 나누기 계산은 버림을 하기때문에 값이 다를수 있음
- 캐스팅한다음에 나눠야 데이터가 제대로나옴

___

**#2 정수 나눗셈 에제코드 for문으로 바꾸기**

```cpp
#include <iostream>

using namespace std;


int main()
{
	const int num_students = 5;
	int scores[num_students] = { 84,92,76,81,56 };

	int total_score = 0;

	for (int i = 0; i < num_students; ++i)
	{
		total_score += scores[i];
	}

	double avg_score = static_cast<double>(total_score) / num_students;
	//Note: double(total_score) / num_students != double(total_score / num_students);

	return 0;
}
```

**#3 sizeof로 num_students 크기 지정**

```cpp
#include <iostream>

using namespace std;


int main()
{
	/*const int num_students = 5;*/
	int scores[] = { 84,92,76,81,56 };

	const int num_students = sizeof(scores) / sizeof(int);

	int total_score = 0;

	for (int i = 0; i < num_students; ++i)
	{
		total_score += scores[i];
	}

	double avg_score = static_cast<double>(total_score) / num_students;
	//Note: double(total_score) / num_students != double(total_score / num_students);

	return 0;
}
```

- `#2` 코드를 이런식으로 바꾸면 `num_students` 의 사이즈를 연산하여 할당받게 만들 수 있음
- **함수파라메타로 넘어갈때** 포인터 주소만 넘어감으로 비트별로 엉뚱한 숫자가 나올수 있음
- 파라메터로 array를 보낼떈 첫 주소와 엘리먼트의 수 까지 같이 보내야함
- 동적 할당을 사용하게되면 실험데이터를 손으로 입력안해도됨

___

**array 원소중 max 값 찾기**

```cpp
#include <iostream>

using namespace std;


int main()
{
	/*const int num_students = 5;*/
	int scores[] = { 84,92,76,81,56 };

	const int num_students = sizeof(scores) / sizeof(int);

	int max_score = 0;
	int total_score = 0;

	for (int i = 0; i < num_students; ++i)
	{
		total_score += scores[i];

		max_score = (max_score < scores[i]) ? scores[i] : max_score; // 1

		if (max_score < scores[i]) // 2
			max_score = scores[i];
	}

	double avg_score = static_cast<double>(total_score) / num_students;
	//Note: double(total_score) / num_students != double(total_score / num_students);

	return 0;
}
```

- `#1` 비교 연산자 사용
- `#2` if 문 사용

- `for (int i = 0; i < num_students; ++i)` 를
`for (int i = 0; i <= num_students; ++i)` 과같이 `=` 를 붙이면 런타임 에러가 발생할 수 있음


### **🌱 6.4 배열과 선택 정렬 selection sort**


- 순서를 맞춰주는걸 정렬 (sorting) 이라고함
- index: 배열에 저장되어있는 위치 
- value: 배열에 저장되어있는 값 

**swap**

```cpp
#include <iostream>

using namespace std;

void printAarry(const int array[], const int length)
{
	for (int index = 0; index < length; ++index)
		cout << array[index] << " ";
	cout << endl;
}

int main()
{
	const int length = 5;

	int array[length] = { 3,5,2,1,4 };

	printAarry(array, length);

	// swap
	int temp = array[0];
	array[0] = array[1];
	array[1] = temp;

	printAarry(array, length);
	// std::swap(...)

	return 0;
}
```

- 배열의 원소의 위치를 서로 바꾸는 방법
- `std::swap()` 이 있음

___

**선택정렬**

- **선택정렬:**  현재 index를들고 배열의 index를 쭉 둘러보면서 목표로하는값 과 자리를 스왑핑 하는 동작을 indx 요소만큼 반복하여 정렬하는 방식
- 선택정렬가 이해되면 버블정렬 연습해보기

**내가짠 선택정렬 코드**

```cpp
#include <iostream>

using namespace std;

void printAarry(int array[], int length)
{

	for (int index = 0; index < length; ++index)
	{
		int temp = array[index];
		for (int j = 0; j < length; ++j)
		{
			if (array[index] < array[j])
			{
				temp = array[index];
				array[index] = array[j];
				array[j] = temp;
			}
		}

		cout << array[0] << array[1] << array[2] << array[3] << array[4] << endl;
	}
}

int main()
{
	const int length = 5;

	int array[length] = { 3,5,2,1,4 };

	printAarry(array, length);

	return 0;
}
```

**선택정렬 예제코드**

```cpp
#include <iostream>

using namespace std;

void printAarry(const int array[], const int length)
{
	for (int index = 0; index < length; ++index)
		cout << array[index] << " ";
	cout << endl;
}

int main()
{
	const int length = 5;

	int array[length] = { 3,5,2,1,4 };


	for (int startIndex = 0; startIndex < length - 1; ++startIndex)
	{
		int smallestIndex = startIndex;

		for (int currentindex = startIndex + 1; currentindex < length; ++currentindex)
		{
			if (array[smallestIndex] > array[currentindex])
			{
				smallestIndex = currentindex;
			}
		}

		// swap twovalues in the array
		// std::swap(array[smallestIndex], array[startIndex]);
		{
			int temp = array[smallestIndex];
			array[smallestIndex] = array[startIndex];
			array[startIndex] = temp;
		}
		
		printAarry(array, length);
	}

	return 0;
}
```

- `startIndex < length - 1;`
  - `-1` 을 해주는 이유는 마지막꺼는 비교할 대상이 없기 때문에 연산을 안해도 되기 떄문임
- Index만 바꿔주면 value 는 알아서바뀌기 때문에 굳이 따로 저장안해줘도됨

### **🌱 6.5 정적 다차원 배열**

- 정적 다차원 배열Multi-dimensional array
- 컴퓨터속 메모리는 일차원적인 주소 공간을 가짐

___

**정적 다차원 배열 예제 코드**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_rows = 3;
	const int num_colnums = 5;

	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_colnums; ++col)
			cout << '[' << row << ']' << '[' << col << ']' << '\t';

		cout << endl;

	}

	cout << endl;

	return 0;
}
```

- 세로 - column
- 가로 - row
- 이미지 처리, 딥러닝에 자주 사용됨

___

**다차원배열 선언 방법**

```cpp
	// 1
	int array[num_rows][num_colnums]; // row-major <-> column-major
	array[0][0] = 1;
	array[0][1] = 2;

	// 2
	int array[num_rows][num_colnums] =
	{
		{1,2,3,4,5}, // row 0
		{6,7,8,9,10}, // row 1
		{11,12,13,14,15} // row 2
	};

	// 3 copy initializing 
	int array[num_rows][num_colnums] 
	{
		{1,2,3,4,5}, // row 0
		{6,7,8,9,10}, // row 1
		{11,12,13,14,15} // row 2
	};
```

- `#3` C++ 11 이후 컴파일러에서만 사용가능

**초기화값 안넣어주기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_rows = 3;
	const int num_colnums = 5;

	int array[num_rows][num_colnums] 
	{
		{1,2,}, // 1,2,0,0,0
		{6,7,8,9,10}, // row 1
		{11,12,13,14,15} // row 2
	};

	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_colnums; ++col)
			cout << array[row][col] << '\t';

		cout << endl;

	}

	return 0;
}
```

- `{1,2,}` 초기화를 안해주면 0값으로 자동으로 들어감

**rows 생략**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_rows = 3;
	const int num_colnums = 5;

	int array[][num_colnums] 
	{
		{1,2,}, // row 0
		{6,7,8,9,10}, // row 1
		{11,12,13,14,15}, // row 2
	};

	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_colnums; ++col)
			cout << array[row][col] << '\t';

		cout << endl;

	}

	return 0;
}
```

- `int array[][num_colnums]`  num_rows는 생략할 수 있음
- `{}` 에서 선언 했기 때문에 컴파일러가 알아서 세줌
- `num_colnums` 는 생략안됨
- 나중에 동적 할당 때 포인터로 array를 넣음

**전부 0으로 초기화**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_rows = 3;
	const int num_colnums = 5;

	int array[num_rows][num_colnums] = {0};


	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_colnums; ++col)
			cout << array[row][col] << '\t';

		cout << endl;

	}

	return 0;
}
```
___

**다차원 배열 출력하기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_rows = 3;
	const int num_colnums = 5;

	int array[num_rows][num_colnums] 
	{
		{1,2,3,4,5}, // row 0
		{6,7,8,9,10}, // row 1
		{11,12,13,14,15} // row 2
	};

	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_colnums; ++col)
			cout << array[row][col] << '\t';

		cout << endl;

	}

	return 0;
}
```

___

**다차원 배열의 메모리 주소**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int num_rows = 3;
	const int num_colnums = 5;

	int array[num_rows][num_colnums] 
	{
		{1,2,3,4,5}, // row 0
		{6,7,8,9,10}, // row 1
		{11,12,13,14,15} // row 2
	};

	for (int row = 0; row < num_rows; ++row)
	{
		for (int col = 0; col < num_colnums; ++col)
			cout << int(& array[row][col]) << '\t';

		cout << endl;

	}

	return 0;
}
```

- 메모리가 4byte 단위로 쭉 이어임
- 메모리가 일자로 쭉 나열되어 있음
- 일제로는 일차원임
- 동적할당시 유용함

___

**3차원 array**

```cpp
int array[5][4][3];
```

- 딥러닝 에서 다차원배열로 텐서를 표현함
- 2차원 array 는 행렬임
  - 컴퓨터 시뮬레이션
  - 그래픽스

### **🌱 6.6 C언어 스타일의 배열 문자열**

```cpp
#include <iostream>

using namespace std;

int main()
{
	char myString[] = "string"; // 7칸
	for (int i = 0; i < 7; ++i)
	{
		cout << (int)myString[i] << endl;
	}

	cout << sizeof(myString) / sizeof(myString[0]) << endl; // 7

	return 0;
}
```

- string 문자가 6글자인데 7개의 메모리를 잡아먹는 이유
- 문자열이 마지막이라는 null char가 들어가있음
  - `\0` 이 문자열끝에 들어가있어서 7칸임

___

**cin으로 입력받고 cout으로 출력하기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	char myString[255];

	cin >> myString;

	myString[0] = 'A'; // 첫번째 문자 A로 강제 변경

	cout << myString << endl;

	return 0;
}
```

- 배열하고 똑같은 방식으로 처리함
- 다만 데이터타입이 문자형

___

**cout의 성질**

```cpp
#include <iostream>

using namespace std;

int main()
{
	char myString[255];

	cin >> myString;

	myString[5] = '\0'; 

	cout << myString << endl;

	return 0;
}
```

- 5 이후의 문자는 짤림
- cout 이 문자열을 출력한다는 개념이아니고 `'\0'` 이 나올때까지 출력함 

___

**cin 빈칸입력받고 출력하기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	char myString[255];

	cin.getline(myString, 255);

	cout << myString;

	return 0;
}
```

- geline() 으로 입력받고 출력할 수 있음
- 빈칸과 `\0` 은 다름

___

**빈칸의 아스키코드**

```cpp
#include <iostream>

using namespace std;

int main()
{
	char myString[255];

	cin.getline(myString, 255);

	

	int ix = 0;

	while (true)
	{
		if (myString[ix] == '\0') break;

		cout << myString[ix] << " " << int(myString[ix]) << endl;
		++ix;
	}

	return 0;
}
```

- 입력받은 라인과 해당하는 아스키코드를 보여주는 코드임
- 빈칸은 **아스키코드 32번**인걸 확인할 수 있음

___

**`strcpy()` 로 배열 복사**

```cpp
#include <iostream>
#include <cstring>
#pragma warning(disable:4996)

using namespace std;

int main()
{
	char source[] = "Copy this!";
	char dest[50];
	strcpy(dest, source);

	cout << source << endl;
	cout << dest << endl;

	return 0;
}
```

- `char *` 은 포인터임
- 원본은 바꾸지않고 복사하는 함수임
- `#pragma warning(disable:4996)` c++ 내부적으로 위험하다고 에러가떠서 이구문으로 에러를 무시처리하였음
- `strcpy()` 가 위험한 이유
  - 메모리를 침범해서 런타임 에러가 발생할 수 있음
___

**`strcpy_s()` 로 배열 복사**

```cpp
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	char source[] = "Copy this!";
	char dest[50];
	strcpy_s(dest, 50, source); 

	cout << source << endl;
	cout << dest << endl;

	return 0;
}
```

- `#pragma warning(disable:4996)`  를 사용하지않고 에러가 안뜨게끔 수정한 코드
- 함수의 인수값중 가운데 `50` 값은 최대 메모리를 복사할수있는 메모리사이즈를 적어주는것

___

**`strcat()`**

```cpp
#include <iostream>
#include <cstring>
#pragma warning(disable:4996)

using namespace std;

int main()
{
	char source[] = "Copy this!";
	char dest[50];
	strcpy_s(dest, 50, source); 

	strcat(dest, source);

	cout << source << endl;
	cout << dest << endl;

	return 0;
}
```

- strcpy_s 에서 문자를 한번 복사하고 strcat으로 문자열을 한번더 붙여줌
- 한문자열 뒤에다가 어떤 문자열을 붙여주는 것

___

**`strcmp()`**

```cpp
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	char source[] = "Copy this!";
	char dest[50];
	strcpy_s(dest, 50, source); 

	cout << strcmp(source, dest) << endl;

	return 0;
}
```

- strcmp - string  compare 
- 같으면 `0` 을 반환 
- 다르면 `-1`을 반환
- 실전에선 `std:string`을 많이사용함

### **🌱 6.7 포인터의 기본적인 사용법**

- 지역 변수는 스택 메모리를 사용
- 동적 할당 메모리는 힙 메모리를 사용
- `int x = 5;`  변수를 선언한다는건 변수가 사용할 메모리공간을 os로부터 빌려옴 그 메모리공간에 5 라는 값을 복사해서 넣는 것임
- 큰 메모리에 저장되어 있는 데이터 중에서 일부분을 cpu가 사용하기 위하여 메모리로부터 가져올 때는 메모리 전체를 모두 뒤지면서 찾는 것이 아니라 필요한 데이터가 저장되어 있는 주소를 사용하여 직접 접근하여 가져옴
- `&` address-of operator 
	- 메모리 주소 출력 연산자
	- 기본 16진수로출력, 캐스팅해서 바꿀수 있음
- 메모리 주소를 담는 변수를 포인터라고함
- `*` de-reference operator 
- 포인터는 reference의 일부임
- C++에서는 reference 와 포인터가 있음
- de-reference는, 포인터가 "저쪽 주소에 가면 이데이터가 있어요" 라고 간접적으로 가리키기만 하는것에 대해서, "그럼 거기에 진짜 뭐가 있는지 내가 들여다볼께" 라며 직접적으로 접근하겠다는 의미임

___

**메모리 주소의 value**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 5;

	cout << *&x << endl;

	return 0;
}
```

- 메모리 주소에 담겨있는 실제 값을 보여줌
- 메모리 주소를 갖고오고 메모리의 위치로가서 값을 가져온 것임

___

**포인터:** 메모리 주소를 담는 변수임
- 포인터도 데이터형은 갖고있음

**포인터 기본 문법**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 5;
	int* ptr_x; 
	ptr_x = &x; // int* ptr_x = &x;

	cout << *&x << endl;

	return 0;
}
```

- `*` 는 파라메타로 넣어줄때는 양쪽을띄우기
- 보통은 변수명앞에 `*` 을 많이 붙임

___

**포인터 초기화시 주의사항**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 5;
	
	typedef int* pint;
	int *ptr_x = &x, ptr_y = &x; // 1
	pint ptr_x = &x, ptr_y = &x; // 2

	return 0;
}
```

- 1의 ptr_y 는 포인터가 아님
- `*ptr_y = &x;` 이런식으로 지정해줘야 포인터 변수임
- 대부분 typedef 보다는 각각 포인터 선언해줌
- 포인터 변수명앞에 `*` 붙이기
- 두번쨰,세번째... 포인터 선언시 `*` 붙여주기

___

**함수 포인터 선언**

```cpp
#include <iostream>

using namespace std;

int* dosomething(int* ptr_a)
{
	return nullptr;
}

int main()
{
	int x = 5;
	
	int *ptr_x = &x, * ptr_y = &x;


	return 0;
}
```

- 함수의 리턴값, 파라메타로 포인터 설정 가능

___

**포인터 찍어보기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 5;
	
	int *ptr_x = &x, * ptr_y = &x;

	cout << ptr_x << endl; // 010FFCA4
	cout << *ptr_x << endl; // 5

	return 0;
}
```

- 포인터에 저장되는건 **변수의 주소**임
- 포인터가 데이터 타입을 알아야하는 이유는 de-reference 할때 어떤 자료형으로 가져올지 헷갈리니까 지정해주는 것
- 배열에 데이터가 파라메타로 넣어주면 전부 복사가됨 
  - 포인터로 첫번째 주소와 몇개의 데이터인지 알려줌
- 변수를 그자체로 사용할때 포인터 주소로 보내면 더 좋음
- 다른언어도 내부적으로 포인터를 사용함 
- 타입이 다른 변수를 포인터에 넣을순 없음
- 포인터를 사용자정의 자료형에도 사용할 수 있음
- 직접적으로 메모리주소를 변수에 넣을순없음

___

**`<typeinfo>`로 포인터 찍어보기**

```cpp
#include <iostream>
#include <typeinfo>

using namespace std;

int main()
{
	int x = 5;
	double d = 123.;

	int* ptr_x = &x;

	cout << typeid(ptr_x).name() << endl; // 5

	return 0;
}
```

- gcc 에서는 다르게나옴
  - pi
    - pointer to id 의 약자

___

**포인터의 사이즈**

```cpp
#include <iostream>
#include <typeinfo>

using namespace std;

struct Something
{
	int a, b, c, d;
};

int main()
{
	int x = 5;
	double d = 123.0;

	int* ptr_x;
	double *ptr_d;

	cout << sizeof(x) << endl; // 4
	cout << sizeof(d) << endl; // 8
	cout << sizeof(&d) << " " << sizeof(ptr_x)<< endl; // 8
	cout << sizeof(&d) << " "<< sizeof(ptr_d) <<endl; // 8

	Something ss;
	Something* ptr_s;

	cout << sizeof(Something) << endl; // 16
	cout << sizeof(ptr_s) << endl; // 8


	return 0;
}
```

- 포인터 자체사이즈는 고정임
  - 모든 타입에 대해서 사이즈가 동일함

- 주소는 int던 double던 4byte임
  - 32비트 기준임
- 64비트에서는 주소를 더 길게사용하기 떄문에 8byte로 뜸

___

**주의사항**

```cpp
#include <iostream>
#include <typeinfo>

using namespace std;

int main()
{
	int x = 5;
	double d = 123.0;

	int *ptr_x;
	double *ptr_d;

	cout << *ptr_x << endl; // Error

	return 0;
}
```

- ptr_x 를 초기화하지않고 주소를 접근하라고하니 에러가 발생함


### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)