# -*- coding: utf-8 -*-
"""
Sequenceクラス
"""

from BTBasic import NodeStatus, BehaviorTreeNode, BlackBoard
from Action import Action

class Sequence(BehaviorTreeNode):
    """
    Sequence
    子ノードが全てSuccessならSuccessを返して終了
    """   
    def __init__(self):
        self.childlen = []
        
    def append_node(self, node: BehaviorTreeNode):
        """ ノードを追加 """
        self.childlen.append(node)
    
    def behave(self, bb: BlackBoard):
        """ Sequenceの振る舞い """        
        for child in self.childlen:
            child_status = child.behave(bb)
            if child_status == NodeStatus.failure:
                return NodeStatus.failure
        
        return NodeStatus.success


if __name__ == '__main__':
    root_q = Sequence()
    bb = BlackBoard()
    
    act1 = Action("print('Hello')")    
    act2 = Action("print('World!')")    
    seq1 = Sequence()
    seq1.append_node(act1)
    seq1.append_node(act2)
    
    act3 = Action("print('Good')")
    act4 = Action("print('Bye!')")
    seq2 = Sequence()
    seq2.append_node(act3)
    seq2.append_node(act4)
    
    root_q.append_node(seq1)
    root_q.append_node(seq2)
    
    print(root_q.behave(bb=bb))
    