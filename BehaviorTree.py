# -*- coding: utf-8 -*-
"""
Behavior Treeクラス

"""

from BTBasic import NodeStatus, BehaviorTreeNode, BlackBoard
from Selector import Selector
from Sequence import Sequence
from Action import Action
from Condition import Condition
import pandas as pd
import json

class BehaviorTree():
        
    def __init__(self, root=None):
        self.root = root
        
    def behave(self, bb: BlackBoard):
        """ BTの振る舞い """
        return self.root.behave(bb)
    
    def create(self):
        """ BTを内作する """       
        self.root = Selector()    
        
        seq1 = Sequence()
        cond1 = Condition('turn', '<', 5)        
        
        act1 = Action("hello")
        act2 = Action()
        act2.set_script("print('ask slot')")
        
        seq1.append_node(cond1)
        seq1.append_node(act1)
        seq1.append_node(act2)       
        self.root.append_node(seq1)
       
        seq2 = Sequence()    
        act3 = Action("goodbye")
        act4 = Action()
        act4.set_script("bb['life'] = bb['life'] + 5")
        
        seq2.append_node(act3)
        seq2.append_node(act4)
        
        self.root.append_node(seq2)
                
    
    def load(self, bt_file):
        """ 
        外部で定義したBTをロードする
        bt_filename: BTの定義ファイル　JSON形式
        フォーマット：
        {"Selector": [子ノード]}
        {"Sequence": [子ノード]}
        {"Action": "Action名（スクリプトファイル名）"}
        {"Condition": ["bbの変数名", "比較演算子", "値"]}                
        """
        def decode_json(j_obj, node: BehaviorTreeNode):            
            
            if type(j_obj) is dict:                
                for k in j_obj.keys():                    
                    if k == 'Selector':
                        if node is None:
                            node =  Selector()
                            decode_json(j_obj[k], node)
                        else:
                            sel = Selector() 
                            decode_json(j_obj[k], sel)
                            node.append_node(sel)

                    elif k == 'Sequence':
                        if node is None:
                            node =  Sequence()
                            decode_json(j_obj[k], node)

                        else:
                            seq = Sequence() 
                            decode_json(j_obj[k], seq)
                            node.append_node(seq)
                       
                    elif k == 'Action':
                        act = Action(j_obj[k])
                        node.append_node(act)
                       
                    elif k == 'Condition':
                        cond = Condition(j_obj[k][0], j_obj[k][1], j_obj[k][2])                        
                        node.append_node(cond)
            
            elif type(j_obj) is list:
                for c in j_obj:
                    decode_json(c, node)
            
            self.root = node
            return

        """ jsonフォーマットのファイルを展開 """
        with open(bt_file, 'r') as f:
            bt_json = json.load(f)
            decode_json(bt_json, self.root)            
            
            
#%%
if __name__ == '__main__':
    
    if False:
        root = Sequence()    
        act1 = Action()
        act1.set_script("print('Hello')")    
        act2 = Action()
        act2.set_script("print('World!')")
        #sel1 = Selector()
        sel1 = Sequence()
        
        sel1.append_node(act1)
        sel1.append_node(act2)
    
        act3 = Action()
        act3.set_script("print('Good')")
        act4 = Action()
        act4.set_script("print('Bye!')")
        sel2 = Selector()
        sel2.append_node(act3)
        sel2.append_node(act4)
        
        root.append_node(sel1)
        root.append_node(sel2)
        
        """ behavior tree """
        bb = BlackBoard()
        bt = BehaviorTree(root)
        print(bt.behave(bb))
    
    
    bt = BehaviorTree()
    bt.load('./bt.json')
    
        