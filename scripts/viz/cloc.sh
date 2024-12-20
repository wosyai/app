# Usage: ./scripts/viz/cloc.sh
# Description: Count lines of code in the project

echo "All files:"

cloc --vcs git --not-match-f "^.*\.(json|svg)$" --by-percent cmb

echo "Main code files:"

cloc --vcs git --match-f "^.*\.(js|ts|vue)$" --by-percent cmb