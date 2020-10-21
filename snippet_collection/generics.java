"""
Notes:
Generics 
    * It is an important part of strongly typed languages
    * Allows generalizations of what can be put in a data structure
        * Data Structure - The containers of data
    * Generics help fix data structures from being programmed to a certain type
    * Allow a type or method to operate on objects of various types while providing compile time type
"""

"""
Problem: 
Write a single generic function named printArray; this function must take an array of generic elements as a parameter
"""
import java.util.*;

class Printer <T> {

    /**
    *    Method Name: printArray
    *    Print each element of the generic array on a new line. Do not return anything.
    *    @param A generic array
    **/
    
    // Write your code here
    public void printArray(T[] elements) {
        for (T element : elements) {
            System.out.println(element);
        }
    }
}

public class Generics {
    
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Integer[] intArray = new Integer[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = scanner.nextInt();
        }

        n = scanner.nextInt();
        String[] stringArray = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
        }
        
        Printer<Integer> intPrinter = new Printer<Integer>();
        Printer<String> stringPrinter = new Printer<String>();
        intPrinter.printArray( intArray  );
        stringPrinter.printArray( stringArray );
        if(Printer.class.getDeclaredMethods().length > 1){
            System.out.println("The Printer class should only have 1 method named printArray.");
        }
    } 
}