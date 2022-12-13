<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}
$H = $inputs[0][0];
$W = $inputs[0][1];
unset($inputs[0]);
$S = array_values($inputs);

$results = [];

for ($i = 0; $i < $H; $i++) {
    $s = $S[$i][0];
    for ($j = 0; $j < $W; $j++) {
        if ($s[$j] === '#') $results[] = 1;
    }
}
echo array_sum($results) . PHP_EOL;
