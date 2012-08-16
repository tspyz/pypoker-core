from world.world import World
from tournament.tournament import Tournament, RuleBook
import unittest
import world.messenger

class TestWorld(unittest.TestCase):
    def test_basics(self):
        w = World("test")
        w.reset()
        self.assertTrue(w.record_message("test1", "test2", "unit test base message") != -1)

    def test_player_list(self):
        w = World("")
        w.reset()
        self.assertTrue(len(w.players) == 0)
        p1 = w.players.create_player("Joe Bloggs", 100, world.messenger.NM_file)
        w.players.create_player("Joe Schlabotnik", 200, world.messenger.NM_file)
        self.assertTrue(len(w.players) == 2)
        p2 = w.players.fetch_player_by_id(p1.player_id)
        self.assertTrue(p2.name == "Joe Bloggs")
        p2 = w.players.fetch_player_by_id("ILLEGAL")
        self.assertTrue(p2 == -1)

        return

    def test_table_list(self):
        w = World("")
        w.reset()
        self.assertTrue(len(w.card_tables) == 0)
        w.card_tables.create_card_table("Test Table 1", None, 10)
        w.card_tables.create_card_table("Test Table 2", None, 2)
        w.card_tables.create_card_table("Test Table 3", None, 2)
        self.assertTrue(len(w.card_tables) == 3)

    def test_seat_player(self):
        w = World("")
        w.reset()
        self.assertTrue(len(w.players) == 0)
        p1 = w.players.create_player("Joe Bloggs", 100, world.messenger.NM_file)
        p2 = w.players.create_player("Joe Schlabotnik", 200, world.messenger.NM_file)
        self.assertTrue(len(w.players) == 2)
        self.assertTrue(len(w.card_tables) == 0)
        t1 = w.card_tables.create_card_table("Test Table 1", None, 10)
        t2 = w.card_tables.create_card_table("Test Table 2", None, 2)
        t3 = w.card_tables.create_card_table("Test Table 3", None, 2)
        self.assertTrue(len(w.card_tables) == 3)
        self.assertTrue(len(t1.playerlist) == 0)
        t1.add_new_player(p1)
        self.assertTrue(len(t1.playerlist) == 1)
        t1.add_new_player(p2)
        self.assertTrue(len(t1.playerlist) == 2)
        t1.add_new_player(p2)
        self.assertTrue(len(t1.playerlist) == 2)
        t2.add_new_player(p1)
        t2.add_new_player(p2)
        self.assertTrue(len(t2.playerlist) == 2)
        t2.add_new_player(p2)
        self.assertTrue(len(t2.playerlist) == 2)
        t2.announce("Test message")

    def test_stacks(self):
        w = World("")
        w.reset()
        t1 = w.card_tables.create_card_table("Stack test table", None, 10)
        p1 = w.players.create_player("Mr Moneybags", 100, world.messenger.NM_file)
        t1.add_new_player(p1)
        self.assertTrue(t1.get_player_stack(p1) == 0.0)
        t1.set_player_stack(p1, 1000.0)
        self.assertTrue(t1.get_player_stack(p1) == 1000.0)
        t1.deduct_from_player_stack(p1, 500.0)
        self.assertTrue(t1.get_player_stack(p1) == 500.0)
        t1.add_to_player_stack(p1, 1.0)
        self.assertTrue(t1.get_player_stack(p1) == 501.0)
        t1.place_bet(p1, 20.0)
        self.assertTrue(t1.get_player_stack(p1) == 501.0 - 20.0)
        self.assertTrue(t1.get_current_bet(p1) == 20.0)
        self.assertTrue(t1.place_bet(p1, 1000.0) == 501.0)
        self.assertTrue(t1.get_current_bet(p1) == 501.0)

    def test_button(self):
        w = World("")
        w.reset()
        t1 = w.card_tables.create_card_table("Stack test table", None, 10)
        p1 = w.players.create_player("Mr Moneybags", 100, world.messenger.NM_file)
        p2 = w.players.create_player("test1", 100, world.messenger.NM_file)
        p3 = w.players.create_player("test2", 100, world.messenger.NM_file)
        t1.add_new_player(p1)
        t1.add_new_player(p2)
        t1.add_new_player(p3)
        self.assertTrue(t1.get_button_position() == -1)
        self.assertTrue(t1.set_button_position(100) == -1)
        self.assertTrue(t1.set_button_position(-1) == -1)

        t1.set_button_position(1)
        self.assertTrue(t1.get_button_position() == 1)

        t1.deal_for_button()
        self.assertTrue(t1.get_button_position() != -1)

        old_button = t1.get_button_position()
        t1.move_button()
        self.assertTrue(t1.get_button_position() != old_button)

        w.close()
        return

    def test_balance(self):
        w = World("")
        w.reset()
        p1 = w.players.create_player("Mr Moneybags", 100, world.messenger.NM_file)
        self.assertTrue(p1.deduct(2000, "internal test") == -1)
        self.assertTrue(p1.balance == 100)
        self.assertTrue(p1.credit(100, "internal test") == 200)
        self.assertTrue(p1.deduct(100, "internal test") == 100)
        self.assertTrue(p1.balance == 100)
        self.assertTrue(p1.credit(-100, 'internal test') == -1)
        self.assertTrue(p1.deduct(-100, 'internal test') == -1)
        w.close()

        return

    def test_notify(self):
        return

    def test_hand_and_pot(self):
        w = World("test4")
        w.reset()
        p1 = w.players.create_player("test1", 100, world.messenger.NM_file)
        p2 = w.players.create_player("test2", 100, world.messenger.NM_file)
        g1 = w.tournaments.create_game(RuleBook.DEFAULT_HU_NLHE_RULES)
        g1.add_new_player(p1)
        g1.add_new_player(p2)
        h1 = w.holdem_hands.start_new_hand(g1.table, g1, 1, 10, 20)
        self.assertTrue(h1.ante == 1)
        self.assertTrue(h1.big_blind == 20)
        self.assertTrue(h1.small_blind == 10)
        self.assertTrue(len(h1.players) == 2)
        p1 = w.pots.create_sub_pot(h1)
        self.assertTrue(p1 == None)
        p1 = w.pots.create_new_pot(h1)
        self.assertTrue(p1.amount == 0.0)
        self.assertTrue(p1.game == g1)
        p2 = w.pots.create_sub_pot(h1)
        p3 = w.pots.create_sub_pot(h1)
        p1.add_chips(24)
        self.assertTrue(p1.amount == 24)

        return

    def test_tournament(self):
        w = World("test3")
        w.reset()
        p1 = w.players.create_player("Joe Bloggs", 100, world.messenger.NM_file)
        p2 = w.players.create_player("Joe Schlabotnik", 200, world.messenger.NM_file)
        p3 = w.players.create_player("David Kelly", 100, world.messenger.NM_file)

        g1 = w.tournaments.create_game(RuleBook.DEFAULT_HU_NLHE_RULES)

        self.assertTrue(g1.is_open())
        g1.add_new_player(p1)
        g1.add_new_player(p2)
        g1.close_entries()
        self.assertFalse(g1.is_open())

        self.assertTrue(g1.add_new_player(p1) == -1)
        self.assertTrue(g1.add_new_player(p3) == -1)

        g1.start_game()

        w.close()

if __name__ == '__main__':
    unittest.main()
