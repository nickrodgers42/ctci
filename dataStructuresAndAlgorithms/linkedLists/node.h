//
// Created by nick on 6/3/2018.
//

#ifndef LINKEDLISTS_NODE_H
#define LINKEDLISTS_NODE_H

#include <iostream>
#include <cstdlib>

class node {
public:
    node();
    node(int n);
    ~node();
    node* getNextNode();
    void setNextNode(node* n);
    int getValue();
    void setValue(int n);
private:
    node* nextNode;
    int value;
};


#endif //LINKEDLISTS_NODE_H
