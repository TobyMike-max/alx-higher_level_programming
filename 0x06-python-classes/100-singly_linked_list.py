#!/usr/bin/python3
# 100-singly_linked_list.py
"""Define a Node and SinglyLinkedList."""


class Node:
    """A singly_linked_list Node class"""

    def __init__(self, data, next_node=None):
        """Instantiate a new class Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets next_node"""
        if (not isinstance(value, Node) or
                value != None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while(tmp.next_node is != None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SInglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is != None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
