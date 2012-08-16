from mailengine.msg_queue import MailQueue
import unittest
import time

class TestMsgQueue(unittest.TestCase):
    def test_basics(self):
        myqueue = MailQueue("")
        myqueue.reset()
        myqueue.sync_to_server()
        return

    def test_new_message(self):
        myqueue = MailQueue("test3")
        myqueue.reset()
        myqueue.add_message("terence@voltage.com", "test message", "body element 1")
        myqueue.add_message("terence@voltage.com", "test message", "body element 2")
        myqueue.add_message("terence@voltage.com", "test message 2", "body element 3")
        myqueue.sync_to_server()

    def test_get_messages(self):
        myqueue = MailQueue("")
        myqueue.reset()
        myqueue.add_message("twitterpokerbot@gmail.com", "test message", "body element 1")
        myqueue.sync_to_server()
        time.sleep(2)
        myqueue.sync_to_server()
        self.assertTrue(myqueue.get_next_message() != None)



        
        
