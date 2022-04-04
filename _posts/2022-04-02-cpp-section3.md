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
 
date: 2022-04-04
last_modified_at: 2022-04-04
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


### **🌱 **

### **🌱 **

### **🌱 **


# 😊 배우게 된 점


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)