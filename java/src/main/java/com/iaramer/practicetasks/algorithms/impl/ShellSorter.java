package com.iaramer.practicetasks.algorithms.impl;

public class ShellSorter extends AbstractSorter {

    /**
     * Algorithm: unstable
     * ================
     * Time complexity|
     * ================
     * Worst – O(n2)
     * Average – depends on gap sequence
     * Best – O(n log n)
     * =================
     * Space complexity|
     * =================
     * Worst – O(n)
     *
     * @param array
     * @return sorted array
     */
    @Override
    public int[] sort(int[] array) {
        for (int gap = array.length / 2; gap >= 1; gap /= 2) {
            for (int i = gap; i < array.length; i++) {
                if (array[i] < array[i - gap]) {
                    for (int j = i; j > 0; j -= gap) {
                        if (j < gap || array[j] >= array[j - gap]) {
                            break;
                        }
                        int temp = array[j];
                        array[j] = array[j - gap];
                        array[j - gap] = temp;
                    }
                }
            }
        }
        return array;
    }
}
