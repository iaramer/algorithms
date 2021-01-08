package com.iaramer.practicetasks.streams;

import java.util.AbstractMap;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamTasks {
    public static void main(String[] args) {

        task5();

    }

    static void task1() {
        String[] str1 = {"Word", "trrr_trrr", "dfsgsdf"};
        String[] str2 = {"d1", "lololololo-lolol"};
        String[] str3 = {"W11", "bzz", "cololcolo", "lflfl"};

        String result = Stream.of(str1, str2, str3)
                .flatMap(Arrays::stream)
                .map(String::length)
                .sorted()
                .map(String::valueOf)
                .limit(3)
                .collect(Collectors.joining(" "));

        System.out.println(result);
    }

    static void task2() {
        String str1 = "Word trrr_trrr dfsgsdf";
        String str2 = "d1 lololololo-lolol";
        String str3 = "W11 bzz cololcolo lflfl k";

        AtomicInteger i = new AtomicInteger();

        String result = Stream.of(str1, str2, str3)
                .map(str -> str.split(" "))
                .flatMap(Arrays::stream)
                .map(str -> {
                    i.getAndIncrement();
                    return new AbstractMap.SimpleEntry<>(i.get(), str.length());
                })
                .sorted(Comparator.comparing(AbstractMap.SimpleEntry::getValue))
                .limit(3)
                .map(AbstractMap.SimpleEntry::getKey)
                .map(String::valueOf)
                .collect(Collectors.joining(" "));

        System.out.println(result); // 10 4 6
    }

    static void task3() {
        // Задача - есть строка на вход, определить является ли она палиндром

        String word = "abcba";
        boolean result = word.equalsIgnoreCase(new StringBuilder(word).reverse().toString());

        System.out.println(result);
    }

    static void task4() {
        // Из строки создать мапу слово - количество повторений слова (case sensitive, убрать запятые)
        Map<String, Integer> result = Stream.of("  go, my go, go whaat ")
                .map(String::trim)
                .map(str -> str.split(" "))
                .flatMap(Arrays::stream)
                .map(str -> str.replaceAll(",", ""))
                .collect(Collectors.toMap(str -> str, str -> 1, Integer::sum));

        System.out.println(result);
    }

    static void task5() {
        // Прочитать файл с текстом, создать мапу слово - длина слова (case insensitive, убрать всё, кроме букв)
        String[] str1 = {" go, go go", "m go", "  why go, "};

        Map<String, Integer> result = Stream.of(str1)
                .flatMap(str -> Arrays.stream(str.trim().split(" ")))
                .map(str -> str.toLowerCase().trim().replaceAll("[^a-zA-Z]", ""))
                .filter(word -> !word.isEmpty())
                .collect(Collectors.toMap(Function.identity(), String::length, (o1, o2) -> o1));

        System.out.println(result);
    }
}
