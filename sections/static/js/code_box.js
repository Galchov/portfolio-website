const codeExamples = [
        {
            title: "Python - Fibonacci",
            code:
                ">>>def fibonacci(n):\n" +
                ">>>    sequence = [0, 1]\n" +
                ">>>    for i in range(2, n):\n" +
                ">>>        next_number = sequence[i - 1] + sequence[i - 2]\n" +
                ">>>        sequence.append(next_number)\n" +
                ">>>    return sequence[:n]\n" +
                ">>>\n" +
                ">>>print(fibonacci(10))"
        },
        {
            title: "Python - Prime numbers",
            code: ">>>def primes(n):\n" +
                ">>>    primes_list = []\n" +
                ">>>    candidate = 2\n" +
                ">>>    while len(primes_list) < n:\n" +
                ">>>        if all(candidate % p != 0 for p in primes_list):\n" +
                ">>>            primes_list.append(candidate)\n" +
                ">>>        candidate += 1\n" +
                ">>>    return primes_list\n" +
                ">>>\n" +
                ">>>print(primes(5))"
        },
        {
            title: "Python - Exponential Moving Average",
            code: ">>>def ema(prices, alpha=0.1):\n" +
                ">>>    ema_values = [prices[0]]\n" +
                ">>>    for price in prices[1:]:\n" +
                ">>>        ema_values.append(ema_values[-1] * (1 - alpha) + price * alpha)\n" +
                ">>>    return ema_values\n" +
                ">>>\n" +
                ">>>print(ema([10, 11, 12, 13, 14]))"
        }
    ];

    let currentIndex = 0;

    function updateDisplay() {
        document.getElementById("code-title").innerText = codeExamples[currentIndex].title;
        document.getElementById("code-snippet").innerText = codeExamples[currentIndex].code;
    }

    document.getElementById("prev-button").addEventListener("click", () => {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : codeExamples.length - 1;
        updateDisplay();
    });

    document.getElementById("next-button").addEventListener("click", () => {
        currentIndex = (currentIndex < codeExamples.length - 1) ? currentIndex + 1 : 0;
        updateDisplay();
    });

    updateDisplay();
