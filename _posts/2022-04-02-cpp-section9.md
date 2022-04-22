---
published: true
title:  "따라하며 배우는 C++ Section 9. 연산자 오버로딩"
excerpt: ""

categories:
  - 따배씨++
tags:
  - [C++]

toc: true
toc_sticky: true
 
date: 2022-04-22
last_modified_at: 2022-04-22
---

# 🤔 학습목표
- 따라하며 배우는 C++ Section 9. 연산자 오버로딩

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 9. 연산자 오버로딩**

### **🌱 9.1 산술 연산자 오버로딩 하기**

- Overloading
- 기본적으로 int등 같은 자료형은 산술 연산자 가 모두 정의되어 있음
- 사용자 정의 자료형끼리 산술하는방법임

**기본 코드**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

private:
	Cents(int cents) { m_cents = cents; }
	int getCents() const { return m_cents; }
};

int main()
{
	Cents cents1(6);
	Cents cents2(8);

	return 0;
}
```

- io operater 로 오버로딩 할수 있음
- cents1 과 cents2의 합을 구하고 싶은상황임

**add 함수를 만들어서 합 구하기**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents=0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }
};

void add(const Cents& c1, const Cents& c2, Cents& c_out)
{
	c_out.getCents() = c1.getCents() + c2.getCents();
}

int main()
{
	Cents cents1(6);
	Cents cents2(8);

	Cents sum;
	add(cents1, cents2, sum);

	cout << sum.getCents() << endl;

	return 0;
}
```

- add 함수를 만들어서 더함
- 불편하고 복잡함

- 출력값을 파라메타로 받는걸 많이 사용됐는데 최근엔 리턴으로  받는것이 추세임

**리턴값으로 출력받기**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents=0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }
};

Cents add(const Cents& c1, const Cents& c2)
{
	return Cents(c1.getCents() + c2.getCents());
}

int main()
{
	Cents cents1(6);
	Cents cents2(8);

	cout << add(cents1, cents2).getCents() << endl;

	return 0;
}
```
___


**연산자 오버로딩**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents=0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }
};

Cents operator + (const Cents& c1, const Cents& c2)
{
	return Cents(c1.getCents() + c2.getCents());
}

int main()
{
	Cents cents1(6);
	Cents cents2(8);

	cout << (cents1 + cents2 + Cents(6)).getCents() << endl; // 20

	return 0;
}
```

- `Cents add` 의 add 부분을 지우고 `operator +` 로 바꿔주면됨 
- `(cents1 + cents2 + Cents(6))`
  - `cents1 + cents2` 가 더해진뒤 `Cents(6)` 이 더해진 형태 

___

**friend 로 `.getCents()` 없애기**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents=0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	friend Cents operator + (const Cents& c1, const Cents& c2)
	{
		return Cents(c1.getCents() + c2.getCents());
	}
};

int main()
{
	Cents cents1(6);
	Cents cents2(8);


	cout << (cents1 + cents2 + Cents(6)+ Cents(10) + Cents(10)).getCents() << endl;

	return 0;
}
```

- 연산자 오버로딩 시 `+` 이외의 `-` `*` `/` 다 가능함
- 주의점
  - 하기 연산자들은 오버로딩이 안됨
    - `?:` 컨디셔널 오퍼레이퍼 삼항연산자
    - `sizeof` 
    - `::` 범위 연산자
    - `.`
    - `.*`
  - 연산자 우선순위는 그대로임 못바꿈
    - `연산자 오버로딩 *` > `연산자 오버로딩 +`
  - 수학시간에 배운것과 직관적으로 통하는것들만 오버로딩하는 것이 좋음
  - 애매하거나 위험성이 있을땐 함수사용하기
    - 위험한것 보다는 불편한게 나음
  - `^` 연산자 우선순위가 매우낮기때문에 () 로 싸서 해줘야하기 때문에 오버로딩 안하는것이 좋음

___

**멤버 펑션 연산자 오버로딩**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents=0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	Cents operator + (const Cents& c2)
	{
		return Cents(this ->m_cents + c2.m_cents);
	}
};

int main()
{
	Cents cents1(6);
	Cents cents2(8);


	cout << (cents1 + cents2 + Cents(6)+ Cents(10) + Cents(100)).getCents() << endl;

	return 0;
}
```

- `+` 연산자는 멤버로 바꾸는 순간 왼쪽 파라메타는 this로 바꿔야함
- 멤버 함수로만 오버로딩이 되는 연산자가 있음 `=`, `[]`, `()` `->`












### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

# 😊 배우게 된 점

# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)