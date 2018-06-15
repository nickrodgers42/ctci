//
// Created by nick on 6/3/2018.
//

#include "linkedList.h"

linkedList::linkedList() {
    head = nullptr;
}

void linkedList::append(int value) {
    node * iterator = head;
    while (iterator->getNextNode() != nullptr) {
        iterator = iterator->getNextNode();
    }

    node* n = new node(value);
    iterator->setNextNode(n);
}

void linkedList::insert(int value, int index) {
    node* iterator = head;
    for (int i = 0; i < index; ++i) {
        if (iterator->getNextNode() != nullptr) {
            iterator = iterator->getNextNode();
        }
    }
    node* n = new node(value);
    node* nextNode = iterator->getNextNode();
    iterator->setNextNode(n);
    n->setNextNode(nextNode);
}

void linkedList::deleteVal(int index) {
    node* iterator = head;
    bool hasIndex = true;
    for (int i = 0; i < index; ++i) {
        iterator = iterator->getNextNode();
    }
    if (iterator != nullptr) {
        node* nextNode = iterator->getNextNode();
    }
}

void linkedList::update(int index) {

}