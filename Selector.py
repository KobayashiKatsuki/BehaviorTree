# -*- coding: utf-8 -*-
"""
Selectorクラス
"""

from BTBasic import NodeStatus, BehaviorTreeNode, BlackBoard
from Action import Action

class Selector(BehaviorTreeNode):
    """
    Selector
    子ノードのいずれかひとつがSuccessならSuccessを返して終了
    """    
    def __init__(self):
        self.childlen = []
        
    def append_node(self, node: BehaviorTreeNode):
        """ ノードを追加 """
        self.childlen.append(node)
        
    def behave(self, bb: BlackBoard):
        """ Selectorの振る舞い """        
        for child in self.childlen:
            child_status = child.behave(bb)
            if child_status == NodeStatus.success:
                return NodeStatus.success
        
        return NodeStatus.failure


if __name__ == '__main__':
    root_l = Selector()
    bb = BlackBoard()
    
    act1 = Action("print('Hello')")    
    act2 = Action("print('World!')")
    sel1 = Selector()
    sel1.append_node(act1)
    sel1.append_node(act2)

    act3 = Action("print('Good')")
    act4 = Action("print('Bye!')")
    sel2 = Selector()
    sel2.append_node(act3)
    sel2.append_node(act4)
    
    root_l.append_node(sel1)
    root_l.append_node(sel2)
    
    print(root_l.behave(bb=bb))
    