# -*- coding: utf-8 -*-
"""
Conditionクラス
"""

from BTBasic import NodeStatus, BehaviorTreeNode, BlackBoard

class Condition(BehaviorTreeNode):

    """ Conditionノード """
    def __init__(self, key, cmp, th):
        self.key = key
        self.th = th
        
        # 比較演算子
        # >, <, >=, <=, ==, != 以外はエラー
        operator = ['>', '<', '>=', '<=', '==', '!=']
        if cmp in operator:
            self.cmp = cmp
        else:
            raise ValueError('argument \'cmp\' must be an operator string.') 
        

    def behave(self, bb: BlackBoard):
        """
          条件処理　
          key の val を th と cmp して True なら Success を返す
        """
        cond_rlt = NodeStatus.failure
        try:
            val = bb.get_value(self.key)
            cond_script = f'{val} {self.cmp} {self.th}'
            print(f'condition: {cond_script} ?')
            ret = eval(cond_script)            
            if ret == True:
                cond_rlt = NodeStatus.success            
                
        except :
            cond_rlt = NodeStatus.failure
            
        return cond_rlt    
    
    
if __name__ == '__main__':
    bb = BlackBoard()
    bb.set_key(key='x', val=10)
    
    cond = Condition('x', '>', 0)
    print(cond.behave(bb))
    