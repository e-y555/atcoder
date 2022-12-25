<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}

$N = $inputs[0][0];
$S = $inputs[1];
$r = [];

for ($i = 0; $i < $N; $i++) {
    if ($i === 0) {
        $r[$i] = $S[$i];
        continue;
    }
    $r[$i] = $S[$i] - $S[$i - 1];
}
echo implode(' ', $r) . PHP_EOL;
