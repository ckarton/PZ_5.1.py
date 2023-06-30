// Вариант 22: Арифметические действия над числами пронумерованы следующим образом: 1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление. 
// Дан номер действия N (целое число в диапазоне 1-4) и числа A и B (В не равно 0). Выполнить над числами указанное действие и вывести результат.
function performOperation(N, A, B) {
    var result;

    switch (N) {
        case 1:
            result = A + B;
            break;
        case 2:
            result = A - B;
            break;
        case 3:
            result = A * B;
            break;
        case 4:
            result = A / B;
            break;
        default:
            console.log("Неправильный номер действия.");
            return;
    }

    console.log("Результат: " + result);
}

// Пример
var N = 4; // Номер действия 
var A = 1; // Первое число
var B = 9; // Второе число

performOperation(N, A, B);
