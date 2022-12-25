<?php

[$H, $W] = explode(' ', trim(fgets(STDIN)));

$S = input($H, $W);
$T = input($H, $W);

sort($S);
sort($T);

echo ($S == $T) ? 'Yes' : 'No';
echo PHP_EOL;

function input($H, $W)
{
    $ST = [];
    for ($i = 0; $i < $H; $i++) {
        $s = trim(fgets(STDIN));
        for ($j = 0; $j < $W; $j++) {
            $ST[$j] .= $s[$j];
        }
    }
    return $ST;
}
