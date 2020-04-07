
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix


def is_hit(vel, alpha):
    h = 10
    d = 2000
    g = 9.81
    v_0y = vel*np.sin(alpha*np.pi/180)
    v_0x = vel*np.cos(alpha*np.pi/180)
    D = v_0y**2-2*g*h
    t_f = max((-v_0y-np.sqrt(D))/(-g), (-v_0y+np.sqrt(D))/(-g))
    x_f = t_f * v_0x
    # print(x_f)
    if d <= x_f <= (d + 1000):
        return True
    else:
        return False


vel = 160
alpha = 45
is_hit(160, 45)

train_v = np.random.uniform(low=100, high=200, size=100)
train_alpha = np.random.uniform(low=30, high=60, size=100)

train_x = [[train_v[i], train_alpha[i]] for i in range(100)]
train_y = [is_hit(train_v[i], train_alpha[i]) for i in range(100)]

tree = DecisionTreeClassifier()

tree.fit(train_x, train_y)
plot_tree(tree)

test_v = np.random.uniform(low=100, high=200, size=100)
test_alpha = np.random.uniform(low=30, high=60, size=100)

test_x = [[test_v[i], test_alpha[i]] for i in range(100)]
test_y = [is_hit(test_v[i], test_alpha[i]) for i in range(100)]

predictions = tree.predict(test_x)

print(confusion_matrix(test_y, predictions))

# =================================================================================

N = 10000
n_hits = []
while len(n_hits) < N:
    temp_v = np.random.uniform(low=100, high=200, size=1)[0]
    temp_alpha = np.random.uniform(low=30, high=60, size=1)[0]
    if is_hit(temp_v, temp_alpha):
        n_hits.append([temp_alpha, temp_alpha])

pred_hits = tree.predict(n_hits)

np.sum(pred_hits)
