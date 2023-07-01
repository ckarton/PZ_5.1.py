// Вариант 22: Арифметические действия над числами пронумерованы следующим образом: 1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление. 
// Дан номер действия N (целое число в диапазоне 1-4) и числа A и B (В не равно 0). Выполнить над числами указанное действие и вывести результат.
<!DOCTYPE html>
<html>

<head>
    <title>Форма взаимодействия с пользователем</title>
    <script>
    let deis;
    function sum(A, B) {
        let a = Number(document.getElementById("fst").value); // Первое число
        let b = Number(document.getElementById("snd").value); // Второе число
        let result;
            switch (deis) {
            case "+":
                result = a + b;
                break;
            case "-":
                result = a - b;
                break;
            case "/":
                result = a / b;
                break;
            case "*":
                result = a * b;
                break;
            }
        alert(result)
    }
    </script>
</head>

<body>
    <form>
        <label for="name">Первое число: </label>
        <input type="text" id="fst" name="fst" required><br>

        <label for="name">Второе число: </label>
        <input type="text" id="snd" name="snd" required><br>

        <button type="button" onclick="deis = '+'">Сложить</button>
        <button type="button" onclick="deis = '-'">Вычесть</button>
        <button type="button" onclick="deis = '*'">Умножить</button>
        <button type="button" onclick="deis = '/'">Разделить</button><br>
        <button type="button" onclick="sum();">Посчитать</button>
    </form>
</body>

</html>
