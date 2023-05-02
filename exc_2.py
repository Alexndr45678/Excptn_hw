# 1) Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
# и возвращает введенное значение.
# Ввод текста вместо числа не должно приводить к падению приложения,
# вместо этого, необходимо повторно запросить у пользователя ввод данных.


def read_float():
    flag = False
    while not flag:
        number = input("Введите дробное число: ")
        try:
            number = float(number)
            flag = True
        except ValueError:
            print("Вы ввели не дробное число. Попробуйте еще раз.")
    return print("Ваше число:", number)


read_float()



# Разработайте программу, которая выбросит Exception,
# когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.
EMPTY_STRING = "Вы ввели пустую строку. Попробуйте еще раз."


def isempty() -> str:
    flag = False
    while not flag:
        s = input("Введите строку:\n")
        if s and not s.isspace():
            flag = True
            return print("Ваша строка:", s)
        print(f'{ValueError(EMPTY_STRING)}')

isempty()

# 2) Исправленный код из ДЗ(2 задача) на Java:
# public class Task2 {
#     public static void main(String[] args) {
#         divideArray(new int[]{10, 11, 5, 2, 6, 34, 75, 32, 100, 90, 73});
#         divideArray(new int[]{10, 11, 5, 2, 6, 34, 75, 32, 100, 90, 73});
#         divideArray(null);
#     }

#     private static void divideArray(int[] intArray) {
#         try {
#             int d = 0;
#             double catchedRes1 = intArray[8] / d;
#             System.out.println("catchedRes1 = " + catchedRes1);
#         } catch (ArrayIndexOutOfBoundsException e) {
#             System.out.println("Catching out of bounds exception: " + e);
#         } catch (NullPointerException e) {
#             System.out.println("Catching null pointer exception: " + e);
#         } catch (ArithmeticException e) {
#             System.out.println("Catching arithmetic exception: " + e);
#         } catch (Exception e) {
#             System.out.println("Catching exception: " + e);
#         }
#     }
# }

# 3) Исправленный код из ДЗ(3 задача) на Java:

# public class Task3 {
#     public static void main(String[] args) throws Exception{
#         try {
#             int a = 90;
#             int b = 3;
#             System.out.println(a / b);
#             printSum(23, 234);
#             int[] abc = {1, 2};
#             abc[3] = 9;
#         } catch (NullPointerException ex) {
#             System.out.println("Указатель не может указывать на null!");
#         } catch (IndexOutOfBoundsException ex) {
#             System.out.println("Массив выходит за пределы своего размера!");
#         } catch (Throwable ex) {
#             System.out.println("Что-то пошло не так...");
#         }
#     }
#     public static void printSum (Integer a, Integer b) throws NullPointerException {
#         System.out.println(a + b);
#     }
# }