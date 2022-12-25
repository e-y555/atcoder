<?php
$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}

$N = $inputs[0][0];
$T = $inputs[0][1];
$A = $inputs[1];
$S = array_sum($A);

$T = $T % $S;
foreach ($A as $i => $t) {
    $T -= $t;
    if ($T < 0) {
        echo $i + 1, ' ', $T + $t;
        exit;
    }
}
