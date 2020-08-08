# -*- coding: utf-8 -*-
"""
Actionクラス

"""

from BTBasic import NodeStatus, BehaviorTreeNode, BlackBoard
import action

class Action(BehaviorTreeNode):
    """ Actionノード """   
    def __init__(self, act_name=None):
        self.act_name = act_name
        self.script = None
        
    def set_script(self, script=""):
        """ 手動でスクリプトをセットする場合 """
        self.script = script      
       
    def behave(self, blackboard: BlackBoard):
        """ Actionの実行 スクリプト実行して成功したらSuccessを返す """
        rlt = NodeStatus.success
        try:
            # BlackBoardをロード
            exec(f"bb = {blackboard.get_board()}")
                        
            # Actionスクリプトを実行
            if self.script is not None:            
                exec(self.script)            
                
            elif self.act_name is not None:
                eval(f"action.{self.act_name}.{self.act_name}(bb)")   
            
            # BlackBoardを更新
            for key in blackboard.get_keys():
                val = eval("bb[key]")                
                blackboard.set_key(key, val)
            
        except :
            rlt = NodeStatus.failure
            
        return rlt    
    
    
if __name__ == '__main__':
    bb = BlackBoard()
    bb.set_key('a', 10)
    bb.set_key('b', 20)
    bb.set_key('c', 30)
    bb.set_key('budget', 0)
    
    """
    act_a = Action("bb['a'] = bb['a'] + 3")
    act_b = Action("bb['b'] = bb['b'] - 3")
    act_c = Action("print(bb['c'])")
    """
    
    # スクリプトを外部定義
    #action.hello.hello(bb)
    #action.goodbye.goodbye(bb)
    
    print("Which one?")
    print("1. hello  2.goodbye")
    d = input()
    
    # モジュールディレクトリ.スクリプトファイル名.メソッド名
    act_dict = {'1': "hello", '2': "goodbye"}
    act = Action(act_dict[d])
    print(act.behave(bb))
    
    act.set_script("print('hello')")
    print(act.behave(bb))
                    
    for i in range(5):
        print(f"Episode {i}")
        act_ask = Action("ask_slot")    
        print(act_ask.behave(bb))    
        print(bb.get_board())
