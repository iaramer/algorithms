package com.iaramer.practicetasks.datastructures.list;

public interface IList {

    void add(int val);

//    void addAtHead(int a);

//    void addAtTail(int a);

    void addAtIndex(int index, int val);

    void reverse();

//    void remove(int val);

    void removeByIndex(int index);

    int getAtIndex(int index);

    int getMiddle();
}
