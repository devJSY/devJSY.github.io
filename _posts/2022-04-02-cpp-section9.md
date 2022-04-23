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
last_modified_at: 2022-04-23
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

### **🌱 9.2 입출력 연산자 오버로딩 하기**

- `<<` , `>>`

**기존 class 출력 코드**

```cpp
#include <iostream>

using namespace std;

class Point
{
private:
	double m_x, m_y, m_z;

public:
	Point(double x = 0.0, double y = 0.0, double z = 0.0)
		: m_x(x), m_y(y), m_z(z)
	{}

	double getX() { return m_x; }
	double getY() { return m_y; }
	double getZ() { return m_z; }

	void print()
	{
		cout << m_x << " " << m_y << " " << m_z;
	}
};
int main()
{
	Point p1(0.0, 0.1, 0.2), p2(3.4, 1.5, 2.0);

	p1.print();
	cout << " ";
	p2.print();
	cout << endl;

	return 0;
}
```

**입출력 연산자 오버로딩**

```cpp
#include <iostream>

using namespace std;

class Point
{
private:
	double m_x, m_y, m_z;

public:
	Point(double x = 0.0, double y = 0.0, double z = 0.0)
		: m_x(x), m_y(y), m_z(z)
	{}

	double getX() { return m_x; }
	double getY() { return m_y; }
	double getZ() { return m_z; }

	friend std::ostream& operator << (std::ostream& out, const Point& point)
	{
		out << "( " << point.m_x << " " << point.m_y << " " << point.m_z << " )";

		return out;
	}
};
int main()
{
	Point p1(0.0, 0.1, 0.2), p2(3.4, 1.5, 2.0);

	cout << p1 << " " << p2 << endl;

	return 0;
}
```

- `return out;` 을 하는 이유는 체이닝 하기위해서임
- 멤버 펑션으로 만들수 없음 
  - 첫번째 파라메타가 포인터클래스가 아니라 아웃풋 스트림이기 때문임


**파일 출력하기**

```cpp
#include <iostream>
#include <fstream>

using namespace std;

class Point
{
private:
	double m_x, m_y, m_z;

public:
	Point(double x = 0.0, double y = 0.0, double z = 0.0)
		: m_x(x), m_y(y), m_z(z)
	{}

	double getX() { return m_x; }
	double getY() { return m_y; }
	double getZ() { return m_z; }

	friend std::ostream& operator << (std::ostream& out, const Point& point)
	{
		out << "( " << point.m_x << " " << point.m_y << " " << point.m_z << " )";

		return out;
	}
};
int main()
{
	ofstream of("out.txt");

	Point p1(0.0, 0.1, 0.2), p2(3.4, 1.5, 2.0);

	cout << p1 << " " << p2 << endl;
	of << p1 << " " << p2 << endl;

	of.close();

	return 0;
}
```

- 파일출력이 스트림으로 되기 때문에 그대로 사용할 수 있음
  - 파일출력과 콘솔출력을 둘다 해주는것임
- `#include <fstream>` 한뒤 `ofstream of("out.txt");` 선언후 `of << p1 << " " << p2 << endl;` , `of.close();` 를 해주면 `out.txt` 파일이 생성되고 그안의 p1,p2의 내용이 입력됨

- 리턴타입으로 `std::ostream&` 가 있기때문에 연쇄가 가능함

**입력 오버로딩**

```cpp
#include <iostream>
#include <fstream>

using namespace std;

class Point
{
private:
	double m_x, m_y, m_z;

public:
	Point(double x = 0.0, double y = 0.0, double z = 0.0)
		: m_x(x), m_y(y), m_z(z)
	{}

	double getX() { return m_x; }
	double getY() { return m_y; }
	double getZ() { return m_z; }

	friend std::ostream& operator << (std::ostream& out, const Point& point)
	{
		out << "( " << point.m_x << " " << point.m_y << " " << point.m_z << " )";

		return out;
	}

	friend std::istream& operator >> (std::istream& in, Point& point)
	{
		in >> point.m_x >> point.m_y >> point.m_z;

		return in;
	}
};
int main()
{
	ofstream of("out.txt");

	Point p1, p2;

	cin >> p1 >> p2;

	cout << p1 << " " << p2 << endl;
	of << p1 << " " << p2 << endl;

	of.close();

	return 0;
}
```

### **🌱 9.3 단항 연산자 오버로딩 하기**

- `+`,`-`,`!`

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	Cents operator - () const
	{
		return Cents(-m_cents);
	}

	friend std::ostream& operator << (std::ostream& out, const Cents& cents)
	{
		cout << cents.m_cents;
		return out;
	}
};

int main()
{
	Cents cents1(6);
	Cents cents2(0);

	cout << cents1 << endl; // 6
	cout << -cents1 << endl; // -6
	cout << -Cents(-10) << endl; // 10

	return 0;
}
```

- `Cents operator - () const` 생성자 로 만들어주면됨

**! 연산자 오버로딩**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	Cents operator - () const
	{
		return Cents(-m_cents);
	}

	bool operator ! () const
	{
		return (m_cents == 0) ? true : false; // if 문으로 해도됨
	}

	friend std::ostream& operator << (std::ostream& out, const Cents& cents)
	{
		cout << cents.m_cents;
		return out;
	}
};

int main()
{
	Cents cents1(6);
	Cents cents2(0);

	// auto temp = !cents1; bool 로 잡고있음
	// auto temp = cents1; Cents 로 잡고 있음

	cout << !cents1 << " " << !cents2 << endl; // 0 1

	return 0;
}
```

### **🌱 9.4 비교 연산자 오버로당 하기**

- `==` , `!=` , `>`, `>=`

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	friend bool operator == (const Cents& c1, const Cents& c2)
	{
		return c1.m_cents == c2.m_cents;
	}

	friend std::ostream& operator << (std::ostream& out, const Cents& cents)
	{
		cout << cents.m_cents;
		return out;
	}
};

int main()
{
	Cents cents1(6);
	Cents cents2(6);

	if (cents1 == cents2) 
		cout << "Equal" << endl;

	return 0;
}
```

- 그냥 인스턴스 끼리 `==` 등으로 비교하려고 하면 에러가 발생함
- `friend bool operator ==` 로 만들어줘야 사용할 수 있음

___

**연산자 오버로딩으로 배열 정렬하기**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	friend bool operator < (const Cents& c1, const Cents& c2)
	{
		return c1.m_cents < c2.m_cents;
	}

	friend std::ostream& operator << (std::ostream& out, const Cents& cents)
	{
		cout << cents.m_cents;
		return out;
	}
};

int main()
{
	std::random_device rd;
	std::mt19937 g(rd());

	vector<Cents> arr(20);
	for (unsigned i = 0; i < 20; ++i)
		arr[i].getCents() = i;

	std::shuffle(arr.begin(), arr.end(), g);

	for (auto& e : arr)
		cout << e << " ";
	cout << endl;

	std::sort(begin(arr), end(arr));

	for (auto& e : arr)
		cout << e << " ";
	cout << endl;


	return 0;
}
```

- C++ 17에서 std::random_shuffle 이 폐기됨
- 대신 `<random>` 라이브러리를 include 하여 사용할수 있음
- 인스턴스 끼리 크기비교를 못하기 때문에 연산자를 오버로딩해줘야함
- sort 라이브러리 구현할때는 `<` 연산자를 오버로딩해줘야함
  - `>` 는 에러발생함
  - 리턴타입을 `>` 으로해주면 역 정렬이 되긴함

### **🌱 9.5 증감 연산자 오버로딩 하기**

- `++` , `--`
- 전위형, 후위형 에따라 성질이다름

```cpp
#include <iostream>


using namespace std;

class Digit
{
private:
	int m_digit;

public:
	Digit(int digit = 0) : m_digit(digit) {}

	//prefix
	Digit& operator ++ ()
	{
		++m_digit;
		return *this;
	}

	// postfix
	Digit operator ++ (int)
	{
		Digit temp(m_digit);
		++(*this);

		return temp;
	}

	friend ostream& operator << (ostream& out, const Digit& d)
	{
		out << d.m_digit;
		return out;
	}
};

int main()
{
	Digit d(5);

	cout << ++d << endl; // 5
	cout << d << endl; // 6

	cout << d++ << endl; // 6
	cout << d << endl; // 7

	return 0;
}
```

- `postfix` 일땐 파라메타에 더미로 자료형 아무거나 들어감
- `prefix` 일때는 아무것도 안들어감

### **🌱 9.6 첨자 연산자 오버로딩 하기**

- `[]` subscipt operator
- 동적 메모리 할당 사용할땐 접근하려는 메모리가 제대로 잡혀있는지 주의해야함

**기본 배열 리스트**

```cpp
#include <iostream>

using namespace std;

class IntList
{
private:
	int m_list[10];

public:
	void setItem(int index, int value)
	{
		m_list[index] = value;
	}

	int getItem(int index)
	{
		return m_list[index];
	}
};

int main()
{
	IntList my_list;
	my_list.setItem(3, 1);
	cout << my_list.getItem(3) << endl;

	return 0;
}
```

**배열 포인터로 리턴받아서 바꾸기**

```cpp
#include <iostream>

using namespace std;

class IntList
{
private:
	int m_list[10];

public:
	void setItem(int index, int value)
	{
		m_list[index] = value;
	}

	int getItem(int index)
	{
		return m_list[index];
	}

	int* getList()
	{
		return m_list;
	}
};

int main()
{
	IntList my_list;
	my_list.setItem(3, 1);
	cout << my_list.getItem(3) << endl;

	my_list.getList()[3] = 10;
	cout << my_list.getList()[3] << endl;

	return 0;
}
```

- 배열 자체가 포인터 이기 때문에 리턴값을 받아서 값을 입출력할수 있음

___

**`[]` 연산자 오버로딩**

```cpp
#include <iostream>

using namespace std;

class IntList
{
private:
	int m_list[10];

public:
	int& operator [] (const int index)
	{
		return m_list[index];
	}
};

int main()
{
	IntList my_list;
	my_list[3] = 10;

	cout << my_list[3] << endl;

	return 0;
}
```

- 레퍼런스로 리턴하는 이유는 읽을수도있고 값을 바꿔주기위해서임
  - 항상 L-value 여야되기 때문임

**const `[]`**

```cpp
#include <iostream>

using namespace std;

class IntList
{
private:
	int m_list[10] = {1,2,3,4,5,6,7,8,9,10};

public:
	int& operator [] (const int index)
	{
		return m_list[index];
	}

	const int& operator [] (const int index) const
	{
		return m_list[index];
	}
};

int main()
{
	const IntList my_list;

	cout << my_list[3] << endl;

	return 0;
}
```

___

**포인터를 사용할때 주의사항**

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class IntList
{
private:
	int m_list[10] = {1,2,3,4,5,6,7,8,9,10};

public:
	int& operator [] (const int index)
	{
		assert(index >= 0);
		assert(index < 10);

		return m_list[index];
	}

	const int& operator [] (const int index) const
	{
		assert(index >= 0);
		assert(index < 10);

		return m_list[index];
	}
};

int main()
{
	IntList* list = new IntList;

	list[3] = IntList; // Not Ok
	(*list)[3] = 10; // OK

	return 0;
}
```

- `[]` 보통 이런 서브스크립트 오퍼레이터는 엄청많이 사용하기위해 쓰는것이기 때문에 if문으로 걸어버리면 엄청느려지기 때문에 `assert`를 사용함
- 포인터를 사용할때 `list[3] = 10;` 와같이 접근하려면 에러가 발생함 `(*list)[3] = 10;` 와 같이 사용해줘야함
  - list 자체가 포인터 이기 때문에 de-reference 를 해줘야 리스트를 온전히 받아올수 있다는 뜻!


### **🌱 9.7 괄호 연산자 오버로딩과 함수 객체**

- `()` parenthesis
- Function object(Functor)

- 함수를 호출할때 사용하는 연산자와 같음

```cpp
#include <iostream>

using namespace std;

class Accumulator
{
private:
	int m_counter = 0;

public:
	int operator() (int i) { return (m_counter += i); }
};

int main()
{
	Accumulator acc;
	cout << acc(10) << endl;
	cout << acc(20) << endl;

	return 0;
}
```

- `[]` 와 사용법은 같음
- 위와같은 형태를 Functor 하고함

### **🌱 9.8 형변환을 오버로딩 하기**

- static_cast typecasts

**기본코드**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) 
	{ 
		m_cents = cents; 
	}

	int getCents() { return m_cents; }
	void setCents(int cents) { m_cents = cents; }

	operator int()
	{
		cout << "cast here" << endl;
		return m_cents;
	}
};

void printInt(const int& value)
{
	cout << value << endl;
}

int main()
{
	Cents cents(7);
	int value = (int)cents;
	value = int(cents);
	value = static_cast<int>(cents);

	printInt(cents);

	return 0;
}
```

- 오버로딩을 하지않고 인스턴스를 바로 사용하면 암시적 형변환이 안됨
- 오버로딩한 타입 캐스트를 사용하는 것임

**달러 → 센트로 형변환 하기**

```cpp
#include <iostream>

using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) 
	{ 
		m_cents = cents; 
	}

	int getCents() { return m_cents; }
	void setCents(int cents) { m_cents = cents; }

	operator int()
	{
		cout << "cast here" << endl;
		return m_cents;
	}
};

class Dollar 
{
private:
	int m_dollars= 0;
public:
	Dollar(const int& input) : m_dollars(input) {}

	operator Cents()
	{
		return Cents(m_dollars * 100);
	}
};
void printInt(const int& value)
{
	cout << value << endl;
}

int main()
{
	Dollar dol(2);

	Cents cents = dol;

	printInt(cents);

	return 0;
}
```

### **🌱 9.9 복사 생성자 , 복사 초기화 , RVO**

- Return Value Optimization

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	Fraction(int num = 0, int den = 1)
		: m_numerator(num), m_denominator(den)
	{
		assert(den != 0);
	}

	Fraction(const Fraction& fraction) // copy constructor
		: m_numerator(fraction.m_numerator), m_denominator(fraction.m_denominator)
	{
		cout << "copy construcor called" << endl;
	}

	friend std::ostream& operator << (std::ostream& out, const Fraction& f)
	{
		out << f.m_numerator << " / " << f.m_denominator << endl;
		return out;
	}

};

int main()
{
	Fraction frac(3, 5);

	Fraction fr_copy(frac); // 1
	// Fraction fr_copy = frac; 2 

	// Fraction fr_copy(Fraction(3,10)); // 3

	cout << frac << " " << fr_copy << endl;

	return 0;
}
```

- copy constructor 은 자신과 같은타입의 인스턴스가 들어오면 복사하는 것
- `#1` , `#2` `=` 사용방법은 다르지만 이경우 에도 copy constructor 가 호출이됨
- `#3` 이 경우에는 복사 생성자가 호출이 안됨
  - 컴파일러가 임의로 `Fraction`을 빼서 `fr_copy(3,10)` 형태로 만든것

- 복사를 못하게 막아버리고 싶은경우에는 `copy constructor` 를 `private`로 막아버리면됨

___

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	Fraction(int num = 0, int den = 1)
		: m_numerator(num), m_denominator(den)
	{
		assert(den != 0);
	}

	Fraction(const Fraction& fraction) // copy constructor
		: m_numerator(fraction.m_numerator), m_denominator(fraction.m_denominator)
	{
		cout << "copy construcor called" << endl;
	}

	friend std::ostream& operator << (std::ostream& out, const Fraction& f)
	{
		out << f.m_numerator << " / " << f.m_denominator << endl;
		return out;
	}

};

Fraction doSomething()
{
	Fraction temp(1, 2);
	cout << &temp << endl;
	return temp;
}

int main()
{
	Fraction result = doSomething();

	cout << &result << endl;
	cout << result << endl;

	return 0;
}
```

- 디버거 모드에서는 copy constructor 가 실행이됨
- 릴리즈 모드에서는 copy constructor 가 실행이 안됨
- 반환값 최적화 기능으로 컴파일러가 해주는 기능
  - 디버거 모드에선 주소가 다르지만 릴리즈모드에선 주소가 같음

### **🌱 9.10 변환 생성자 , explicit, delete**

- 변환 생성자 Converting constructor
  - 생성자를 변환 시켜주는것
- explicit 
  - 변환 생성자를 사용못하게 막아버리는 것
  - 직접적으로 하라는 의미
- delete
  - 특정 생성자를 사용못하게 지워버리는 것
  - 동적할당때 delete 와는 다름

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	Fraction(int num = 0, int den = 1)
		: m_numerator(num), m_denominator(den)
	{
		assert(den != 0);
	}

	Fraction(const Fraction& fraction) // copy constructor
		: m_numerator(fraction.m_numerator), m_denominator(fraction.m_denominator)
	{
		cout << "copy construcor called" << endl;
	}

	friend std::ostream& operator << (std::ostream& out, const Fraction& f)
	{
		out << f.m_numerator << " / " << f.m_denominator << endl;
		return out;
	}

};

void doSomething(Fraction frac)
{
	cout << frac << endl;
}

int main()
{
	Fraction frac(7);

	doSomething(frac); // 1
	doSomething(Fraction(7)); // 2
	doSomething(7); // 3

	return 0;
}
```

- 자동으로 기본값이 들어가서 출력이됨
  - 함수입장에서 받아들일수 있는것이 `Fraction` 밖에 없다면 생성자처럼 바꿔 주는 것
  - `num` 에 7이 들어온것 처럼 생성해준 것

___

**explicit , delete**

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	Fraction(char) = delete;

	explicit Fraction(int num = 0, int den = 1)
		: m_numerator(num), m_denominator(den)
	{
		assert(den != 0);
	}

	Fraction(const Fraction& fraction) // copy constructor
		: m_numerator(fraction.m_numerator), m_denominator(fraction.m_denominator)
	{
		cout << "copy construcor called" << endl;
	}

	friend std::ostream& operator << (std::ostream& out, const Fraction& f)
	{
		out << f.m_numerator << " / " << f.m_denominator << endl;
		return out;
	}

};

void doSomething(Fraction frac)
{
	cout << frac << endl;
}

int main()
{
	Fraction('c'); // Error

	Fraction frac(7);

	doSomething(frac); // 1
	doSomething(Fraction(8)); // 2
	doSomething(7); // 3 Error

	return 0;
}
```

- 생성자 이름앞에 explicit을 넣으면 인수값을 더 엄격하게 받음
  - `Converting constructor` 의 기능을 막아버리는 것
- `Fraction(char) = delete;` 를 넣어주면 버전업을 하면서 예전에쓰던방법을 막아버리는 경우사용
  - 자동 컨버전이나 캐스팅이 걱정될때 사용

### **🌱 9.11 대입 연산자 오버로딩, 깊은 복사, 얕은 복사**

- 깊은 복사 Deep copy 
- 얕은 복사 Shallow copy

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class MyString
{
// ptivate:
public:
	char* m_data = nullptr;
	int m_length = 0;

public:
	MyString(const char* source = "")
	{
		assert(source);

		m_length = std::strlen(source) + 1;
		m_data = new char[m_length];

		for (int i = 0; i < m_length; ++i)
			m_data[i] = source[i];
		
		m_data[m_length - 1] = '\0';
	}

	~MyString()
	{
		delete[] m_data;
	}

	char* getString() { return m_data; }
	int getLength() { return m_length; }
};

int main()
{
	MyString hello("Hello");

	cout << (int*)hello.m_data << endl; // 00000241E04A27A0
	cout << hello.getString() << endl; // Hello

	{
		MyString copy = hello;
		cout << (int*)copy.m_data << endl; // 00000241E04A27A0
		cout << copy.getString() << endl; // Hello
	}

	cout << hello.getString() << endl; // 硼硼硼硼硼

	return 0;
}
```

- `strlen()` 문자열 갯수를 뽑아내기위해서 사용
  - +1을 한이유는 문자열의 마지막을 표현하기위해 `'\0'` 을 넣을려고 추가한것

- 똑같은 주소를 가르키고 있는 포인터 변수가 메모리를 지워버리면 힙에 메모리가 지워져서 사라졌는데도 불구하고 다른 포인터가 사라진 주소에 접근하려 하는 문제가 발생됨

- 문자열 클래스 만들때 사용되는 기본적인 형태임

- `MyString copy = hello;` 와 같이 copy가 생성이되고 있으면 생성자를 호출함
- `copy = hello;` 와 같은형태는 대입 연산자를 호출함

- `硼硼硼硼硼` 가 뜨는이유 copy 해서 그주소를 받아와서 갖고 있었는데 같은 주소를 바라보고 있는 상황에서  `{}`이 끝난뒤 `delete[] m_data;` 로 힙에있는 원본데이터를 날려버려서 이상한 값이 출력되는 것임
  - 동적메모리할당은 사용하는 경우에는 copy constructor 나 assignment 할때 주의해야함

___

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class MyString
{
// ptivate:
public:
	char* m_data = nullptr;
	int m_length = 0;

public:
	MyString(const char* source = "")
	{
		assert(source);

		m_length = std::strlen(source) + 1;
		m_data = new char[m_length];

		for (int i = 0; i < m_length; ++i)
			m_data[i] = source[i];
		
		m_data[m_length - 1] = '\0';
	}

	MyString(const MyString &source)
	{ 
		cout << "Copy constructor" << endl;

		m_length = source.m_length;

		if (source.m_data != nullptr)
		{
			m_data = new char[m_length];

			for (int i = 0; i < m_length; ++i)
				m_data[i] = source.m_data[i];
		}
		else
			m_data = nullptr;
	}

	MyString& operator = (const MyString& source)
	{
		//// shallow copy
		//this->m_data = source.m_data;
		//this->m_length = source.m_length;

		cout << "Assignment operator " << endl;

		if (this == &source) // prevent self-assignment
			return *this;

		delete[] m_data;

		m_length = source.m_length;

		if (source.m_data != nullptr)
		{
			m_data = new char[m_length];

			for (int i = 0; i < m_length; ++i)
				m_data[i] = source.m_data[i];
		}
		else
			m_data = nullptr;

		return* this;
	}

	~MyString()
	{
		delete[] m_data;
	}

	char* getString() { return m_data; }
	int getLength() { return m_length; }
};

int main()
{
	MyString hello("Hello");

	cout << (int*)hello.m_data << endl; // 0000019C9AEF35B0
	cout << hello.getString() << endl; // Hello

	{
		MyString copy = hello;
		cout << (int*)copy.m_data << endl; // 0000019C9AEF3510
		cout << copy.getString() << endl; // Hello
	}

	cout << hello.getString() << endl; // Hello

	return 0;
}
```

- `MyString(const MyString &source)` 메모리를 따로잡아야함
  - `source` 가 복사해주고 반드시 사라진다는 보장이 있다면 메모리를 안지우고 `source`메모리를 가져와도됨
  - copy constructor는 반드시 사라질거라는 보장이 없음


**얕은 복사:** 디폴트 copy constructor 가 해주는것은 m_data나 m_length 자체를 복사해준것 포인터 조차도 주소값자체를 복사해주는것 

**깊은 복사** 주소값을 복사하는 대신 메모리를 다시 할당받고 거기에 값을 복사해서 할당하는 것
	- 위 예제코드 에선 copy constructor 안에서 메모리를 새로 할당 받고 할당받은 메모리에 source 메모리가 갖고있는 내용을 복사한것

- 디폴트 대입연산자는 `shallow copy` 와같은 형태로 동작이 수행됨
- `prevent self-assignment` 대입연산자 는 자기자신을 넣을수 있기 때문에 this 와 source의 주소를 비교해서 같다면 끝내버림
- `delete[] m_data;`  copy constructor 와 달리 대입연산자는 메모리를 갖고있을수 있으니 지워주고 시작
- 중복되는 코드는 함수로 묶어서 없애는 것이 좋음

___

```cpp
#include <iostream>
#include <cassert>

using namespace std;

class MyString
{
// ptivate:
public:
	char* m_data = nullptr;
	int m_length = 0;

public:
	MyString(const char* source = "")
	{
		assert(source);

		m_length = std::strlen(source) + 1;
		m_data = new char[m_length];

		for (int i = 0; i < m_length; ++i)
			m_data[i] = source[i];
		
		m_data[m_length - 1] = '\0';
	}

	// MyString(const MyString& source) = delete;

	MyString(const MyString &source)
	{ 
		cout << "Copy constructor" << endl;

		m_length = source.m_length;

		if (source.m_data != nullptr)
		{
			m_data = new char[m_length];

			for (int i = 0; i < m_length; ++i)
				m_data[i] = source.m_data[i];
		}
		else
			m_data = nullptr;
	}

	MyString& operator = (const MyString& source)
	{
		//// shallow copy
		//this->m_data = source.m_data;
		//this->m_length = source.m_length;

		cout << "Assignment operator " << endl;

		if (this == &source) // prevent self-assignment
			return *this;

		delete[] m_data;

		m_length = source.m_length;

		if (source.m_data != nullptr)
		{
			m_data = new char[m_length];

			for (int i = 0; i < m_length; ++i)
				m_data[i] = source.m_data[i];
		}
		else
			m_data = nullptr;

		return* this;
	}

	~MyString()
	{
		delete[] m_data;
	}

	char* getString() { return m_data; }
	int getLength() { return m_length; }
};

int main()
{
	MyString hello("Hello");

	MyString str1 = hello; // 1 Copy constructor 출력
	// MyString str1(hello); 

	MyString str2;
	str2 = hello; // 2 Assignment operator 출력

	return 0;
}
```

- `#1` 선언과 동시에 초기화 시 `=` 가 있지만 Copy constructor 가 실행이됨
- `#2` 선언한뒤 대입 할때는 Assignment operator 가 출력됨

- `#1` 코드를 `MyString str1(hello);` 와같이 하면 기능은 똑같고 보기편함 
- `MyString(const MyString& source) = delete;` Copy constructor를 임시로 막아둘때 사용 가장좋은건 Copy constructor를 구현해 놓는것

- `std::string` 을 사용하기
  - 상속받아서 추가 구현하기
  - `std::string data;`
  - 퍼포먼스가 약간 떨어질수 있음

### **🌱 9.12 이니셜라이즈 리스트 initializer_list**

- 사용자 정의 자료형에서 편하게 사용할수 있는 리스트

```cpp
#include <iostream>
#include <cassert>
#include <initializer_list>

using namespace std;

class IntArray
{
private:
	unsigned m_length = 0;
	int* m_data = nullptr;

public:
	IntArray(unsigned length)
		: m_length(length)
	{
		m_data = new int[length];
	}

	IntArray(const std::initializer_list<int>& list)
		: IntArray(list.size())
	{
		int count = 0;
		for (auto& element : list)
		{
			m_data[count] = element;
			++count;
		}

		//for (unsigned count = 0; count < list.size(); ++count)
		//	m_data[count] = list[count]; // Error
	}

	~IntArray()
	{
		delete[] this->m_data;
	}

	// T0D0

	friend ostream& operator << (ostream& out, IntArray& arr)
	{
		for (unsigned i = 0; i < arr.m_length; ++i)
			out << arr.m_data[i] << " ";
		out << endl;
		return out;

	}
};


int main()
{
	int my_arr1[5] = { 1,2,3,4,5 };
	int* my_arr2 = new int[5]{ 1,2,3,4,5 };

	auto i1 = { 10,20,30 };

	IntArray int_array{ 1,2,3,4,5 };
	cout << int_array << endl;

	return 0;
}
```

- `#include <initializer_list>` 해준뒤 `auto i1 = { 10,20,30 };` 하면 자동으로 `initializer_list` 로 잡아줌
- 이니셜라이즈 리스트 는 `[]` 를 지원하지 않음
- 이니셜라이즈 리스트는 이터레이터를 사용하여 for문을 돌리도록 되어있음
  - for each문에서 사용하는 방식임
- 이니셜라이즈 리스트 를이용하여 생성자 구현할때 대입연산자도 같이 오버로딩하는것이 좋음


# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)