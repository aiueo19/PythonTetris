import stage

class Block:
    # テトリミノブロックを定義するクラスです。

    SIZE = 4    # ブロックのサイズ
    SCALE = 32  # ブロックの描画サイズ
    TYPE_MAX = 7# ブロックの種類
    ROT_MAX = 4 # 最高回転回数

    def __init__(self):
        # テトリミノブロックのポジションを初期化し
        # テトリスで使用するすべてのブロックを生成させます。
        self.x = int(stage.Stage.WIDTH / 2 - Block.SIZE / 2)
        self.y = -1
        self.blocks = [
            # O Block
            [
                # 0 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 90 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 180 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 270 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
            ],
            # I Block
            [
                # 0 度
                [
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0]
                ],
                # 90 度
                [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0]
                ],
                # 180 度
                [
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0]
                ],
                # 270 度
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ],
            ],
            # L Block
            [
                # 0 度
                [
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 90 度
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [1, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 180 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0]
                ],
                # 270 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 1],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                ],
            ],
            # J Block
            [
                # 0 度
                [
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 90 度
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 180 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0]
                ],
                # 270 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 1],
                    [0, 0, 0, 0]
                ],
            ],
            # S Block
            [
                # 0 度
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 1],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 90 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0]
                ],
                # 180 度
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 1],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 270 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0]
                ],
            ],
            # Z Block
            [
                # 0 度
                [
                    [0, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 90 度
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0]
                ],
                # 180 度
                [
                    [0, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                ],
                # 270 度
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0]
                ],
            ],
            # T Block
            [
                # 0 度
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                ],
                # 90 度
                [
                    [0, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0]
                ],
                # 180 度
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 1, 1, 1],
                    [0, 0, 0, 0]
                ],
                # 270 度
                [
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]
                ],
            ],
        ]

    def get_cell_data(self, type, rot, x, y):
        # 指定されたブロックの１マスのデータを取得します。
        # type: ブロックの種類
        # rot: ブロックの回転回数
        # x: ブロックセルのX軸
        # y: ブロックセルのY軸
        return self.blocks[type][rot][y][x]

    def reset(self):
        # ブロックの状態を初期状態に戻すメソッドです。
        self.x = int(stage.Stage.WIDTH / 2 - Block.SIZE / 2)
        self.y = -1


