# coding:utf-8
"""
カードモジュール

カードとして使用するファイルの生成・削除を実施します。
"""
import json

class PlayingCards():
    """
    トランプカードクラス
    """
    
    # トランプの種別総数
    PLAYING_CARD_TYPE = [
        {'full': 'spade', 'initial': 's'}, 
        {'full': 'heart', 'initial': 'h'}, 
        {'full': 'diamond', 'initial': 'd'}, 
        {'full': 'club', 'initial': 'c'}
    ]

    PLAYING_CARD_TYPE_TOTAL_NUM = 4

    # トランプの種別ごとの総数
    PLAYING_CARD_NUM = 13

    def create(self):
        """
        トランプカードのJSONを作成する
        """
        path_w = 'out/card/playing_cards.json'

        # JSONファイル生成用辞書オブジェクト
        jsonList = []

        # JSON文字列作成
        for pcDic in PlayingCards.PLAYING_CARD_TYPE:
            i = 1
            while i <= PlayingCards.PLAYING_CARD_NUM:
                jsonList.append(
                    {
                        'type_initial': pcDic['initial'],
                        'type_full': pcDic['full'],
                        'num': i
                    }
                )
                i = i + 1
                
        s = json.dumps(jsonList)

        with open(path_w, mode='w') as f:
            f.write(s)


class NimZeroType():
    """
    ニム零式クラス
    """