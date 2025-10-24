package com.example;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * Hello2 World Project 2
 * Another Java program that prints "hello2 world" with additional features
 */
public class Hello2World2 {
    
    /**
     * Prints "hello2 world" with timestamp to the console
     */
    public static void printHello2World() {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String timestamp = now.format(formatter);
        
        System.out.printf("[%s] hello2 world%n", timestamp);
        System.out.println("This is hello2 world project 2!");
    }
    
    /**
     * Main method
     * @param args command line arguments
     */
    public static void main(String[] args) {
        printHello2World();
    }
}

