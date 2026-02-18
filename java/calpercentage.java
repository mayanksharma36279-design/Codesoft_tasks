import java.util.Scanner;
public class calpercentage {
public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    System.out.println("enter marks in hindi:");
    int a= sc.nextInt();
    System.out.println("enter marks in english:");
    int b= sc.nextInt();
    System.out.println("enter marks in maths:");
    int c= sc.nextInt();
    System.out.println("enter marks in science:");
    int d= sc.nextInt();
    System.out.println("enter marks in sst:");
    int e= sc.nextInt();
    System.out.println("enter marks in drawing:");
    int f= sc.nextInt();
    float per=(a+b+c+d+e+f)/6;
    System.out.println("the percentage of student is: "+per);

}
    
}
