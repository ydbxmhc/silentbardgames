#!/usr/bin/env bash
# L1 Simple Pool roller. Usage: roll.sh EL [extra_effort_dice] [label]
# One d2 per die via $RANDOM%2 (odd=1). Shows every die. Never fudge.
EL=${1:?EL required}; XE=${2:-0}; LABEL=${3:-roll}
N=$((EL+XE)); T=0; D=""
for ((i=0;i<N;i++)); do r=$((RANDOM%2)); D+="$r "; T=$((T+r)); done
echo "[$LABEL] EL$EL +${XE}XE -> ${N}d[0-1]: $D= $T"
if (( T > EL )); then echo "  OVER EL -> total failure (effect 0)"
elif (( T == 0 && N >= 3 )); then echo "  ALL ZEROES -> EXTREME FAILURE"
elif (( T == 0 )); then echo "  zero -> failure"
elif (( T == EL && T == N && N >= 3 )); then echo "  ALL MAX & = EL -> EXTREME SUCCESS"
else echo "  result $T"; fi
