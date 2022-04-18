---
published: true
title:  "따라하며 배우는 C++ Section 8. 객체지향의 기초"
excerpt: ""

categories:
  - 따배씨++
tags:
  - [C++]

toc: true
toc_sticky: true
 
date: 2022-04-13
last_modified_at: 2022-04-18
---

# 🤔 학습목표
- 따라하며 배우는 C++ Section 8. 객체지향의 기초

# 📃 학습내용
## 📍 **따라하며 배우는 C++ Section 8. 객체지향의 기초**

### **🌱 8.1 객체지향 프로그래밍과 클래스**

- Object Oriented Programming
- Class

**기본코드**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Friend : name, address, age, hright, weight, ...

void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	string name;
	string address;
	int age;
	double height;
	double weight;

	print(name, address, age, height, weight);

	vector<string> name_vec;
	vector<string> addr_vec;
	vector<int> age_vec;
	vector<double> height_vec;
	vector<double> weight_vec;

	print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);

	return 0;
}
```

___

**구조체**
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Friend : name, address, age, hright, weight, ...

struct Friend
{
	string name;
	string address;
	int age;
	double height;
	double weight;
};


void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	Friend jj{"Jack Jack", "Uptown" , 2, 30 , 10};
	/*jj.name = "Jack Jack";
	jj.age = 2;*/

	print(jj.name, jj.address, jj.age, jj.height, jj.weight);

	vector<string> name_vec;
	vector<string> addr_vec;
	vector<int> age_vec;
	vector<double> height_vec;
	vector<double> weight_vec;

	print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);

	return 0;
}
```

- `jj.` 멤버선택자

___

**매개변수를 구조체로 받기**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Friend : name, address, age, hright, weight, ...

struct Friend
{
	string name;
	string address;
	int age;
	double height;
	double weight;
};

void print(const Friend &fr)
{
	cout << fr.name << " " << fr.address << " " << fr.age << " " 
		<< fr.height << " " << fr.weight << endl;
}

void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	Friend jj{"Jack Jack", "Uptown" , 2, 30 , 10};

	print(jj);
	/*print(jj.name, jj.address, jj.age, jj.height, jj.weight);*/

	vector<string> name_vec;
	vector<string> addr_vec;
	vector<int> age_vec;
	vector<double> height_vec;
	vector<double> weight_vec;

	print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);

	return 0;
}
```

___

**print() 구조체에 넣어버리기**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Friend : name, address, age, hright, weight, ...

struct Friend
{
	string name;
	string address;
	int age;
	double height;
	double weight;

	void print()
	{
		cout << name << " " << address << " " << age << " "
			<< height << " " << weight << endl;
	}

};

void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	Friend jj{"Jack Jack", "Uptown" , 2, 30 , 10};

	jj.print();
	/*print(jj.name, jj.address, jj.age, jj.height, jj.weight);*/

	vector<string> name_vec;
	vector<string> addr_vec;
	vector<int> age_vec;
	vector<double> height_vec;
	vector<double> weight_vec;

	print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);

	return 0;
}
```
- print() 함수를 구조체에 직접넣어 같은멤버이기 때문에 접근할수 있어 코드량을 줄일수 있음.
- 데이터와 기능이 묶여있는 걸 오브젝트라고 부름

___

**class**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Object
// Friend : name, address, age, hright, weight, ...
// print()

class Friend
{
public: // access specifier (public, private, protected)
	string name;
	string address;
	int age;
	double height;
	double weight;

	void print()
	{
		cout << name << " " << address << " " << age << " "
			<< height << " " << weight << endl;
	}

};

void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	Friend jj{"Jack Jack", "Uptown" , 2, 30 , 10}; // instanciation, instance
	cout << &jj << endl;

	jj.print();
	/*print(jj.name, jj.address, jj.age, jj.height, jj.weight);*/

	vector<string> name_vec;
	vector<string> addr_vec;
	vector<int> age_vec;
	vector<double> height_vec;
	vector<double> weight_vec;

	print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);

	return 0;
}
```

- 단순한 기능, 데이터를 묶을때는 구조체
- 데이터를 묶는것 + 기능을 넣을 때는 클래스를 사용하는것이 일반적임
- C 에서는 구조체에 기능을 못넣음
  - C++ 에서는 가능함

- 접근 지정자 (access specifier)
  - public
  - private
  - protected

- **객체 (Object)**
  - 데이터와 기능을 묶여있는걸 개념적으로 생각하는것이 객체임
  - 이를 프로그램으로 구현하는 개념이 **Class임**

- 실제로 메모리를 차지하도록 정의 해주는 것을 **instanciation** 라고함
  - 오브젝트를 구현하기위해 만든것 `jj` 를 **instance** 라고함

- 코드는 짧고 간결할수록 좋음

___

**for 문으로 출력하여 코드량 줄이기**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Object
// Friend : name, address, age, hright, weight, ...
// print()

class Friend
{
public: // access specifier (public, private, protected)
	string m_name;
	string m_address;
	int m_age;
	double m_height;
	double m_weight;

	void print()
	{
		cout << m_name << " " << m_address << " " << m_age << " "
			<< m_height << " " << m_weight << endl;
	}

};

void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	Friend jj{"Jack Jack", "Uptown" , 2, 30 , 10}; // instanciation, instance
	cout << &jj << endl;

	jj.print();

	vector<Friend> my_friends;
	my_friends.resize(2);

	/*my_friends[0].print();
	my_friends[1].print();*/

	for (auto& ele : my_friends)
		ele.print();

	/*vector<string> name_vec;
	vector<string> addr_vec;
	vector<int> age_vec;
	vector<double> height_vec;
	vector<double> weight_vec;

	print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);*/

	return 0;
}
```

- 멤버변수 표현하는 방식으로 변수 이름앞에 `m_` 을 붙여줌
  - 최근 구글 스타일에서는 뒤에만 `_` 를 붙여주는 경우도 있음
  - 맨앞에 `_` 를 붙여주는 경우도 있음

- 구조체 에는 access specifier 가 안들어감


### **🌱 8.2 캡슐화, 접근 지정자, 접근 함수**

- 캡슐화 - Encapsulation
- 접근 지정자 - Access Specifiers
- 접근 함수 - Access Functions

___

**class 초기화 방법**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Date 
{
private: // Access Specifiers
	int m_month;
	int m_day;
	int m_year;

};

int main()
{
	Date today/*{8,4,2025}*/;
	today.m_month = 8;
	today.m_day = 4;
	today.m_year = 2025;

	return 0;
}
```
- 초기화 방법은 구조체와 비슷함

**Access Specifiers**

- `:` 를 접근 지정자 Access Specifiers 라고 부름
  - 클래스 내부 멤버들을 밖에서 접근할수 있게할지 없게할지 지정해줌
- **public:** 전역변수
- **private:** 지역변수
  - public을 안써주면 private가 기본임
- **protected:** 상속배운뒤 설명
- 접근을 할때 **Access Function**을 만들어줘야함
  - 연구등을 할때는 혼자서하기 때문에 public으로 두고 사용하는 경우가 있음
  - 오픈소스등에서는 Access Function 을 해주는것이 좋음
- private를 써주거나 안써줌

___

**Access Function**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Date 
{
	int m_month;
	int m_day;
	int m_year;

public:
	void setDate(const int& month_input, const int& day_input, const int& year_input)
	{
		m_month = month_input;
		m_day = day_input;
		m_year = year_input;
	}

	void setMonth(const int& month_input) 
	{
		m_month = month_input;
	}

	// setDat, setYear ... // setters

	const int& getDay() // getters
	{
		return m_day;
	}
};

int main()
{
	Date today;
	today.setDate(8,4,2025);
	today.setMonth(10);

	cout << today.getDay() << endl;

	return 0;
}
```

- 생성자 강의 때 초기화 방법 다룸
- 출력할때 변수는 지역변수로 막혀있으니 `getDay()` 와 같이 함수를 하나 만들어서 그 리턴값으로 출력받도록 해줘야함
  - 값으로 리턴시 복사가됨 레퍼런스로 리턴하는 경우도 있음
  - 출력함수 이기때문에 const 로 막아놓고 값을 바꾸고 싶다면 setDate 등의 함수에서 바꾸도록 정리하기
  - getters 라고부름

___

**class 복사**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Date 
{
	int m_month;
	int m_day;
	int m_year;

public:
	void setDate(const int& month_input, const int& day_input, const int& year_input)
	{
		m_month = month_input;
		m_day = day_input;
		m_year = year_input;
	}

	void setMonth(const int& month_input) 
	{
		m_month = month_input;
	}

	// setDat, setYear ... // setters

	const int& getDay() // getters
	{
		return m_day;
	}

	void copyFrom(const Date& original)
	{
		m_month = original.m_month;
		m_day = original.m_day;
		m_year = original.m_year;
	}
};

int main()
{
	Date today;
	today.setDate(8,4,2025);
	today.setMonth(10);

	Date copy;
	/*copy.copyFrom(today.setMonth, today.getDay ....); */
	copy.copyFrom(today);
		
	return 0;
}
```

- 인스턴스의 이름이 길어지니 복사하고자하는 클래스의 인스턴스 하나를 넣어주면 깔끔해짐
- 메모리 통째로 복사하는 경우도 있음
- 서로다른 메모리의 인스턴스에도 같은 클래스에서 나왔으면 멤버 접근할수 있음
- 클래스 멤버변수를 public 으로 해놓았을때 변수이름을 바꿔야하는 상황일때 class 이외의 함수에서 이름을 바꿔줘야하는 불편함이 있음
  - private 즉 캡슐화를 해주면 class 내부에서만 수정하면되기 때문에 편함

### **🌱 8.3 생성자 Constructors**

- 이 클래스의 인스턴스들은 만들어질 때 이러한속성을, 이러한 기능을 수행해야해 하는 경우 생성자를 사용함

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Frsaction
{
private:
	int m_numerator;
	int m_denominator;

public:
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{
	Frsaction frac;

	frac.print();
	
		
	return 0;
}
```

- 분자 / 분모를 출력하는 코드 
- 초기화를 해주지않았기 때문에 쓰레기 값이 출력됨

___

**해결법 1**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Frsaction
{
public:
  // int m_numerator = 0;
	// int m_denominator = 1; 기본값 넣기
	int m_numerator;
	int m_denominator;

public:
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{
  Frsaction frac;

	// Frsaction frac{0 ,1};
	frac.m_numerator = 0;
	frac.m_denominator = 1;

	frac.print(); // 0 / 1
	
		
	return 0;
}
```

- 클래스 멤버변수를 public 으로 바꿔주고 메인함수에서 초기화하기
- 하나하나 멤버변수를 초기화해주는것이 번거로움
  - 유니폼 이니셜라이징을 해서 초기화해도됨

___

**인스턴스 기본값셋팅 1**

```cpp
class Frsaction
{
public:
	int m_numerator = 0;
	int m_denominator = 1;

public:
	Frsaction()
	{
		m_numerator = 0;
		m_denominator = 1;
	}

};
```

- public 인스턴스라 권장하지않음

**인스턴스 기본값셋팅 2**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Frsaction
{
private:
	int m_numerator;
	int m_denominator;

public:
	Frsaction()
	{
		m_numerator = 1;
		m_denominator = 1;

		cout << "Fraction constructor" << endl;
	}

	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{
	Frsaction frac;

	frac.print(); 
	
		
	return 0;
}
```

- 생성자를 사용하는 방법
- 리턴 값이 없고 class와 이름이 같다면 생성자임
- 외부에서 호출하는 용도가 아니고 class 선언시(`Frsaction frac`) 실행이 됨
- frac 다음에 () 가 없는 이유
  - 생성자의 파라메타가 하나도없는 경우에만 괄호를 빼도록 되어 있음 
  - 생성자의 파라메타가 하나도없는 경우 함수와 헷갈림

___

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Frsaction
{
private:
	int m_numerator;
	int m_denominator;

public:
  // Frsaction() {} 디폴트 생성자
	Frsaction(const int& num_in, const int& den_in = 1)
	{
		m_numerator = num_in;
		m_denominator = den_in;

		cout << "Fraction constructor" << endl;
	}

	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{
	/*Frsaction frac; 오류
	frac.print(); */

	Frsaction one_thirds(1);
	one_thirds.print();
	
	return 0;
}
```

- 생성자에도 파라메타를 넣을 수 있음
  - 디폴트 벨류를 넣어줄수도 있음
- `Frsaction frac;` 가 오류나는 이유
  - 생성자가 없을땐 디폴트 생성자가 숨어있음
  - 컴파일러가 생성자가 없을때 알아서 디폴트생성자를 만들어서 넣어줌 생성자가 아예없으면 인스턴스 생성을 못하기 때문임
  - 생성자가 클래스의 인스턴스를 만드는것은 아니고 생성될때 호출되는 함수임
  - 생성자를 하나만이라도 생성해주면 기본 생성자는 생성이 안됨
- 생성자의 파라메타가 없는 경우
  - `Frsaction frac()` 문법적인 이유로 이렇게 호출하면안됨
  - `Frsaction frac` 이런식을 괄호를 빼주어야함


```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Frsaction
{
private:
	int m_numerator;
	int m_denominator;

public:

	Frsaction() // 1
	{
		m_numerator = 1;
		m_denominator = 1;
	}

	Frsaction(const int& num_in = 1, const int& den_in = 1) // 2
	{
		m_numerator = num_in;
		m_denominator = den_in;

		cout << "Fraction constructor" << endl;
	}

	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{

	Frsaction one_thirds; // Error
	one_thirds.print();
	
	return 0;
}
```

- `Frsaction one_thirds;` 가 에러가발생하는 이유
  - 1번 생성자와 2번 생성자가 디폴트 파라메타가 중복되어 에러가 발생하는 것 


```cpp
int main()
{

  Frsaction one_thirds = Frsaction{1, 3}; // 1
	Frsaction one_thirds{ 1.0, 3 }; // 2
	Frsaction one_thirds( 1.0, 3 ); // 3

	one_thirds.print();
	
	return 0;
}
```

- `#1` 과 같이 copy initialize 를해도되지만 `#2` 처럼 쓰는게 코드길이가 짧아서 더좋음
- `{}` 와 `()` 의 차이
  - 멤버들이 public 일때는 `{}`으로 초기화 할 수 있음 `()` 는 안됨
    - 단 생성자가 있을땐 `{}` 와  `()` 를 둘다 사용할 수 있음
    - `{}` 은 타입 변환을 허용을 안함
    - `()` 은 warring 이 뜨긴하지만 컴파일이 되긴함
    - 대부분의 경우 둘다 비슷함 `{}` 이 최근에 나왔고 조금 더 엄격함

___

**class 안의 class**

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Second
{
public:
	Second()
	{
		cout << "class Second constructor()" << endl;
	}
};

class First
{
	Second sec;

public:
	First()
	{
		cout << "class First constructor()" << endl;
	}
};

int main()
{
	First fir;
	/*
	class Second constructor()
	class First constructor()
	*/
	
	return 0;
}
```

- Second가 First의 멤버로 들어가 있기 때문에 멤버를 먼저 초기화 해줘야 거기에 대해서 First가 뭔거 작업을 할수 있기 때문임
- 한 class 가 다른 class를 멤버 변수로 사용할 경우 멤버 변수의 생성자가 먼저 실행됨
- 생성자를 private로 사용할 수도 있음
  - 특별한 경우에 사용함 

### **🌱 8.4 생성자 맴버 초기화 목록**

- 생성자의 멤버 이니셜라이져 리스트 Member Initializeer List
- 멤버 초기화 리스트, 멤버 초기자 리스트 라고도 부름

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Something
{
private:
	int		m_i;
	double	m_d;
	char	m_c;
	int m_arr[5];

public:
	Something()
		:m_i(1), m_d(3.14), m_c('a'), m_arr{1,2,3,4,5}
	{
		/*m_i = 1;
		m_d = 3.14;
		m_c = 'a';*/
	}

	void print()
	{
		cout << m_i << " " << m_d << " " << m_c << endl;
		for (auto& e : m_arr)
			cout << e << " ";
		cout << endl;
	}
};
int main()
{
	Something som;
	som.print();

	
	return 0;
}
```

- 멤버 이니셜라이즈 리스트 초기화 후에 생성자에서 값을 변경하는것 가능함
- `:` 를 적어줘야하고 마지막에는 `,` 가없음
- `()` 대신에 `{}` 를 써도됨
  - 형변환이 안됨
  - 자동으로 캐스팅안하고 막아버림 
  - 좀더엄격함
- C++ 11부터는 배열도 초기화 할 수 있음

___

**초기화 우선순위**

```cpp
#include <iostream>

using namespace std;

class B
{
private:
	int m_b;

public:
	B(const int& m_b_in)
		: m_b(m_b_in)
	{}
};

class Something
{
private:
	int		m_i = 100;
	double	m_d = 100.0;
	char	m_c = 'F';
	int		m_arr[5] = {100,200,300,400,500};
	B		m_b{1024};

public:
	Something()
		:m_i(1), 
		m_d(3.14), 
		m_c('a'), 
		m_arr{1,2,3,4,5}, 
		m_b(m_i -1)
	{
		m_i *= 3;
		m_d *= 3.0;
		m_c += 3;
	}

	void print()
	{
		cout << m_i << " " << m_d << " " << m_c << " " << endl;
		for (auto& e : m_arr)
			cout << e << " ";
		cout << endl;
	} 
};
int main()
{
	Something som;
	som.print();

	
	return 0;
}
```

- 멤버 안에 다른 클래스 멤버가 들어갈 경우
- 코드가 가로로 길면 줄바꿈을 해서 정리해주기 
  - 한칸씩 줄바꿈
  - 콤마를 앞으로 빼주기
    - 코드의 변동이 많을때 편함
- `Something` 의 `private` non-static 멤버들은 초기화 할수 있음
- 멤버를 초기화하고 생성자에서도 초기화 했을때 생성자 의 우선순위가 더 높아서 생성자에서 초기화 한 값이 적용됨
- 멤버 이니셜라이즈 리스트 초기화 후에 생성자에서 값을 변경한 값이 최종 대입값임

### **🌱 8.5 위임 생성자**

- Delegating Construvtors
- 생성자가 다른 생성자를 사용하는것을 위임 생성자 라고함
- 파라메타가 여러개일때 사용하는 경우가 많음

___

**함수 파라메타 기본값 할당 코드**

```cpp
#include <iostream>
#include <string>

using namespace std;

class Student
{
private:
	int		m_id;
	string	m_name;

public:
	Student(const string& name_in)
		: m_id(0), m_name(name_in)
	{}

	Student(const int& id_in, const string& name_in)
		: m_id(id_in), m_name(name_in)
	{}

	void print()
	{
		cout << m_id << " " << m_name << endl;
	}

};


int main()
{
	Student st1(0, "Jack jack");
	st1.print();

	Student st2("Dash");
	st2.print();

	return 0;
}
```

- `m_id` 에 기본값을 넣고 싶을때 사용할수 있는방법임
- 매우 비추천하는 방법
  - 어떠한 기능을하는 코드는 한군데만 나와야함
  - 초기화 해주는것도 한군데서만 하기
  - `m_id(0)` 미리 이렇게 값을 넣어두면 나중에 찾기 힘듬


**위임 생성자**

```cpp
#include <iostream>
#include <string>

using namespace std;

class Student
{
private:
	int		m_id;
	string	m_name;

public:
	Student(const string& name_in)
		// : m_id(0), m_name(name_in)
		: Student(0, name_in)
	{}

	Student(const int& id_in, const string& name_in)
		: m_id(id_in), m_name(name_in)
	{}

	void print()
	{
		cout << m_id << " " << m_name << endl;
	}

};

int main()
{
	Student st1(0, "Jack jack");
	st1.print();

	Student st2("Dash");
	st2.print();

	return 0;
}
```

- C++ 11이후에 가능한 코드

___

**만능초기화 함수를 하나 만들어 분리하기**

```cpp
#include <iostream>
#include <string>

using namespace std;

class Student
{
private:
	int		m_id;
	string	m_name;

public:
	Student(const string& name_in)
		// : m_id(0), m_name(name_in)
		: Student(0, name_in)
	{
		init(0, name_in);
	}

	Student(const int& id_in, const string& name_in)
	//	: m_id(id_in), m_name(name_in)
	{
		init(id_in, name_in);
	}

	void init(const int& id_in, const string& name_in)
	{
		m_id = id_in;
		m_name = name_in;
	}

	void print()
	{
		cout << m_id << " " << m_name << endl;
	}

};

int main()
{
	Student st1(0, "Jack jack");
	st1.print();

	Student st2("Dash");
	st2.print();

	return 0;
}
```

- `init()` 함수를 하나 만들고 여기서 초기화 후 다른 함수에서 불러다가 사용하는 방법
- 어떤 경우는 이 문법을 더 추천 함

### **🌱 8.6 소멸자 destrctor**

- 생성자는 함수가 만들어질때 실행되는것
- 소멸자는 변수가 영역을 벗어나 소멸이될때 실행되는 것

```cpp
#include <iostream>
#include <string>

using namespace std;

class Simple 
{
private:
	int m_id;

public:
	Simple(const int& id_in)
		: m_id(id_in)
	{
		cout << "Construtor " << m_id << endl;
	}

	~Simple()
	{
		cout << "Destructoir " << m_id << endl;
	}
};

int main()
{
	Simple s1(0);
	Simple s2(1);

	/*Construtor 0
	Construtor 1
	Destructoir 1
	Destructoir 0*/

	return 0;
}
```

- 리턴 타입이 없음
- `~` 틀다
- 소멸자는 파라메타가 없음

___

**동적할당**

```cpp
#include <iostream>
#include <string>

using namespace std;

class Simple 
{
private:
	int m_id;

public:
	Simple(const int& id_in)
		: m_id(id_in)
	{
		cout << "Construtor " << m_id << endl;
	}

	~Simple()
	{
		cout << "Destructoir " << m_id << endl;
	}
};

int main()
{
	/*Simple s1(0);*/
	Simple* s1 = new Simple(0);
	Simple s2(1);

	delete s1;

	/*Construtor 0
	Construtor 1
	Destructoir 0
	Destructoir 1*/

	return 0;
}

```

- 중괄호 영역을 벗어나서 호출
- 소멸자는 instance 가 메모리에서 해제될때 내부에서 자동으로 호출됨 동적할당으로 만들어진 경우에는 영역을 벗어나도 자동으로 메모리가 해제되지 않기 때문에 delete으로 메모리를 해제할 때에만 소멸자가 호출됨 
- 소멸자를 프로그래머가 직접 호출하는 것은 대부분의 경우 권장 하지 않음
- 용도
  - delete 해주는 부분

___

**메모리 릭**

```cpp
#include <iostream>

using namespace std;

class IntArray
{
private:
	int* m_arr = nullptr;
	int m_length = 0;
	 
public:
	IntArray(const int length_in)
	{
		m_length = length_in;
		m_arr = new int[m_length];

		cout << "Constructor" << endl;
	}

	int size() { return m_length; }
};

int main()
{
	while (true)
	{
		IntArray my_int_arr(10000);
		// delete[] my_int_arr.m_arr; 접근을 못함
	}

	return 0;
}
```

- 메모리를 계속 먹음
- delete를 해줘야하는데 `delete[]` 가 번거롭기도하고 접근이 안됨

**소멸자를 활용한 해결 코드**

```cpp
#include <iostream>

using namespace std;

class IntArray
{
private:
	int* m_arr = nullptr;
	int m_length = 0;
	 
public:
	IntArray(const int length_in)
	{
		m_length = length_in;
		m_arr = new int[m_length];

		cout << "Constructor" << endl;
	}

	~IntArray()
	{
		if (m_arr != nullptr) delete[] m_arr;
	}

	int size() { return m_length; }
};

int main()
{
	while (true)
	{
		IntArray my_int_arr(10000);
	}

	return 0;
}
```

- while문의 `{}` 가 끝날때마다 소멸자를 호출해서 `delete[]` 를 해줌
- 메모리 사용시 new가 있다면 delete는 필수
- class 사용할때 new 사용하는 class 에서 위 코드와같이 소멸자로 delete 해주면됨 
- vector 내부에 위 매커니즘같이 메모리를 반납하는 기능이 구현이 되어있음
- new 와 delete 가 느리니까 vector 사용하기

### **🌱 8.7 this 포인터와 연쇄 호출**

- Chaining Member Functions

```cpp
#include <iostream>

using namespace std;

class Simple
{
private:
	int m_id;

public:
	Simple(int id)
	{
		this -> setID(id);
		this -> m_id;
		(*this).setID(id);

		cout << this << endl;
	}

	void setID(int id) { m_id = id; }
	int getId() { return m_id; }
};

int main()
{
	Simple s1(0), s2(1);
	s1.setID(2);
	s2.setID(4);

	cout << &s1 << " " << &s2 << endl;

	//Simple::setID(&s1, 1); == s1.setID(1);
	//Simple::setID(&s2, 4); == s2.setID(4);

	return 0;
}
```

- s1,s2에 각각 따로 저장되있진 않고 
- `this` 자기 자신의 주소를 찍어줌
- `void setID()` 는 클래스의 모든 인스턴스가 공유를 해서 사용하는것 내부적으로 어떻게 구분하느냐면 `this -> setID(id)` 가 숨어있는 것
- `->` 클래스나 구조체가 포인터일 경우 멤버 선택 연산자임
- `this -> m_id;` 와 같이 멤버변수도 접근할 수 있음
- `Simple::setID(&s1, 1);` 문법적으론 사용이 불가능하지만 개념적으론 이와같은 방식으로 작동함
- 각 인스턴스들이 자기의 포인터를 갖고있고 이 포인터를 볼려면 this 키워드를 사용하면 됨
- 현재 주소를 갖고있는 인스턴스에서 setID라는 함수를 사용한다는 의미에서 `this -> setID(id);`
- 현재 this에 들어있는 주소를 갖고 있는 인스턴스의 `m_id` 를 접근한다는 뜻에서 `this -> m_id;`
- 실제 사용할때는 this 를 빼버림

___

**this pointer 의 용법**

```cpp
#include <iostream>

using namespace std;

class Calc
{

private:
	int m_value;

public:
	Calc(int init_value)
		: m_value(init_value)
	{}

	void add(int value) { m_value += value; }
	void sub(int value) { m_value -= value; }
	void mult(int value) { m_value *= value; }

	void print()
	{
		cout << m_value << endl;
	}

};
int main()
{
	Calc cal(10);
	cal.add(10);
	cal.sub(1);
	cal.mult(2);

	cal.print();

	return 0;
}
```

- `cal.` 이 반복됨

**this pointer 의 용법 적용 코드**

```cpp
#include <iostream>

using namespace std;

class Calc
{

private:
	int m_value;

public:
	Calc(int init_value)
		: m_value(init_value)
	{}

	Calc& add(int value) { m_value += value; return *this; }
	Calc& sub(int value) { m_value -= value; return *this; }
	Calc& mult(int value) { m_value *= value; return *this; }

	void print()
	{
		cout << m_value << endl;
	}

};
int main()
{
	Calc cal(10);

	// 1
	Calc& temp1 = cal.add(10);
	Calc& temp2 = cal.sub(1);
	Calc& temp3 = cal.mult(2);
	temp3.print();

	// 2
	cal.add(10).sub(1).mult(2).print();

	return 0;
}
```

- `Calc&` 클래스의 레퍼런스 타입을 리턴하고 자기가신의 주소값을 de-reference 해서 리턴해줌
- clac 타입의 레퍼런스 실제 리턴되는건 정확한 메모리를 가지고 있는 메모리 여야함
- `#1` 과 같이 동작하는 코드를 `#2` 와같이 줄일수 있음
- 이러한 기법을 멤버펑션체이닝 이라고함
  - 실용성은 명확하진않음
  - c++ 입장에선 번거로움
  - api가 좀 복잡할 경우 사용가능한 함수 사용못하는 함수 구분해야되기 때문에 사용자입장에서도 쪼금 애매함

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