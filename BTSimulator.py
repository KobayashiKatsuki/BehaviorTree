# -*- coding: utf-8 -*-
"""
BehavioTree simulator

BTをロードしてうごかす

Actionは、その中でBBの更新は行わない
Actionはスクリプトを渡すのではなく
Actionがどのスクリプトかを指定し、実行する
Actionで実行すべきスクリプトは外部管理

"""

from BehaviorTree import BehaviorTree as BT
from BTBasic import BlackBoard as BB
from BTBasic import NodeStatus

class BTEngine:
    """ BT実行系  """
    def __init__(self, bt: BT):
        self.bt = bt
        self.stat = NodeStatus.failure
                
    def start(self, bb: BB) -> NodeStatus:
        """ BTの実行 """
        self.stat = self.bt.behave(bb)
        return self.stat


#%%
if __name__ == '__main__':
        # シミュレーション環境の各種インスタンス生成
    bt = BT()
    bt.load('./bt.json')
    
    bb = BB()
    bb.set_key('life', 100)
    bb.set_key('turn', 0)
    
    # BT実行系
    bt_engine = BTEngine(bt=bt)

    for tick in range(10):                
        # 動作実行
        print(f'Tick {tick}: ')              
        bb.set_key('turn', tick)
        stat = bt_engine.start(bb)
        print(f"  {bb.get_board()}")
        print(f'...{stat}')
        
        # 環境更新        
        life = bb.get_value('life')
        bb.set_key('life', life-10)
