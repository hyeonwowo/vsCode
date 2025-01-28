# 클래스 기본 구조

class 클래스이름:
    # 생성자 (객체를 초기화할 때 호출)
    def __init__(self, 속성1, 속성2):
        self.속성1 = 속성1  # 객체 속성 초기화
        self.속성2 = 속성2

    # 메서드 정의
    def 메서드이름(self):
        print(f"{self.속성1}와 {self.속성2}를 사용합니다.")



# ex1) 학생 관리 클래스

class Student:
    def __init__(self, name, age, major):
        """
        Student 클래스의 생성자
        :param name: 학생 이름
        :param age: 학생 나이
        :param major: 전공
        """
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        """학생 정보를 출력하는 메서드"""
        print(f"안녕하세요! 저는 {self.name}, {self.age}살이고 {self.major} 전공입니다.")

    def update_major(self, new_major):
        """학생의 전공을 변경하는 메서드"""
        self.major = new_major
        print(f"{self.name}의 전공이 {self.major}(으)로 변경되었습니다.")


# 사용 방법

    # 객체 생성
student1 = Student("철수", 20, "컴퓨터공학")
student2 = Student("영희", 22, "경영학")

    # 메서드 호출
student1.introduce()
student2.introduce()

    # 전공 변경
student1.update_major("인공지능")
