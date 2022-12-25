<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}
$N = $inputs[0][0];
$K = $inputs[0][1];
$A = $inputs[1];

for ($i = 0; $i < $K; $i++) {
    array_shift($A);
    array_push($A, 0);
}
echo implode(' ', $A) . PHP_EOL;
