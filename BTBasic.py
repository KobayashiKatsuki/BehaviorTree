# -*- coding: utf-8 -*-
"""
BehaviorTreeの基本クラス集

"""

from abc import ABCMeta, abstractmethod

#%%
class NodeStatus:
    """ ノードの状態 """
    success = 'Success'
    failure = 'Failure'
    

#%%
class BlackBoard:
    """ BlackBoard """
    def __init__(self):
        self.board = dict()
        
    def set_key(self, key, val=None):
        """ キーに値をセット """
        self.board[key] = val
        
    def get_value(self, key):
        """ キーの値を取得 """
        return self.board[key]
    
    def get_board(self):
        """ blackboard自体を取得 """
        return self.board
    
    def get_keys(self):
        """ キー一覧を取得 """
        return self.board.keys()
    

#%%
class BehaviorTreeNode(metaclass=ABCMeta):
    """ BTノード抽象クラス """
    @abstractmethod
    def behave(self, bb: BlackBoard) -> NodeStatus:
        pass  # あるいは raise NotImplementedError()
    


#%%
if __name__ == '__main__':
    bb = BlackBoard('bb')
    bb.set_key(key='x', val=10)
    bb.set_key(key='y', val=20)
    bb.set_key(key='z')
       
    print(bb.get_value(key='x'))
    