import sys


# 트라이 알고리즘 : 문자열 검색에 이용 O(m) m은 문자열의 길이
# 문자열 검색 알고리즘 중 가장 빠른 시간복잡도

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    li = []
    trie = Trie()
    for j in range(n):
        li.append(sys.stdin.readline().rstrip())
    for word in li:
        trie.insert(word)
    check = False
    for word in li:
        temp = trie.starts_with(word)
        if len(temp) > 1:
            check = True
    if check:
        print("NO")
    else:
        print("YES")

# 시간 초과 O(n^2)
# T = int(sys.stdin.readline())
#
# for i in range(T):
#     n = int(sys.stdin.readline())
#     li = []
#     for j in range(n):
#         li.append(sys.stdin.readline().rstrip())
#     li.sort(key=lambda x: len(x))
#
#     breaker = False
#     for j in range(len(li)):
#         if breaker:
#             print("NO")
#             break
#         for z in range(j+1, len(li)):
#             if li[j] != li[z][:len(li[j])]:
#                 continue
#             else:
#                 breaker = True
#                 break
#     if not breaker:
#         print("YES")
