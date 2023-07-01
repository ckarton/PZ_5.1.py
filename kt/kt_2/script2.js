// Вариант 22: Составить программу вычисления функции: y=x+5,еслиX<-4,  3x^2 ,если -4 ≤ x ≤ 2,  y=2х-1,еслиX>2
function calculateY(x) {
    if (x < -4) {
        return x + 5;
    } else if (x >= -4 && x <= 2) {
        return 3 * Math.pow(x, 2);
    } else {
        return 2 * x - 1;
    }
}

// Пример использования функции
let x = 3; // Задайте значение переменной x, для которого нужно вычислить Y
let result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);
