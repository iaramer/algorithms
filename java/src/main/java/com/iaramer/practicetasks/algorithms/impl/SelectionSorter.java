package com.iaramer.practicetasks.algorithms.impl;

public class SelectionSorter extends AbstractSorter {

    /**
     * Algorithm: unstable
     * ================
     * Time complexity|
     * ================
     * Worst – O(n2)
     * Average – O(n2)
     * Best – O(n2)
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
        for (int i = 0; i < array.length; i++) {
            int min = array[i];
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] < min) {
                    int temp = min;
                    min = array[j];
                    array[j] = temp;
                }
            }
            array[i] = min;
        }
        return array;
    }
}