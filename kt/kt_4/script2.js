// Вариант 22: Составить программу вычисления функции  y=n∑i=1 (x^2i + 2x^3 )
function calculateY(n, x) {
    var sum = 0;

    for (var i = 1; i <= n; i++) {
        var term = Math.pow(x, 2 * i) + 2 * Math.pow(x, 3);
        sum += term;
    }

    return sum;
}

// Пример использования функции
var n = 3; // Количество итераций
var x = 2; // Значение переменной

var result = calculateY(n, x);
console.log("Результат вычисления функции Y: " + result);
