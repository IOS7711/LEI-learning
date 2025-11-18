#定义一个学生类
# 要求:
# 1.属性包括学生姓名、学号，以及语数英三科的成绩
#2.能够设置学生某科目的成绩
#3.能够打印出该学生的所有科目成绩
class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = {'语文': 0, '数学': 0, '英语': 0} #初始化成绩为0 “{}”指的是字典

    def set_score(self, subject, score):
        if subject in self.scores:
            self.scores[subject] = score  #更新学生某门课程的成绩
        else:
            print(f"科目 {subject} 不存在。")

    def print_scores(self):
        print(f"学生姓名: {self.name}, 学号: {self.student_id}")
        for subject, score in self.scores.items():  ##调用  self.scores.items()  后，会返回一个可迭代的对象，这个对象包含了字典中所有的键值对
            print(f"{subject} 成绩: {score}")
chen = student("小成","20254330301")
chen.set_score("语文", 85)
chen.set_score("数学", 90)
chen.set_score("英语", 88)
ming = student("小明","20254330302")
ming.set_score("语文", 80)
ming.set_score("数学", 91)
ming.set_score("英语", 82)
print(chen.print_scores())
print(ming.print_scores())
