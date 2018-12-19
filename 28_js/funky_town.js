    // Team Whirlpool (Mohtasim Howlader and Soojin Choi)
    // SoftDev1 pd8
    // K28 -- Sequential Progression
    // 2018-12-19

    var fibonacci = function(n) {
        if (n == 0)
        return 0;
        if (n == 1)
        return 1;
        else
        return fibonacci(n-1) + fibonacci(n-2);
    };

    var gcd = function(a,b) {
        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }
        return gcd(b,a%b);
    };

    var students = ["mohtasim", "soojin", "bob", "sam", "emily"];

    var randomStudent = function() {
        randInd = Math.random() * students.length;
        return students[Math.floor(randInd)];

    }
