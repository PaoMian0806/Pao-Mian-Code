angular
    .module("app", [])
    .controller("controller", ["$scope", "$interval", function ($, $interval) {
        $.hhmmss = "00:01:00";
        $.hms = "000";
        $.total = 0;
        $.start = 0;
        $.lap = 0;
        $.intervalID = 0;
        /* $.mtb1 = "開始";
        $.mtb2 = "重設"; */
        $.mode = 0;
        $.left_text = "開始";
        $.right_text = "單圈計時";
        $.arr = [];

        $.ps0 = function (value, num){
            return value.toString().padStart(num, "0");
        }

        $.formatTime = function (time) {
            return $.ps0(parseInt(time / 1000 / 60 / 60), 2)
                + ":" + $.ps0(parseInt(time / 1000 / 60) % 60, 2)
                + ":" + $.ps0(parseInt(time / 1000) % 60, 2);
        }

        $.left = function () {
            if ($.mode == 0) {
                $.mode = 1;
                $.left_text = "暫停";
                $.right_text = "單圈計時";

                $.start = new Date().getTime();
                $.lap = $.start;
                $.intervalID = $interval(function () {
                    var current = $.total + new Date().getTime();
                    $.ms = $.ps0((current - $.start) % 1000, 3);
                    $.hhmmss = $.formatTime(current - $.start);
                }, 10);
            }
            else { // Stop
                $.mode = 0;
                $.left_text = "繼續";
                $.right_text = "重設";

                $interval.cancel($.intervalID);
                $.total += new Date().getTime() - $.start;

            }
        }

        $.right = function () {
            if ($.mode == 0) { //Reset
                $.hhmmss = "00:00:00";
                $.ms = "000";
                $.total = 0;
                $.arr = []; // Clear array
            }
            else { // Count
                var current = new Date().getTime();
                $.arr.push({
                    lap: $.formatTime(current - $.lap) + "." + $.ps0((current - $.lap) % 1000, 3),
                    total: $.formatTime($.total + current - $.start) + "." + $.ps0(($.total + current - $.start) % 1000, 3)
                })
                $.lap = current;
            }
        }
    }]);
