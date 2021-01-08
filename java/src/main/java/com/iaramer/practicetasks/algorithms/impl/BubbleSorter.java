package com.iaramer.practicetasks.algorithms.impl;

public class BubbleSorter extends AbstractSorter {

    /**
     * Algorithm: STABLE
     * ================
     * Time complexity|
     * ================
     * Worst – O(n2)
     * Average – O(n2)
     * Best – O(n)
     * =================
     * Space complexity|
     * =================
     * Worst – O(1)
     *
     * @param array
     * @return sorted array
     */
    @Override
    public int[] sort(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - 1 - i; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j + 1];
                    array[j + 1] = array[j];
                    array[j] = temp;
                }
            }
        }
        return array;
    }
}