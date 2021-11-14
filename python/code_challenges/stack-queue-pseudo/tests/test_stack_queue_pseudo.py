from stack_queue_pseudo import __version__
from stack_queue_pseudo.psuedo import *

def test_version():
    assert __version__ == '0.1.0'



def test_enqueue():
    queue=Psuedo()
    queue.enqueue(21)
    queue.enqueue(0)
    queue.enqueue(8)
    expected=21
    actual=queue.dequeue()
    assert expected == actual



def test_dequeue():

    queue=Psuedo()
    queue.enqueue(17)
    queue.enqueue(20)
    queue.enqueue(3)
    expected=17
    actual=queue.dequeue()
    assert expected == actual



def test_pop_multi_psudo():
    queue=Psuedo()
    queue.enqueue(11)
    queue.enqueue(24)
    queue.enqueue(0)

    assert 11 == queue.dequeue()
    assert 24 == queue.dequeue()
    assert 0 == queue.dequeue()


