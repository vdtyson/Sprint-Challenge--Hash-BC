#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables_sprint.ex2.hashtables import *


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # insert each ticket source and destination into hastable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # plan the route, starting destinations source will always equal none
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    # loop and set next destination on the list.
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    return route[:-1]
