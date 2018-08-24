# coding=utf-8
def hello_world():
    print("hello, world!")
def triple_kill():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    triple_kill()