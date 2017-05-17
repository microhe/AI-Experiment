import random
from config import configs


class HGS24NumsNode(object):
    start_nums_table = ''
    end_nums_table = ''
    r_num = configs['ROWNUM']
    c_num = configs['COLNUM']
    '''
    启发式搜索算法的节点
    '''

    def __init__(self, nums_table):
        '''
        nums_table: 数码表
        '''
        self.nums_table = nums_table.copy()
        self.score = 0
        self.last_move = ''
        self.blank_location = self.get_blank_location()
        self.last_node = None
        self.move_count = 0
        self.calc_graph_score()

        # self.next_nodes = []

    def new_node(self):
        new_node = HGS24NumsNode(self.nums_table)
        new_node.score = self.score
        new_node.last_move = self.last_move
        new_node.blank_location = self.blank_location
        new_node.last_node = self
        new_node.move_count = self.move_count
        return new_node

    def calc_graph_score(self):
        h = 0
        for i in range(len(self.nums_table)):
            j = HGS24NumsNode.end_nums_table.index(self.nums_table[i])
            i_x = i % HGS24NumsNode.c_num
            i_y = int(i / HGS24NumsNode.c_num)
            j_x = j % HGS24NumsNode.c_num
            j_y = int(j / HGS24NumsNode.c_num)
            h += (abs(i_x - j_x) + abs(i_y - j_y))
        self.score = self.move_count + h

    def get_blank_location(self):
        return self.nums_table.index(0)

    def blank_move(self, index2):
        index1 = self.blank_location
        tmp = self.nums_table[index1]
        self.nums_table[index1] = self.nums_table[index2]
        self.nums_table[index2] = tmp
        self.blank_location = index2
        self.move_count += 1
        self.calc_graph_score()

    def blank_up(self):
        '''
        数码表空位置上移
        若不能移则返回NULL
        '''
        index = self.blank_location - HGS24NumsNode.c_num
        if self.last_move == 'D' or index < 0:
            return None
        node = self.new_node()
        node.last_move = 'U'
        node.blank_move(index)
        return node

    def blank_down(self):
        '''
        数码表空位置下移
        若不能移则返回NULL
        '''
        index = self.blank_location + HGS24NumsNode.c_num
        if self.last_move == 'U' or index >= len(self.nums_table):
            return None
        node = self.new_node()
        node.last_move = 'D'
        node.blank_move(index)
        return node

    def blank_right(self):
        '''
        数码表空位置右移
        若不能移则返回NULL
        '''
        index = self.blank_location + 1
        if self.last_move == 'L' or index % HGS24NumsNode.c_num == 0:
            return None
        node = self.new_node()
        node.last_move = 'R'
        node.blank_move(index)
        return node

    def blank_left(self):
        '''
        数码表空位置右移
        若不能移则返回NULL
        '''
        index = self.blank_location - 1
        if self.last_move == 'R' or self.blank_location % HGS24NumsNode.c_num == 0:
            return None
        node = self.new_node()
        node.last_move = 'L'
        node.blank_move(index)
        return node


if __name__ == '__main__':
    nums_list = []
    for i in range(25):
        nums_list.append(i)
    HGS24NumsNode.start_nums_table = nums_list
    HGS24NumsNode.end_nums_table = nums_list
    start_node = HGS24NumsNode(nums_list)
    nums = []
    for j in (20, 50, 100, 150, 200, 300, 400, 500):
        node_n = start_node
        move_steep = ''
        for i in range(j):
            node_n_move = []

            moved_node = node_n.blank_up()
            if moved_node is not None:
                node_n_move.append(moved_node)
            moved_node = node_n.blank_down()
            if moved_node is not None:
                node_n_move.append(moved_node)
            moved_node = node_n.blank_right()
            if moved_node is not None:
                node_n_move.append(moved_node)
            moved_node = node_n.blank_left()
            if moved_node is not None:
                node_n_move.append(moved_node)

            random_index = random.randint(0, len(node_n_move) - 1)

            node_n = node_n_move[random_index]
            move_steep += node_n_move[random_index].last_move
        print(node_n.nums_table)
        nums.append(node_n.nums_table)
        print(move_steep)

    print(nums)
