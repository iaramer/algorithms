package com.iaramer.practicetasks.datastructures.tree;

public class TripleTree<T> {

    private class Node<V> implements Comparable {
        private Node<V> lessNode;
        private Node<V> equalNode;
        private Node<V> largerNode;
        private V value;

        Node(V value) {
            this.value = value;
        }

        public V getValue() {
            return value;
        }

        public void setValue(V value) {
            this.value = value;
        }

        @Override
        public int compareTo(Object o) {
            if (!(o instanceof Comparable)) {
                throw new ClassCastException("Object should implement interface Comparable");
            }
            Comparable objectToCompare = (Comparable) o;
            Comparable value = (Comparable) this.value;
            return value.compareTo(objectToCompare);
        }
    }

    private Node<T> root;

    public void add(T t) {
        if (!(t instanceof Comparable)) {
            throw new ClassCastException("Object should implement interface Comparable");
        }
        Node<T> newNode = new Node<>(t);
        if (root == null) {
            root = newNode;
            return;
        }
        //todo: stopped here
    }

    private Node<T> recursivelyCompare(Node<T> node) {
        return node; //todo: work here
    }

}
