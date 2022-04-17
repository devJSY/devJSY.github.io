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
last_modified_at: 2022-04-17
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



### **🌱 **

### **🌱 **

### **🌱 **

### **🌱 **

# 😊 배우게 된 점

# 📌참조링크
인프런 **따라하면서 배우는 C++** - [https://www.inflearn.com/course/following-c-plus](https://www.inflearn.com/course/following-c-plus)