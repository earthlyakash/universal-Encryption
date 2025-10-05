
app.bringToFront();

(function () {
    // === Python-equivalent constants ===
    var ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*-_=+";
    var TOKEN_LEN = 8;
    var SEED = 123456789;

    // === Mersenne Twister 19937 implementation ===
    function MersenneTwister(seed) {
        this.N = 624;
        this.M = 397;
        this.MATRIX_A = 0x9908b0df;
        this.UPPER_MASK = 0x80000000;
        this.LOWER_MASK = 0x7fffffff;
        this.mt = new Array(this.N);
        this.mti = this.N + 1;
        this.init_genrand(seed);
    }

    MersenneTwister.prototype.init_genrand = function (s) {
        this.mt[0] = s >>> 0;
        for (this.mti = 1; this.mti < this.N; this.mti++) {
            var t = (1812433253 * (this.mt[this.mti - 1] ^ (this.mt[this.mti - 1] >>> 30)) + this.mti) >>> 0;
            this.mt[this.mti] = t;
        }
    };

    MersenneTwister.prototype.genrand_int32 = function () {
        var y;
        var mag01 = [0x0, this.MATRIX_A];
        if (this.mti >= this.N) {
            var kk;
            for (kk = 0; kk < this.N - this.M; kk++) {
                y = (this.mt[kk] & this.UPPER_MASK) | (this.mt[kk + 1] & this.LOWER_MASK);
                this.mt[kk] = this.mt[kk + this.M] ^ (y >>> 1) ^ mag01[y & 0x1];
            }
            for (; kk < this.N - 1; kk++) {
                y = (this.mt[kk] & this.UPPER_MASK) | (this.mt[kk + 1] & this.LOWER_MASK);
                this.mt[kk] = this.mt[kk + (this.M - this.N)] ^ (y >>> 1) ^ mag01[y & 0x1];
            }
            y = (this.mt[this.N - 1] & this.UPPER_MASK) | (this.mt[0] & this.LOWER_MASK);
            this.mt[this.N - 1] = this.mt[this.M - 1] ^ (y >>> 1) ^ mag01[y & 0x1];
            this.mti = 0;
        }
        y = this.mt[this.mti++];
        y ^= (y >>> 11);
        y ^= (y << 7) & 0x9d2c5680;
        y ^= (y << 15) & 0xefc60000;
        y ^= (y >>> 18);
        return y >>> 0;
    };

    // === Python's random.random() implementation ===
    function py_random(mt) {
        // identical to CPython _randommodule.c
        var a = mt.genrand_int32() >>> 5; // 27 bits
        var b = mt.genrand_int32() >>> 6; // 26 bits
        return (a * 67108864.0 + b) / 9007199254740992.0;
    }

    // === Generate mapping ===
    var mt = new MersenneTwister(SEED);
    var used = {};
    var mapping = [];

    for (var b = 0; b < 256; b++) {
        while (true) {
            var tokenChars = [];
            for (var i = 0; i < TOKEN_LEN; i++) {
                var idx = Math.floor(py_random(mt) * ALPHABET.length);
                tokenChars.push(ALPHABET.charAt(idx));
            }
            var token = tokenChars.join("");
            if (!used[token]) {
                used[token] = true;
                mapping.push(token);
                break;
            }
        }
    }

    // === Show results ===
    var msg =
        "JSX mapping test result:\n\n" +
        "Byte 0:   " + mapping[0] + "\n" +
        "Byte 1:   " + mapping[1] + "\n" +
        "Byte 2:   " + mapping[2] + "\n" +
        "Byte 255: " + mapping[255];

    alert(msg);
})();
