//
// Created by nick on 6/3/2018.
//

#include "node.h"

node::node() {
    nextNode = nullptr;
    value = NULL;
}

node::node(int n) {
    nextNode = nullptr;
    value = n;
}

node::~node() {

}

node* node::getNextNode() {
    return nextNode;
}

void node::setNextNode(node* n) {
    nextNode = n;
}

int node::getValue() {
    return value;
}

void node::setValue(const int n) {
    value = n;
}