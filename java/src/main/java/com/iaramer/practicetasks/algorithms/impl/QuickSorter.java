package com.iaramer.practicetasks.algorithms.impl;

import java.util.Arrays;

public class QuickSorter extends AbstractSorter {

    /**
     * Algorithm: unstable, divide & conquer
     * ================
     * Time complexity|
     * ================
     * Worst – O(n2)
     * Average – O(n log n)
     * Best – O(n log n)
     * =================
     * Space complexity|
     * =================
     * Worst – O(log n)
     *
     * @param array
     * @return sorted array
     */
    @Override
    public int[] sort(int[] array) {

        if (array.length == 0 || array.length == 1) {
            return array;
        }

        int pivotPoint = (int) (Math.random() * (array.length));

        boolean isPivotPointPast = false;
        int[] smallerArray = new int[array.length];
        int smallerArraySize = 0;
        int[] largerArray = new int[array.length];
        int largerArraySize = 0;

        for (int i = 0; i < array.length; i++) {
            if (!isPivotPointPast && array[i] == array[pivotPoint]) {
                isPivotPointPast = true; // skip the pivotPoint
            } else if (array[i] < array[pivotPoint]) {
                smallerArray[smallerArraySize++] = array[i];
            } else {
                largerArray[largerArraySize++] = array[i];
            }
        }

        smallerArray = sort(Arrays.copyOf(smallerArray, smallerArraySize));
        largerArray = sort(Arrays.copyOf(largerArray, largerArraySize));

        array[smallerArraySize] = array[pivotPoint];
        System.arraycopy(smallerArray, 0, array, 0, smallerArraySize);
        System.arraycopy(largerArray, 0, array, smallerArraySize + 1, largerArraySize);

        return array;
    }
}
