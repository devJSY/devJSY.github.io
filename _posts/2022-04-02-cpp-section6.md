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


### **🌱 6.7a Null Pointer**

- 쓰레기 주소값이 들어간경우 de-reference 실행하게되면 엉뚱한곳에가서 데이터를 찾게되기 때문에 os에서 에러가 뜸

___

**Null 포인터 초기화 방법**

```cpp
#include <iostream>
#include <typeinfo>

using namespace std;

int main()
{
	double *ptr = 0; // c-style
	double *ptr = NULL; 
	double *ptr = nullptr; // modern c++ 
	double *ptr {nullptr};
	double *ptr {0};

	if (ptr != nullptr)
	{
		// do something useful
	}
	else
	{
		// do nothing with ptr
	}

	return 0;
}
```

-  변수와 동일하게 유니폼 이니셜라이징 도 가능함
-  nullptr 로 적어주는게 좋음

___

**Null ptr 확인 함수**

```cpp
#include <iostream>
#include <cstddef>

using namespace std;

void dosomething(double* ptr)
{

	if (ptr != nullptr)
	{
		// do something useful
		cout << *ptr << endl;
	}
	else
	{
		// do nothing with ptr
		cout << "Null ptr, do something" << endl;
	}
}

int main()
{

	double *ptr = nullptr; // modern c++ 

	dosomething(ptr); // Null ptr, do something
	dosomething(nullptr); // Null ptr, do something

	double d = 123.4;

	dosomething(&d); // 123.4

	ptr = &d;

	dosomething(ptr); // 123.4

	std::nullptr_t nptr; // null ptr 


	return 0;
}
```

___

- `#include <cstddef>` 라이브러리의 `std::nullptr_t nptr;` null ptr를 넣을 때 사용함

___

**파라메타의 메모리 주소**

```cpp
#include <iostream>
#include <cstddef>

using namespace std;

void dosomething(double *ptr)
{
	cout << "address of pointer in dosomething() " << &ptr << endl; // 012FFD28


	if (ptr != nullptr)
	{
		// do something useful
		cout << *ptr << endl;
	}
	else
	{
		// do nothing with ptr
		cout << "Null ptr, do something" << endl;
	}
}

int main()
{

	double *ptr = nullptr; // modern c++ 

	dosomething(ptr); // Null ptr, do something
	dosomething(nullptr); // Null ptr, do something

	double d = 123.4;

	dosomething(&d); // 123.4

	ptr = &d;

	dosomething(ptr); // 123.4

	cout << "address of pointer in main() " << &ptr << endl; // 012FFD3C


	return 0;
}
```

- main 함수와 dosomething함수의 `&ptr`의 주소는 **서로 다름**
- dosomething함수의 파라메타로 넘어오는 변수는 **다시 선언되고** 파라메타로 들어오는값이 복사가 되어 다른 메모리를 갖는것임

### **🌱 6.8 포인터와 정적 배열**

- 포인터와 배열의 성질은 둘다 같음

```cpp
#include <iostream>
#include <cstddef>

using namespace std;

int main()
{
	int array[5] = { 9,7,5,3,1 };

	cout << array[0] << endl; // 9
	cout << array << endl; // array의 첫번째 주소 00B8FA14
	cout << &array[0] << endl; // array의 첫번째 주소 00B8FA14
	
	cout << *array << endl; // 9

	char name[] = "jack jack";
	cout << *name << endl; // j

	int * ptr = array;
	cout << ptr << endl; // 00B8FA14 &ptr 자체주소는 다름
	cout << *ptr << endl; // 9

	return 0;
}
```

- `cout << array << endl` 에서 array는 배열이아니고 **포인터**임
  - 첫번째 byte의 주소를 담음 
- 포인터는 주소를담음 
- 적정 array == 포인터 이다.

___

**포인터의 사이즈**

```cpp
#include <iostream>

using namespace std;

//void printArray(int array[]) 아래와 동일함
void printArray(int *array)
{
	cout << sizeof(array) << endl; // 4
	cout << *array << endl; // 9

	*array = 100;
}



int main()
{
	int array[5] = { 9,7,5,3,1 };

	cout << sizeof(array) << endl; // 배열 전체의 사이즈 20

	int * ptr = array;

	cout << sizeof(ptr) << endl; // 포인터의 사이즈 4

	printArray(array); 

	cout << array[0] << " " << *array << endl; // 100 100

	return 0;
}
```

- 포인터 변수 자체의 사이즈 4
  - 64비트에서는 8
- `int arry[]` 가 내부적으로 포인터이기 때문에 포인터의 사이즈인 4가 출력되는 것
- 함수 안에서 `*array = 100;` 라고 정의하면 함수밖 array에도 100값이 적용이됨
  - c++ 에서는 레퍼런스를 더 많이 사용함
  - C에서 많이 사용함

___

**pointer Arithmetic**

```cpp
int main()
{
	int array[5] = { 9,7,5,3,1 };

	cout << sizeof(array) << endl; // 배열 전체의 사이즈 20

	int * ptr = array;

	cout << *ptr << " " <<  * (ptr + 1) << endl; // 9 7

	return 0;
}
```

- 포인터에 연산을해서 `ptr +1` 이런식으로 다음 배열값을 가져올 수 있음
- pointer Arithmetic 이라고함

___


**구조체 파라메타**

```cpp
#include <iostream>

using namespace std;

struct MyStruct 
{
	int array[5] = { 9,7,5,3,1 };
};

void dosomething(MyStruct ms)
{
	cout << sizeof(ms.array) << endl; // 20
}

int main()
{
	MyStruct ms;

	cout << ms.array[0] << endl; // 9
	cout << sizeof(ms.array) << endl; // 20
	dosomething(ms);


	return 0;
}
```
- 배열 자체가 파라메타로 감
- 배열의 값인 20이 출력됨

**포인터로 강제 전환**

```cpp
#include <iostream>

using namespace std;

struct MyStruct 
{
	int array[5] = { 9,7,5,3,1 };
};

void dosomething(MyStruct *ms)
{
	cout << sizeof(( * ms).array) << endl; // 20
}

int main()
{
	MyStruct ms;

	cout << ms.array[0] << endl; // 9
	cout << sizeof(ms.array) << endl; // 20
	dosomething(&ms);


	return 0;
}
```

- 결과값은 똑같음
- 구조체나 클래스 안에있을때는 포인터로 강제 변환되지않고 배열자체가 감
- 배열을 포인터로 다 접근할 수 있음

### **🌱 6.9 포인터 연산과 배열 인덱싱**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 7;
	int* ptr = &value;

	cout << uintptr_t(ptr -1) << endl; // 16579104
	cout << uintptr_t(ptr) << endl; // 16579108
	cout << uintptr_t(ptr +1) << endl; // 16579112
	cout << uintptr_t(ptr +2) << endl; // 16579116
	
	return 0;
}
```

- 언사인드인티저 포인트 타입
- unsigned int point type
- 데이터 타입의 맞춰서 한칸식 이동함
  - double 타입이면 8 씩 이동함

**포인터에 데이터 타입을 넣어주는 이유**
1. `de-reference` 할때 어떤 데이터형으로 가져올지 정해주는것
2. 포인터 연산 할때 몇 byte인지 정해주기위해 

___

**배열의 메모리 찍어보기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int array[] = { 9,7,5,3,1 };

	cout << array[0] << " " << (uintptr_t) & array[0] << endl;
	cout << array[1] << " " << (uintptr_t) & array[1] << endl;
	cout << array[2] << " " << (uintptr_t) & array[2] << endl;
	cout << array[3] << " " << (uintptr_t) & array[3] << endl;
	
	for (int i = 0; i < 5; ++i)
		cout << array[i] << " " << (uintptr_t) & array[i] << endl;
	
	return 0;
}
```

- 배열의 메모리는 한줄로 나열되어 있음

___

**포인터로 배열의 메모리 찍어보기**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int array[] = { 9,7,5,3,1 };

	int *ptr = array;

	for (int i = 0; i < 5; ++i)
		cout << *(ptr + i) << " " << (uintptr_t)(ptr + i) << endl;

	return 0;
}
```

___

**포인터로 문자열 출력**

```cpp
#include <iostream>

using namespace std;

int main()
{
	char name[] = "jack jack";
	const int n_name = sizeof(name) / sizeof(name[0]);

	char * ptr = name;

	for (int i = 0; i < n_name; ++i)
	{
		cout << *(ptr + i);
	}
		
	return 0;
}
```

- `jack jack\0` 출력됨

### **🌱 6.10 C 스타일의 문자열 기호적 상수**

- 문자열은 문자의 배열
- 배열은 포인터와 호환이됨

**문자열 배열**

```cpp
#include <iostream>

using namespace std;

int main()
{
	char name[] = "jack jack"; // 1
	char *name = "jack jack"; // 2 Error
	const char *name = "jack jack"; // 3 기호적인 상수
		
	return 0;
}
```

- `#1` 문자열을 배열에 담는 방법
- `#2` "jack jack" 리터럴이라서 포인터에는 담을수 없음
  - 포인터는 메모리의 주소를 가르키기만 할 수 있음
- `#3` const를 앞에 붙여 기호적인 상수 개념으로 지정할 수 있음

___

**기호적 상수**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const char *name = "jack jack"; // Error
	const char *name2 = "jack jack"; // Error

	cout << (uintptr_t)name << endl; //1 5579036
	cout << (uintptr_t)name2 << endl; //2 5579036

	return 0;
}
```

- `#1` , `#2` 의 주소가 동일함
- 컴파일러가 `"jack jack"` 두개가 같으니까 같은 메모리를 사용하라고 지정해 준 것
- 앞에 const가 붙어야 기호적 상수로 사용할 수 있음


___

**리턴 타입**

```cpp
#include <iostream>

using namespace std;

const char* getName()
{
	return "Jackjack";
}

int main()
{
	const char* name = getName();
	const char *name2 = getName();

	cout << (uintptr_t)name << endl; //5579036
	cout << (uintptr_t)name2 << endl; //5579036

	return 0;
}
```

- 함수의 리턴타입으로도 기호적 상수를 사용하여 메모리주소가 동일한다는거을 확인 할 수 있음

___


**문자 포인터의 특성**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int int_arr[5] = { 1,2,3,4,5 };
	char char_arr[] = "Hello, World!";
	const char* name = "Jack Jack";

	cout << int_arr << endl; // 008FFDF8
	cout << char_arr << endl; // Hello, World!
	cout << name << endl; // Jack Jack

	return 0;
}
```

- cout 에서 문자열은 특별히 처리함
- 문자의 포인터가 들어오면 문자열로 가정함
- cout 을 만든 사람이 문자의 포인터는 C스타일의 문자의 배열일 가능성이 높다고 생각하여 주소를 출력하지않고 `\0` 을 만날때 까지 쭉 출력해줌

```cpp
#include <iostream>

using namespace std;

int main()
{
	char c = 'Q';
	cout << & c << endl; // Q숪4z

	return 0;
}
```

- C에 메모리 주소가 들어가니까 문자열로 인식하여 `\0` 이 나올때까지 쭉 출력한 것


### **🌱 6.11 메모리 동적 할당 new 와 delete**

- Dynamic Memory Allocation
- 메모리 할당 3가지
  1. static Memory Allocation
    - 전역, static 변수 등 한번만들면 프로그램이 끝날때까지 계속 메모리를 갖고있는것
  2. 자동 메모리 할당
    - 변수를 선언하거나, 정적배열을 선언했을때 블럭 밖으로 나가면 전부 사라지고 메모리가 os로 할당 되는것
  3. 동적 메모리 할당

___


**정적 메모리 할당 에러**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int array[10000000]; // 정적 배열 stack

	return 0;
}
```

- 정적 메모리 할당은 용량이 큰 데이터는 메모리를 할당할수 없어서 에러
- **정적으로 할당하는 메모리는 stack에 저장되고 용량이 작음**
- **동적으로 저장하는 메모리는 hip에 저장되고 용량이 큼**

___


**new**

```cpp
#include <iostream>

using namespace std;

int main()
{
	// 1
	int var;
	var = 7;

	// 2
	new int;
	int* ptr = new int;
	*ptr = 7; // 역참조

	// 3
	int* ptr = new int{7};

	cout << ptr << endl; // 00C5C1E8
	cout << *ptr << endl; // 7


	return 0;
}
```

- `new int;` int 사이즈에 맞춰서 os에게 메모리를 받아오고 그 메모리 주소를 알려줌 즉 포인터로 받아줘야함
- `#1` , `#2` 가 동일함

___

**delete**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int* ptr = new int{7};

	cout << ptr << endl; // 0095B058
	cout << *ptr << endl; // 7

	delete ptr;

	return 0;
}
```

- `delete ptr;` 을 안해도 에러가 안나는 이유
  - os가 이프로그램에게 메모리를 어디에 얼마나 줬는지 **기억**하기 떄문에 끝날때 자동으로 알아서 걷어감
- `delete ptr;` os가 알아서 걷어가기전에 반납하겠다는 뜻

- **할당받은 메모리를 os에게 돌려주는 것이 중요한 이유**
  - 빅데이터나 딥러닝을 돌릴때 컴퓨터 한대로 감당할수 없는 메모리를 사용해야함 메모리에 한번에 데이터가 안들어 갈수도있음 일부 데이터가지고 작업을하고 os에게 반납하고 다시 os에게 받아서 작업
  - 여러 프로그램들이 메모리를 다 많이 사용하고싶다면 급한애한테 먼저 주고 급한일이 끝나면 다른프로그램에게 주는 방식으로 하면 효율적임 

**delete 주의점**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int* ptr = new int{7};

	cout << ptr << endl; // 0095B058
	cout << *ptr << endl; // 7

	delete ptr;

	cout << "After delete" << endl;
	cout << ptr << endl; // 00008123
	cout << *ptr << endl; // 없음

	return 0;
}
```

- `delete ptr;` 이후에도 주소는 남아있음
  - 주소는 변수에 따로 저장하는것 으로 뜨는것 
  - 변수안의 데이터는 사라졌으니 알수없는 값이 나오거나 안나옴
  - 스마트포인터를 사용하면 해결됨


**delete 주의점 해결방법**

```cpp
delete ptr;
ptr = 0; 
ptr = NULL;
ptr = nullptr;
```
- `delete ptr;` 이후 ptr에 0, NULL, nullptr을 넣어주면 방지할 수 있음
  - 아무것도 없는 값이라고 기억해두는 것


```cpp
#include <iostream>

using namespace std;

int main()
{
	int* ptr = new int{ 7 };

	cout << ptr << endl; 
	cout << *ptr << endl; 

	delete ptr;
	ptr = nullptr;

	cout << "After delete" << endl;

	//1
	if (ptr != nullptr)
	{
		cout << ptr << endl;
		cout << *ptr << endl;
	}

	//2
	if (ptr)
	{
		cout << ptr << endl;
		cout << *ptr << endl;
	}

	return 0;
}
```

- `#1`, `#2` 의 방법으로 ptr 이 지워지지않고 의미가 있을때만 de-reference 를 하도록 할 수 있음

```cpp
#include <iostream>

using namespace std;

int main()
{
	int* ptr = new (std::nothrow) int{ 7 };

	if (ptr) 
	{
		cout << ptr << endl;
		cout << *ptr << endl;
	}
	else
	{
		cout << "Could not allocate memory" << endl;
	}

	delete ptr;
	ptr = nullptr;

	cout << "After delete" << endl;
	if (ptr != nullptr)
	{
		cout << ptr << endl;
		cout << *ptr << endl;
	}

	return 0;
}
```

-  다른프로그램이 메모리를 다쓰고 있어서 메모리를 사용할수 없는 경우가 있음
   - **해결법 1 :** 프로그램이 지워버리게 짜는 방법
   - **해결법 2 :** 다른 프로그램이 메모리를 다쓸때까지 기다렸다 할당받는 방법
- `new (std::nothrow)`  오류를 발생시키지 않고 쭉 진행시킴
- new가 실패를 하면 `new (std::nothrow)` 가 ptr에 NULL 값을 넣어줌 


___

**주의점**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int* ptr = new (std::nothrow) int{ 7 };
	int* ptr2 = ptr;

	delete ptr;
	ptr = nullptr;
	/*ptr2 = nullptr;*/
	// *ptr2 

	return 0;
}
```

- ptr2도 같이 nullptr을 넣어줘야함
- 스마트포인터라는 안전장치로 해결할순 있지만 속도가 조금 느려짐

___

**메모리 누수**

```cpp
#include <iostream>

using namespace std;

int main()
{
	// memory leak
	while (true)
	{
		int* ptr = new int;
		cout << ptr << endl;

		// delete ptr; 메모리 반납으로 해결
	}

	return 0;
}
```
- `delete ptr;` 를 안적어주면 메모리를 *ptr로 받아오고 {}가 끝날떄 사라지는 형태의 오류코드
- 메모리를 계속 만들기만 함 어딘가 갖다 놓는데 어디인지 알수도없음 
- 컴퓨터 메모리를 다시 만날 경우는 없음 같은 메모리인지 확인 할 수 없음
- 오류코드인지 확인하는 방법
  - 메모리를 할당받는 데이터가 클경우 작업관리자를 띄우고 메모리 사용량이 쭉 올라가면 어딘가 세고있다는 뜻 
- new하고 delete 가 os를 다녀와야하기 때문에 좀느림
  - new하고 delete를 적게 사용하는게 좋음

### **🌱 6.12 동적 할당 배열**

- Dynamically Allocating Arrays

- 정적 배열은 배열의 사이즈가 컴파일 타임에 결정되어 있았어야했음
- 동작 할당은 런타임에 배열의 사이즈를 정의하고 그때그때 메모리 os로 부터 받아옴

___

**정적 할당 배열 & 동적 할당 배열**

```cpp
#include <iostream>

using namespace std;

int main()
{
	// 정적 할당 배열
	const int length = 5;

	int array[length];

	// 동적 할당 배열

	int length;
	
	cin >> length;

	int* array = new int[length]; // 초기화 파트

	array[0] = 1;
	array[1] = 2;

	for (int i = 0; i < length; ++i)
	{
		cout << (uintptr_t) & array[i] << endl;
		cout << array[i] << endl;
	}

	//delete array; // 하나의 변수일떄
	delete [] array; // 배열일때


	return 0;
}
```

- 배열의 사이즈를 입력받고 주소와, value 를 출력하는 코드
  - 초기화한 0,1번 인덱스의 값이 출력되고 이외에는 쓰레기값(0) 이 출력됨

**동적 할당 배열 초기화**

```cpp
#include <iostream>

using namespace std;

int main()
{

	int length;

	cin >> length;

	int* array = new int[length] {11,22,33,44,55};
	// int* array = new int[length] ();

	array[0] = 1;
	array[1] = 2;

	for (int i = 0; i < length; ++i)
	{
		cout << (uintptr_t) & array[i] << endl;
		cout << array[i] << endl;
	}

	//delete array; // 하나의 변수일떄
	delete [] array; // 배열일때


	return 0;
}
```

- 전부 0으로 초기화 하고싶다면 **초기화 파트 코드**를 `int* array = new int[length]();` 으로 바꾸면됨
  - 배열이기 떄문에 () 안에 값을 넣을순없음 
- `{}` 유니폼 이니셜라이징으로 배열안에 값을 넣어줄수 있음
  - `int* array = new int[length] {11,22,33,44,55};`
- 입력된 숫자가 만약 유니폼 이니셜라이징의 숫자보다 적다면 에러가 발생됨 (입력값 4 가정)
  - 동적 할당시 55를 넣을려고했더니 엉뚱한 메모리 여서 메모리가 충돌이되서 에러발생
  - 부여받지못한 메모리를 사용하려해서 에러가 발생한 것

___

**동적 할당 배열 resizing**

```cpp
#include <iostream>

using namespace std;

int main()
{
	// 정적 배열 초기화
	int fixedArray[] = { 1,2,3,4,5 }; // 1

	// 동적 배열 초기화
	int* array = new int[5]{ 1,2,3,4,5 }; // 2

	delete[] array;

	return 0;
}
```

- `[5]` 안에 입력값을 넣어주지않거나 초기화한값보다 적은값을 적어주면 에러가 발생함
- 직접적으로 resizing 은 안됨
  - **resizing:** 기존 배열값에 새로운값을 추가하는 것
  1. 더큰 메모리를 받아온다음에 원래갖고있던걸 복사해서 넣고 새로추가될것을 붙여넣는 방식으로 가능함
  2. os한테 메모리를 달라고 요청하면 될수도있고 안될수도 있음
  3. vector에서 다해줌
- 동적 할당 배열도 포인터 연산을 사용해서 배열값을 접근할수 있음


### **🌱 6.13 포인터와 const**

- 일반 변수에 const를 사용해 상수를 만들수 있음

**case 1**

```cpp
#include <iostream>

using namespace std;

int main()
{
	const int value = 5;
	const int* ptr = &value;
	// *ptr = 6; 불가능

	cout << ptr << endl;

	return 0;
}
```

- 포인터를 통해서 const value 를 읽어 주소나 데이터를 가져올순 있음
  - 값을 변경 하는것은 불가능함
- `*ptr = 6;` 이 불가능한이유는 value = 6 이 안되기 떄문임
  - value 변수 cosst 선언되서 상수 이기떄문에 변경이 불가능함

___

**case 2**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 5;
	const int* ptr = &value;
	*ptr = 6; // 불가능
	value = 6; // 가능

	cout << ptr << endl;

	return 0;
}
```

- 포인터가 가르키고있는 주소에 있는 값을 바꾸지 않겠다는 의지임
- 포인터로만 못바꾸게 막는 방법임

___

**case 3**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value1 = 5;
	const int* ptr = &value1;
	*ptr = 7; // 불가능

	int value2 = 6;
	ptr = &value2; // 가능
	*ptr = 8; // 불가능

	return 0;
}
```

- 내가 가르키고 있는 주소에 있는 값을 안바꾸겠다는 것임
- ptr에 있는 주소값을 안바꾸겠다는 의미는 아님

___

**case 4**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 5;
	int* const ptr = &value;

	*ptr = 10;
	cout << *ptr << endl;

	int value2 = 8;
	ptr = &value2; // 불가능

	return 0;
}
```

- 포인터자체가 상수인 경우
- `int* const ptr`  변수로써 포인터 자체를 상수로 만드는것

___

**case 5**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 5;
	const int* const ptr; // 초기화르 안해서 에러

	return 0;
}
```

- 포인터자체가 const 선언을하여 상수가 되었으므로 초기화를 안해주면 에러가 발생함

___

**포인터 상수 선언 케이스**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 5;
	const int* const ptr = &value;
	int* const ptr2 = &value;
	const int* const ptr3 = &value;

	return 0;
}
```

- 함수 파라메타를 들어갈떄 배열을 집어넣을때 안전하게 코딩하고자 사용함
- 참조를 사용하면 타이핑하는게 쉬워지고 깔끔해짐

___

**포인터 정리**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int value = 5;
	const int* const ptr = &value;

	cout << &ptr << endl; // ptr 변수 자체의 주소
	cout << ptr << endl; // value 변수의 주소
	cout << &value << endl; // value 변수의 주소
	cout << *ptr << endl; // value 변수의 값
	cout << value << endl; // value 변수의 값

	return 0;
}
```

- 포인터를 변수의 주소값과 value 를 바라볼수있는 하나의 **변수** 라고 생각하니까 이해하기 쉬웠음

### **🌱 6.14**

### **🌱 6.15**

### **🌱 6.16**

### **🌱 6.17**

### **🌱 6.18**

### **🌱 6.19**

### **🌱 6.20**

### **🌱 6.21**

# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)