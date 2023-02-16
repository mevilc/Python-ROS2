import rclpy
#import cards_pypkg.cards
from rclpy.node import Node
from std_msgs.msg import String
from cards_pypkg.cards import Card, Deck


def create_hand():
    # create standard deck
    d = Deck()
    for i in range(1, 5):
        for j in range(1, 11):
            c = Card()
            c.Suit = str(c.Suit(i).name)
            if j == 1:
                c.Rank = 'A'
            else:
                c.Rank = str(j)
            d.deck.append(c)

    for i in range(1, 5):
        for j in range(1, 4):
            c = Card()
            c.Suit = str(c.Suit(i).name)
            if j == 1:
                c.Rank = 'J'
            elif j == 2:
                c.Rank = 'Q'
            elif j == 3:
                c.Rank = 'K'
            d.deck.append(c)

    d.deck = d.shuffle(d.deck[:len(d.deck)//2], d.deck[len(d.deck)//2:])
    d.deck = d.shuffle(d.deck[:len(d.deck)//2], d.deck[len(d.deck)//2:])
    d.deck = d.shuffle(d.deck[:len(d.deck)//2], d.deck[len(d.deck)//2:])
    d.deck = d.cut()
    hand = [d.draw_from_top(), d.draw_from_top(), d.draw_from_top(),
            d.draw_from_top(), d.draw_from_top()]
    return hand


class SimplePublisher(Node):
    def __init__(self):
        super().__init__('DEALER')
        self.publisher_ = self.create_publisher(String, 'messageTopic', 10)
        #timer_period = 0.5
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0
        self.publish_msg()

    def publish_msg(self):
        msg1 = String()
        msg1.data = 'Deck of 52 cards'
        self.publisher_.publish(msg1)
        self.get_logger().info('%s' % msg1.data)
        msg1.data = 'Performing 3 riffle shuffles'
        self.publisher_.publish(msg1)
        self.get_logger().info('%s' % msg1.data)
        msg1.data = 'Cutting the deck'
        self.publisher_.publish(msg1)
        self.get_logger().info('%s' % msg1.data)
        msg1.data = '5 card hand drawn!'
        self.publisher_.publish(msg1)
        self.get_logger().info('%s' % msg1.data)
        #self.i += 1


def main():
    #hand = create_hand()
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destory_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
