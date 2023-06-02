from typing import Tuple
import enum

class Card :
    def __init__(self, rank:str, suit:str) -> None :
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()   # 내부에서 호출하는 메서드
        
    def _points(self) -> Tuple[int,int] :
        return int(self.rank), int(self.rank)
    
class AceCard(Card) :
    def _points(self) -> Tuple[int,int] :
        return 1,11
    
class FaceCard(Card) :
    def _points(self) -> Tuple[int,int] :
        return 10,10
    
class Suit (str, enum.Enum) :
    Club = "♣️"
    Diamond = "♦️"
    Heart="❤️ "
    Spade = "♠️"
