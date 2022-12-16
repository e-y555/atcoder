<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}
$S = $inputs[0][0];
$T = $inputs[1][0];

for ($i = 0; $i < strlen($S); $i++) {
    if ($S[$i] === $T[0]) {
        for ($j = 1; $j < strlen($T); $j++) {
            if ($S[$i + $j] !== $T[$j]) {
                continue 2;
            }
        }
        echo 'Yes' . PHP_EOL;
        exit;
    }
}
echo 'No' . PHP_EOL;
