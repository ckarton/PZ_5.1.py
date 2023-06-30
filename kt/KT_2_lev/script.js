// Вариант 22: Составить программу вычисления функции: y=x^3-2,еслиX≤3 y=4-x,еслиX > 3
function calculateY(x) {
    if (x <= 3) {
        return Math.pow(x, 3) - 2;
    } else {
        return 4 - x;
    }
}

// Пример использования функции
var x = 2; // Задайте значение переменной x, для которого нужно вычислить Y
var result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);
