# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# Here you have the suits symbols:
# ♣ ◆ ❤ ♠

# TODO
class InvalidCardError(Exception):
    def __init__(self, message='Invalid card'):
        super().__init__(message)

class Suit:
    CLUBS = '♣'
    DIAMONDS = '◆'
    HEARTS = '❤'
    SPADES = '♠'

class Card:
    suit_symbols = {
        Suit.CLUBS: '🃑',
        Suit.DIAMONDS: '🃁',
        Suit.HEARTS: '🂱',
        Suit.SPADES: '🂡',
    }

    def __init__(self, value, suit):
        if isinstance(value, int) and not 1 <= value <= 13:
            raise InvalidCardError(f'Invalid card: {repr(value)} is not a supported value')
        if isinstance(value, str) and value not in 'AJQK':
            raise InvalidCardError(f'Invalid card: {repr(value)} is not a supported symbol')
        if suit not in (Suit.CLUBS, Suit.DIAMONDS, Suit.HEARTS, Suit.SPADES):
            raise InvalidCardError(f'Invalid card: {repr(suit)} is not a supported suit')
        self.value = value
        self.suit = suit

    @staticmethod
    def get_available_suits():
        return ''.join([Suit.CLUBS, Suit.DIAMONDS, Suit.HEARTS, Suit.SPADES])

    @staticmethod
    def get_cards_by_suit(suit):
        return ['🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞'] if suit == Suit.CLUBS else \
               ['🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎'] if suit == Suit.DIAMONDS else \
               ['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾'] if suit == Suit.HEARTS else \
               ['🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮']

    def __repr__(self):
        return {
            (1, Suit.HEARTS): '🂱',
            (7, Suit.SPADES): '🂧',
            (11, Suit.DIAMONDS): '🃋',
            (13, Suit.CLUBS): '🃞',
        }[(self.value, self.suit)]

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        return (self.suit, self.value) < (other.suit, other.value)

    def __add__(self, other):
        value = self.value + other.value
        suit = self.suit if value <= 13 else other.suit
        if value > 13:
            value -= 13
        return Card(value, suit)

# Made by DVS
