---
published: true
title:  "따라하며 배우는 C++ Section 5. 흐름제어"
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
- 따라하며 배우는 C++ Section 5. 흐름제어

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 5. 흐름제어**

### **🌱 5.1 제어 흐름 개요 (Control flow)**

- **프로그램:** cpu에게 할일을 지정해주는 것
  - 이때 cpu가 해나갈 일을 복잡하게 만들수 있음
- 순서도 (Flow chart)
  - 흐름이 일렬로 쭉가는걸 시퀀셜 플로우 라고함

 **제어 흐름(Control flow)**
1. 중단 (Halt)
2. 점프 (Jump) 
   - goto
     - 많이 사용하진 않음
   - break
   - continue 
3. 조건 분기 (Conditional branches)
   - if
   - switch 
4. 반복(루프 Loops)
   - while
   - do while
   - for 
5. 예외 처리 (Exceotions)
   - try
   - catch
   - throw 

___

**exit()**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{
	std::cout << "I love you" << std::endl;

	exit(0);

	/*return 0;*/

	// ...

	/*std::cout << "I love you too" << std::endl;

	return 0;*/
}
```

- return 대신 exit 를 사용 할수도 있음
- `#include <cstdint>` 라이브러리를 include 해야함
- exit(0);
  - 0 값을 os에게 돌려줌
- 리턴은 정상적으로 리턴되서 나간다는 뜻
  - 리턴타입에 맞게 리턴해줘야 문법적으로 문제가 없이 컴파일됨
- exit는 긴급하게 나간다는 뜻
  - 코드에 어디에있던지 `()`안에 정수를 넣어주면 종료를 시킬 수 있음
  - 프로그램이 무조건 종료되야하는 경우 사용
  - 디버깅할때 사용됨
    - 코드의 부분적으로 확인할때 사용됨

### **🌱 5.2 조건문 if**

**if 문 기본 문법**

> **입력받은 정수가 10보다 큰지 알려주는 예제 코드**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x;
	cin >> x;

	if (x > 10)
		cout << x << " is greater then 10" << endl; // true인경우 실행
  else
  	cout << x << " not is greater then 10" << endl; // false 인경우 실행

	return 0;
}
```

- `if (...)` 안에는 bool 타입 데이터가 들어감
- bool 타입 데이터가 true 인경우 구문을 실행 시켜줌
- 내용에는 cout, 대입, 연산 등 스테이트먼트가 다 들어갈 수 있음
- **else:** if 문 안에 bool 타입이 false 일 경우 ture 구문을 무시하고 false 구문을 실행시켜줌 
- 
___

**주의사항**

**#1 중괄호 블럭 `{}`**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x;
	cin >> x;

	if (x > 10)
	{
		cout << x << " is greater then 10" << endl; // 1
		cout << x << " test 1" << endl; 
	}	
	else
		cout << x << " not is greater then 10" << endl; // 2
		cout << x << " test 1" << endl; // 블럭이 없으면 실행되지 않음

	return 0;
}
```
- `#1` 중괄호로 쓰여주는게 일반적임
  - 구문이 한줄인 경우 생략할 수 있음
- `#2` 구문이 두줄 이상일떄 블럭 `{}`을 안싸주면 실행이 되지않음


**#2 if 문 내부 변수 선언시**


```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x;
	cin >> x;

	if (1) // bool 은 0 이 아니면 true임
		int x = 5;
	else
  {
		int x = 6;
  }
	cout << x << endl; // 68

	return 0;
}
```

- bool 은 0 이 아니면 true임
- cout << x << endl; 이 if 문을 거쳐 5가 아닌 사용자의 입력값이 출력되는 이유는 **if문 내부적으로 `{}`가 그어져 있기 때문에 if문을 벗어나면 사라져버림**
- if문안에 변수 선언을 하지 말라는 뜻이아님 스코프가 `{}` 밖을 벗어나지 못한다는 뜻

**#3 Null**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{
	int x;
	cin >> x;
  // 1
	if (x > 10)
		; // {}; 와 똑같음 null 스테이트먼트

  // 2
	if (x > 10); // 여기서 끝나버림 
	{
		x = 1; // if문과 상관없이 실행됨
	}

	return 0;
}
```

- `;` 을 넣으면 `{};` 으로 인식하여 아무것도 실행되지않음 null 스테이트 먼트가됨
  - null 스테이트먼트를 사용하는경우 주석을달아서 기록해놓기
- 간혹실수로 2번과 같이 코드를 작성하는 경우 `x=1;` 은 if문에 거치지 않고 실행됨 

**#4 `=` 와 `==`**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{
	int x;
	cin >> x;

	if (x = 0) // if (0)
		cout << x << endl; // 실행되지않음

	cout << x << endl; // 0

	return 0;
}
```

- x와 0 을 비교하는 연산자는 `==` 인데 간혹가다 `=` 인 대입연산자를 사용하는경우
- x에 0이 대입되고 `if(0)`으로 인식되어 if문 내부 구문은 실행되지 않음

___

**else if 문**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x;
	cin >> x;

	if (x > 10)
		cout << "x is greater then 10" << endl;
	else if (x < 10)
		cout << "x is less then 10" << endl;
	else // if (x == 100
		cout << "x is exactly 10" << endl;

	return 0;
}
```
- else if 문으로 조건을 여러번 처리할 수 있음

___

**이중 if문**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x;
	cin >> x;

	if (x > 10)
		cout << "x is greater then 10" << endl;
	else
	{
		if (x < 10)
			cout << "x is less then 10" << endl;
		else
			cout << "x is exactly 10" << endl;
	}

	return 0;
}
```

- if문 내부에 `{}` 처리로 이중 if문 사용이 가능함
- 문법상 얼마든지 가능함
- 논리구조를 파악하기 어려우니 권장하지 않음

**이중 if문 주의사항**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x;
	cin >> x;

	if (x > 10)
		cout << "1" << endl; 

		if (x > 20)
			cout << "2" << endl;
	else
		cout << "..." << endl;

	return 0;

```

- 위 예제 코드에서는 else 가 2번 if 에 적용됨
- 인댄팅, 들여쓰기를 해놓아도 **문법상 else 는 가까히 있는 if에 붙음**
- 이경우에 목적에 따라 물결괄호로 구분을 잘 해놓아야함

___

**if문 논리연산자**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x, y;
	cin >> x >> y;

	if (x == y)
		cout << "same numbers" << endl;
	else
		cout << "Not same" << endl;

	if (x > 0 && y > 0)
		cout << "both numbers are positive" << endl;
	else if (x > 0 || y > 0)
		cout << "one of the numbers is positive" << endl;
	else
		cout << "Neither number is positive" << endl;


	return 0;
}
```

- if문에 논리 연산자도 사용할 수 있음

___

**if 문으로 프로그램 종료**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

int main()
{

	int x;
	cin >> x;

	if (x > 10)
		cout << "A" << endl;
	else if (x == 1)
		return 0;
	else if (x < 0)
		cout << "B" << endl;

	cout << "Hello " << endl;

	return 0;
}
```

- return 으로 종료하기
- exit도 가능함
- 어떤 함수를 수행을 멈추고 리턴해서 나가버리는 경우도있음

___

**if문 코드스타일 1**

```cpp
int min(int x, int y)
{
    if (x > y)
       return y;
    else 
       return x;

}
```

- 기본적인 코드스타일

**if문 코드스타일 2**

```cpp
int min(int x, int y)
{
	if (x > y) return y;
	else return x;

}
```
- 코드 길이를 줄일 때 사용

**if문 코드스타일 3**

```cpp
int min(int x, int y)
{
	
	return (x > y) ? y : x;
}
```

- 삼항 연산자

### **🌱 5.3 switch-case**

**switch-case 문 기본 문법**

```cpp
int main()
{
	/*printColorName(Colors::BLACK);*/

	int x;
	cin >> x;

	{
		switch (x)
		{
		case 0:
			cout << "Zero";
		case 1:
			cout << "One";
		case 2:
			cout << "Two";

		}

		cout << endl;
	}
	return 0;
}
```
- 입력으로 0 입력 시
  - ZeroOneTwo 출력됨
- 입력으로 1 입력 시
  - OneTwo 출력됨
- 의도적으로 이렇게 사용하는 경우도 많음

**break**

```cpp
int main()
{
	/*printColorName(Colors::BLACK);*/

	int x;
	cin >> x;

	{
		switch (x)
		{
		case 0:
			cout << "Zero";
			break;
		case 1:
			cout << "One";
			break;
		case 2:
			cout << "Two";
			break;

		}

		cout << endl;
	}
	return 0;
}
```

- 입력받은 문자에 대해서만 출력하고싶을 경우 break 사용
- 특별한 방식으로 코딩한 경우 주석남기기#

___

**열거형 & switch-case**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

enum class Colors
{
	BLACK,
	WHITE,
	RED,
	GREEN,
	BLUE

};

void printColorName(Colors color)
{
	switch (color)
	{
	case Colors::BLACK:
		cout << "BLACK";
		break;
	}

	cout << endl;
}

int main()
{
	printColorName(Colors::BLACK);

	
	return 0;
}
```

**열거형 & switch-case 개선된 코드**

```cpp
#include <iostream>
#include <cstdint>

using namespace std;

enum class Colors
{
	BLACK,
	WHITE,
	RED,
	GREEN,
	BLUE

};

void printColorName(Colors color)
{
	
	switch (static_cast<int>(color))
	{
	case 0:
		cout << "BLACK";
		break;
	case 1:
		cout << "WHITE";
		break;
	}

	cout << endl;
}

int main()
{
	printColorName(Colors::WHITE);

	
	return 0;
}
```

- color 파라메타를 int 타입으로 캐스팅해서 코드길이를 줄일수 있음

___

**주의사항**

**#1**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x;
	cin >> x;

	switch (x)
	{
		int x;
		int b = 5; // 불가능

	case 0:
    int b = 5; // 가능
		break;

	}
	
	return 0;
}
```

- switch-case문 안에서 변수선언 은 할 수 있음
- **초기화는 할수 없음**
  - 메모리 할당이 안됨
  - 케이스문 안에서만 할수 있음

**#2**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x;
	cin >> x;

  {
    // 여기에 switch 문에서 사용할 변수 선언하기

    switch (x)
    {
      int x;
      // int y; // case0 에서 선언한것과 동일하게 작동함
        
      case 0:
        int y; 
        break;

      case 1:
        y = 5;
        cout << y << endl; // 5

      case 2:
        cout << y << endl; // 에러 y가 초기화가 안됨
      
      case 3:
      {
        int y(156);
        cout << y << endl; // 156
        break;
      }
      
      default:
        cout << "Undefined input" << x << endl;
        break; // 혹시 몰라서 넣은것

    }
	}
	return 0;
}
```

- case 문 내에서 변수 선언시 모든 케이스문에 영향이 있음
- 차라리 switch 문 바깥에 변수 선언함
- `#3` 과 같이 케이스문도 각각 `{}` 블럭으로 감싸주기
- 변수는 가급적이면 사용하기 직전사용하고 적은범위에서 사용하는 것이 좋음
- `default` 는 case 에 정의가 안된 모든 경우에 대해서 실행을 시켜줌
  - `default` 밑에는 아무것도 안쓰는 경우가 일반적임
- `switch-case문` 안에 함수나 if문 등도 사용가능함

### **🌱 5.4 goto**

**goto 문 기본 문법**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double x;

tryAgain: // label

	cout << "Enter a non-negative number" << endl;
	cin >> x;

	if (x < 0.0)
		goto tryAgain;

	cout << sqrt(x) << endl;
	
	
	return 0;
}
```

- 음수를 입력하면 다시 실행하게 해줌
- 반복문을 대신하기위해 goto를 사용함
  - 어셈블리언어에서는 goto 도 반복문
  - 반복문의 원조격임
- **레이블:** 위치를 책갈피처럼 지정할 수 있음
- 거의 사용안함

**주의사항**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	goto skip;

	int x = 5;

skip:
	x += 3;
	
	return 0;
}
```

- goto 문으로 int x = 5; 가 스킵되어 변수 선언이 안된것으로 판단해 에러가 발생됨

### **🌱 5.5 반복문 while**

- 컴퓨터의 장점
  - 정확하다
  - 반복을 지루해하지않는다
- For문을 더 많이 사용되긴하지만 while 문이 사용되야하는 경우도 있음

**while문 기본 문법**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	cout << "While-loop test" << endl;
	int count = 0;

	while (count < 10)
	{
    // int count = 0; // 무한루프 됨
    // static int count = 0;
		cout << count << endl;
		++count;
	}
}
```
- `()` 안에 조건이 들어감
  - true면 작동함
  - false면 작동안함
- 무한 루프 주의
- while 문 안에 변수선언을 할때 무한루프 가능성있음
  - `static int count = 0;` 로 int 값이 변하도록 막을수 있음

___

**무한루프 빠져나오는 방법**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	cout << "While-loop test" << endl;
	int count = 0;

	while (1)
	{
		cout << count << endl;
		++count;

		if (count >= 10) break;
	}
}
```

- break 문으로 빠져나올 수 있음

- for문
  - 카운터 변수, if - break, while 을 합친것
  - while 을 사용하기 편하게만든게 for문임

___

**이중 while문**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	cout << "While-loop test" << endl;

	int outer_count = 1;

	while (outer_count <= 5)
	{
		int inner_count = 1;
		while (inner_count <= outer_count)
		{
			cout << inner_count++ << " ";
		}

		cout << endl;
		++outer_count;
	}
}
```

___

**주의사항**

**#1 overflow**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	cout << "While-loop test" << endl;
	unsigned int count = 10;

	while (count >= 0)
	{
		if (count == 0) cout << "Zero";
		else cout << count << " ";

		count--;
	}
}
```

- `unsigned int` 를 count 등의 변수로 사용하면 0이하로 내려갔을때 이상한값이 쭈루루루룩 나옴
  - `int`를 사용하면 해결되긴함
- `unsigned int`이 `int` 보다 속도가 빠르다고함
  - 최적화에선 `unsigned int`를 많이 사용함

### **🌱 5.6 반복문 do-while**

- 처음에 무조건 한번 실행하고 while 문 조건 체크함

**do-while문 기본 문법**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int selection; // must be declared outside do/while loop

	do
	{
		cout << "1. add" << endl;
		cout << "2. sub" << endl;
		cout << "3. mult" << endl;
		cout << "4. div" << endl;
		cin >> selection;
	} while (selection <= 0 || selection >= 5);

	cout << "You selected " << selection << endl;

	return 0;
}
```

- `int selection;` 가 밖으로 나와 있어야함
  - do 블럭에 선언하면 do 블럭이 끝나면서 selection 이 사라지기 때문임
- do-while 문 은 while문 끝에 `;` 이 꼭 붙어야함
- 0,1,2,3,4 중 하나가 입력될때까지 게속 반복해서 입력받음
- 많이 사용되진않음
- 특정 알고리즘에서 필요한 경우가 있음

### **🌱 5.7 반복문 for**

- 반복횟수가 정해져있을때 사용하기 좋음
- for 와 while 은 상호 변환이 가능함

**for문 기본 문법**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	for (int count = 0; count < 10; ++count) // iteration
		cout << count << endl;
	return 0;
}
```

- 한줄일떄는 `{}`을 안써도됨
  - 여러줄일때는 `{}` 사용
- for 옆에 `()`에다가 (카운터로 사용할 변수를 선언, 조건, 카운터를 증감 or 다른 연산) 순서대로 넣음
- 변수 명으로 iteration 의약자 i를 많이 사용함
  - i,j,k 등등

**for 문의 동작 순서**
1. 카운터로 사용할 변수를 선언
2. 조건 체크
3. { cout << count << endl; } 등의 구문 실행
4.  카운터를 증감 or 다른 연산 처리

___

**for문 변수 선언**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int count = 0;
	for (   ; count < 10; ++count)
  {
		cout << count << endl;
  }

	cout << count << endl;
	return 0;
}
```

- 예전엔 for문이 끝난다음에도 count 변수가 살아있었음
  - 지금은 안됨
  - 만약 for문 밖에서도 사용하고싶다면 for 문 위로 선언해주면됨
- `for (   ; count < 10; ++count)` 처럼 `;` 옆에 빈칸으로 비워놔도 됨

___

**for문의 무한루프**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int count = 0;
  for (   ;; ++count)
	for (   ;true; ++count)
		cout << count << endl;

	cout << count << endl;
	return 0;
}
```
- 두번쨰값에 `true` 를 넣어서 무한루프를 돌릴수 있음
  - true르 안넣고 `;` 만 남겨도 `true`가 들어간것처럼 동작함

___

**for문으로 pow함수 만들기**

```cpp
#include <iostream>
#include <cmath>

int pow(int base, int exponent)
{
	int result = 1;

	for (int count = 0; count < exponent; ++count)
		result *= base;

	return result;
	
}
using namespace std;

int main()
{
	cout << pow(2, 4) << endl; // 16

	return 0;
}
```

- **동작 설명**
  1. result 값 1에 첫번째 인수값인 2 를 곱해줌
  2. exponent번 만큼 연산을 함
     - 4번 
  3. 2^4 = 16 출력됨

___

**for문 1 씩 감소되는 예제코드**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{

	for (int count = 9; count >= 0; --count)
	{
		cout << count << endl;
	}

	return 0;
}
```

- over flow 현상으로 unsigned int 정수로 감소 연산을하면 문제가 될수 있음
___

**for문 2 씩 감소되는 예제코드**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{

	for (int count = 9; count >= 0; count -= 2)
	{
		cout << count << endl;
	}

	return 0;
}
```

- over flow 현상으로 unsigned int 정수로 감소 연산을하면 문제가 될수 있음

___

**for문 내의 여러개의 변수 선언**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{

	for (int i =0, j =0; (i + j) < 10; ++i, j +=2)
	{
		cout << i << " " << j << endl;
	}

	return 0;
}
```
- for 문 `()` 안에 `,` 를 사용하여 여러 변수를 동시에 선언할 수 있음

___

**이중 for 문**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	for(int j =0; j < 9; ++j)
		for (int i = 0; i < 9; ++i)
		{
			cout << i << " " << j << endl;
		}

	return 0;
}
```

- j를 안쪽 루프에서도 사용할 수 있음

___

**for 문 overflow 예제**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{

	for (unsigned int count = 9; count >= 0; --count)
	{
		cout << count << endl;
	}

	return 0;
}
```

- 0이하로 내려가면 4294965856 값 쭉쭉 계속해서 뺌

### **🌱 5.8 break, continue**

- 반복문을 제어하는 방법
- break 는 현재 블럭에서 빠져나감
- switch 문에서 많이 사용함

**break 와 return**

```cpp
#include <iostream>
#include <cmath>

using namespace std;

void breakorReturn()
{
	while (true)
	{
		char ch;
		cin >> ch;

		if (ch == 'b')
			break;

		if (ch == 'r')
			return;
	}

	cout << "Hello " << endl;
}

int main()
{
	breakorReturn();
	return 0;
}
```

- `b` 입력시 while문을 빠져나가고 `cout << "Hello " << endl;` 이 실행되어 `Hello`가 출력됨
- `r` 입력시 `void breakorReturn()`를 빠져나가서 `Hello`가 출력 되지않음

___

**for문 break**

```cpp
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	for (int i = 0; i < 10; ++i)
	{
		cout << i << endl;
		if (i == 5) break;
	}
}
```

- for문에서도 동일하게 break를 사용가능
- 5까지 출력하고 종료됨

___

**continue 사용예제**

```cpp
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	for (int i = 0; i < 10; ++i)
	{
		if (i % 2 == 0) continue;

		cout << i << endl;

		if (i % 2 == 1) cout << i << endl; // continue 사용 X
		
	}
}
```

- 짝수인 경우 continue하고 홀수만 출력하는 코드
- continue는 for문을 돌때 조건이 참이면 `{}` 내용을 실행시키지 않고 `++i` 부분으로 건너뛰어버림

___

**do-while문의 continue**

```cpp
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	int count(0);

	do
	{
		if (count == 5)
			continue;

		cout << count << endl;
	} while (++count < 10);

	return 0;
}
```

- while `()`안에 증감 연산자를 넣을수 있음
- 만약 `count++;` 를 `cout << count << endl;` 에 넣어버리면 무한루프에 빠져버림

- 사용자 정의 변수에 while문 안에 정의하면 엄청느려질 수도 있음
  - while문 밖으로 빼주는게 좋음

___

**특정 입력값을 break 를 사용 안하고 빠져나가기**

```cpp
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	int count(0);
	bool escape_flag = false;
	while (!escape_flag)
	{
		char ch;
		cin >> ch;

		cout << ch << " " << endl;

		if (ch == 'x')
			escape_flag = true;
	}
	
	return 0;
}
```

**특정 입력값을 break를 사용하여 빠져나가기**

```cpp
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	int count(0);
	while (true)
	{
		char ch;
		cin >> ch;

		cout << ch << " " << endl;

		if (ch == 'x')
			break;
	}
	
	return 0;
}
```

### **🌱 5.9 난수 만들기 random numbers**

- 난수 만들기 Random Number Generation

- 컴퓨터는 랜덤 숫자를 만들 수 없음
  - 유사, 가짜 랜덤 넘버를 만들기

___

**overflow 를 이용하여 난수 만들기**

```cpp
#include <iostream>

using namespace std;

unsigned int PRNG() // Pseudo Random Number Generator
{
	static unsigned int seed = 5523; // send number

	seed = 8253729 * seed + 2396403;

	return seed % 32768;
}

int main()
{
	for (int count = 1; count <= 100; ++count)
	{
		cout << PRNG() << "\t";

		if (count % 5 == 0) cout << endl;

	}
	
	return 0;
}
```

- seed 넘버 시작하는 숫자
  - 5523은 임의의 숫자임
- overflow로 seed 넘버와 먼 숫자를 뽑아냄
- 랜덤함수를 사용할때 범위를 지정하기위해서 `%`를 사용
  - 간단한경우는 괜찮음
  - 정밀한 데이터를 요구하면 안좋음

___

**`<cstdlib>` 라이브러리를 이용하여 난수 만들기**

```cpp
#include <iostream>
#include <cstdlib> // std::rand(), std::srand()

using namespace std;

int main()
{
	std::srand(5323);

	for (int count = 1; count <= 100; ++count)
	{
		cout << std::rand() << "\t";

		if (count % 5 == 0) cout << endl;

	}
	
	return 0;
}
```

- srand와 rand의 차이
  - s는 seed라는 뜻임
- 시드넘버가 고정되어있을때는 다른 숫자를 뽑아낼수 없음
- 디버깅 할때는 오히려 시드넘버를 고정 시켜야함

___

**`<ctime>` 라이브러리의 `std::time()`로 seed 넘버 바꾸기**

```cpp
#include <iostream>
#include <cstdlib> // std::rand(), std::srand()
#include <ctime> // std::time()

using namespace std;

int main()
{
	std::srand(static_cast<unsigned int>(std::time(0)));

	for (int count = 1; count <= 100; ++count)
	{
		cout << std::rand() << "\t";

		if (count % 5 == 0) cout << endl;

	}
	
	return 0;
}
```

- time 시간 별로 seed 넘버를 바꿔서 난수를 뽑을 수 있음

___

**지정한 범위의 int 난수를 만들기**

```cpp
#include <iostream>
#include <cstdlib> // std::rand(), std::srand()
#include <ctime> // std::time()

using namespace std;

int getRandomNumber(int min, int max)
{
	static const double fraction = 1.0 / (RAND_MAX + 1.0);

	return min + static_cast<int>((max - min + 1) * (std::rand() * fraction));

}


int main()
{
	std::srand(static_cast<unsigned int>(std::time(0)));

	for (int count = 1; count <= 100; ++count)
	{
		cout << getRandomNumber(5, 8) << "\t";

		if (count % 5 == 0) cout << endl;

	}
	
	return 0;
}
```

- RAND_MAX
  - 랜덤넘버를 뽑을때 가장 큰 숫자

___

**`rand()` 함수로 난수 만들기**

```cpp
#include <iostream>
#include <cstdlib> // std::rand(), std::srand()
#include <ctime> // std::time()

using namespace std;

int main()
{
	std::srand(static_cast<unsigned int>(std::time(0)));

	for (int count = 1; count <= 100; ++count)
	{
		cout << rand() % 4 + 5 << "\t";

		if (count % 5 == 0) cout << endl;

	}
	
	return 0;
}
```

- 5 ~ 8 범위의 난수를 뽑아줌
- `% 4 `가 작은 범위면 사용해도됨
- `% 4 `가 큰 범위라면 난수가 특정 숫자로 몰리는 현상이 일어날수도 있음
- C스타일 난수 뽑는방법임

___

**`<random>` 라이브러리 사용하여 난수 만들기**

```cpp
#include <iostream>
#include <cstdlib> // std::rand(), std::srand()
#include <ctime> // std::time()
#include <random>

using namespace std;

int main()
{
	std::random_device rd;
	std::mt19937 mesenne(rd()); // create a mesenne twister
	std::uniform_int_distribution<> dice(1, 6); // 1포함 6이하

	for (int count = 1; count <= 20; ++count)
		cout << dice(mesenne) << endl;

	return 0;
}
```

- C++ 11 부터 들어옴
- 시간에 맞춰 난수를 뽑던걸 device를 제공해줌 
- `std::mt19937_64;` 
  - std난수를 만들어주는 알고리즘임
  - `_64` 64비트 난수를 생성해줌
  - `_64` 를 안붙여주면 32비트 짜리를 생성해줌
- `uniform_int_distribution`
  - 노말 distribution, 포화 distribution 등등 있음
- 1 포함 6 이하 까지 동일한 확률로 난수를 생성해줌

**동작 구조**
- 랜덤디바이스 만듬
- 랜덤디바이스를 넣어서 생성기를 만듬
- 생성기가 어떤 분포를 따르지를 지정
- 사용할 분포를 만듬
- 분포가 생성기로 난수를 만듬

### **🌱 5.10 std::cin 더 잘 쓰기**


- ignire(), clear(), fail()
- cin은 콘솔에서 텍스트입력을 받을떄 이용하게 사용됨
  - cin에 의도하지 않은 입력이 들어왔을때 대응방법

___

**원본 코드**

```cpp
#include <iostream>

using namespace std;

int getInt()
{
	cout << "Enter an integer number :";
	int x;
	cin >> x;

	return x;
}

char getOperator()
{
	while (true)
	{
		cout << "Enter an operator (+,-) : "; // T0D0: more operators *, / etc.
		char op;
		cin >> op;

		return op;
	}
}

void printResult(int x, char op, int y)
{
	if (op == '+') cout << x + y << endl;
	else if (op == '-') cout << x - y << endl;
	else
	{
		cout << "Invalid operator" << endl;
	}

}


int main()
{
	int x = getInt();
	char op = getOperator();
	int y = getInt();

	printResult(x, op, y);

	return 0;
}
```

**문제점 :** 한번에 두개의 입력을 줬을때 문제가 생김 


___

**입력 개선 코드**

```cpp
#include <iostream>

using namespace std;

int getInt()
{
	cout << "Enter an integer number :";
	int x;
	cin >> x;
	std::cin.ignore(32767, '\n');

	return x;
}

char getOperator()
{
	while (true)
	{
		cout << "Enter an operator (+,-) : "; // T0D0: more operators *, / etc.
		char op;
		cin >> op;
		std::cin.ignore(32767, '\n');

		return op;
	}
}

void printResult(int x, char op, int y)
{
	if (op == '+') cout << x + y << endl;
	else if (op == '-') cout << x - y << endl;
	else
	{
		cout << "Invalid operator" << endl;
	}

}


int main()
{
	int x = getInt();
	char op = getOperator();
	int y = getInt();

	printResult(x, op, y);

	return 0;
}
```

- cin에서는 사용자의 입력을 버퍼에 담아놓고 x,y에 넣도록 보내주도록 되어있음
- 한번에 두개의 입력을 받으면 하나씩 버퍼에 담아줌
- 버퍼를 지우는 방법
  - `std::cin.ignore(32767, '\n');` 를넣어주면 첫번쨰 버퍼이외의 나머지를 지워줌
  - 32767은 적당히 큰숫자임

**문제점 :** 연산자에 `+`,`-` 이외의 다른걸 넣었을때 문제가 생김

___

**연산자 입력 개선 코드**

```cpp
#include <iostream>

using namespace std;

int getInt()
{
	cout << "Enter an integer number :";
	int x;
	cin >> x;
	std::cin.ignore(32767, '\n');

	return x;
}

char getOperator()
{
	while (true)
	{
		cout << "Enter an operator (+,-) : "; // T0D0: more operators *, / etc.
		char op;
		cin >> op;
		std::cin.ignore(32767, '\n');

		if (op == '+' || op == '-')
			return op;
		else
			cout << "Invaild operator, please try again" << endl;
	}
}

void printResult(int x, char op, int y)
{
	if (op == '+') cout << x + y << endl;
	else if (op == '-') cout << x - y << endl;
	else
	{
		cout << "Invalid operator" << endl;
	}

}

int main()
{
	int x = getInt();
	char op = getOperator();
	int y = getInt();

	printResult(x, op, y);

	return 0;
}
```

**문제점 :** int 의 범위를 넘어서는 정수를 입력했을때 문제가생김

___

**int 범위를 넘어서는 입력 개선 코드**

```cpp
#include <iostream>

using namespace std;

int getInt()
{
	while (true) 
	{
		cout << "Enter an integer number :";
		int x;
		cin >> x;

		if (std::cin.fail())
		{
			std::cin.clear(); // 버퍼 클리어
			std::cin.ignore(32767, '\n');
			cout << "Invalid number, please try again" << endl;

		}
		else
		{
			std::cin.ignore(32767, '\n');
			return x;
		}	
	}
}

char getOperator()
{
	while (true)
	{
		cout << "Enter an operator (+,-) : "; // T0D0: more operators *, / etc.
		char op;
		cin >> op;
		std::cin.ignore(32767, '\n');

		if (op == '+' || op == '-')
			return op;
		else
			cout << "Invaild operator, please try again" << endl;
	}
}

void printResult(int x, char op, int y)
{
	if (op == '+') cout << x + y << endl;
	else if (op == '-') cout << x - y << endl;
	else
	{
		cout << "Invalid operator" << endl;
	}

}

int main()
{
	int x = getInt();
	char op = getOperator();
	int y = getInt();

	printResult(x, op, y);

	return 0;
}
```

- `std::cin.fail()` 시 `std::cin.clear();` 로 버퍼를 초기화하고 입력을 다시 받음

# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)