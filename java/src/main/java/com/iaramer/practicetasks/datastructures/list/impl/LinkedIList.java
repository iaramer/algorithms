package com.iaramer.practicetasks.datastructures.list.impl;

import com.iaramer.practicetasks.datastructures.list.IList;

public class LinkedIList implements IList {

    private static class Node {

        int val;
        Node next;

        Node(int val) {
            this.val = val;
            next = null;
        }
    }

    Node head = null;
    int size = 0;

    @Override
    public void add(int val) {
        Node node = new Node(val);
        size++;
        if (head == null) {
            head = node;
            return;
        }
        Node currNode = head;
        while (currNode.next != null) {
            currNode = currNode.next;
        }
        currNode.next = node;
    }

    @Override
    public int getMiddle() {
        if (head == null) return -1;
        Node slowPointer = head;
        Node fastPointer = head;
        while (fastPointer.next != null && fastPointer.next.next != null) {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
        }
        return slowPointer.val;
    }

    @Override
    public void reverse() {
        if (head == null || head.next == null) {
            return;
        }
        Node prevNode = null;
        Node currNode = head;
        Node nextNode = null;
        while (currNode != null) {
            nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }
        head = prevNode;
    }

    @Override
    public void addAtIndex(int index, int val) {
        Node node = new Node(val);
        if (index == 0) {
            if (head != null) {
                node.next = head;
            }
            head = node;
            size++;
            return;
        }

        Node prevNode = head;
        int prevIndex = 0;
        while (prevNode.next != null && prevIndex < index - 1) {
            prevNode = prevNode.next;
            prevIndex++;
        }

        if (prevIndex == index - 1) {
            if (prevNode.next != null) {
                node.next = prevNode.next;
            }
            prevNode.next = node;
            size++;
            return;
        }
        System.out.println("Index " + index + " is out of range, list size is " + size);
    }

    @Override
    public void removeByIndex(int index) {
        if (head == null) {
            System.out.println("Can't remove: empty list");
            return;
        }

        if (index == 0) {
            if (head.next != null) {
                head = head.next;
            } else {
                head = null;
            }
            size--;
            return;
        }

        Node prevNode = head;
        int prevIndex = 0;
        while (prevNode.next != null && prevIndex < index - 1) {
            prevIndex++;
            prevNode = prevNode.next;
        }

        if (prevNode.next != null && prevIndex == index - 1) {
            if (prevNode.next.next != null) {
                prevNode.next = prevNode.next.next;
            } else {
                prevNode.next = null;
            }
            size--;
            return;
        }
        System.out.println("Can't remove: index " + index + " is out of range");
    }

    @Override
    public int getAtIndex(int index) {
        if (head == null) {
            System.out.println("Can't get: empty list");
            return -111111;
        }

        Node currNode = head;
        int currIndex = 0;
        while (currNode.next != null && currIndex < index) {
            currNode = currNode.next;
            currIndex++;
        }

        if (currNode.next == null && currIndex < index) {
            System.out.println("Can't get : index " + index + " is out of range");
            return -111111;
        }
        return currNode.val;
    }

    public void show() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        Node currNode = head;
        System.out.print("LinkedIList:");
        while (currNode.next != null) {
            System.out.print(" " + currNode.val);
            currNode = currNode.next;
        }
        System.out.print(" " + currNode.val);
        System.out.println();
    }
}
