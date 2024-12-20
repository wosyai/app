# Usage: ./scripts/viz/cloch.sh
# Description: Count lines of code in the project's git history

echo "All files:"

git log --shortstat -- ':!*.json' ':!*.svg' \
    | egrep "file[s]* changed" \
    | sed 's/changed, \([0-9]\+\) deletions/changed, 0 insertions(+), \1 deletions/g' \
    | awk '{files+=$1; inserted+=$4; deleted+=$6; min_total+=($4>$6)?$4:$6; max_total+=$4+$6} END {average_total=(min_total + max_total) / 2; print "files changed:", files, "- lines inserted:", inserted, "- lines deleted:", deleted, "- min total lines changed:", min_total, "- max total lines changed:", max_total, "- average total lines changed:", average_total}'

echo "Main code files:"

git log --shortstat -- ':*.js' ':*.ts' ':*.vue' \
    | egrep "file[s]* changed" \
    | sed 's/changed, \([0-9]\+\) deletions/changed, 0 insertions(+), \1 deletions/g' \
    | awk '{files+=$1; inserted+=$4; deleted+=$6; min_total+=($4>$6)?$4:$6; max_total+=$4+$6} END {average_total=(min_total + max_total) / 2; print "files changed:", files, "- lines inserted:", inserted, "- lines deleted:", deleted, "- min total lines changed:", min_total, "- max total lines changed:", max_total, "- average total lines changed:", average_total}'
