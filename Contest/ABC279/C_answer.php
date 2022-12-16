<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}
$H = $inputs[0][0];
$W = $inputs[0][1];
unset($inputs[0]);
$inputs = array_values($inputs);

$S = [];
$T = [];

foreach ($inputs as $k => $v) {
    if ($k < $H) {
        $S[] = $v[0];
    } else {
        $T[] = $v[0];
    }
}

$s = [];
$t = [];
for ($i = 0; $i < $H; $i++) {
    for ($j = 0; $j < $W; $j++) {
        $s[$j] .= $S[$i][$j];
        $t[$j] .= $T[$i][$j];
    }
}

sort($s);
sort($t);

echo ($s == $t) ? 'Yes' . PHP_EOL : 'No' . PHP_EOL;
