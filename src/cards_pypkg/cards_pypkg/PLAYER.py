import rclpy
from cards_pypkg.DEALER import create_hand
from rclpy.node import Node
from std_msgs.msg import String
#from cards_pypkg.cards import Card, Deck


class SimplePublisher(Node):
    def __init__(self, hand):
        super().__init__('PLAYER')
        self.publisher_ = self.create_publisher(String, 'messageTopic', 10)
        #self.timer = self.create_timer(0.5, self.publish_msg)
        self.publish_msg(hand)

    def publish_msg(self, hand):
        msg1, msg2, msg3 = String(), String(), String()
        msg1.data = 'Empty Hand'
        msg2.data = 'Adding 5 cards to hand'

        self.publisher_.publish(msg1)
        self.get_logger().info('%s' % msg1.data)
        self.publisher_.publish(msg2)
        self.get_logger().info('%s' % msg2.data)

        for i in range(1, 6):
            msg3.data = 'Card ' + str(i) + ' -- ' + \
                hand[i-1].Rank + ' of ' + hand[i-1].Suit
            self.publisher_.publish(msg3)
            self.get_logger().info('%s' % msg3.data)


def main():
    hand = create_hand()
    rclpy.init()
    simple_publisher = SimplePublisher(hand)
    rclpy.spin(simple_publisher)
    simple_publisher.destory_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
