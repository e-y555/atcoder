<?php

[$H, $M] = explode(' ', trim(fgets(STDIN)));

while (true) {
    $H = sprintf('%02d', $H);
    $M = sprintf('%02d', $M);
    $h = $H[0] . $M[0];
    $m = $H[1] . $M[1];
    if (isMisjudge($h, $m)) {
        echo $H . ' ' . $M . PHP_EOL;
        break;
    }
    $M += 1;
    if ($M === 60) {
        $M = 0;
        $H += 1;
        if ($H === 24) {
            $H = 0;
            continue;
        }
    }
}
function isMisjudge($h, $m)
{
    return $h <= 23 && $m <= 59;
}
