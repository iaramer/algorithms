package com.iaramer.practicetasks;

public class Deadlock {
    public static void main(String[] args) {
        final String r1 = "resource 1";
        final String r2 = "resource 2";

        Thread t1 = new Thread() {
            public void run() {
                synchronized (r1) {
                    System.out.println("Thread 1: locked res 1");
                    try{ sleep(100);} catch(Exception e) {}
                    synchronized (r2) {
                        System.out.println("Thread 1: locked res 2");
                    }
                }
            }
        };

        Thread t2 = new Thread() {
            public void run() {
                synchronized (r2) {
                    System.out.println("Thread 2: locked res 2");
                    try{ sleep(100);} catch(Exception e) {}
                    synchronized (r1) {
                        System.out.println("Thread 2: locked res 1");
                    }
                }
            }
        };

        t1.start();
        t2.start();
    }
}
