import random

print "Hello Bushido!\n"

random.seed( 0 )
NUM_PLAYERS = 2
DECK_SIZE   = 13

def deal( deck, player_hands ):
    remainder = len( deck ) % len( player_hands )
    if remainder > 0:
        deal_deck = deck[:-remainder]
        remainder_deck = deck[-remainder:]
    elif remainder is 0:
        deal_deck = deck
        remainder_deck = []
    else:
        print "Error: invalid deal."
        return
        
    for i, card in enumerate( deal_deck ):
        player_hands[ i % len( player_hands ) ].append( card )

    return remainder_deck


class PlayerAISimple:
    def __init__( self, name ):
        self.name = name
        
    def pickCardToAttack( self, hand ):
        return hand[0]
        
    def pickCardToDefend( self, Acard, hand ):
        if Acard - 1 in hand:
            return card - 1
        hand.sort()
        hand.reverse()
        closets = Acard - 1
        for card in hand:
            if card < Acard:
                return card
        return hand[:]


class PlayerAIRandom:
    def __init__( self, name ):
        self.name = name
        
    def pickCardToAttack( self, hand ):
        return hand[0]
        
    def pickCardToDefend( self, card, hand ):
        return hand[0]

class Engine:
    def __init__( self, playerAIs ):
        self.playerAIs = playerAIs
        self.setup()
        
    def setup( self ):
        self.player_hands = []
        for i in range( 0, NUM_PLAYERS ):
            self.player_hands.append( [] )

        deck = range( 1, DECK_SIZE + 1 )
        random.shuffle( deck )
        self.remainder_hand = deal( deck, self.player_hands )
        
        
    def checkPlayerHand( self, card, pi ):
        if card not in self.player_hands[ pi ]:
            print self.playerAIs[ 1 ].name + " was caught cheating."
            return False
    
    @staticmethod
    def scoreCards( Acard, Dcard ):
        if Acard < Dcard:
            return Acard
        elif Acard - 1 is Dcard:
            return 0
        else:
            return Acard - Dcard
            
    def run( self ):
        score = [0,0]
        while( len( self.player_hands[0] ) is not 0 ):
            Acard = self.playerAIs[0].pickCardToAttack( self.player_hands[0] )
            if self.checkPlayerHand( Acard, 0 ):
                return
            self.player_hands[0].remove( Acard )
                
            Dcard = playerAIs[1].pickCardToDefend( Acard, self.player_hands[1] )
            if self.checkPlayerHand( Dcard, 1 ):
                return
            self.player_hands[1].remove( Dcard )
            
            
            score[0] = score[0] + self.scoreCards( Acard, Dcard )
            
            Acard = self.playerAIs[1].pickCardToAttack( self.player_hands[1] )
            if self.checkPlayerHand( Acard, 1 ):
                return
            self.player_hands[1].remove( Acard )

            Dcard = playerAIs[0].pickCardToDefend( Acard, self.player_hands[0] )
            if self.checkPlayerHand( Dcard, 0 ):
                return
            self.player_hands[0].remove( Dcard )
                
            score[1] = score[1] + self.scoreCards( Acard, Dcard )

        return score
                
playerAIs = []
playerAIs.append( PlayerAI( "Player 1" ) )
playerAIs.append( PlayerAI( "Player 2" ) )
wins = [0,0,0]
engine = Engine( playerAIs )

i = 0
while(i < 10000):
    engine.setup()
    scores = engine.run()
    if scores[0] > scores[1]:
        wins[0] = wins[0] + 1
    elif scores[1] > scores[0]:
        wins[1] = wins[1] + 1
    else:
        wins[2] = wins[2] + 1
    i = i + 1

print wins
