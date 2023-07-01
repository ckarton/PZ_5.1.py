// Вариант 22: Составить программу вычисления функции  y=n∑i=1 (x^2i + 2x^3 )
function calculateY(n, x) {
    let sum = 0;

    for (let i = 1; i <= n; i++) {
        let term = Math.pow(x, 2 * i) + 2 * Math.pow(x, 3);
        sum += term;
    }

    return sum;
}

// Пример использования функции
let n = 3; // Количество итераций
let x = 2; // Значение переменной

let result = calculateY(n, x);
console.log("Результат вычисления функции Y: " + result);
