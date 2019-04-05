# coding:utf-8
class CardInitializer:
    
    # トランプの種別総数
    PLAYING_CARD_TYPE_TOTAL_NUM = 4

    # トランプの種別ごとの総数
    PLAYING_CARD_NUM = 13

    def createPlayingCards():
        """
        トランプカードのJSONを作成する
        """
        path_w = 'out/card/test.json'

        s = '['

        # JSON文字列作成
        i = 0
        while i < CardInitializer.PLAYING_CARD_TYPE_TOTAL_NUM:
            s = s + '{'
            s = s + '"type_initial":'
            s = s + str(i)
            s = s + '}'
            i += 1
            if (i < CardInitializer.PLAYING_CARD_TYPE_TOTAL_NUM):
                s = s + ','

        s = s + ']'

        with open(path_w, mode='w') as f:
            f.write(s)