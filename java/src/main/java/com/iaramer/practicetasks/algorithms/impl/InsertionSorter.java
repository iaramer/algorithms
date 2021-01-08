package com.iaramer.practicetasks.algorithms.impl;

public class InsertionSorter extends AbstractSorter {

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
        for (int i = 1; i < array.length; i++) {
            if (array[i] < array[i - 1]) {
                for (int j = i; j > 0; j--) {
                    if (array[j - 1] < array[j]) {
                        break;
                    }
                    int temp = array[j];
                    array[j] = array[j - 1];
                    array[j - 1] = temp;
                }
            }
        }
        return array;
    }
}