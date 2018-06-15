//
// Created by nick on 6/3/2018.
//

#ifndef LINKEDLISTS_LINKEDLIST_H
#define LINKEDLISTS_LINKEDLIST_H


#include "node.h"

class linkedList {
public:
    linkedList();
    void append(int value);
    void insert(int value, int index);
    void deleteVal(int index);
    void update(int index);
private:
    node* head;

};


#endif //LINKEDLISTS_LINKEDLIST_H
