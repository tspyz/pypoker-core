from world.world import World
from tournament.tournament import Tournament, RuleBook
import unittest
import world.messenger

class TestEmailPlayer(unittest.TestCase):
    def test_basics(self):
        w = World("")
        w.reset()
        p1 = w.players.create_player("terence@voltage.com", 100, world.messenger.NM_mail)
        p2 = w.players.create_player("trspies@gmail.com", 100, world.messenger.NM_mail)
        
        g1 = w.tournaments.create_game(RuleBook.DEFAULT_HU_NLHE_RULES)

        self.assertTrue(g1.is_open())
        g1.add_new_player(p1)
        g1.add_new_player(p2)
        g1.close_entries()
        self.assertFalse(g1.is_open())

        g1.start_game()
        return

