from .enums import GamePhase, Action
from .deck import Deck
from .player import Player, Dealer


class BlackJackGame:
    def __init__(self, players: list[Player]):
        self.deck = Deck()
        self.players: list[Player] = []
        self.dealer = Dealer()
        self.current_player: Player = None
        self.player_turn_status_map: dict = {}
        self.current_phase: GamePhase = GamePhase.STARTED

        for player in players:
            if player:
                self.players.append(player)
                self.player_turn_status_map[player] = None

        self.player_turn_status_map[self.dealer] = None
        self.deck.shuffle()

    def getNextEligiblePlayer(self) -> Player:
        if not self.current_player:
            for player in self.players:
                if Action.STAND != self.player_turn_status_map.get(player) and not player.isBusted():
                    self.current_player = player
                    return self.current_player

            if Action.STAND != self.player_turn_status_map.get(self.dealer):
                self.current_player = self.dealer
                return self.current_player
        else:
            current_player_index = self.players.index(self.current_player)
            for i in range(current_player_index + 1, len(self.players)):
                player = self.players[i]
                if Action.STAND != self.player_turn_status_map.get(player) and not player.isBusted():
                    self.current_player = player
                    return self.current_player

            if self.current_player != self.dealer and Action.STAND != self.player_turn_status_map.get(self.dealer):
                self.current_player = self.dealer
                return self.current_player

        return None

    def startNewRound(self):
        self.deck.resetDeck()
        for player in self.players:
            player.getHand().clearHand()
        self.dealer.getHand().clearHand()
        self.current_player = None
        self.current_phase = GamePhase.STARTED
        for k in self.player_turn_status_map:
            self.player_turn_status_map[k] = None

    def dealInitialCards(self):
        if GamePhase.BET_PLACED != self.current_phase:
            raise Exception("All players must bet before dealing")

        for player in self.players:
            player.getHand().addCard(self.deck.drawCard())

        self.dealer.getHand().addCard(self.deck.drawCard())

        for player in self.players:
            player.getHand().addCard(self.deck.drawCard())

        self.dealer.getHand().addCard(self.deck.drawCard())

        self.current_phase = GamePhase.INITIAL_CARD_DRAWN

    def bet(self, player: Player, amount: float):
        if GamePhase.STARTED != self.current_phase:
            raise Exception("Bets must be placed at the start of the round")
        player.placeBet(amount)

        if len(self.players) == sum(p.getBet() > 0 for p in self.players):
            self.current_phase = GamePhase.BET_PLACED

    def hit(self, player: Player):
        if Action.STAND == self.player_turn_status_map.get(player):
            raise Exception("Player has already stood")

        if player.isBusted():
            raise Exception("Player is already bust")

        drawn_card = self.deck.drawCard()
        player.getHand().addCard(drawn_card)
        self.player_turn_status_map[player] = Action.HIT

    def stand(self, player: Player):
        if Action.STAND == self.player_turn_status_map.get(player):
            raise Exception("Player has already stood")

        if player.isBusted():
            raise Exception("Player is already bust")

        self.player_turn_status_map[player] = Action.STAND

    def checkGameEndCondition(self):
        all_players_done = len([
            player
            for player in self.players
            if self.player_turn_status_map.get(player) == Action.STAND
        ])
        if not all_players_done:
            return

        dealer_value = max(self.dealer.getHand().getPossibleValues(), default=0)
        dealer_busts = self.dealer.isBusted()

        for player in self.players:
            if player.isBusted():
                player.loseBet()
            else:
                player_value = max(player.getHand().getPossibleValues(), default=0)
                if dealer_busts or player_value > dealer_value:
                    player.payout()
                elif player_value == dealer_value:
                    player.returnBet()
                else:
                    player.loseBet()

        self.current_phase = GamePhase.ROUND_END

    def playNextTurn(self):
        next_player = self.getNextEligiblePlayer()
        if next_player:
            self.performPlayerAction(next_player)

    def performPlayerAction(self, player: Player):
        action = player.getDecisionLogic().decideAction(player.getHand())
        if action == Action.HIT:
            self.hit(player)
        elif action == Action.STAND:
            self.stand(player)
