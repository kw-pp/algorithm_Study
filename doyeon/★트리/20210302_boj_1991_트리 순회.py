def preorder(node):  # (루트) (왼쪽 자식) (오른쪽 자식)
    if node == '.':
        return
    print(node,end='')
    preorder(my_dict[node][0])
    preorder(my_dict[node][1])

def inorder(node):  # (왼쪽 자식) (루트) (오른쪽 자식)
    if node == '.':
        return
    inorder(my_dict[node][0])
    print(node, end='')
    inorder(my_dict[node][1])

def postorder(node):  # (왼쪽 자식) (오른쪽 자식) (루트)
    if node == '.':
        return
    postorder(my_dict[node][0])
    postorder(my_dict[node][1])
    print(node, end='')

N = int(input())
my_dict = {}
for _ in range(N):
    root, left, right = input().split()
    my_dict[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()