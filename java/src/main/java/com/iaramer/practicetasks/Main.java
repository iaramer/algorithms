package com.iaramer.practicetasks;

import com.iaramer.practicetasks.algorithms.Sorter;
import com.iaramer.practicetasks.algorithms.impl.ShellSorter;
import com.iaramer.practicetasks.datastructures.list.impl.LinkedIList;

import static com.iaramer.practicetasks.AdditionalFunctionsSupplier.createAndPrintRandomArray;
import static com.iaramer.practicetasks.AdditionalFunctionsSupplier.printArray;

public class Main {
    public static void main(String[] args) {
        System.out.println("Here we go!\n");
//        testAlgorithm();
        testCollection();
    }

    static void testCollection() {
        LinkedIList list = new LinkedIList();

        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.show();

        list.reverse();
        list.show();

        list.reverse();
        list.show();

        System.out.println(list.getMiddle());
    }

    static void testAlgorithm() {
        Sorter sorter = new ShellSorter();

        int[] array = createAndPrintRandomArray(20);
        array = sorter.sort(array);
        System.out.println("Sorted array:");
        printArray(array);
    }
}