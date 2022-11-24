import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Person

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Person, "person", 10)   #パブリッシャのオブジェクト作成
n = 0 #カウント用変数 
 
def cb():          #17行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしてい
    msg = Person()  #メッセージの「オブジェクト」
    msg.name = "上田隆一" 
    msg.age = n            #msgファイルに書いた「age」 
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1

node.create_timer(0.5, cb)  #タイマー設定
rclpy.spin(node)            #実行（無限ループ）
