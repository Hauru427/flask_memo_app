import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import  sessionmaker, relationship, declarative_base

# create DB
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# create database engine
db_engine = create_engine(database, echo=True)
Base = declarative_base()

# model
class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    # relation one to many
    employees = relationship("Employee", back_populates= "department")
    # diplay function
    def __str__(self):
        return f"部署ID：{self.id}, 部署名：{self.name}"

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # ForeignLeyには「テーブル名、カラム名」を指定
    department_id = Column(Integer, ForeignKey('departments.id'))
    # relation one to one
    department = relationship("Department", back_populates="employees", uselist=False)

    # display func
    def __str__(self):
        return f"従業員ID：{self.id}, 従業員名:{self.name}"

# table oparations
print('(1)テーブルを削除してから作成')
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)

# create session
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

# データ作成
print('(2)データ登録実行：実行')
# department
dept01 = Department(name='開発部')
dept02 = Department(name='営業部')

# employee
emp01 = Employee(name='太郎')
emp02 = Employee(name='ジロウ')
emp03 = Employee(name='サブちゃん')
emp04 = Employee(name='花子')

# Link employee to departments
# 開発部：太郎、ジロウ
# 営業部：サブちゃん、花子
dept01.employees.append(emp01)
dept01.employees.append(emp02)
dept02.employees.append(emp03)
dept02.employees.append(emp04)

# セッションで部署をとうろk
session.add_all([dept01, dept02])
session.commit()

print('(3)データ参照：実行')
print('▪️：Employeeの参照')
target_emp = session.query(Employee).filter_by(id=1).first()
print(target_emp)
print('▪️：Employeeに紐づいたDepartmentの参照')
print(target_emp.department)

print('▪️' * 100)

print('▪️：Departmentの参照')
target_dept = session.query(Department).filter_by(id=1).first()
print(target_dept)
print('▪️：Departmentに紐づいたEmployeeの参照')
for emp in target_dept.employees:
    print(emp)