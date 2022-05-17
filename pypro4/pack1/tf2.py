# tf에서 변수 선언 후 사용
import tensorflow as tf

f = tf.Variable(1.0)   # 변수는 초기값을 줘야한다. 안주면 err
v = tf.Variable(tf.ones((2,)))
m = tf.Variable(tf.ones((2, 1)))
print(f, f.numpy())
print(v)
print(m)

print()
v1 = tf.Variable(1)
print(v1)
v1.assign(10)       # assign : 1 변수 값에서 10으로 변경하기 
print(v1)

print()
v2 = tf.Variable(tf.ones(shape=(1)))    # 1차원 tensor
v2.assign([20])
print(v2)

print()
v3 = tf.Variable(tf.ones(shape=(1,2)))  # 2차원 tensor    
v3.assign([[20, 30]])
print(v3)

print()
v1 = tf.Variable([3])
v2 = tf.Variable([5])
v3 = v1 * v2 + 10
print(v3)

print()
va = tf.Variable([1,2,3,4,5], dtype=tf.float32)
result = va + 10
print(result)

print()
w = tf.Variable(tf.ones(shape=(1,)))
b = tf.Variable(tf.ones(shape=(1,)))
w.assign([2])
b.assign([3])

def func1(x):           # python 일반 함수에서 텐서를 수행하면 python 순수 연산을 하므로 속도가 느림 
    return w * x + b

out_a = func1([3])
print('out_a : ', out_a)

@tf.function            # auto graph 기능 - 텐서 연산시 속도를 증진. 일반 python 함수를 호출 가능한 그래프 객체로 만듦 
def func2(x):
    return w * x + b

out_b = func2([3])
print('out_b : ', out_b)

print('----------------------' * 10)
gr = tf.Graph()

with gr.as_default():
    c1 = tf.constant(1, name='c_one')
    print(c1, type(c1))
    print(c1.op)
    # print(gr.as_graph_def())
    print('----------------------' * 10)
    v1 = tf.Variable(initial_value = 5, name='v1')
    print(v1.op)
    print(gr.as_graph_def())
    
    