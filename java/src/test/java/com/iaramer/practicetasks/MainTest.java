package com.iaramer.practicetasks;

import com.iaramer.practicetasks.algorithms.Sorter;
import com.iaramer.practicetasks.algorithms.impl.*;
import org.junit.Assert;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static com.iaramer.practicetasks.AdditionalFunctionsSupplier.createAndPrintRandomArray;

class MainTest {
    @BeforeEach
        // how to deal with it?
    void setUp() {
        System.out.println("Hey!");
        Sorter bubbleSorter = new BubbleSorter();
        Sorter insertionSorter = new InsertionSorter();
        Sorter selectionSorter = new SelectionSorter();
        Sorter quickSorter = new QuickSorter();
    }

    @Test
    void sortTest() {

        int testArraySize = 20;
        int[] testArray1;
        int[] testArray2;
        Sorter bubbleSorter = new BubbleSorter();
        Sorter insertionSorter = new InsertionSorter();
        Sorter selectionSorter = new SelectionSorter();
        Sorter quickSorter = new QuickSorter();
        Sorter shellSorter = new ShellSorter();

        System.out.println();
        testArray1 = createAndPrintRandomArray(testArraySize);
        testArray2 = Arrays.copyOf(testArray1, testArraySize);
        Assert.assertArrayEquals(bubbleSorter.sort(testArray1), insertionSorter.sort(testArray2));

        System.out.println();
        testArray1 = createAndPrintRandomArray(testArraySize);
        testArray2 = Arrays.copyOf(testArray1, testArraySize);
        Assert.assertArrayEquals(bubbleSorter.sort(testArray1), selectionSorter.sort(testArray2));

        System.out.println();
        testArray1 = createAndPrintRandomArray(testArraySize);
        testArray2 = Arrays.copyOf(testArray1, testArraySize);
        Assert.assertArrayEquals(bubbleSorter.sort(testArray1), quickSorter.sort(testArray2));

        System.out.println();
        testArray1 = createAndPrintRandomArray(testArraySize);
        testArray2 = Arrays.copyOf(testArray1, testArraySize);
        Assert.assertArrayEquals(bubbleSorter.sort(testArray1), quickSorter.sort(testArray2));

        System.out.println();
        testArray1 = createAndPrintRandomArray(testArraySize);
        testArray2 = Arrays.copyOf(testArray1, testArraySize);
        Assert.assertArrayEquals(bubbleSorter.sort(testArray1), shellSorter.sort(testArray2));
    }
}