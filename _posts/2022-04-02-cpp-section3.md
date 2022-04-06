---
published: true
title:  "따라하며 배우는 C++ Section 3. 연산자들"
excerpt: ""

categories:
  - 따배씨++
tags:
  - [C++]

toc: true
toc_sticky: true
 
date: 2022-04-05
last_modified_at: 2022-04-05
---

# 🤔 학습목표
- 따라하며 배우는 C++ Section 3. 연산자들

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 3. 연산자들**

### **🌱 3.1 연산자 우선순위와 결합 법칙**

- Operator Precedence and Associativity

- `int x = 4 + 2 * 3;` 한식에 서로다른 연산자들이 들어있을때 컴파일러의 우선순위
- 컴파일러는 수식이 들어오면 그래프로 만들어서 어느쪽을 먼저 계산할껀지 결정함
  - 자료구조 때 배움
- `int x = (4 + 2) * 3;` 괄호를 넣으면 우선순위가 더 높음
- `int x = 4 * 2 / 3;`  `*`와 `/` 는 우선순위가 같음


**C, C++ 우선순위표**

- **결합 법칙 (Associativity)**
  - 같은 레벨의 연산자 끼리의 계산 순서를 정해줌
  - 대부분 Left-to-right (왼쪽 먼저 계산)
    - Urary 연산자 (`-3`)같은건 right-ro-Left 임
      - 왼쪽에 아무것도 없기 때문에
- `* / %` 연산자 레벨은 5 임
- `+ -` 은 레벨 6임 
- 애매할떈 **괄호**를 쳐서 명확하게 표현해주기

- `^` 기호는 캐럿 (caret, kerat) 이라고 읽음
  - 수학에서는 제곱 표현에 많이사용 `2^3 = 8`
  - C언어 에서는 제곱이 아니라 Bitwise XOR 임

___

**C++ 의 제곱표현**

```cpp
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	int x = std::pow(2, 3);


	cout << x << endl;

	return 0;
}
```

- `#include <cmath>` 라이브러리 에서 pow 를 사용함
- double 로 반환함

___

**연습문제**

> 우선순위와 결합법칙 맞춰보기

```cpp
r = 1 + 2 + 3 *4;
a = b = c
t /= --w + 5
a || b && c || d
```

### **🌱 3.2 산술 연산자 (arithmetic operators)**

- 수학의 산수하고는 애매하게 조금 다른 부분이 있음

**단항 연산자**

```cpp
#include <iostream>

using namespace std;


int main()
{
	int x = 1;
	int y = -x; 

	return 0;
}
```

- 값 앞에 부호를 붙여서 단항의 부호를 바꿀수 있음
  - `-x`
  - `+x` + 는 거의 의미가없어서 안붙이는 경우가 많음
- `- x` 같이 단항연산자를 듸어쓰기하면 알아보기 힘듬
- `+x` 도있긴함

___


**사칙연산**

```cpp
#include <iostream>

using namespace std;


int main()
{
	// 정수의 사칙연산
	int x = 7;
	int y = 4;
	int z = x + y; // 더하기
	int d = x - y; // 빼기
	int f = x * y; // 곱하기
	int q = x / y; // 나누기
	int w = x % y; // 나머지

	// 나머지 연산 주의점

	cout << x / y << endl; // 1 정수
	cout << float(x) / y << endl; // 1.75 실수
	cout << x / float(y) << endl; // 1.75 실수
	cout << float(x) / float(y) << endl; // 1.75 실수

	return 0;
}
```

- 정수끼리의 나머지 출력값은 정수값 으로 출력됨
- 정수 + 실수 끼리의 출력은 실수값 으로 출력됨

___

**주의사항**

```cpp
#include <iostream>

using namespace std;


int main()
{

	cout << -5 / 2 << endl; // -2
	cout << -5 % 2 << endl; // -1

	return 0;
}
```

- 음의 정수를 나누는 경우 c++ 11 부터는 -2.5면 뒷부분 -0.5를 절삭해서 -2로 출력해줌
- 나머지 `%`는 왼쪽 의 값과 동일한 부호로 값을 반환해줌
  - C++ 규정으로 정해진 사항임


___

**증가 대입 연산자**

```cpp
#include <iostream>

using namespace std;


int main()
{

	int x = 7;
	int y = 4;

	int z = x;
	z += y; // z = z + y;
  z -= y; // z = z - y;
  z *= y; // z = z * y;
  z /= y; // z = z / y;
  z %= y; // z = z % y;

	return 0;
}
```

**증가 대입 연산자의 장정**
- 코드의 양이 줄어듬
- 오타가 줄어들수 있음
- 가독성이 좋음


### **🌱 3.3 증감 연산자**

```cpp
#include <iostream>

using namespace std;


int main()
{

	int x = 5;
	int y = --x;
	int z = x--;

	cout << y << endl; // 4
	cout << z << endl; // 4

	return 0;
}
```

- `++x` or `x++`
  - x에 1을 더한 값을 넣는다는 뜻
- `--x` or `x--`
  - x에 1을 뺀 값을 넣는다는 뜻
- 앞 이나 뒤에 붙일수 있고 + 와 - 둘다 가능함

___

**주의사항**

```cpp
#include <iostream>

using namespace std;


int main()
{

	int x = 6, y = 6;
	cout << x << " " << y << endl; // 6 6
	cout << x++ << " " << y-- << endl; // 6 6
	cout << x << " " << y << endl; // 7 5
	cout << ++x << " " << --y << endl; // 8 4 

	return 0;
}
```
  
- **변수 앞에 `++` 나 `--` 이 붙는경우**
  - 1을 빼거나 더한다음에 x에 넣고 스트림에 더했기 때문에 1이 적용된 x값이 출력됨
- **변수 뒤에 ++ 나 -- 이 붙는 경우**
  - x의 값을 일단 스트림으로 보내고 출력한 뒤에 그다음에 1을 더하거나 뺌

___

**이런식으로 코딩 하기 금지**

> **금지 예제 1**

```cpp
#include <iostream>

using namespace std;

int add(int a, int b)
{
	return a + b;
}

int main()
{
	int x = 1;
	int v = add(x, ++x); // 4 do not use

	cout << v << endl;

	return 0;
}
```

- 함수의 인수로 증감연산자를 넣으면 출력값이 꼬일수도 있음

> **금지 예제 2**

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 1;
	x = x++; // x++; ++x;

	cout << x << endl;

	return 0;
}
```

- 명확하게 결과가 정의 되지않으니 금지

### **🌱 3.4 sizeof, 쉼표 연산자, 조건부 연산자**

**sizeof**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	float a;

	sizeof(float); // 4
	sizeof(a); // 4

	return 0;
}
```

- 어떤 데이터형의 크기를 알고 싶을때 사용
- byte(바이트) 단위로 출력됨
- 1 바이트는 8 비트임
- 데이터 타입을 넣을수 있음
- 변수를 넣을수 있음
- 스트럭쳐나 클래스도 자료형을 만드는 개념이라 사용할 수 있음
- 메모리 관리할때 유용함
- 함수가아닌 연산자임
  - 표준에서 연산자라고 정의를 해두었음
- 변수명일 경우에는 괄호가 없어도 작동함
  - `sizeof a;`

___

**쉼표연산자 (Comma Operator)**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	int x = 3;
	int y = 10;
	int z = (++x, ++y);
	// ++x;
	// ++y;
	// int z = y; 랑 똑같음

	cout << x << " " << y << " " << z << endl; // 4 11 11
}
```

- 콤마 연산자 `int z = (++x, ++y);` 는 마지막에 계산된 값 ++y를 z에 넣어줌 
- for문에서 유용하게 사용됨

**comma operator 주의점**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	int a = 1, b = 10; // 선언에 사용되는 콤마는 연산자가 아니고 구분해주는 기호임
	int z;
	
	z = a, b; // 연산자의 우선순위가 대입 연산자가 낮아서 대입을 먼저 해버린 것
	/*(z = a), b; 이렇게 된것*/

	cout << z << endl; // 1

	z = (a, b);

	cout << z << endl; // 10

	int v = (++a, a + b);
	cout << v << endl; // 12
}
```

- for 문 이외에는 콤마 안쓰는게 편함

___

**조건부 연산자 (Conditional Operator)**

- 삼항 연산자 라고도 부름
  - 나중에 삼항연산자가 추가될수도 있으니 조건부 연산자 라고부르기
- arithmetric if 라고도 부름
  - 조건문을 처리할때 if를 안쓰고 처리하기때문에 이렇게 부름

**조건부 연산자 예제코드**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	bool onSale = true;

	const int price = (onSale == true)? 10 : 100;

	cout << price << endl; // 10

	/*if (onSale)
		price = 10;
	else
		price = 100;*/

}
```

- if문에서는 const 를 사용할수 없기때문에 const로 사용하고싶을땐 조건부 연산자를 사용
- 간단한 경우에만 사용
- 내용이 복잡할경우에는 if문 이나 함수로 쓰기

___

**함수로 표현하기**

```cpp
#include <iostream>

int getPrice(bool onSale)
{
	if (onSale)
		return 10;
	else
		return 100;
}


int main()
{

	using namespace std;

	bool onSale = true;

	const int price = getPrice(onSale);

	
}
```

- 예전에는 이런식으로 짜면 부담이 되었음 최적화때문에 조건부 연산자를 사용하는게 나음

```cpp
#include <iostream>

int main()
{

	using namespace std;

	int x = 5;

	cout << (x % 2 == 0) ? "even" : "odd" << endl; // #1
	cout << ((x % 2 == 0) ? "even" : "odd") << endl; // #2
	cout << ((x % 2 == 0) ? 0 : "odd") << endl; // #3
	
}
```

- #1 조건부 연산자때문에 오류발생함
- #2 처럼 사용
- #3 이런식으론 사용하지말기 좌항과 우항의 타입이 달라 공정하지않음


### **🌱 3.5 관계 연산자 (Relational Operators)**

- 관계 연산자
  - `> < =`

**2개의 정수 동시에 입력받기**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	int x, y;

	cin >> x >> y; // 2개 입력받기
	cout << x << " "  << y << endl;

	return 0;
}
```

___

**관계 연산자 예제코드**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	int x, y;

	cin >> x >> y; // 2개 입력받기
	cout << x << " "  << y << endl;

	if (x == y)
		cout << "equal" << endl;
	
	if (x != y)
		cout << "not equal" << endl;

	if (x > y)
		cout << "x is greater then y" << endl;

	if (x < y)
		cout << "x is less then y" << endl;

	if (x >= y) 
		cout << "x is greater then y or equal to y" << endl;

	if (x <= y)
		cout << "x is less then y or equal to y" << endl;

	return 0;
}
```
- 코드는 가급적으로 영어 사용하기

___

**while 문으로 반복 테스트**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	while (true)
	{
		int x, y;

		cin >> x >> y; // 2개 입력받기
		cout << x << " " << y << endl;

		if (x == y)
			cout << "equal" << endl;

		if (x != y)
			cout << "not equal" << endl;

		if (x > y)
			cout << "x is greater then y" << endl;

		if (x < y)
			cout << "x is less then y" << endl;

		if (x >= y)
			cout << "x is greater then y or equal to y" << endl;

		if (x <= y)
			cout << "x is less then y or equal to y" << endl;
	}
	return 0;
}
```

___

**주의사항**

**부동소수점 비교**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	double d1(100 - 99.99); // 0.001
	double d2(10 - 9.99);	// 0.001

	if (d1 == d2)
		cout << "equal" << endl;
	else
		cout << "not equal" << endl; // 출력

	if (d1 > d2) cout << "d1 > d2 " << endl; // 출력
	else // if (d1 < d2) bacause d1 != d2
		cout << "d1 < d2" << endl;

	return 0;
}
```

- 딥러닝, 금융 소프트웨어 할떄 주의해야함
- 수치해석학 이라는 전공이 있음

**부동소수점 오차 찾기**

```cpp
#include <iostream>
#include <cmath>

int main()
{

	using namespace std;

	double d1(100 - 99.99); // 0.001
	double d2(10 - 9.99);	// 0.001

	cout << std::abs(d1 - d2) << endl; // 5.32907e-15
}
```

- `#include <cmath>` 라이브러리의 ` std::abs()` 절대값을 구해주는 함수

___

**오차값 조절하여 출력하기**

```cpp
#include <iostream>
#include <cmath>

int main()
{

	using namespace std;

	double d1(100 - 99.99); // 0.001
	double d2(10 - 9.99);	// 0.001

	const double epsilon = 1e-10;

	if (std::abs(d1 - d2) < epsilon)
		cout << "Approximately equal" << endl; // 출력
	else
		cout << "Not equal" << endl;
}
```

- epsilon 값을 조절해서 출력을 조절할수 있음.

### **🌱 3.6 논리 연산자 (Logical operators)**

**logical NOT**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	// logical NOT
	bool x = true;

	cout << !x << endl; // 0 출력
}
```

- not 연산자 `!`

___

**logical AND**

**예제 1**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	// logical AND
	bool x = true;
	bool y = false;

	cout << (x && y) << endl; 

	return 0;
}
```

- and 연산자 `&&`
- and 연산자는 && 두개 필수 &이랑은 의미가 완전다름

**예제 2**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	bool hit = true;
	int health = 10;

	if (hit == true && health < 20) // (hit && health < 20) 이렇게 사용하도 됨
	{
		cout << "die" << endl;
	}
	else
		health -= 20;

	return 0;
}
```

- `==`, `<` 관계연산자
- `&&` 논리 연산자

___

**logical OR**

**예제 1**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	bool x = true;
	bool y = false;

	cout << (x || y) << endl; // 1
}
```

- or연산자 `||`

**예제 2**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	int v = 1;

	if (v == 0 || v == 1)
		cout << "v is 0 or 1" << endl;

}
```

- or, and 여러개 가 이을수 있지만 보기 힘들어서 길게는 안씀
  - 만약 길어지면 주석달기

___


**주의 사항**

**예제 1**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	int x = 5;
	int y = 5;

	if (!x == y) // 올바른 예제 (x != y) 
	{
		cout << "x does not equal y" << endl;
	}
	else
		cout << "x equals y" << endl; // 출력

}
```

- `==` 연산자보다 `!` 연산자의 우선순위가 높고, int 형 자료형에 `!`을 넣으면 강제로 bool 형변환이 되어 의도치 않은 값이 출력될 수 있음
- 논리연산자가 있으면 가급적 명확하고 간단하게 표현하기


**예제 2**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	bool v1 = true;
	bool v2 = false;
	bool v3 = false;


	bool r1 = v1 || v2 && v3; // bool r1 = v1 || (v2 && v3); 처럼 동작함
	bool r2 = (v1 || v2) && v3;

	cout << r1 << endl; // 1
	cout << r2 << endl; // 0

	return 0;
}
```

- `&&` 가 `||` 보다 **우선 순위가 높음**
- 그냥 웬만하면 괄호 치기

___

**short circuit ebaluation**

**예제 1**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	// short circuit ebaluation

	int x = 1;
	int y = 2;

	if (x == 1 && y++ == 2)
	{
		// do something
	}

	cout << y << endl; // 3

	return 0;
}
```

**예제 2**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	// short circuit ebaluation

	int x = 2;
	int y = 2;

	if (x == 1 && y++ == 2)
	{
		// do something
	}

	cout << y << endl; // 2

	return 0;
}
```

- 예제 2와 예제 3의 차이는 x의 값밖에 없는데 y의 출력값이 달라진 이유
  - and 연산자는 왼쪽 먼저 계산하는데 **왼쪽이 만약 false 면 오른족을 계산을 안함**

___

**De Morgan's Law**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	bool x = true;
	bool y = false;

	!(x && y);
	!x || !y;

	!(x || y);
	!x && !y;

	return 0;
}
```

- 분배 법칙이 적용되지않음
  - `&&`가 `||`로 서로 바뀜

___

**XOR**

```cpp
#include <iostream>

int main()
{

	using namespace std;

	bool x = true;
	bool y = false;

	// XOR
	// false false false
	// false true true
	// true false true
	// true true false

	if (x != y)
	{

	}

	return 0;
}
```

- C++ 에서는 **XOR 연산자가 없음**
	- 위 예제코드 로 대체함

### **🌱 3.7 이진수 (Binary Numbers)**

- 컴퓨터는 전압을 이용해서 숫자를 구분함
  - 전압이 낮고(0) 높고(1)
  - 전압을 여러개 나열해서 정보를 표현 할 수 있음

- 비트 연산자 & 비트 플래그
  - 게임에 많이 사용함

**10진법**
- 한자리수 0 ~ 9 까지 표현
- 두자리수 표현
  - 10 = 10^1 + 0
  - 337 = 300 + 30 + 7 = 10^2 \* 3 + 10^1 \* 3 + 10^0 \* 7
- 모든 숫자의 0제곱은 1
- **C언어에서는 제곱 연산자가 없음**

**2진법**
10 = 2^1 + 2^0\*0 = 2
11 = 2^1 + 2^0\*1 = 3

- 사람이 10진수를 입력하면 컴퓨터가 2진수로 바꾸어 메모리에 저장함
- 메모리에 저장되있던 2진수를 출력할때는 10진수로 바꾸어 출력함

___

**2진수를 10진수로 바꾸는 법**

> 2진수 예제 `0101 1110` 

**2byte 기준**
- 제곱자리 7654 3210
  - 2^7 = 128
  - 2^6 = 64
  - 2^5 = 32
  - 2^4 = 16
  - 2^3 = 8
  - 2^2 = 4
  - 2^1 = 2
  - 2^0 = 1

- `128 * 0` + `64 * 1` + `32 * 0` + `16 * 1` + `8 * 1` + `4 * 1` + `2 * 1` + `1 * 0`
- `64` + `16` +` 8` + `4` + `2`
- `94`

___

**10진수를 2진수로 바꾸는 법**

- decimal to binary

**방법 1**

> 10진수 에제 `148`

- `148 / 2 = 74` r0 
- `74 / 2 = 37` r0
- `37 / 2 = 18` r1
- `18 / 2 = 9` r0
- `9 / 2 = 4` r1
- `4 / 2 = 2` r0
- `2 / 2 = 1` r0
- `1 / 2 = 0` r1

- r = remainder 나머지값
- 나머지값 나열
- 결과값 `1001 0100`

**방법 2**

![KakaoTalk_20220405_190746570](https://user-images.githubusercontent.com/90514882/161731334-cfa4cc85-f40e-434a-b462-48f630dd424c.jpg)

- 주로 방법 1을 많이사용함

___

**2진수 끼리 더하기**

- `0110` + `0111`
  - 1101

___

**10진수 음의 정수 를 2진수로 바꾸기**

> 예제 `-5`

1. 부호는 생각하지말고 정수만 2진수로 먼저 바꾸어 준다
   - `0000 0101`
   - 맨앞에 0 은 부호 표현할떄 사용하는 것
     - 0이면 양수
     - 1이면 음수

2. 보수 (complement): 0을 1로 바꾸고 1을 0 으로 바꾸기
   - `1111 1010`
3. 마지막에 1을 더하기
   - 결과값 `1111 1011`  
   - 1을 더하는 이유는 숫자 0을 표현할때 두가지숫자로 표현되는걸 막기위해서임
     1. 0을 2진수로 표현하면 `0000 0000`
     2. 이를 음수로 바꾸면 `1111 1111` 이되어 두가지로 표현이 되어버림
     3. 따라서 1을 더해주면 `0000 0000`으로 표현이됨

___

**2진수 음의 정수를 10진수로 바꾸기**

> 예제 `1001 1110`

1. 보수를 취함
   - `0110 0001` 
2. 1을 더하기
   - `0110 0010`
3. 10진수로 바꾸기
   - `98`
4. 처음시작할때 2진수의 첫번째가 1이면 음수 0 이면 양수니까 `-`를 붙여주기
   - `-98` 

___

**signed vs unsigned**

> 예제 1001 1110

- signed
  - 부호가 있는 숫자이기때문에 맨앞에 1이 부호로 표현이됨 
  - `-98`
- unsigned
  - 부호가 있는 숫자이기때문에 맨앞에 1이 부호가 아닌 숫자로 표현이됨 
  - `158`

### **🌱 3.8 비트단위 연산자 (Bitwise Operators)**


- 각각의 비트 끼리의 연산 각자리에 대해서 계산하는방식
- int, float 등은 타입단위의 연산임

- 예전엔 메모리가 비쌌음  
- 메모리 주소 구조상 저장 최소 단위가 byte임
  - bool 연산자를 저장항때 1비트만 필요한데 남는 자리가많음

**비트단위 연산자의 장점**

- 남는 자리를 줄일수 있음
- 계산 속도가 빠름

___

**bitwise 종류**

- `<<` Leftshift
  - 기본임
  - cout 이나 cin 에서는 다른 의미로 사용한다고 라이브러리에서 강제로 덮어씌움
    - 오퍼레이터 오버로딩 이라고함
- `>>` Rightshift
- `~` not
- `&` and
- `|` or
- `^` xor

- 주로 shift 를 많이씀

- `#include <bitset>`
  - 2진수로 바꿔서 출력해주는 라이브러리

- bitwise 사용할때는 unsigned를 사용함

___

**bitset 라이브러리 사용법**

```cpp
#include <iostream>
#include <bitset>

int main()
{

	using namespace std;

	unsigned int a = 1;

	cout << std::bitset<4>(a) << endl; // 0001


	return 0;
}
```

- 4는 2진수의 4까지만 출력해주는 템플릿임

___

**bitwise Leftshift**

**예제 코드 1**

```cpp
#include <iostream>
#include <bitset>

int main()
{

	using namespace std;

	unsigned int a = 3;

	cout << std::bitset<4>(a) << endl; // 0011

	unsigned int b = a << 1;
	
	cout << std::bitset<4>(b) << endl; // 0110

	return 0;
}
```

- `unsigned int b = a << 1;` bit를 한칸 옆으로 shift 해주는 것 남은자리를 0으로 채움

**예제 코드 2**

```cpp
#include <iostream>
#include <bitset>

int main()
{

	using namespace std;

	unsigned int a = 3;

	cout << std::bitset<4>(a) << endl; // 0011

	unsigned int b = a << 2;
	
	cout << std::bitset<4>(b) << " " << b << endl; // 1100 12

	return 0;
}
```

- `unsigned int b = a << 2;` 옆으로 두칸 이동이 되었고 실수값도 2진수에 맞춰 바뀐것을 확인할 수 있음
- 즉 `a x 2^2` 이 되는것임
- 많이 쓰는이유는 unsigned 숫자를 **2^n 을 곱하고싶은 경우 그냥 곱하는 것 보다 속도가 훨신빠름**

___

**bitwise Rightshift**

```cpp
#include <iostream>
#include <bitset>

int main()
{

	using namespace std;

	unsigned int a = 1024;

	cout << std::bitset<16>(a >> 1) << " " << (a >> 1) << endl; // 0000001000000000 512
	cout << std::bitset<16>(a >> 2) << " " << (a >> 2) << endl; // 0000000100000000 256
	cout << std::bitset<16>(a >> 3) << " " << (a >> 3) << endl; // 0000000010000000 128
	cout << std::bitset<16>(a >> 4) << " " << (a >> 4) << endl; // 0000000001000000 64

	return 0;
}
```

- 일반적인 `1024 / 8` 은 컴퓨터가 내부적으로 8이아닌 다른 숫자로도 나눌수 있는 방식으로 계산하기 때문에 느림
- bitwise 는 컴퓨터 내부에 저장된 방식으로 계산하기 때문에 속도가 훨신 빠름
  - 대신 일반적인 나누기 곱하기엔 사용할수 없음 

___

**bitwise not**

```cpp
#include <iostream>
#include <bitset>

int main()
{

	using namespace std;

	unsigned int a = 1024;

	cout << std::bitset<16>(a) << " " << (a) << endl; // 0000010000000000 1024

	cout << std::bitset<16>(~a) << " " << (~a) << endl; // 1111101111111111 4294966271

	return 0;
}
```

- 2진수의 0과 1을 모두 반대로바꿔버림

___

**bitwise and, bitwise or, bitwise xor**

- 2진수 표현은 앞에 `0b`를 붙임

```cpp
#include <iostream>
#include <bitset>

int main()
{

	using namespace std;

	unsigned int a = 0b1100;
	unsigned int b = 0b0110;

	cout << a << " " << b << endl; // 12 6 10진수로 출력된것
	cout << std::bitset<4>(a & b) << endl; // and 0100
	cout << std::bitset<4>(a | b) << endl; // or 1110
	cout << std::bitset<4>(a ^ b) << endl; // xor 1010

	a = a & b;
	a &= b;

	return 0;
}
```

- 2진수 비트 단위로 and, or, xor 비교해서 출력해줌
- `a = a & b;`, `a &= b;` 같이 assignment Operator 와 결합된 형태로 사용할 수 있음

___

**Quiz**

```cpp
#include <iostream>
#include <bitset>

int main()
{

	using namespace std;

	cout << std::bitset<4>(5) << endl;
	cout << std::bitset<4>(12) << endl;

	cout << std::bitset<4>(5 & 12) << endl; // 0000000000000100
	cout << (5 & 12) << endl; // 4

	cout << std::bitset<4>(5 | 12) << endl; // 0000000000001101
	cout << (5 | 12) << endl; // 13

	cout << std::bitset<4>(5 ^ 12) << endl; // 0000000000001001
	cout << (5 ^ 12) << endl; // 9

	return 0;
}
```

- 정수값으로 비트단위 연산을하면 내부적으로 2진수로 비트단위 연산을 해서 계산된 값을 반환해줌

### **🌱 3.9 비트 플래그, 비트 마스크 사용법 (Bit flags, Bit masks)**


```cpp
#include <iostream>
#include <bitset>

using namespace std;


int main()
{
	/*bool item_flag = false;
	bool item2_flag = false;
	bool item3_flag = false;
	bool item4_flag = false;
	*/
	unsigned char item_flag = 0;

	cout << bitset<8>(item_flag) << endl;

	return 0;
}
```

- bool type 를 여러개 선언해서 만들어도되긴하지만 메모리의 낭비가 있고 속도도 느림
- `unsigned char item_flag = 0;` 를 만들어서 1byte 니까 8가지 표현할수 있음

___

**비트 플래그 예제코드**

**예제코드 1**

```cpp
#include <iostream>
#include <bitset>

using namespace std;


int main()
{
	const unsigned char opt0 = 1 << 0;
	const unsigned char opt1 = 1 << 1;
	const unsigned char opt2 = 1 << 2;
	const unsigned char opt3 = 1 << 3;
	// opt4, 5, 6 ,7
	
	cout << bitset<8>(opt0) << endl; // 00000001
	cout << bitset<8>(opt1) << endl; // 00000010
	cout << bitset<8>(opt2) << endl; // 00000100
	cout << bitset<8>(opt3) << endl; // 00001000

	unsigned char item_flag = 0;

	cout << "No item " << bitset<8>(item_flag) << endl; // 00000000

	// item0 on
	item_flag |= opt0;
	cout << "item0 obtained " << bitset<8>(item_flag) << endl; // 00000001

	// item3 on
	item_flag |= opt3;
	cout << "item2 obtained " << bitset<8>(item_flag) << endl; // 00000101

	// item lost
	item_flag &= ~opt3;
	cout << "item2 lost " << bitset<8>(item_flag) << endl; // 00000001

	// has item1 ?
	if (item_flag & opt1) {cout << "Has item1" << endl;}
	else { cout << "Has not item1" << endl; }

	// has item0 ?
	if (item_flag & opt0) { cout << "Has item0" << endl; }
	else { cout << "Has not item0" << endl; }

	// obtain item 2, 3
	item_flag |= (opt2 | opt3);

	cout << bitset<8>(opt2 | opt3) << endl;
	cout << "item2,3 obtained " << bitset<8>(item_flag) << endl; // 00000001

	if ((item_flag & opt2) && !(item_flag & opt1))
	{
		/*item_flag ^= opt2;
		item_flag ^= opt1;*/

		item_flag ^= (opt1 | opt2);

		cout << bitset<8>(item_flag) << endl;
	}

	return 0;
}
```

- 초기화할때 16진수로 많이함
- `glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)`
  - or 가 들어가있는 코딩을 많이하게됨
  - api 디자인 할때 옵션이 많아지는 걸 줄일때 사용
	
___

- **컬러테이블**
  - 웹, 그래픽스, 이미지처리
  - 컬러를 표현할때 쓰는 R,G,B 의 16진수로 표현함
    - RRGGBB
    - 숫자 두개가 1Byte임
    - 1 Byte 는 8bit 니까 `2^8` 해서 0 ~ 255 까지 256개의 정보 표현이 가능함 
  - 색을 표현할때 float도 있긴한데 디자인 할때는 1Byte 3개로 표현을 많이함

___

**16진수 컬러값 추출하기**

```cpp
#include <iostream>
#include <bitset>

using namespace std;


int main()
{
	const unsigned int red_mask = 0xFF0000;
	const unsigned int green_mask = 0x00FF00;
	const unsigned int blue_mask = 0x0000FF;

	cout << std::bitset<32>(red_mask) << endl;
	cout << std::bitset<32>(green_mask) << endl;
	cout << std::bitset<32>(blue_mask) << endl;

	unsigned int pixel_color = 0xDAA520;

	cout << std::bitset<32>(pixel_color) << endl;

	unsigned char red = (pixel_color & red_mask) >> 16;
	unsigned char green = (pixel_color & green_mask) >> 8;
	unsigned char blue = pixel_color & blue_mask;

	cout << "red " << bitset<8>(red) << " " << int(red) << endl; // red 11011010 218
	cout << "green " << bitset<8>(green) << " " << int(green) << endl; // green 10100101 165
	cout << "blue " << bitset<8>(blue)<< " "<< int(blue)<< endl; // blue 00100000 32

	return 0;
}
```

- `0xFF0000` 16 진수표현
  - `0x00` 뒤에 00 이 생략된것
- maks 값에 FF 값 즉 11111111 값을 넣어놓고 & 비트마스크로 값을 추출해와서 bitshift로 char 데이터 자료형에 맞춰준뒤 int 데이터 자료형으로 캐스팅해서 데이터를 뽑아올 수 있음

___

**연습 문제**

**문제 1**

```cpp
#include <iostream>
#include <bitset>

using namespace std;


int main()
{
	const char option_viewed = 0x01;
	const char option_edited = 0x02;
	const char option_liked = 0x04;
	const char option_shared = 0x08;
	const char option_deleted = 0x80;

	unsigned char my_article_flages = 0;

	my_article_flages |= option_viewed; // 기사를 봤을 때

	cout << std::bitset<8>(my_article_flages) << endl;
	
	my_article_flages |= option_liked; // 기사의 좋아요를 클릭 했을 때

	cout << std::bitset<8>(my_article_flages) << endl;

	my_article_flages ^= option_liked; // 기사의 좋아요를 다시 클릭 했을 때

	cout << std::bitset<8>(my_article_flages) << endl;

	my_article_flages ^= option_viewed; // 본 기사만 삭제할 때

	cout << std::bitset<8>(my_article_flages) << endl;

	return 0;
}
```

**문제 2**

> 다음 코드가 똑같이 동작하는이유

```cpp
myflags &= ~(option4 | option5);
myflags &= ~option4 & ~option5;
```

- **드모르간의 법칙**
  - 수리 집합론이나 논리학에서 여집합, 합집합, 교집합의 관계를 기술하여 정리한 것, 수학자 오거스터스 드 모르간의 이름을 따서 드 모르간의 법칙이라함

![드모르간의법칙](https://user-images.githubusercontent.com/90514882/161777882-7c4e7e81-0ae6-49f7-b3d2-a91813d61801.jpg)


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)