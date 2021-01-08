package com.iaramer.practicetasks;

public class AdditionalFunctionsSupplier {
    static int[] createAndPrintRandomArray(int size) {
        System.out.println("Unsorted array:");
        int[] array = new int[size];
        for (int i = 0; i < array.length; i++) {
            array[i] = (int) Math.round(10 + Math.random() * 90);
            System.out.print(array[i] + " ");
        }
        System.out.println();
        return array;
    }

    public static void printArray(int[] array) {
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
